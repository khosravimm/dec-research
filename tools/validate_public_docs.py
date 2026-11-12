#!/usr/bin/env python3
"""Validate public, paired bilingual DEC research dossier without extra dependencies.

Checks structural consistency only: this is NOT a security audit or translation quality review.
"""
from __future__ import annotations

import json
import re
import statistics
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
            expected_grade = "E1" if name.as_posix() in ("model-warmloaded-general20.md", "minicpm5-sampler-ablation.md", "liquid-warmloaded-general20.md", "model-english-instruction-tools.md") else "E0"
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


def check_minicpm_sampler_ablation() -> None:
    path=ROOT/"research/benchmarks/dec-minicpm5-sampler-ablation-v1.json"
    if not path.exists():
        issue("Missing MiniCPM sampler diagnosis JSON")
        return
    data=json.loads(path.read_text(encoding="utf8"))
    if data.get("evidence_level")!="E1 limited single-run model-parameter ablation":
        issue("Sampler evidence level changed unexpectedly")
    if data.get("dec_architecture_evidence")!="E0, no DEC learning or integration":
        issue("Sampler study cannot assert successful DEC integration")
    if not re.fullmatch("[a-f0-9]{64}",data.get("private_raw_sha256","")):
        issue("Sampler evidence hash malformed")
    profiles=data.get("profiles",[])
    responses=data.get("responses",[])
    if len(profiles)!=3 or len(responses)!=60:
        issue("Sampler study incomplete (expected 3 profiles and 60 cases)")
        return
    pairs={(x.get("profile"),x.get("id")) for x in responses}
    if len(pairs)!=60:
        issue("Duplicate sampler profile/question pair")
    for profile in profiles:
        name=profile["name"]
        for lang in ("fa","en"):
            group=[z for z in responses if z.get("profile")==name and z.get("lang")==lang]
            if len(group)!=10 or any(z.get("http_status")!=200 for z in group):
                issue("Sampler profile/language incomplete: "+name+"/"+lang)
                continue
            summary=profile["summary"][lang]
            mean=round(statistics.mean(z["trigram_repeat_fraction"] for z in group),5)
            if abs(mean-summary["mean_repeated_trigram_fraction"])>0.00001:
                issue("Sampler repetition-rate summary inconsistent")
            if sum(z.get("finish_reason")=="length" for z in group)!=summary.get("length_capped"):
                issue("Sampler output length summary inconsistent")
    for lang in ("fa","en"):
        path=ROOT/"docs"/lang/"minicpm5-sampler-ablation.md"
        if not path.exists():
            issue("MiniCPM sampler bilingual doc missing: "+lang)


def check_liquid_model_warm20() -> None:
    p=ROOT/"research/benchmarks/dec-liquid-warmloaded-fa-en-v1.json"
    if not p.exists():
        issue("Liquid 2-model warm20 file missing")
        return
    data=json.loads(p.read_text(encoding="utf8"))
    if data.get("evidence_level")!="E1 model-only single-run feasibility; no quality benchmark accepted":
        issue("Liquid screening evidence overclaimed")
    if data.get("dec_evidence")!="E0 unchanged":
        issue("DEC evidence incorrectly upgraded by Liquid load tests")
    models=data.get("models",[])
    if len(models)!=2 or sum(len(m.get("responses",[])) for m in models)!=40:
        issue("Liquid screening requires 2 models x 20 general questions")
        return
    for m in models:
        if not m.get("warmup_success"):
            issue("Liquid evaluation occurred without successful warmup")
        if not re.fullmatch(r"[a-f0-9]{64}",str(m.get("sha256",""))):
            issue("Missing Liquid model pinned hash")
        for lang in ("fa","en"):
            rows=[r for r in m.get("responses",[]) if r.get("lang")==lang]
            metrics=m.get("summary",{}).get(lang,{})
            if len(rows)!=10 or any(r.get("http_status")!=200 for r in rows):
                issue("Liquid general test incomplete "+m.get("id","?")+" "+lang)
                continue
            if metrics.get("empty_final")!=sum(not r.get("final_response","").strip() for r in rows):
                issue("Liquid empty-final count inconsistent")
            if metrics.get("length_capped")!=sum(r.get("finish_reason")=="length" for r in rows):
                issue("Liquid length-cap count inconsistent")
    for lang in ("en","fa"):
        if not (ROOT/"docs"/lang/"liquid-warmloaded-general20.md").exists():
            issue("Missing bilingual Liquid report "+lang)


