#!/usr/bin/env python3
"""Validate public, paired bilingual DEC research dossier without extra dependencies.

Checks structural consistency only: this is NOT a security audit or translation quality review.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
issues: list[str] = []

def issue(message: str) -> None:
    issues.append(message)

def check_docs() -> int:
    en = {p.relative_to(ROOT / "docs/en") for p in (ROOT / "docs/en").glob("*.md")}
    fa = {p.relative_to(ROOT / "docs/fa") for p in (ROOT / "docs/fa").glob("*.md")}
    if not en or en != fa:
        issue(f"Doc language pairs mismatch: en={sorted(map(str,en))}, fa={sorted(map(str,fa))}")
    for name in sorted(en & fa):
        ids = {}
        for lang in ("en", "fa"):
            p = ROOT / "docs" / lang / name
            s = p.read_text(encoding="utf-8")
            if not s.startswith("---\n") or "\n---\n" not in s[4:]:
                issue(f"No valid frontmatter: {p}")
                continue
            front = s.split("\n---\n", 1)[0][4:]
            def field(key: str):
                hit = re.search(rf"(?m)^{re.escape(key)}:\s*(.+)$", front)
                return hit.group(1).strip() if hit else None
            ids[lang] = field("doc_id")
            if field("language") != lang:
                issue(f"Language incorrect: {p}")
            expected_grade = "E1" if name.as_posix() == "model-warmloaded-general20.md" else "E0"
            if field("evidence_level") != expected_grade:
                issue(f"Incorrect scoped evidence grade in {p}: expected {expected_grade}")
            if not field("version") or not field("date"):
                issue(f"Missing version/date: {p}")
            if len(s) < 600:
                issue(f"Suspiciously short scientific document: {p}")
        if ids.get("en") != ids.get("fa") or not ids.get("en"):
            issue(f"Doc id differs between languages: {name} {ids}")
    return len(en & fa)

def check_machine_records() -> tuple[int, int]:
    cat = json.loads((ROOT / "research/catalogue.json").read_text(encoding="utf-8"))
    exp = json.loads((ROOT / "research/experiment-register.json").read_text(encoding="utf-8"))
    res = json.loads((ROOT / "research/results.json").read_text(encoding="utf-8"))
    def is_localized(x: dict, k: str):
        return isinstance(x.get(k), dict) and all(str(x[k].get(lang, "")).strip() for lang in ("fa", "en"))
    srcs = cat.get("sources", [])
    ids = set()
    for s in srcs:
        if not s.get("id") or s["id"] in ids:
            issue("Duplicate/empty source id")
        ids.add(s.get("id"))
        if not is_localized(s, "title") or not is_localized(s, "limitation"):
            issue(f"Missing bilingual source record {s.get('id')}")
        if not str(s.get("url", "")).startswith("https://"):
            issue(f"Invalid source link {s.get('id')}")
        if s.get("dec_evidence") != "E0":
            issue(f"Unexpected DEC evidence beyond E0: {s.get('id')}")
    testids = set()
    for e in exp.get("experiments", []):
        if not e.get("id") or e["id"] in testids:
            issue("Duplicate or missing experiment id")
        testids.add(e.get("id"))
        if not is_localized(e, "title") or not is_localized(e, "question"):
            issue(f"Experiment missing bilingual fields: {e.get('id')}")
        if e.get("status") not in ("planned","deferred") or e.get("result") is not None or e.get("runs"):
            issue(f"False positive experimental result claim: {e.get('id')}")
    if res.get("results") or res.get("status") != "no_dec_experiments_run":
        issue("Results file falsely claims actual DEC experiment")
    return len(srcs), len(testids)

def check_roadmap() -> tuple[int, int]:
    data = json.loads((ROOT / "research/roadmap.json").read_text(encoding="utf-8"))
    packages = data.get("work_packages", [])
    phase_ids = {p["id"] for p in data.get("phases", [])}
    package_ids = {w["id"] for w in packages}
    legacy = set()
    for w in packages:
        if w["phase"] not in phase_ids:
            issue(f"Invalid roadmap phase in {w['id']}")
        for key in ("title", "scope", "deliverable", "acceptance"):
            if not isinstance(w.get(key), dict) or not all(str(w[key].get(lang,"")).strip() for lang in ("en","fa")):
                issue(f"Missing bilingual work package {w['id']}:{key}")
        for d in w.get("dependencies", []):
            if d not in package_ids:
                issue(f"Unknown work-package dependency {w['id']} -> {d}")
        if w.get("status") == "in_progress":
            evidence_ref=w.get("public_evidence_ref")
            if not evidence_ref or not (ROOT/evidence_ref).is_file():
                issue(f"Running work package missing public evidence record: {w['id']}")
        elif w.get("status") not in ("planned","deferred"):
            issue(f"Roadmap publication claims unsupported completion: {w['id']}")
        legacy.update(w.get("legacy_backlog_ids", []))
    if len(package_ids) != len(packages):
        issue("Duplicate work-package IDs")
    expected_legacy={f"DEC-BK-{i:03}" for i in range(1,40)}
    if not expected_legacy.issubset(legacy):
        issue(f"Legacy backlog mapping incomplete: {expected_legacy-legacy}")
    deps={w["id"]:w.get("dependencies",[]) for w in packages}
    visiting=set()
    visited=set()
    def visit(k):
        if k in visiting:
            issue(f"Cycle in roadmap work packages at {k}")
            return
        if k in visited:
            return
        visiting.add(k)
        for d in deps.get(k, []):
            if d in deps:
                visit(d)
        visiting.remove(k)
        visited.add(k)
    for name in deps:
        visit(name)
    for lang in ("en","fa"):
        body=(ROOT/"docs"/lang/"roadmap.md").read_text(encoding="utf-8")
        for w in packages:
            if w["id"] not in body:
                issue(f"Missing work-package in rendered {lang} roadmap: {w['id']}")
        if "version: "+data["version"] not in body:
            issue(f"Rendered roadmap stale in {lang}")
    status_file=ROOT/"research/p0-execution-status.json"
    if status_file.exists():
        status=json.loads(status_file.read_text(encoding="utf-8"))
        if status.get("overall_dec_evidence_grade") != "E0" or status.get("p0_gate") != "not_accepted":
            issue("P0 public status falsely claims DEC success or gate acceptance")
        if status.get("test_summary",{}).get("model_quality_tested") is not False:
            issue("P0 integration smoke cannot claim model quality tests")
    if len(data.get("gates", [])) < 6 or len(data.get("risks", [])) < 10:
        issue("Roadmap risk or gate coverage low")
    return len(packages), len(legacy)


def check_utf8_integrity() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix not in {".md", ".json", ".py", ".yaml", ".yml"}:
            continue
        content=path.read_text(encoding="utf-8",errors="replace")
        if chr(0xfffd) in content:
            issue(f"Unicode replacement character in public artifact: {path.relative_to(ROOT)}")
        if path.parent==ROOT / "docs/fa":
            persian=sum(0x600<=ord(ch)<=0x6ff for ch in content)
            if persian<100:
                issue(f"Persian documentation file lacks actual Persian text: {path.relative_to(ROOT)}")
    roadmap=json.loads((ROOT/"research/roadmap.json").read_text(encoding="utf-8"))
    for w in roadmap["work_packages"]:
        if sum(0x600<=ord(ch)<=0x6ff for ch in w["title"]["fa"])<5:
            issue(f"Invalid Persian title in {w['id']}")


def check_model_preflight_integrity() -> None:
    path=ROOT/"research/model-preflight.json"
    if not path.exists():
        return
    import json
    x=json.loads(path.read_text(encoding="utf-8"))
    if x.get("evidence_level_DEC_architecture")!="E0":
        issue("Model preflight cannot upgrade DEC architecture evidence")
    if x.get("evidence_level_model_runtime")!="E1":
        issue("Model inference preflight grade unexpected")
    if x.get("selected_model") is not None:
        issue("Model core selection incorrectly claimed from small smoke")
    models=x.get("models",[])
    if len(models)!=4:
        issue("Missing model family in model-only screening")
    for m in models:
        if not re.fullmatch(r"[a-f0-9]{64}",str(m.get("sha256",""))):
            issue("Invalid model sha256 in public preflight")
    for lang in ("en","fa"):
        path=ROOT/"docs"/lang/"model-preflight.md"
        if not path.exists():
            issue("Model preflight bilingual document missing: "+lang)
            continue
        body=path.read_text(encoding="utf-8")
        for m in models:
            if m.get("id","").split("-Q4")[0].split("-Base")[0].split("-3B")[0] not in body and m.get("id","") not in body:
                issue("Model omitted from "+lang+" preflight: "+m["id"])


def check_bilingual_warmloaded_model_evaluation() -> None:
    path=ROOT/"research/benchmarks/dec-general-warmloaded-fa-en-v1.json"
    if not path.exists():
        issue("Bilingual warmloaded evaluation JSON missing")
        return
    data=json.loads(path.read_text(encoding="utf-8"))
    questions=data.get("reference_questions",[])
    models=data.get("models",[])
    if len(questions)!=20 or len(models)!=3:
        issue("Warmloaded test must contain 20 questions and 3 candidate models")
        return
    ids={q.get("id") for q in questions}
    if len(ids)!=20 or sum(q.get("language")=="fa" for q in questions)!=10 or sum(q.get("language")=="en" for q in questions)!=10:
        issue("Question count, IDs, or bilingual balance invalid")
    forbidden=("cybersecurity","networking","programming","شبکه","امنیت اطلاعات","رمزنگاری")
    for q in questions:
        if any(term.lower() in q.get("prompt","").lower() for term in forbidden):
            issue("Specialist question in general-purpose test: "+q.get("id","?"))
        if not q.get("prompt") or not q.get("reference"):
            issue("Incomplete question or reference")
    if data.get("prior_two_question_test_accepted") is not False or data.get("selection",{}).get("backbone") is not None:
        issue("Rejected prior two-item test or backbone selection misrepresented")
    if not re.fullmatch(r"[a-f0-9]{64}",str(data.get("questions_sha256",""))):
        issue("Missing source gold-set integrity hash")
    for m in models:
        if m.get("warmup_success") is not True:
            issue("Model was tested without successful warmup: "+m.get("id","?"))
        responses=m.get("responses",[])
        if len(responses)!=20:
            issue("Incomplete loaded-model set: "+m.get("id","?"))
            continue
        if len({r.get("case_id") for r in responses}) != 20:
            issue("Duplicate case for model: "+m.get("id","?"))
        for lang in ("fa","en"):
            rs=[r for r in responses if r.get("language")==lang]
            if len(rs)!=10 or any(r.get("http_status")!=200 for r in rs):
                issue("Noncompliant language request count/HTTP: "+m.get("id","?")+" "+lang)
            count=sum(r.get("strict_correct_first_review") is True for r in rs)
            content=sum(r.get("semantic_correct_first_review") is True for r in rs)
            metrics=m.get("metrics",{}).get(lang,{})
            if count!=metrics.get("strict_pass") or content!=metrics.get("semantic_pass"):
                issue("Scores inconsistent with case-level judgments: "+m.get("id","?")+" "+lang)
            if count>content:
                issue("Strict score exceeds semantic score")
        for r in responses:
            if r.get("case_id") not in ids:
                issue("Unknown model question ID")
            if not isinstance(r.get("response"),str) or not r.get("review_reason"):
                issue("Missing model output or audit rationale")
        if not re.fullmatch(r"[a-f0-9]{64}",str(m.get("sha256",""))):
            issue("Missing weight SHA256: "+m.get("id","?"))
    for lang in ("fa","en"):
        if not (ROOT/"docs"/lang/"model-warmloaded-general20.md").exists():
            issue("Bilingual warmloaded report missing: "+lang)


def check_rights_and_leaks() -> None:
    rights = (ROOT / "RIGHTS.md").read_text(encoding="utf-8")
    if "No blanket" not in rights or not (ROOT / "RIGHTS.fa.md").exists():
        issue("Missing rights declaration")
    if (ROOT / "LICENSE").exists() or (ROOT / "LICENSE.md").exists():
        issue("Unexpected license file; decision is rights-reserved until legal review")
    banned = [
        (re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"), "private key"),
        (re.compile(r"(?:ghp_|github_pat_|gho_|sk-proj-)[A-Za-z0-9_\-]{12,}"), "token-like value"),
        (re.compile(r"(?i)(?:E:\\\\Projects\\\\ai-lab|state/lab-state\.json)"), "private lab detail"),
    ]
    for p in ROOT.rglob("*"):
        if not p.is_file() or ".git" in p.parts:
            continue
        if p.suffix not in {".md", ".json", ".py", ".yml", ".yaml", ".cff", ""}:
            continue
        txt = p.read_text(encoding="utf-8")
        for pattern, desc in banned:
            if pattern.search(txt) and p.name != "validate_public_docs.py":
                issue(f"Possible {desc} in {p.relative_to(ROOT)}")
    for readme in ("README.md", "README.fa.md"):
        t = (ROOT / readme).read_text(encoding="utf-8")
        for rel in re.findall(r"\]\((docs/(?:fa|en)/[^)#]+)\)", t):
            if not (ROOT / rel).is_file():
                issue(f"Missing README target {rel}")

def main() -> int:
    n_docs = check_docs()
    n_sources, n_experiments = check_machine_records()
    n_work,n_backlog = check_roadmap()
    check_utf8_integrity()
    check_model_preflight_integrity()
    check_bilingual_warmloaded_model_evaluation()
    check_rights_and_leaks()
    if issues:
        for x in issues:
            print("ERROR:", x)
        return 1
    print(f"PASS: {n_docs} bilingual pairs; {n_sources} public sources; {n_experiments} experiments; {n_work} roadmap packages linked to {n_backlog} historical tasks; DEC cognitive-model experiments not yet accepted; E1-only local model screening recorded.")
    print("NOTE: structural and basic leak checks only; copyright, inventorship, translation and patent novelty need independent review.")
    return 0

if __name__ == "__main__":
    sys.exit(main())