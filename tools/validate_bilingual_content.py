#!/usr/bin/env python3
"""Audit bilingual research pairs: lexical + structure checks, not semantic proof."""
from pathlib import Path
import json, re, hashlib, sys

ROOT = Path(__file__).resolve().parents[1]
pairs = [
("docs/research/README.md", "docs/research/README.fa.md", "research-index"),
("docs/research/reference-architecture/REFERENCE_ARCHITECTURE_EN.md", "docs/research/reference-architecture/REFERENCE_ARCHITECTURE_FA.md", "short-overview"),
("PROJECT-CHARTER.en.md", "PROJECT-CHARTER.md", "charter"),
("ADR-001-MODEL-OR-ECOSYSTEM-20261116.en.md", "ADR-001-MODEL-OR-ECOSYSTEM-20261116.md", "adr001"),
("docs/research/reference-architecture/DEC_CRA_REFERENCE_ARCHITECTURE_EN.md", "docs/research/reference-architecture/DEC_CRA_REFERENCE_ARCHITECTURE_FA.md", "architecture"),
("docs/research/reference-architecture/VALIDATION_PLAN.md", "docs/research/reference-architecture/VALIDATION_PLAN_FA.md", "validation"),
("docs/research/reference-architecture/ADR-002-REFERENCE-ARCHITECTURE.md", "docs/research/reference-architecture/ADR-002-REFERENCE-ARCHITECTURE_FA.md", "adr"),
("docs/research/reference-architecture/README.md", "docs/research/reference-architecture/README.fa.md", "index"),
("docs/research/mobilemoe-technical-review-20261116.md", "docs/research/mobilemoe-technical-review-20261116.fa.md", "mobilemoe"),
("docs/research/persian-tokenizer-20261116.md", "docs/research/persian-tokenizer-20261116.fa.md", "tokenizer"),
("docs/research/composition-methods-20261116.md", "docs/research/composition-methods-20261116.fa.md", "composition"),
("docs/research/model-landscape-20261116.md", "docs/research/model-landscape-20261116.fa.md", "models")
]
def prose(s):
    s=re.sub(r"(?s)" + chr(96)*3 + r".*?" + chr(96)*3,"",s)
    s=re.sub(r"https?://[^\s|)>]+","",s)
    s=re.sub(chr(96)+r"[^\n]*?"+chr(96),"",s)
    return s
def lang(s):
    s=prose(s)
    f=len(re.findall(r"[\u0600-\u06ff]",s));e=len(re.findall(r"[A-Za-z]",s))
    return f,e,round(f/max(1,f+e),3)
def urls(s):return {x.rstrip(".,;،") for x in re.findall(r"https?://[^\s|)<>]+",s)}
def heads(s):return [x for x in s.splitlines() if re.match(r"^#{1,6}\s",x)]
def rows(s):return [x for x in s.splitlines() if x.startswith("|") and not re.fullmatch(r"[|\-: ]+",x)]
issues=[];warnings=[];items=[]
for en,fa,key in pairs:
    if not (ROOT/en).exists() or not (ROOT/fa).exists():
        issues.append("unpaired "+key);continue
    a=(ROOT/en).read_text();b=(ROOT/fa).read_text()
    f,e,ratio=lang(b);missing=sorted(urls(a)-urls(b))
    info=dict(category=key,english=en,persian=fa,persian_fraction=ratio,
      section_count_en=len(heads(a)),section_count_fa=len(heads(b)),
      table_rows_en=len(rows(a)),table_rows_fa=len(rows(b)),missing_primary_urls=missing,
      source_sha256=hashlib.sha256((ROOT/en).read_bytes()).hexdigest(),
      persian_sha256=hashlib.sha256((ROOT/fa).read_bytes()).hexdigest())
    items.append(info)
    if ratio<0.45:issues.append("mostly English: "+fa+" ratio="+str(ratio))
    if key in ("architecture","validation","adr") and len(heads(a))!=len(heads(b)):
        issues.append("section mismatch: "+key)
    if key in ("architecture","validation","models","mobilemoe") and len(rows(a))!=len(rows(b)):
        issues.append("table count mismatch: "+key+" "+str((len(rows(a)),len(rows(b)))))
    if missing:issues.append("missing URLs: "+fa+" "+repr(missing))
    if len(b)<800:issues.append("too short: "+fa)
# Discover newly added English-only research markdown, not just hard-coded pairs.
paired_english={en for en,_,_ in pairs}
for research_file in (ROOT/"docs/research").rglob("*.md"):
    relative=research_file.relative_to(ROOT).as_posix()
    name=research_file.name
    if name.endswith(".fa.md") or name.endswith("_FA.md"):
        continue
    if relative in paired_english:
        continue
    # Other machine/decision docs are covered through their explicit pairs above.
    issues.append("unregistered or unpaired research document: "+relative)
en_files={p.name for p in (ROOT/"docs/en").glob("*.md")}
fa_files={p.name for p in (ROOT/"docs/fa").glob("*.md")}
if en_files != fa_files:issues.append("legacy docs/en and docs/fa are not paired")
legacy=[]
for name in sorted(en_files & fa_files):
    f,e,x=lang((ROOT/"docs/fa"/name).read_text())
    legacy.append(dict(file=name,persian_fraction=x,persian_characters=f,latin_characters=e))
    if x<0.25:warnings.append("manual editorial check of legacy mixed-language material: "+name)
report=dict(schema="dec-bilingual-audit-v1",status="PASS_STRUCTURAL_LEXICAL" if not issues else "FAIL",
  new_pairs=len(items),existing_docs_pairs=len(legacy),research_checks=items,legacy_checks=legacy,
  issues=issues,editorial_warnings=warnings,
  limitations=["Character ratios and URL/heading/table parity cannot prove accurate translation.","Technical names, raw user prompts and machine fields intentionally retain original spelling.","Independent editorial review is required for semantic equivalence."])
(ROOT/"research/bilingual-audit-20261116.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print("RESULT",report["status"],"pairs",len(items),"legacy",len(legacy))
for d in items:print(d["category"],d["persian_fraction"],"sections",d["section_count_en"],d["section_count_fa"],"tables",d["table_rows_en"],d["table_rows_fa"],"url_loss",len(d["missing_primary_urls"]))
for x in issues:print("ISSUE",x)
for x in warnings:print("WARNING",x)
sys.exit(1 if issues else 0)
