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
            if field("evidence_level") != "E0":
                issue(f"Non-E0 doc (no DEC local results published): {p}")
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
        if w.get("status") not in ("planned","deferred"):
            issue(f"Roadmap publication claims activity or results without evidence: {w['id']}")
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
    check_rights_and_leaks()
    if issues:
        for x in issues:
            print("ERROR:", x)
        return 1
    print(f"PASS: {n_docs} bilingual pairs; {n_sources} public sources; {n_experiments} experiments; {n_work} roadmap packages linked to {n_backlog} historical tasks; no DEC results.")
    print("NOTE: structural and basic leak checks only; copyright, inventorship, translation and patent novelty need independent review.")
    return 0

if __name__ == "__main__":
    sys.exit(main())