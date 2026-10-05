# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""
list_indications.py  (v001.2 DRAFT 2026-10-04)

Step 0 で「適応症の名前（indication_key）」を決めるための一覧と、名前の照合。

  uv run scripts/list_indications.py                          # 在る名前の一覧（疾患パック・先例の材料・別名）
  uv run scripts/list_indications.py --match "アトピー性皮膚炎"   # 利用者の言葉が、名前か別名に一致するか

一覧に出すもの（_ で始まる雛形は除く）:
  disease_packs/<名前>.yaml   … meta.status（confirmed / draft）と meta.aliases（別名）
  precedents/<名前>/index.md  … 「- 別名: a, b, c」の行（任意）

--match の照合は**機械の完全一致だけ**（大文字小文字・全角半角・空白・ハイフン・下線の違いは無視）。
似た病名の推測はしない。一致しなければ「一致なし」と出す → Claude が医学的に近い候補を示し、
**利用者が確認してから**名前を決める（00-initialize.md の手順 2）。
終わり方: 一致あり exit 0 ／ 一致なし exit 3 ／ 2 つ以上の名前に一致 exit 4（利用者に選んでもらう）。
"""
import argparse
import json
import pathlib
import re
import sys
import unicodedata

import yaml

SKILL = pathlib.Path(__file__).resolve().parent.parent


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s).strip().lower()
    return re.sub(r"[\s\-_‐－・]+", "", s)


def collect():
    ent = {}
    for p in sorted((SKILL / "disease_packs").glob("[!_]*.yaml")):
        meta = (yaml.safe_load(open(p, encoding="utf-8")) or {}).get("meta", {}) or {}
        e = ent.setdefault(p.stem, {"pack": None, "precedents": False, "aliases": []})
        e["pack"] = meta.get("status", "?")
        e["aliases"] += [a for a in (meta.get("aliases") or []) if a not in e["aliases"]]
    pdir = SKILL / "precedents"
    for d in sorted(x for x in pdir.glob("[!_]*") if x.is_dir()) if pdir.is_dir() else []:
        e = ent.setdefault(d.name, {"pack": None, "precedents": False, "aliases": []})
        idx = d / "index.md"
        e["precedents"] = idx.is_file()
        if idx.is_file():
            m = re.search(r"^- 別名: (.+)$", idx.read_text(encoding="utf-8"), re.M)
            if m:
                e["aliases"] += [a.strip() for a in m.group(1).split(",") if a.strip() and a.strip() not in e["aliases"]]
    return ent


def main():
    ap = argparse.ArgumentParser(description="適応症の名前（indication_key）の一覧と照合")
    ap.add_argument("--match", help="利用者が書いた適応症の言葉（英語・日本語・略号どれでも）")
    ap.add_argument("--json", action="store_true", help="JSON で出す")
    a = ap.parse_args()
    ent = collect()
    if a.match is None:
        if a.json:
            print(json.dumps(ent, ensure_ascii=False, indent=1))
            return
        if not ent:
            print("名前はまだありません（疾患パックも先例の材料も無い）。適応症から新しい名前を作る。")
            return
        print(f"{'名前（indication_key）':28} {'疾患パック':10} {'先例':4} 別名")
        for k, e in ent.items():
            print(f"{k:28} {e['pack'] or '—':10} {'在り' if e['precedents'] else '—':4} {', '.join(e['aliases']) or '—'}")
        return
    q = norm(a.match)
    hits = [k for k, e in ent.items() if q == norm(k) or any(q == norm(x) for x in e["aliases"])]
    if len(hits) == 1:
        e = ent[hits[0]]
        print(f"一致: {hits[0]}（疾患パック {e['pack'] or '無し'} ／ 先例 {'在り' if e['precedents'] else '無し'}）")
        sys.exit(0)
    if len(hits) > 1:
        print("2 つ以上の名前に一致: " + ", ".join(hits) + " → 利用者に選んでもらう")
        sys.exit(4)
    print(f"一致なし: 「{a.match}」は、在る名前にも別名にも完全には一致しない。")
    print("在る名前: " + (", ".join(f"{k}（別名: {', '.join(e['aliases']) or '—'}）" for k, e in ent.items()) or "なし"))
    print("→ Claude が医学的に同じ・近い候補を示し、利用者の確認を取ってから名前を決める（推測で決めない）")
    sys.exit(3)


if __name__ == "__main__":
    main()
