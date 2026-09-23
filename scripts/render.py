from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(lang): return json.loads((ROOT/f"data/assessment.{lang}.json").read_text(encoding="utf-8"))
def render(lang):
    a=load(lang); m=json.loads((ROOT/"data/meta.json").read_text(encoding="utf-8")); out=[f"# {m[f'title_{lang}']}","",f"> {m[f'method_note_{lang}']}","","## "+("Response states" if lang=="en" else "Atbilžu stāvokļi"),""]
    out += [f"- `{s['id']}` — {s['label']}" for s in a["states"]]; out += ["","## "+("Assessment" if lang=="en" else "Novērtējums"),""]
    by={d["id"]:[] for d in a["domains"]}
    for x in a["items"]: by[x["domain"]].append(x)
    for d in a["domains"]:
        out += [f"### {d['title']}",""]
        for x in by[d["id"]]: out += [f"#### {x['id']}","",x["prompt"],"",f"**{'Recommended action' if lang=='en' else 'Ieteiktā darbība'}:** {x['recommended_action']}","",f"**{'Sources' if lang=='en' else 'Avoti'}:** "+", ".join(f"`{r}`" for r in x["source_refs"]),""]
    return "\n".join(out).rstrip()+"\n"
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); args=ap.parse_args(); bad=[]
    for lang,p in (("en",ROOT/"docs/en/assessment.md"),("lv",ROOT/"docs/lv/assessment.md")):
        exp=render(lang)
        if args.check:
            if not p.exists() or p.read_text(encoding="utf-8")!=exp: bad.append(str(p.relative_to(ROOT)))
        else: p.parent.mkdir(parents=True,exist_ok=True); p.write_text(exp,encoding="utf-8")
    if bad: print("Generated documentation is stale: "+", ".join(bad)); return 1
    print("Generated documentation check passed." if args.check else "Generated documentation written."); return 0
if __name__=="__main__": raise SystemExit(main())
