# /// script
# requires-python = ">=3.10"
# dependencies = ["scipy>=1.11", "numpy>=1.24"]
# ///
"""
sample_size.py  (v001.2 DRAFT 2026-10-03)

第 3 相の例数計算。旧 sample_size_calculator.py（2 群・単一評価項目）を置き換える。

できること:
  - 二値（反応率の差）／連続量（平均の差）
  - co-primary（2 つの二値評価項目の両方で有意＝成功）: 同時検出力を相関つきで計算
  - 実薬群が複数（用量 m 個）× プラセボ: 用量ごとの比較の α を Bonferroni で分割（--alpha-split）
  - 割付比（例 1:1:1、2:1）
  - NRI（欠測＝非反応）: 脱落率 d で両群の反応率を p*(1-d) に薄めて計算（例数の割増しはしない）
  - 感度表: 相関・反応率を振った結果を同じ JSON に出す
  - 生存時間（tte）: Schoenfeld の必要事象数 ＋ 指数分布・一様登録での必要例数
  - 非劣性（ni_binary）: 反応率の差に対する非劣性マージン
  - 組み合わせ（combine）: 主要・key secondary の計算結果 JSON と安全性曝露の割当を受け取り、
    最終例数 = 最大値 とどれが効いたかを出す

使い方（例: AD, 2 用量 + プラセボ, 1:1:1, co-primary IGA と EASI-75）:
  uv run scripts/sample_size.py coprimary \
      --p-control 0.10 0.15 --p-active 0.30 0.45 \
      --rho 0.6 --arms-active 2 --ratio 1 --alpha 0.05 --alpha-split bonferroni \
      --power 0.90 --dropout 0.10 --missing nri --out waypoints/sample_size.json

出力の JSON には入力（仮定）・方法・群ごとの例数・総数・感度表をすべて書く。
仮定の出典は呼び出し側（Step 4）が protocol_facts.json に書く。この script は出典を作らない。

近似: 正規近似（非プール分散）。相関は検定統計量どうしの相関として扱う（保守側は rho=0）。
本番の例数は統計担当がシミュレーション等で確認すること。
"""
from __future__ import annotations

import argparse
import json
import math
import sys

from scipy.stats import multivariate_normal, norm


def crit(alpha: float, sides: int) -> float:
    return norm.ppf(1 - alpha / sides)


def z_mean_binary(p_c: float, p_a: float, n_c: float, n_a: float) -> float:
    se = math.sqrt(p_c * (1 - p_c) / n_c + p_a * (1 - p_a) / n_a)
    return abs(p_a - p_c) / se


def z_mean_cont(delta: float, sd: float, n_c: float, n_a: float) -> float:
    return abs(delta) / (sd * math.sqrt(1 / n_c + 1 / n_a))


def joint_power(mus: list[float], c: float, rho: float) -> float:
    if len(mus) == 1:
        return float(norm.cdf(mus[0] - c))
    cov = [[1.0, rho], [rho, 1.0]]
    return float(multivariate_normal(mean=[0, 0], cov=cov).cdf([mus[0] - c, mus[1] - c]))


def per_comparison_alpha(alpha: float, m: int, how: str) -> float:
    if m <= 1 or how == "none":
        return alpha
    if how == "bonferroni":
        return alpha / m
    raise ValueError(how)


def solve(kind, p_c, p_a, delta, sd, rho, m, ratio, alpha, split, sides, power, dropout, missing, n_max=20000):
    a = per_comparison_alpha(alpha, m, split)
    c = crit(a, sides)
    if missing == "nri" and kind != "continuous":
        p_c = [p * (1 - dropout) for p in p_c]
        p_a = [p * (1 - dropout) for p in p_a]
    for n_c in range(2, n_max):
        n_a = n_c * ratio
        if kind == "continuous":
            mus = [z_mean_cont(delta, sd, n_c, n_a)]
        else:
            mus = [z_mean_binary(pc, pa, n_c, n_a) for pc, pa in zip(p_c, p_a)]
        pw = joint_power(mus, c, rho)
        if pw >= power:
            n_a = math.ceil(n_a)
            per_arm = {"control": n_c, "each_active": n_a}
            total = n_c + n_a * m
            if missing == "inflate":
                total_adj = math.ceil(total / (1 - dropout))
            else:
                total_adj = total
            return {
                "alpha_per_comparison": a,
                "critical_value": c,
                "achieved_power": round(pw, 4),
                "effective_rates_after_nri": {"control": p_c, "active": p_a} if kind != "continuous" else None,
                "n_per_arm": per_arm,
                "n_total": total,
                "n_total_enrolled": total_adj,
            }
    raise RuntimeError("n_max に達した（効果が小さすぎる）")


