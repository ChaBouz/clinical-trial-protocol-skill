# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""
check_protocol.py  (v001.2 DRAFT 2026-10-03)

連結後のプロトコル（markdown）を、枠（assets/section_spec_m11.yaml）と
事実の正典（waypoints/protocol_facts.json）に突き合わせる整合性検査。
食い違いが 1 つでもあれば exit 1。[TBD] の数は申告するだけ（0 でなくてよい）。

  uv run scripts/check_protocol.py waypoints/protocol_complete.md \
      --spec assets/section_spec_m11.yaml --facts waypoints/protocol_facts.json

検査:
  C1 見出し: spec の 14 節（＋2 段目）が、その番号・その順で全部ある
  C2 評価項目の文: facts の各 endpoint.text が 1.1・3・10 節のすべてに逐語で出る
  C3 時点: facts の各 endpoint.timepoint が 1.3（SoA）節に出る
  C4 救済療法 ↔ 中間事象: facts.rescue の各行の ice が facts.estimands の ice に在る（逆も）
  C5 相互参照: 本文の "Section N(.N)*" が実在の見出し番号を指す
  C6 出典ラベル: depth=full の各 2 段目節に [CTG|PACK|PREC|STD|DERIVED|USER|PRIOR|INSTR|TBD] が 1 つ以上
  C7 粒度: 節の語数（出典ラベルを除く）が「目安頁 × 語/頁 × min-ratio」未満なら fail。
     目安頁 = 2 段目は spec の target_pages（範囲なら下限）、1 段目は ref_pages。
     疾患領域の重み（design_archetypes の emphasis に頁数があれば）で上書き。
     語/頁の既定 250 は参照プロトコル NCT05398445 の本文 82 頁・21,418 語（261 語/頁, pdftotext で 2026-10-03 計測）から丸めた値。
     12〜14 節（付録）は申告のみで fail にしない。
  申告: [TBD] の数（節ごと）、ラベルごとの数
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict

import yaml

LABELS = ["CTG", "PACK", "PREC", "STD", "DERIVED", "USER", "PRIOR", "INSTR", "TBD"]
LABEL_RE = re.compile(r"\[(" + "|".join(LABELS) + r")(?::[^\]]*)?\]")
HEAD_RE = re.compile(r"^(#{1,4})\s+(\d+(?:\.\d+)*)\.?\s+(.+?)\s*$")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def spec_ids(spec):
    out = []
    for s in spec["sections"]:
        if s["id"] == "TP":
            continue
        out.append((s["id"], s["title"]))
        for ss in s.get("subsections", []) or []:
            out.append((ss["id"], ss["title"], ss.get("depth")))
    return out


