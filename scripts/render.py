from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def render(lang: str) -> str:
    assessment = load_json(f"data/assessment.{lang}.json")
    meta = load_json("data/meta.json")

    title = meta[f"title_{lang}"]
    note = meta[f"method_note_{lang}"]

    lines = [
        f"# {title}",
        "",
        f"> {note}",
        "",
        "## " + ("Response states" if lang == "en" else "Atbilžu stāvokļi"),
        "",
    ]

    for state in assessment["states"]:
        lines.append(
            f"- `{state['id']}` — {state['label']}: {state['meaning']}"
        )

    lines += [
        "",
        "## " + ("Assessment" if lang == "en" else "Novērtējums"),
        "",
    ]

    by_domain = {domain["id"]: [] for domain in assessment["domains"]}
    for item in assessment["items"]:
        by_domain[item["domain"]].append(item)

    for domain in assessment["domains"]:
        lines += [f"### {domain['title']}", ""]

        for item in by_domain[domain["id"]]:
            action_label = (
                "Recommended action" if lang == "en" else "Ieteiktā darbība"
            )
            source_label = "Sources" if lang == "en" else "Avoti"

            lines += [
                f"#### {item['id']}",
                "",
                item["prompt"],
                "",
                f"**{action_label}:** {item['recommended_action']}",
                "",
                f"**{source_label}:** "
                + ", ".join(f"`{ref}`" for ref in item["source_refs"]),
                "",
            ]

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    stale = []

    for lang, path in (
        ("en", ROOT / "docs/en/assessment.md"),
        ("lv", ROOT / "docs/lv/assessment.md"),
    ):
        expected = render(lang)

        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != expected:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8")

    if stale:
        print("Generated documentation is stale: " + ", ".join(stale))
        return 1

    print(
        "Generated documentation check passed."
        if args.check
        else "Generated documentation written."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
