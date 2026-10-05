# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""validate_pack.py — 疾患パック（確定版・下書き）が _schema.yaml の required を満たすか。
  uv run scripts/validate_pack.py disease_packs/atopic_dermatitis.yaml
欠けたキー・src の無い行・archetype/family の名前違いがあれば exit 1。"""
import sys, yaml, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
schema = yaml.safe_load(open(root / "disease_packs/_schema.yaml", encoding="utf-8"))
arch = yaml.safe_load(open(root / "assets/design_archetypes.yaml", encoding="utf-8"))
pack = yaml.safe_load(open(sys.argv[1], encoding="utf-8"))
errs = []
for k, v in schema["required"].items():
    if k not in pack:
        errs.append(f"missing key: {k}")
    elif isinstance(v, dict):
        for kk in v:
            if kk not in (pack[k] or {}):
                errs.append(f"missing key: {k}.{kk}")
m = pack.get("meta", {})
if m.get("therapeutic_area_family") not in arch["therapeutic_area_families"]:
    errs.append(f"unknown therapeutic_area_family: {m.get('therapeutic_area_family')}")
if m.get("endpoint_archetype") not in arch["endpoint_types"]:
    errs.append(f"unknown endpoint_archetype: {m.get('endpoint_archetype')}")
def rows(x):
    if isinstance(x, list):
        for r in x:
            if isinstance(r, dict) and "text" in r or isinstance(r, dict) and "therapy" in r or isinstance(r, dict) and "class" in r:
                yield r
    elif isinstance(x, dict):
        for v in x.values():
            yield from rows(v)
nosrc = [r for r in rows({k: pack.get(k) for k in ("inclusion", "exclusion", "rescue_table")}) if "src" not in r]
errs += [f"row without src: {str(r)[:80]}" for r in nosrc]
print("OK" if not errs else "\n".join(errs))
sys.exit(1 if errs else 0)
