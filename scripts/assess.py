from __future__ import annotations
import argparse,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("answers"); ap.add_argument("--lang",choices=("en","lv"),default="en"); args=ap.parse_args()
    a=json.loads((ROOT/f"data/assessment.{args.lang}.json").read_text(encoding="utf-8")); ans=json.loads(Path(args.answers).read_text(encoding="utf-8")).get("answers",{})
    valid={s["id"] for s in a["states"]}; unknown=a["states"][0]["id"]; gaps=set(a["gap_states"]); domains={d["id"]:[] for d in a["domains"]}; actions=[]; unknowns=[]; all_states=[]
    for x in a["items"]:
        st=ans.get(x["id"],unknown)
        if st not in valid: raise SystemExit(f"invalid state for {x['id']}: {st}")
        all_states.append(st); domains[x["domain"]].append(st)
        if st==unknown: unknowns.append(x["id"])
        if st in gaps: actions.append({"id":x["id"],"domain":x["domain"],"state":st,"priority":x["priority"],"recommended_action":x["recommended_action"]})
    actions.sort(key=lambda x:(0 if x["priority"]=="high" else 1,x["id"]))
    print(json.dumps({"assessment_id":a["assessment_id"],"version":a["version"],"language":args.lang,"overall_state_counts":dict(Counter(all_states)),"unknown_items":unknowns,"domain_state_counts":{k:dict(Counter(v)) for k,v in domains.items()},"priority_gaps":actions,"note":"No overall safety, compliance or maturity score is produced."},ensure_ascii=False,indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