def solve_tte(hr, alloc, alpha, sides, power, median_c, accrual, follow_up, dropout):
    """Schoenfeld: D = (z_a + z_b)^2 / (p(1-p) (ln HR)^2). p = 実薬群の割合。"""
    za, zb = crit(alpha, sides), norm.ppf(power)
    p = alloc / (1 + alloc)
    events = math.ceil((za + zb) ** 2 / (p * (1 - p) * math.log(hr) ** 2))
    out = {"events_required": events, "alloc_active_fraction": round(p, 4)}
    if median_c and accrual is not None and follow_up is not None:
        lam_c = math.log(2) / median_c
        lam_a = lam_c * hr
        def pev(lam):
            if accrual == 0:
                return 1 - math.exp(-lam * follow_up)
            return 1 - (math.exp(-lam * follow_up) - math.exp(-lam * (accrual + follow_up))) / (lam * accrual)
        pe = (1 - p) * pev(lam_c) + p * pev(lam_a)
        n = math.ceil(events / pe)
        out.update({"prob_event_pooled": round(pe, 4), "n_total": n,
                    "n_total_enrolled": math.ceil(n / (1 - dropout))})
    return out


def solve_ni(p_c, p_a, margin, ratio, alpha, sides, power, dropout):
    """非劣性: H0: p_a - p_c <= -margin。n_c = (za+zb)^2 (pc qc + pa qa / k) / (pa - pc + margin)^2"""
    za, zb = crit(alpha, sides), norm.ppf(power)
    d = p_a - p_c + margin
    assert d > 0, "p_active - p_control + margin must be > 0"
    n_c = math.ceil((za + zb) ** 2 * (p_c * (1 - p_c) + p_a * (1 - p_a) / ratio) / d ** 2)
    n_a = math.ceil(n_c * ratio)
    return {"n_per_arm": {"control": n_c, "active": n_a}, "n_total": n_c + n_a,
            "n_total_enrolled": math.ceil((n_c + n_a) / (1 - dropout))}