def check_english_instructions_and_tools() -> None:
    path=ROOT/"research/benchmarks/dec-english-instruction-tools-v1.json"
    if not path.exists():
        issue("Missing English tools and instruction dataset")
        return
    data=json.loads(path.read_text(encoding="utf8"))
    cases=data.get("frozen_test_cases",[])
    models=data.get("models",[])
    if len(cases)!=24 or len(models)!=5:
        issue("English tool benchmark must contain 24 questions and 5 models")
        return
    if data.get("model_selected") is not None or data.get("evaluation",{}).get("level") != "E1 limited real-host implementation feasibility":
        issue("DEC model selection or E1 evidence overclaimed")
    if sum(c.get("kind")=="instruction" for c in cases)!=12 or sum(c.get("kind")=="tool" for c in cases)!=12:
        issue("English instruction/tool split wrong")
    if len({c.get("id") for c in cases})!=24:
        issue("Duplicate English benchmark case IDs")
    if any(not str(c.get("prompt","")).isascii() for c in cases):
        issue("English-only benchmark has non-ASCII or Persian test prompts")
    for key in ("source_sha256","original_private_evidence_archive_sha256","posthoc_review_sha256"):
        if not re.fullmatch(r"[a-f0-9]{64}",str(data.get(key,""))):
            issue("Broken benchmark evidence chain: "+key)
    for model in models:
        name=model.get("id","unknown")
        rs=model.get("cases",[])
        s=model.get("summary",{})
        if len(rs)!=24 or not model.get("verified_postload_warmup"):
            issue("Model test incomplete/not warmloaded: "+name)
            continue
        if not re.fullmatch(r"[a-f0-9]{64}",str(model.get("model_sha256",""))):
            issue("Missing pinned model weight hash: "+name)
        if not re.fullmatch(r"[a-f0-9]{64}",str(model.get("raw_evidence_sha256",""))):
            issue("Missing model raw evidence SHA: "+name)
        if {x.get("case_id") for x in rs}!={c["id"] for c in cases}:
            issue("Model did not answer all frozen questions: "+name)
        instructions=[x for x in rs if x.get("kind")=="instruction"]
        tools=[x for x in rs if x.get("kind")=="tool"]
        if len(instructions)!=12 or len(tools)!=12:
            issue("Invalid model question group sizes: "+name)
            continue
        strict=sum(x.get("criterion_aligned_pass_v1_1") is True for x in instructions)
        original=sum(x.get("initial_strict_pass") is True for x in tools)
        revised=sum(x.get("criterion_aligned_pass_v1_1") is True for x in tools)
        positive=sum(x.get("criterion_aligned_pass_v1_1") is True for x in tools if x.get("case_id") not in ("T09","T10"))
        negative=sum(x.get("criterion_aligned_pass_v1_1") is True for x in tools if x.get("case_id") in ("T09","T10"))
        if strict!=s.get("instruction_exact_pass") or original!=s.get("original_tool_strict_pass") or revised!=s.get("tool_end_to_end_pass"):
            issue("Model scores inconsistent with case rows: "+name)
        if positive!=s.get("positive_tool_end_to_end_pass") or negative!=s.get("no_tool_decision_and_exact_final_pass"):
            issue("Tool/non-tool scores inconsistent: "+name)
        if any(r.get("api_response_statuses") is None or not r.get("final_answer") is not None for r in rs):
            issue("Missing case-level model output: "+name)
        if s.get("all_http_ok")!=24:
            issue("Reported 24 successful API requests inconsistent: "+name)
    for lang in ("en","fa"):
        if not (ROOT/"docs"/lang/"model-english-instruction-tools.md").is_file():
            issue("Missing bilingual English-only test report: "+lang)


def check_model_candidates_20261112() -> None:
    file=ROOT/"research/model-candidates-20261112.json"
    if not file.exists():
        issue("Current model-candidate registry missing")
        return
    obj=json.loads(file.read_text(encoding="utf8"))
    if obj.get("schema")!="DEC-MODEL-CANDIDATES-20261112-v1":
        issue("Unexpected model candidate catalogue schema")
    choices=obj.get("candidates",[])
    if len(choices)!=18:
        issue("Not all source-reviewed candidates are registered")
        return
    ids=[x.get("id") for x in choices]
    names=[x.get("name") for x in choices]
    if len(set(ids))!=18 or len(set(names))!=18:
        issue("Candidate ids or names duplicated")
    groups={p:0 for p in ("NOW","NEXT","CONTROL","RESEARCH")}
    for c in choices:
        tier=c.get("tier")
        if tier not in groups:
            issue("Unknown candidate priority tier")
            continue
        groups[tier]+=1
        if not str(c.get("url","")).startswith("https://"):
            issue("Model official source URL missing")
        if not str(c.get("license","")).strip() or not str(c.get("params","")).strip():
            issue("Missing model license or parameter information: "+str(c.get("id")))
        for field in ("role","risk"):
            if not isinstance(c.get(field),dict) or not all(str(c[field].get(l,"")).strip() for l in ("fa","en")):
                issue("Bilingual candidate annotation incomplete: "+str(c.get("id")))
        if c.get("model_dec_evidence") not in ("E0 source review only","E1 local tool/instruction scope only"):
            issue("Candidate evidence status ungrounded: "+str(c.get("id")))
    if groups["NOW"]<5 or groups["CONTROL"]<2:
        issue("Immediate/current experiment comparator groups missing")
    if obj.get("owner_constraints",{}).get("test_language")!="English only":
        issue("User English-only test requirement lost")
    if obj.get("owner_constraints",{}).get("doc_languages")!=["fa","en"]:
        issue("Publication bilingual requirement lost")
    if not any(x["id"]=="QW25-3" and x["license"]=="qwen-research" for x in choices):
        issue("Historical Qwen2.5:3B commercial license risk missing")
    if not any(x["id"]=="RAON1" for x in choices) or not any(x["id"]=="BOTPSY" for x in choices):
        issue("New November 2026 releases omitted")
    for lang in ("fa","en"):
        file=ROOT/"docs"/lang/"model-candidates-20261112.md"
        if not file.exists():
            issue("Bilingual model-candidate research report missing")
        elif len(file.read_text(encoding="utf8"))<4500:
            issue("Model candidate report suspiciously short")


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
    check_minicpm_sampler_ablation()
    check_liquid_model_warm20()
    check_english_instructions_and_tools()
    check_model_candidates_20261112()
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