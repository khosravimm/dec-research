#!/usr/bin/env python3
"""Repair/verify roadmap GitHub milestone and issue UTF-8 using existing issue URLs.

Opt-in explicit --apply, idempotent PATCH, no secrets or private source files.
"""
from pathlib import Path
import json,sys,re,subprocess,argparse

ROOT=Path(__file__).resolve().parents[1]
REPO="khosravimm/dec-research"
D=json.loads((ROOT/"research/roadmap.json").read_text(encoding="utf-8"))

def gh(verb,path,payload=None):
 args=["gh","api","--method",verb,path,"-H","Accept: application/vnd.github+json"]
 if payload is not None:args+=["--input","-"]
 p=subprocess.run(args,input=json.dumps(payload,ensure_ascii=False) if payload is not None else None,
                  capture_output=True,text=True,encoding="utf-8",errors="replace")
 if p.returncode:raise RuntimeError(f"GitHub {verb} {path} failed: {p.stderr[:500]}")
 return json.loads(p.stdout) if p.stdout.strip() else {}

def body_for(w):
 dep=", ".join(w["dependencies"]) or "\u0646\u062f\u0627\u0631\u062f / None"
 bk=", ".join(w["legacy_backlog_ids"]) or "\u0646\u062f\u0627\u0631\u062f / None"
 return f"""# {w['id']}: {w['title']['fa']} / {w['title']['en']}

**\u0645\u0631\u062d\u0644\u0647 / Phase:** {w['phase']} | **\u0627\u0648\u0644\u0648\u06cc\u062a / Priority:** {w['priority']}
**\u0634\u0648\u0627\u0647\u062f / Evidence:** E0 \u2014 planned, no DEC execution / \u0628\u0631\u0646\u0627\u0645\u0647\u200c\u0631\u06cc\u0632\u06cc\u200c\u0634\u062f\u0647 \u0648 \u0627\u062c\u0631\u0627 \u0646\u0634\u062f\u0647
**\u0646\u0642\u0634 \u0645\u0633\u0626\u0648\u0644 / Responsible role:** {w['owner_role']} (no individual assigned / \u0641\u0631\u062f \u062a\u0639\u06cc\u06cc\u0646 \u0646\u0634\u062f\u0647)
**\u0628\u0631\u0622\u0648\u0631\u062f / Effort:** {w['estimated_person_days']} \u0646\u0641\u0631\u0631\u0648\u0632 / person-days, not a delivery commitment

## \u062f\u0627\u0645\u0646\u0647 / Scope
{w['scope']['fa']}

{w['scope']['en']}

## \u062e\u0631\u0648\u062c\u06cc / Deliverable
{w['deliverable']['fa']}

{w['deliverable']['en']}

## \u0645\u0639\u06cc\u0627\u0631 \u067e\u0630\u06cc\u0631\u0634 / Acceptance
{w['acceptance']['fa']}

{w['acceptance']['en']}

**\u067e\u06cc\u0634\u200c\u0646\u06cc\u0627\u0632 / Dependencies:** {dep}

**\u0627\u0642\u062f\u0627\u0645\u200c\u0647\u0627\u06cc \u067e\u06cc\u0634\u06cc\u0646 / Historical work IDs:** {bk}

## \u0686\u06a9\u200c\u0644\u06cc\u0633\u062a / Checklist
- [ ] \u062b\u0628\u062a \u0646\u0633\u062e\u0647 \u0648 \u0645\u0646\u0628\u0639 \u0645\u062f\u0644\u060c \u06a9\u062f\u060c \u062f\u0627\u062f\u0647 \u0648 \u0645\u062c\u0648\u0632 / Pin model/code/data and legal provenance
- [ ] \u0627\u062c\u0631\u0627\u06cc \u0622\u0632\u0645\u0648\u0646 \u0628\u0627 \u0634\u0648\u0627\u0647\u062f \u06cc\u0627 \u062b\u0628\u062a \u0634\u06a9\u0633\u062a / Run measured test or record negative result
- [ ] \u0627\u0631\u0632\u06cc\u0627\u0628\u06cc \u0645\u0633\u062a\u0642\u0644 \u062f\u0631 \u06af\u06cc\u062a \u0641\u0627\u0632 / Independent phase gate review
- [ ] \u06a9\u0646\u062a\u0631\u0644 \u0645\u062d\u0631\u0645\u0627\u0646\u06af\u06cc \u0648 \u0645\u0627\u0644\u06a9\u06cc\u062a \u0641\u06a9\u0631\u06cc \u067e\u06cc\u0634 \u0627\u0632 \u0627\u0641\u0634\u0627 / IP and privacy clearance before disclosure
- [ ] \u062b\u0628\u062a \u0646\u062a\u06cc\u062c\u0647 \u062f\u0631 \u062f\u0648 \u0632\u0628\u0627\u0646 \u0648 \u0628\u0647\u200c\u0631\u0648\u0632\u0631\u0633\u0627\u0646\u06cc \u0648\u0636\u0639\u06cc\u062a / Bilingual documentation and status update

**\u0631\u0648\u062f\u0645\u067e / Roadmap:** [\u0641\u0627\u0631\u0633\u06cc](https://github.com/{REPO}/blob/main/docs/fa/roadmap.md) \u00b7 [English](https://github.com/{REPO}/blob/main/docs/en/roadmap.md)
No success, invention registration, deploy or commercial claim is implied by this Issue.
"""

