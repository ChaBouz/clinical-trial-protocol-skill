# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
check_prec_ids.py  (v001.2 DRAFT 2026-10-05)

本文・疾患パック・waypoints の中の [PREC:<ID>] ／ PREC:<ID> が、実在する先例の ID かを照らす。
記憶から書いた先例・打ち間違い・材料の作り直しで消えた ID を機械で止めるため。

  uv run scripts/check_prec_ids.py disease_packs/atopic_dermatitis.yaml                       # パックは名前から適応症が決まる
  uv run scripts/check_prec_ids.py --indication atopic_dermatitis <作業フォルダ>/waypoints/protocol_complete.md

★照らす相手は**同じ適応症の材料だけ**（別の適応症の先例の ID を既知に数えない）:
  disease_packs/<名前>.yaml を照らすとき … precedents/<名前>/prec_ids.txt
  ほかのファイル（--indication <名前> が必須）… precedents/<名前>/prec_ids.txt ＋ disease_packs/<名前>.yaml に書かれた PREC の ID
ID の書式: 空白・]・カンマ・読点を含まない文字列。「PREC:A:s1/Q4a, Q4e」のように、カンマの後の
           短い続き（数字を含み、: と / を含まない語）は、直前の ID の最後の / の後ろを置き換えた ID として照らす。
           カンマの後が : と / を含む語なら、それも ID として照らす。
終わり方: 実在しない ID が 1 つでもあれば exit 1。照らす相手が無いとき（その適応症の先例もパックの PREC も無い）は
          「照らす材料なし（未検証）」と表示して exit 0（ID の数は表示する）。引数の誤りは exit 2。
"""
import argparse
import pathlib
import re
import sys

SKILL = pathlib.Path(__file__).resolve().parent.parent
STOP = r"\s\],;、。)）\"'{}<>`"
HEAD = re.compile(rf"PREC:([^{STOP}]+)")
CONT = re.compile(rf"\s*,\s*([^{STOP}]+)")


def ids_in(text: str):
    """(行番号, ID) を返す"""
    for ln, line in enumerate(text.splitlines(), 1):
        for m in HEAD.finditer(line):
            first = m.group(1).rstrip(".")
            yield ln, first
            pos, last = m.end(), first
            while True:
                c = CONT.match(line, pos)
                if not c:
                    break
                tok = c.group(1).rstrip(".")
                if ":" in tok and "/" in tok:
                    last = tok
                elif ":" not in tok and "/" not in tok and re.search(r"\d", tok) and "/" in last:
                    last = last.rsplit("/", 1)[0] + "/" + tok
                else:
                    break
                yield ln, last
                pos = c.end()


def prec_ids(key: str) -> set:
    p = SKILL / "precedents" / key / "prec_ids.txt"
    return {x.strip() for x in p.read_text(encoding="utf-8").splitlines() if x.strip()} if p.is_file() else set()


def main():
    ap = argparse.ArgumentParser(description="[PREC] の ID が、同じ適応症の先例の材料（と疾患パック）に実在するか")
    ap.add_argument("--indication", help="適応症の名前（indication_key）。疾患パック以外のファイルを照らすときは必須")
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    packs = SKILL / "disease_packs"
    total_n, unverified, bad = 0, 0, []
    for f in a.files:
        fp = pathlib.Path(f).resolve()
        is_pack = fp.parent == packs.resolve() and fp.suffix == ".yaml" and not fp.name.startswith("_")
        key = fp.stem if is_pack else a.indication
        if not key:
            print(f"[引数の誤り] {f} は疾患パックではないので --indication <名前> が要る", file=sys.stderr)
            sys.exit(2)
        known = prec_ids(key)
        pack = packs / f"{key}.yaml"
        if not is_pack and pack.is_file():
            known |= {i for _, i in ids_in(pack.read_text(encoding="utf-8"))}
        found = list(ids_in(fp.read_text(encoding="utf-8")))
        total_n += len(found)
        if not known:
            unverified += len(found)
            if found:
                print(f"{f}: PREC の ID {len(found)} 個は照らす材料なし（未検証。precedents/{key}/ が無い）")
            continue
        bad += [f"{f}:{ln}: {i}" for ln, i in found if i not in known]
    print(f"PREC の ID {total_n} 個のうち {total_n - unverified} 個を照らした（同じ適応症の材料だけ）。実在しない: {len(bad)}")
    for b in bad:
        print("  -", b)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