def split_sections(md: str):
    """見出し番号 -> 本文（その見出しから次の同じか上の階層の見出しまで）"""
    lines = md.split("\n")
    heads = []
    for i, l in enumerate(lines):
        m = HEAD_RE.match(l)
        if m:
            heads.append((i, m.group(2), m.group(3)))
    body = {}
    for k, (i, num, _t) in enumerate(heads):
        depth = num.count(".")
        j = len(lines)
        for (i2, num2, _t2) in heads[k + 1:]:
            if num2.count(".") <= depth:
                j = i2
                break
        body[num] = "\n".join(lines[i:j])
    return heads, body


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("protocol")
    ap.add_argument("--spec", required=True)
    ap.add_argument("--facts", required=True)
    ap.add_argument("--archetypes", help="design_archetypes.yaml（省略時は spec と同じフォルダ）")
    ap.add_argument("--words-per-page", type=int, default=250)
    ap.add_argument("--min-ratio", type=float, default=0.5)
    ap.add_argument("--only-c7", action="store_true", help="書きかけのファイル（1 回分の節）に粒度だけを測る。C1〜C6 は回さない")
    a = ap.parse_args(argv)

    md = open(a.protocol, encoding="utf-8").read()
    spec = yaml.safe_load(open(a.spec, encoding="utf-8"))
    facts = json.load(open(a.facts, encoding="utf-8"))
    heads, body = split_sections(md)
    present = [h[1] for h in heads]
    fails = []

    # C1
    expected = spec_ids(spec)
    order = [e[0] for e in expected]
    missing = [e for e in order if e not in present]
    if missing:
        fails.append(("C1", f"見出しが無い: {missing}"))
    seen = [p for p in present if p in order]
    if seen != [o for o in order if o in seen]:
        fails.append(("C1", "見出しの順番が spec と違う"))

    # C2 / C3
    for ep in facts.get("endpoints", []):
        t = norm(ep["text"])
        for sec in ("1.1", "3", "10"):
            if t not in norm(body.get(sec, "")):
                fails.append(("C2", f"評価項目 {ep.get('id')} の文が {sec} 節に逐語で無い"))
        tp = ep.get("timepoint")
        if tp and norm(tp) not in norm(body.get("1.3", "")):
            fails.append(("C3", f"評価項目 {ep.get('id')} の時点 '{tp}' が SoA(1.3) に無い"))

    # C4
    ices = {norm(e["ice"]) for e in facts.get("estimands", {}).get("intercurrent_events", [])}
    rescue_ices = {norm(r["estimand_ice"]) for r in facts.get("rescue", [])}
    for r in rescue_ices - ices:
        fails.append(("C4", f"救済療法の行の中間事象 '{r}' が estimand に無い"))
    if facts.get("rescue") and not (ices & rescue_ices):
        fails.append(("C4", "estimand に救済療法の中間事象が 1 つも無い"))

    # C5
    nums = set(present)
    for m in re.finditer(r"Section\s+(\d+(?:\.\d+)*)", md):
        if m.group(1) not in nums:
            fails.append(("C5", f"相互参照先が無い: Section {m.group(1)}"))

    # C6
    for e in expected:
        if len(e) == 3 and e[2] == "full" and e[0] in body:
            if not LABEL_RE.search(body[e[0]]):
                fails.append(("C6", f"{e[0]} 節に出典ラベルが 1 つも無い"))

    # C7
    import os
    arch_path = a.archetypes or os.path.join(os.path.dirname(os.path.abspath(a.spec)), "design_archetypes.yaml")
    emph = {}
    fam = (facts.get("design", {}).get("archetype", {}) or {}).get("family")
    if fam and os.path.exists(arch_path):
        arch = yaml.safe_load(open(arch_path, encoding="utf-8"))
        emph = arch.get("therapeutic_area_families", {}).get(fam, {}).get("emphasis", {}) or {}

    def first_num(x):
        m = re.search(r"(\d+(?:\.\d+)?)", str(x))
        return float(m.group(1)) if m else None

    def emph_pages(x):
        # 重み付けの文字列から頁数だけを読む（"3–6 pp" → 3）。"RECIST 1.1" の 1.1 を頁と誤読しない
        m = re.search(r"(\d+(?:\.\d+)?)\s*(?:[–-]\s*\d+(?:\.\d+)?)?\s*pp\b", str(x))
        return float(m.group(1)) if m else None

    granularity = []
    for sec in spec["sections"]:
        if sec["id"] == "TP":
            continue
        cands = [(sec["id"], sec.get("ref_pages"))]
        cands += [(ss["id"], ss.get("target_pages")) for ss in (sec.get("subsections") or [])]
        for sid, tp in cands:
            pages = emph_pages(emph[sid]) if sid in emph and emph_pages(emph[sid]) else first_num(tp) if tp is not None else None
            if not pages or sid not in body:
                continue
            words = len(LABEL_RE.sub("", body[sid]).split())
            need = pages * a.words_per_page * a.min_ratio
            ratio = words / (pages * a.words_per_page)
            granularity.append({"section": sid, "words": words, "target_pages": pages, "ratio_to_target": round(ratio, 2)})
            top = int(sid.split(".")[0])
            if words < need and top < 12:
                fails.append(("C7", f"{sid} 節の語数 {words} が目安 {pages:g} 頁×{a.words_per_page} 語の {int(a.min_ratio*100)}% 未満（比 {ratio:.2f}）"))

    # 申告
    tbd = defaultdict(int)
    for num, txt in body.items():
        if num.count(".") == 0:
            tbd[num] = len(re.findall(r"\[TBD", txt))
    labels = Counter(m.group(1) for m in LABEL_RE.finditer(md))

    # 申告 C8（fail にはしない）: 数値を含むのに出典ラベルが DERIVED だけの段落。E1（数値は出典があるときだけ）の見落とし候補
    num_re = re.compile(r"(?<![\w.])\d+(?:\.\d+)?\s*(?:%|×|mg|ms|days?|weeks?|months?|years?|hours?|mm|cells)")
    derived_only_numbers = []
    for para in re.split(r"\n\s*\n", md):
        labs = {m.group(1) for m in LABEL_RE.finditer(para)}
        if labs and labs <= {"DERIVED"}:
            hits = num_re.findall(LABEL_RE.sub("", para))
            if hits:
                derived_only_numbers.append({"numbers": hits[:5], "text": LABEL_RE.sub("", para).strip()[:120]})

    if a.only_c7:
        fails = [f for f in fails if f[0] == "C7"]

    report = {
        "headings_found": len(present),
        "headings_expected": len(order),
        "fails": [{"check": c, "detail": d} for c, d in fails],
        "tbd_by_top_section": dict(tbd),
        "labels": dict(labels),
        "granularity": granularity,
        "derived_only_numbers": derived_only_numbers,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
