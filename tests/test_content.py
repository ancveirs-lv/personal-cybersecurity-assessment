import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.validate import validate


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Tests(unittest.TestCase):
    def test_validation(self):
        self.assertEqual(validate(), [])

    def test_item_count_and_parity(self):
        meta = load("data/meta.json")
        en = load("data/assessment.en.json")
        lv = load("data/assessment.lv.json")
        self.assertEqual(len(en["items"]), meta["expected_item_count"])
        self.assertEqual(
            [x["id"] for x in en["items"]],
            [x["id"] for x in lv["items"]],
        )

    def test_domains(self):
        meta = load("data/meta.json")
        en = load("data/assessment.en.json")
        self.assertEqual(
            [x["id"] for x in en["domains"]],
            meta["domain_ids"],
        )

    def test_sources_exist(self):
        sources = set(load("data/sources.json")["sources"])
        for lang in ("en", "lv"):
            for item in load(f"data/assessment.{lang}.json")["items"]:
                self.assertTrue(item["source_refs"])
                self.assertTrue(set(item["source_refs"]).issubset(sources))

    def test_state_meanings(self):
        meta = load("data/meta.json")
        for lang in ("en", "lv"):
            payload = load(f"data/assessment.{lang}.json")
            self.assertEqual(
                [x["id"] for x in payload["states"]],
                meta["state_ids"],
            )
            self.assertTrue(all(x.get("meaning") for x in payload["states"]))

    def test_generated_docs(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/render.py"), "--check"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_example_assessment_has_no_aggregate_score(self):
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts/assess.py"),
                str(ROOT / "examples/answers.example.json"),
            ],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        self.assertIn("priority_gaps", report)
        self.assertNotIn("score", report)

    def test_not_applicable_requires_note_when_enabled(self):
        meta = load("data/meta.json")
        if not meta.get("not_applicable_requires_note"):
            self.skipTest("NOT_APPLICABLE is not part of this assessment model")

        assessment = load("data/assessment.en.json")
        first_id = assessment["items"][0]["id"]

        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad.json"
            bad.write_text(
                json.dumps(
                    {
                        "assessment_id": assessment["assessment_id"],
                        "version": assessment["version"],
                        "answers": {first_id: "NOT_APPLICABLE"},
                    }
                ),
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/assess.py"), str(bad)],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("requires note", result.stdout + result.stderr)

            good = Path(tmp) / "good.json"
            good.write_text(
                json.dumps(
                    {
                        "assessment_id": assessment["assessment_id"],
                        "version": assessment["version"],
                        "answers": {
                            first_id: {
                                "state": "NOT_APPLICABLE",
                                "note": "Documented assessment-scope rationale.",
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/assess.py"), str(good)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
