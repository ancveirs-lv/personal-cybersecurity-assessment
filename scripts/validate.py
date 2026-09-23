from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def validate() -> list[str]:
    errors: list[str] = []
    meta = load("data/meta.json")
    en = load("data/assessment.en.json")
    lv = load("data/assessment.lv.json")
    sources = load("data/sources.json")

    if en.get("canonical_language") != "en" or lv.get("canonical_language") != "en":
        errors.append("canonical language contract failed")

    expected = meta["expected_item_count"]
    if len(en["items"]) != expected or len(lv["items"]) != expected:
        errors.append("item count failed")

    if [x["id"] for x in en["items"]] != [x["id"] for x in lv["items"]]:
        errors.append("item parity failed")

    if [x["id"] for x in en["domains"]] != meta["domain_ids"]:
        errors.append("English domain contract failed")
    if [x["id"] for x in lv["domains"]] != meta["domain_ids"]:
        errors.append("Latvian domain contract failed")

    en_states = [x["id"] for x in en["states"]]
    lv_states = [x["id"] for x in lv["states"]]
    if en_states != meta["state_ids"] or lv_states != meta["state_ids"]:
        errors.append("state contract failed")

    for lang, payload in (("en", en), ("lv", lv)):
        for state in payload["states"]:
            if not isinstance(state.get("meaning"), str) or not state["meaning"].strip():
                errors.append(f"{lang}: state {state.get('id')} missing meaning")

    if meta.get("not_applicable_requires_note") and "NOT_APPLICABLE" not in en_states:
        errors.append("NOT_APPLICABLE required by methodology contract")

    valid_sources = set(sources["sources"])
    for lang, payload in (("en", en), ("lv", lv)):
        for item in payload["items"]:
            if not item.get("prompt") or not item.get("recommended_action"):
                errors.append(f"{lang}:{item['id']}: missing text")
            if item.get("domain") not in meta["domain_ids"]:
                errors.append(f"{lang}:{item['id']}: invalid domain")
            refs = item.get("source_refs", [])
            if not refs or any(ref not in valid_sources for ref in refs):
                errors.append(f"{lang}:{item['id']}: invalid source refs")

    if meta.get("global_english"):
        blob = json.dumps(en, ensure_ascii=False).lower()
        for forbidden in ("cert.lv", "latvij"):
            if forbidden in blob:
                errors.append(f"global English boundary failed: {forbidden}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print(f"Validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    meta = load("data/meta.json")
    print(
        "Validation passed: "
        f"{meta['expected_item_count']} bilingual items, "
        f"{len(meta['domain_ids'])} domains, "
        "parity, source and methodology contracts."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