def combine(inputs, exposure_n, exposure_reason, out):
    rows = []
    for path in inputs:
        d = json.load(open(path, encoding="utf-8"))
        r = d["result"]
        n = r.get("n_total_enrolled") or r.get("n_total")
        rows.append({"component": d.get("label") or path, "kind": d["inputs"]["kind"], "n_total": n, "source": path})
    # exposure: None = not decided ([TBD], excluded from max but listed); 0 = not applicable (listed with reason)
    rows.append({"component": "safety exposure allocated to this trial", "kind": "exposure",
                 "n_total": exposure_n if exposure_n is not None else 0,
                 "status": "TBD (unallocated)" if exposure_n is None else ("not applicable" if exposure_n == 0 else "allocated"),
                 "source": exposure_reason or "[TBD]"})
    final = max(rows, key=lambda x: x["n_total"])
    res = {"rule": "final N = max(components)", "components": rows, "final_n_total": final["n_total"], "driven_by": final["component"]}
    s = json.dumps(res, ensure_ascii=False, indent=2)
    if out:
        open(out, "w", encoding="utf-8").write(s + "\n")
    print(s)
    return 0


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if argv and argv[0] == "combine":
        cp = argparse.ArgumentParser(prog="sample_size.py combine")
        cp.add_argument("--inputs", nargs="+", required=True, help="result JSONs from this script")
        cp.add_argument("--exposure-n", type=int, help="participants needed in this trial for safety exposure (0 if N/A)")
        cp.add_argument("--exposure-reason", default="", help="why (ICH E1 share / N/A reason)")
        cp.add_argument("--out")
        c = cp.parse_args(argv[1:])
        return combine(c.inputs, c.exposure_n, c.exposure_reason, c.out)
    ap = argparse.ArgumentParser(description="Phase 3 sample size (binary / continuous / co-primary, multi-arm, NRI)")
    ap.add_argument("kind", choices=["binary", "coprimary", "continuous", "tte", "ni_binary"])
    ap.add_argument("--hr", type=float, help="target hazard ratio (tte)")
    ap.add_argument("--median-control", type=float, help="control median time (months) (tte)")
    ap.add_argument("--accrual", type=float, help="accrual duration (months) (tte)")
    ap.add_argument("--follow-up", type=float, help="minimum follow-up after last enrolled (months) (tte)")
    ap.add_argument("--margin", type=float, help="non-inferiority margin on risk difference (ni_binary)")
    ap.add_argument("--p-control", type=float, nargs="+", help="control response rate(s); 2 values for coprimary")
    ap.add_argument("--p-active", type=float, nargs="+", help="active response rate(s); 2 values for coprimary")
    ap.add_argument("--delta", type=float, help="mean difference (continuous)")
    ap.add_argument("--sd", type=float, help="standard deviation (continuous)")
    ap.add_argument("--rho", type=float, default=0.0, help="correlation between the two test statistics (coprimary). 0 = conservative")
    ap.add_argument("--arms-active", type=int, default=1, help="number of active arms (doses) each compared with control")
    ap.add_argument("--ratio", type=float, default=1.0, help="allocation ratio active:control per active arm")
    ap.add_argument("--alpha", type=float, default=0.05)
    ap.add_argument("--alpha-split", choices=["none", "bonferroni"], default="bonferroni")
    ap.add_argument("--sides", type=int, choices=[1, 2], default=2)
    ap.add_argument("--power", type=float, default=0.90)
    ap.add_argument("--dropout", type=float, default=0.10)
    ap.add_argument("--missing", choices=["nri", "inflate"], default="nri",
                    help="nri: dilute response rates by dropout (binary); inflate: divide N by (1-dropout)")
    ap.add_argument("--sens-rho", type=float, nargs="*", default=[0.0, 0.3, 0.5, 0.7])
    ap.add_argument("--out", help="write JSON here (otherwise stdout)")
    ap.add_argument("--label", help="name of this component (e.g. 'primary: PFS', 'key secondary: OS')")
    a = ap.parse_args(argv)

    if a.kind in ("tte", "ni_binary"):
        if a.kind == "tte":
            assert a.hr and 0 < a.hr < 1, "tte needs --hr in (0,1)"
            res = solve_tte(a.hr, a.ratio, a.alpha, a.sides, a.power, a.median_control, a.accrual, a.follow_up, a.dropout)
            method = "Schoenfeld events; exponential survival with uniform accrual for N"
        else:
            assert a.margin and a.p_control and a.p_active, "ni_binary needs --margin --p-control --p-active"
            res = solve_ni(a.p_control[0], a.p_active[0], a.margin, a.ratio, a.alpha, a.sides, a.power, a.dropout)
            method = "normal approximation, non-inferiority on risk difference"
        out = {"label": a.label, "method": method, "inputs": vars(a), "result": res,
               "caveat": "Planning estimate. Assumptions must carry sources; biostatistician review required."}
        s = json.dumps(out, ensure_ascii=False, indent=2)
        if a.out:
            open(a.out, "w", encoding="utf-8").write(s + "\n")
        print(s)
        return 0

    if a.kind == "binary":
        assert a.p_control and a.p_active and len(a.p_control) == 1 == len(a.p_active), "binary needs 1 value each"
    if a.kind == "coprimary":
        assert a.p_control and a.p_active and len(a.p_control) == 2 == len(a.p_active), "coprimary needs 2 values each"
    if a.kind == "continuous":
        assert a.delta is not None and a.sd is not None, "continuous needs --delta and --sd"

    args = dict(kind=a.kind, p_c=a.p_control or [], p_a=a.p_active or [], delta=a.delta, sd=a.sd, m=a.arms_active,
                ratio=a.ratio, alpha=a.alpha, split=a.alpha_split, sides=a.sides, power=a.power,
                dropout=a.dropout, missing=a.missing if a.kind != "continuous" or a.missing == "inflate" else "inflate")
    main_res = solve(rho=a.rho, **args)
    sens = []
    if a.kind == "coprimary":
        for r in a.sens_rho:
            res = solve(rho=r, **args)
            sens.append({"rho": r, "n_per_arm_control": res["n_per_arm"]["control"], "n_total": res["n_total_enrolled"]})
    out = {
        "label": a.label,
        "method": "normal approximation, unpooled variance; coprimary = joint power via bivariate normal",
        "inputs": vars(a),
        "result": main_res,
        "sensitivity_rho": sens,
        "caveat": "Planning estimate. Assumptions must carry sources in protocol_facts.json; biostatistician review required.",
    }
    s = json.dumps(out, ensure_ascii=False, indent=2)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(s + "\n")
    print(s)


if __name__ == "__main__":
    sys.exit(main())
