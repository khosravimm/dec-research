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
    check_rights_and_leaks()
    if issues:
        for x in issues:
            print("ERROR:", x)
        return 1
    print(f"PASS: {n_docs} bilingual pairs; {n_sources} public cited sources; {n_experiments} planned/deferred experiments; no published DEC results.")
    print("NOTE: structural and basic leak checks only; copyright, inventorship, translation and patent novelty need independent review.")
    return 0

if __name__ == "__main__":
    sys.exit(main())