def main():
 a=argparse.ArgumentParser()
 a.add_argument("--apply",action="store_true")
 a.add_argument("--from",dest="start",type=int,default=1)
 a.add_argument("--to",dest="end",type=int,default=35)
 a.add_argument("--milestones",action="store_true")
 args=a.parse_args()
 if not args.apply:
  print("Dry run; use --apply. / \u0627\u062c\u0631\u0627\u06cc \u0648\u0627\u0642\u0639\u06cc \u0641\u0642\u0637 \u0628\u0627 \u06af\u0632\u06cc\u0646\u0647 apply")
  return 0
 if args.milestones:
  arr=gh("GET",f"repos/{REPO}/milestones?state=all&per_page=100")
  bynum={x["number"]:x for x in arr}
  for idx,p in enumerate(D["phases"],1):
   if idx not in bynum:raise RuntimeError(f"Missing milestone {idx}")
   dur=p["duration_weeks"]
   duration=(f"{dur[0]}\u2013{dur[1]} weeks / \u0647\u0641\u062a\u0647\u061b \u0641\u0642\u0637 \u0628\u0631\u0622\u0648\u0631\u062f" if dur else "\u0628\u062f\u0648\u0646 \u062a\u0627\u0631\u06cc\u062e \u062a\u0639\u0647\u062f\u0622\u0648\u0631 / Not scheduled")
   title=f"{p['name']['en']} / {p['name']['fa']}"
   desc=f"\u0641\u0627\u0632 \u067e\u0698\u0648\u0647\u0634 / Research phase: {p['id']}\n\u06af\u06cc\u062a / Gate: {p['gate']}\n\u0645\u062f\u062a / Duration: {duration}\n\u0648\u0636\u0639\u06cc\u062a / Status: {p['state']}\nhttps://github.com/{REPO}/blob/main/docs/fa/roadmap.md\nNo DEC execution results yet."
   gh("PATCH",f"repos/{REPO}/milestones/{idx}",{"title":title,"description":desc})
   print(f"MILESTONE {idx} UTF8 fixed",flush=True)
  return 0
 for w in D["work_packages"][args.start-1:args.end]:
  url=w.get("github_issue")
  if not url:raise RuntimeError(f"No issue link: {w['id']}")
  m=re.search(r"/issues/(\d+)$",url)
  if not m:raise RuntimeError("Bad Issue URL")
  number=int(m.group(1))
  title=f"[{w['id']}] {w['title']['fa']} / {w['title']['en']}"
  body=body_for(w)
  if number in (1,2):
   old=gh("GET",f"repos/{REPO}/issues/{number}")
   marker="### Previous public issue context"
   if marker in str(old.get("body") or ""):
    body+="\n\n"+marker+"\n\n"+old["body"].split(marker,1)[1]
  gh("PATCH",f"repos/{REPO}/issues/{number}",{"title":title,"body":body})
  print(f"ISSUE {number} {w['id']} repaired",flush=True)
 return 0

if __name__=="__main__":
 sys.exit(main())
