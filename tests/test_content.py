import json,subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from scripts.validate import validate
def load(p): return json.loads((ROOT/p).read_text(encoding="utf-8"))
class Tests(unittest.TestCase):
    def test_validation(self): self.assertEqual(validate(),[])
    def test_item_count_and_parity(self):
        m=load("data/meta.json"); en=load("data/assessment.en.json"); lv=load("data/assessment.lv.json"); self.assertEqual(len(en["items"]),m["expected_item_count"]); self.assertEqual([x["id"] for x in en["items"]],[x["id"] for x in lv["items"]])
    def test_domains(self): self.assertEqual([x["id"] for x in load("data/assessment.en.json")["domains"]],load("data/meta.json")["domain_ids"])
    def test_sources_exist(self):
        s=set(load("data/sources.json")["sources"])
        for lang in ("en","lv"):
            for x in load(f"data/assessment.{lang}.json")["items"]: self.assertTrue(x["source_refs"] and set(x["source_refs"]).issubset(s))
    def test_generated_docs(self): self.assertEqual(subprocess.run([sys.executable,str(ROOT/"scripts/render.py"),"--check"]).returncode,0)
    def test_example_assessment(self):
        r=subprocess.run([sys.executable,str(ROOT/"scripts/assess.py"),str(ROOT/"examples/answers.example.json")],capture_output=True,text=True); self.assertEqual(r.returncode,0); p=json.loads(r.stdout); self.assertIn("priority_gaps",p); self.assertNotIn("score",p)
if __name__=="__main__": unittest.main()
