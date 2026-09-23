from __future__ import annotations
import json,urllib.request,urllib.error
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    d=json.loads((ROOT/"data/sources.json").read_text(encoding="utf-8")); fail=[]
    for sid,x in d["sources"].items():
        req=urllib.request.Request(x["url"],headers={"User-Agent":"Mozilla/5.0 assessment-link-check/0.1"})
        try:
            with urllib.request.urlopen(req,timeout=20) as r: code=getattr(r,"status",200)
        except urllib.error.HTTPError as e: code=e.code
        except Exception as e: print(f"WARN ERR {sid}: {e}"); continue
        if 200<=code<400: print(f"OK   {code} {sid}: {x['url']}")
        elif code in (403,429,999): print(f"WARN {code} {sid}: rate-limited or bot-blocked")
        else: print(f"FAIL {code} {sid}: {x['url']}"); fail.append(sid)
    if fail: return 1
    print("Link health passed."); return 0
if __name__=="__main__": raise SystemExit(main())
