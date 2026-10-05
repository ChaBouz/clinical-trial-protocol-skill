# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
validate_precedents.py  (v001.2 DRAFT 2026-10-04)

先例の材料のフォルダ（precedents/<indication_key>/）が、precedents/README.md の形の約束を満たすかを検査する。
材料をどこから作っても（手作り・別の道具の出力）、置いたら 1 回回す。

  uv run scripts/validate_precedents.py precedents/<indication_key>
  uv run scripts/validate_precedents.py precedents/_template        # 雛形そのものも通る

検査:
  V1 index.md・prec_ids.txt・topics/*.md（1 つ以上）が在る
  V2 index.md に「M11 の節」の列を持つ表があり、topics/ の各ファイルがその表に載っている
  V3 prec_ids.txt の ID に重複・空白が無い
  V4 索引の見出し「### <n>. [PREC:<ID>] …」の ID が、すべて prec_ids.txt に在る
  V5 索引の各項目に「- 本文: `<道>` <a>–<b> 行」が在り、その道のファイルが在り、a≦b≦行数で、
     その範囲に逐語の囲み（~~~ で始まる行）が少なくとも 1 つ在る
1 つでも外れれば exit 1。
"""
import pathlib
import re
import sys

ENTRY = re.compile(r"^### \d+\. \[PREC:([^\]]+)\]", re.M)
PTR = re.compile(r"^- \*{0,2}本文: `([^`]+)` (\d+)[–\-](\d+) 行", re.M)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    root = pathlib.Path(sys.argv[1])
    errs, n_entries = [], 0
    idx, ids_p, tdir = root / "index.md", root / "prec_ids.txt", root / "topics"
    topics = sorted(tdir.glob("*.md")) if tdir.is_dir() else []
    for p, what in ((idx, "index.md"), (ids_p, "prec_ids.txt")):
        if not p.is_file():
            errs.append(f"V1 {what} が無い")
    if not topics:
        errs.append("V1 topics/*.md が 1 つも無い")
    if errs:
        report(root, errs, 0)
    text = idx.read_text(encoding="utf-8")
    if not re.search(r"^\|.*M11 の節.*\|", text, re.M):
        errs.append("V2 index.md に「M11 の節」の列を持つ表が無い")
    for t in topics:
        if f"topics/{t.name}" not in text:
            errs.append(f"V2 index.md の表に topics/{t.name} が載っていない")
    raw = [x for x in ids_p.read_text(encoding="utf-8").splitlines() if x.strip()]
    ids = set()
    for x in raw:
        if x != x.strip() or " " in x:
            errs.append(f"V3 ID に空白: {x!r}")
        if x.strip() in ids:
            errs.append(f"V3 ID が重複: {x}")
        ids.add(x.strip())
    cache = {}
    for t in topics:
        body = t.read_text(encoding="utf-8")
        heads = list(ENTRY.finditer(body))
        for i, h in enumerate(heads):
            n_entries += 1
            pid = h.group(1)
            where = f"{t.name}: [PREC:{pid}]"
            if pid not in ids:
                errs.append(f"V4 {where} が prec_ids.txt に無い")
            block = body[h.end(): heads[i + 1].start() if i + 1 < len(heads) else len(body)]
            m = PTR.search(block)
            if not m:
                errs.append(f"V5 {where} に「- 本文: `<道>` <a>–<b> 行」が無い")
                continue
            rel, a, b = m.group(1), int(m.group(2)), int(m.group(3))
            f = root / rel
            if not f.is_file():
                errs.append(f"V5 {where} の本文のファイルが無い: {rel}")
                continue
            lines = cache.setdefault(rel, f.read_text(encoding="utf-8").splitlines())
            if not (1 <= a <= b <= len(lines)):
                errs.append(f"V5 {where} の行の範囲 {a}–{b} がファイルの行数 {len(lines)} を超える")
            elif not any(l.startswith("~~~") for l in lines[a - 1:b]):
                errs.append(f"V5 {where} の行の範囲 {a}–{b} に逐語の囲み（~~~）が無い")
    report(root, errs, n_entries)


def report(root, errs, n):
    print(f"{root}: 索引の項目 {n} 個を検査。問題 {len(errs)} 件")
    for e in errs[:50]:
        print("  -", e)
    if len(errs) > 50:
        print(f"  …ほか {len(errs) - 50} 件")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
