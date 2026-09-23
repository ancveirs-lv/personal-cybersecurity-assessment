from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("answers")
    parser.add_argument("--lang", choices=("en", "lv"), default="en")
    args = parser.parse_args()

    assessment = json.loads(
        (ROOT / f"data/assessment.{args.lang}.json").read_text(encoding="utf-8")
    )
    answer_payload = json.loads(Path(args.answers).read_text(encoding="utf-8"))
    supplied = answer_payload.get("answers", {})

    valid = {state["id"] for state in assessment["states"]}
    unknown = assessment["states"][0]["id"]
    gaps = set(assessment["gap_states"])
    domains = {domain["id"]: [] for domain in assessment["domains"]}

    actions = []
    unknown_items = []
    not_applicable_items = []
    all_states = []

    for item in assessment["items"]:
        raw = supplied.get(item["id"], unknown)

        if isinstance(raw, dict):
            state = raw.get("state", unknown)
            note = raw.get("note", "")
        else:
            state = raw
            note = ""

        if state not in valid:
            raise SystemExit(f"invalid state for {item['id']}: {state}")

        if state == "NOT_APPLICABLE" and not str(note).strip():
            raise SystemExit(f"NOT_APPLICABLE requires note for {item['id']}")

        all_states.append(state)
        domains[item["domain"]].append(state)

        if state == unknown:
            unknown_items.append(item["id"])

        if state == "NOT_APPLICABLE":
            not_applicable_items.append({"id": item["id"], "note": note})

        if state in gaps:
            actions.append(
                {
                    "id": item["id"],
                    "domain": item["domain"],
                    "state": state,
                    "priority": item["priority"],
                    "recommended_action": item["recommended_action"],
                }
            )

    actions.sort(key=lambda item: (0 if item["priority"] == "high" else 1, item["id"]))

    report = {
        "assessment_id": assessment["assessment_id"],
        "version": assessment["version"],
        "language": args.lang,
        "overall_state_counts": dict(Counter(all_states)),
        "unknown_items": unknown_items,
        "not_applicable_items": not_applicable_items,
        "domain_state_counts": {
            key: dict(Counter(values)) for key, values in domains.items()
        },
        "priority_gaps": actions,
        "note": "No overall safety, compliance or maturity score is produced.",
    }

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
