from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(p): return json.loads((ROOT/p).read_text(encoding="utf-8"))
def validate():
    e=[]; m=load("data/meta.json"); en=load("data/assessment.en.json"); lv=load("data/assessment.lv.json"); src=load("data/sources.json")
    if en.get("canonical_language")!="en" or lv.get("canonical_language")!="en": e.append("canonical language contract failed")
    if len(en["items"])!=m["expected_item_count"] or len(lv["items"])!=m["expected_item_count"]: e.append("item count failed")
    if [x["id"] for x in en["items"]] != [x["id"] for x in lv["items"]]: e.append("item parity failed")
    if [x["id"] for x in en["domains"]] != m["domain_ids"] or [x["id"] for x in lv["domains"]] != m["domain_ids"]: e.append("domain contract failed")
    if [x["id"] for x in en["states"]] != m["state_ids"] or [x["id"] for x in lv["states"]] != m["state_ids"]: e.append("state contract failed")
    valid=set(src["sources"])
    for lang,a in (("en",en),("lv",lv)):
        for x in a["items"]:
            if not x.get("prompt") or not x.get("recommended_action"): e.append(f"{lang}:{x['id']}: missing text")
            if x.get("domain") not in m["domain_ids"]: e.append(f"{lang}:{x['id']}: invalid domain")
            if not x.get("source_refs") or any(r not in valid for r in x["source_refs"]): e.append(f"{lang}:{x['id']}: invalid source refs")
    if m.get("global_english"):
        blob=json.dumps(en,ensure_ascii=False).lower()
        for bad in ("cert.lv","latvij"):
            if bad in blob: e.append(f"global English boundary failed: {bad}")
    return e
def main():
    e=validate()
    if e:
        print(f"Validation failed with {len(e)} error(s):")
        [print(f"- {x}") for x in e]; return 1
    m=load("data/meta.json"); print(f"Validation passed: {m['expected_item_count']} bilingual items, {len(m['domain_ids'])} domains, parity, source and methodology contracts."); return 0
if __name__=="__main__": raise SystemExit(main())
