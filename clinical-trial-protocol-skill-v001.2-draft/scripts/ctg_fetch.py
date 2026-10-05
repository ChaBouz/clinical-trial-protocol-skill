# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
ctg_fetch.py  (v001.2 DRAFT 2026-10-03, ★この環境では未検証)

ClinicalTrials.gov API v2 から 1 試験の全記録（designModule・armsInterventionsModule・
resultsSection を含む）を取り、そのまま保存する。MCP の get_trial_details が返さない
群・用量・割付・盲検・結果の数値を取るための「根本の」取り方。

  uv run scripts/ctg_fetch.py NCT05398445 --out waypoints/ctg/NCT05398445.api.json

検索（MCP が無いときに参照試験の候補を探す。2026-10-04 追加・★通信できる環境で未検証）:
  uv run scripts/ctg_fetch.py search --cond "<疾患の英語名>" --phase PHASE3 \
      --status COMPLETED,ACTIVE_NOT_RECRUITING --max 25 --out waypoints/ctg/_search.json

ネットワークが clinicaltrials.gov に出られない環境では失敗する（その場合は 01-research.md の
1a-2 の「MCP で値を当てる」方法に落ちる）。失敗したら例外の型と相手の返事の本文を表示して exit 2。
"""
import argparse
import json
import sys
import urllib.error
import urllib.request

API = "https://clinicaltrials.gov/api/v2/studies/{nct}?format=json"
SEARCH = "https://clinicaltrials.gov/api/v2/studies"


def get_json(url):
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "ctp-skill/1.2"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def search(argv):
    """MCP が無いときの参照試験の検索（2026-10-04 追加。★この環境では通信できず未検証）。
    uv run scripts/ctg_fetch.py search --cond "neovascular age-related macular degeneration" --phase PHASE3 \
        --status COMPLETED,ACTIVE_NOT_RECRUITING --max 25 --out waypoints/ctg/_search.json"""
    import urllib.parse
    ap = argparse.ArgumentParser(prog="ctg_fetch.py search")
    ap.add_argument("--cond", required=True, help="疾患（英語）")
    ap.add_argument("--intr", help="介入（薬剤名・機序。任意）")
    ap.add_argument("--phase", default="PHASE3")
    ap.add_argument("--status", default="COMPLETED,ACTIVE_NOT_RECRUITING")
    ap.add_argument("--max", type=int, default=25)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    q = {"query.cond": a.cond, "query.term": f"AREA[Phase]{a.phase}", "filter.overallStatus": a.status,
         "pageSize": str(min(a.max, 100)), "format": "json",
         "fields": "NCTId,BriefTitle,Phase,OverallStatus,StartDate,EnrollmentCount,HasResults,Condition,InterventionName"}
    if a.intr:
        q["query.intr"] = a.intr
    url = SEARCH + "?" + urllib.parse.urlencode(q)
    try:
        d = get_json(url)
    except urllib.error.HTTPError as e:
        print(f"HTTPError {e.code}: {e.read().decode('utf-8', 'replace')[:500]}", file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001
        print(f"{type(e).__name__}: {e}", file=sys.stderr)
        return 2
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump({"query": q, "result": d}, f, ensure_ascii=False, indent=2)
    for st in d.get("studies", []):
        ps = st.get("protocolSection", {})
        idm, stm = ps.get("identificationModule", {}), ps.get("statusModule", {})
        print(json.dumps({"nct": idm.get("nctId"), "title": idm.get("briefTitle"),
                          "status": stm.get("overallStatus"), "start": (stm.get("startDateStruct") or {}).get("date"),
                          "has_results": st.get("hasResults")}, ensure_ascii=False))
    return 0


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if argv and argv[0] == "search":
        return search(argv[1:])
    ap = argparse.ArgumentParser()
    ap.add_argument("nct")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    url = API.format(nct=a.nct.upper())
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "ctp-skill/1.2"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            body = r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"HTTPError {e.code}: {e.read().decode('utf-8', 'replace')[:500]}", file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001
        print(f"{type(e).__name__}: {e}", file=sys.stderr)
        return 2
    d = json.loads(body)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    ps = d.get("protocolSection", {})
    design = ps.get("designModule", {})
    arms = ps.get("armsInterventionsModule", {})
    summary = {
        "nct": a.nct,
        "allocation": design.get("designInfo", {}).get("allocation"),
        "masking": design.get("designInfo", {}).get("maskingInfo", {}).get("masking"),
        "model": design.get("designInfo", {}).get("interventionModel"),
        "n_arm_groups": len(arms.get("armGroups", [])),
        "has_results_section": "resultsSection" in d,
    }
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
