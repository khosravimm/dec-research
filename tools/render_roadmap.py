#!/usr/bin/env python3
"""Render bilingual DEC public roadmap from a single versioned JSON source.

Output is a pair of documentation pages. No network, no hidden private data,
no implicit experiment results. Intended for local reproducible generation.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "research" / "roadmap.json"

def parse() -> dict:
    return json.loads(SRC.read_text(encoding="utf-8"))

HEADINGS = {
    "en": {
        "title": "Detailed research and delivery roadmap",
        "intro": "This versioned roadmap supersedes the short v0.1.0 outline as the **public, disclosure-safe execution plan**. Work has been designed, **not performed**. Selection of a language model, LoRA training, complete DEC implementation or measured benchmark superiority is **not claimed**.",
        "status":"Status and guiding decisions",
        "phases":"Phases, planning duration and evidence gates",
        "dependencies":"Phase dependencies and critical path",
        "work":"Work breakdown structure ? complete package definitions",
        "budget":"Effort and scheduling assumptions",
        "metrics":"Preregistered evaluation design (proposed values)",
        "gates":"Go / No-go decision rules",
        "risks":"Risk register",
        "publication":"Scientific publication, collaboration and commercial protections",
        "operations":"Operating rhythm, traceability and status reporting",
        "first":"First actionable tasks",
        "sources":"Methodological references and related records",
        "deliver":"Deliverable",
        "scope":"Scope / method",
        "accept":"Acceptance / verification",
        "needs":"Depends on",
        "backlog":"Links to original internal DEC-BK items (identifiers only)",
        "status_col":"State",
        "effort":"Estimate",
        "role":"Accountable role",
        "owner":"Approval role",
        "time":"Duration",
        "stage":"Stage",
        "risk":"Risk",
        "treatment":"Mitigation and response",
        "sev":"Initial severity",
    },
    "fa": {
        "title": "����? ��?�? ??�� � ����? DEC",
        "intro": "�?� ����? 뫦�?���? ᩥ ?�? v0.1.0 �� ��?���� **����� ����? � ?��?�?��� ����??** ����� �??��. ����?�? ?��? **᩟�? ���?��? �� ����**. �뢦�� ���? ��? ����� LoRA? ??���?���? ?��� DEC ?� ����� ����? ��?꟩? ��� ��??���.",
        "status":"���?� � ���?�?�? ��?�",
        "phases":"埪�? ꧢ ������? � ��ퟪ�?�? ���",
        "dependencies":"ퟠ��?? 埪� � �?� �����?",
        "work":"�?�� ?�� (WBS) � ��� ?��� ����?�",
        "budget":"������ �럠�? ���?��? � ��?�",
        "metrics":"᩟�? ??��쟧? ���?��? � ??�?��� ���?�",
        "gates":"��� ���?� ����� ?� ����",
        "risks":"�墩 �?�?",
        "publication":"�뢬�� ���?? ��?��? � ��� ���� ����?",
        "operations":"?��� �?�?�? ��?��? � ?���� ���?�",
        "first":"릫�?� �租�?�? 矠� ����",
        "sources":"�럠� ���?�럫? � ꧟�? ꩢ��",
        "deliver":"����? 矠� ���?�",
        "scope":"����� / ���",
        "accept":"��?�� ?�?�� / ���",
        "needs":"??�?�?��",
        "backlog":"�럫� ??�� �� Backlog ����? DEC-BK (���� ���� ����?)",
        "status_col":"���?�",
        "effort":"������",
        "role":"�� ?���??�",
        "owner":"�� ���?�??���",
        "time":"ꧢ",
        "stage":"ꩥ��",
        "risk":"�?�?",
        "treatment":"?뢩� � �租�",
        "sev":"��� ���?�",
    },
}
LABELS = {
    "en":{
        "P0":"P0 ? foundations and preregistration",
        "P1A":"P1-A ? core and tool/router baselines",
        "P1B":"P1-B ? trained expertise and retrieval",
        "P1C":"P1-C ? runnable three-level cognitive system",
        "P2":"P2 ? latent/in-process efficiency, conditional",
        "P3":"P3 ? native integrated cognition, conditional",
        "CONT":"Ongoing ? scientific publication & governance",
        "FUTURE":"Future ? multitenancy/distribution deferred",
    },
    "fa":{
        "P0":"P0 ? �꟧�?���? � ??�?��� �����",
        "P1A":"P1-A ? 쫢�? ����� � Router",
        "P1B":"P1-B ? ����? LoRA � ���?��? ���",
        "P1C":"P1-C ? ����� �럦�? ��?��? 矠� ����",
        "P2":"P2 ? ��?��?���? ������ � ꥟��� ���� (ꬩ��)",
        "P3":"P3 ? ??�� ��꟩? �럦�? ����? (ꬩ��)",
        "CONT":"??���� ? �뢬��? ���� � ��?�?�",
        "FUTURE":"�?�� ? ?�?����� � ?맫���? ����",
    }
}
ROLE = {
 "en":{"research-engineering":"Research engineering lead","evaluation":"Independent evaluation lead","project-owner":"Project owner","research-governance":"Research / publication steward"},
 "fa":{"research-engineering":"꫞�� ��맫? ??��","evaluation":"꫞�� ���?��? ꫢ��","project-owner":"��? ?��?�","research-governance":"꫞�� �뢬�� � ��?�?� ??��"},
}

def render(lang:str, doc:dict)->str:
    h=HEADINGS[lang]
    lines=[
        "---",
        "doc_id: DEC-DOC-007",
        f"language: {lang}",
        f"title: \"{h['title']}\"",
        f"version: {doc['version']}",
        f"date: {doc['created_at']}",
        "evidence_level: E0",
        "publication_status: public-research-draft",
        "---", "",
        f"# {h['title']}", "", h["intro"], "",
        f"## 1. {h['status']}", "",
    ]
    if lang=="en":
        lines += [
        "**Current evidence:** E0 architecture plus linked public prior art and an internal 39-item planned study backlog. The initial bilingual research dossier has been published. **No DEC execution result or selected core exists.**",
        "",
        "**Scope:** one trusted local cognitive domain, one active case at a time; replaceable small LLM; domain LoRA and own-RAG; authorized default-on Cross-RAG with opt-out; three L1/L2/L3 reasoning levels; evidence-aware, bounded latent-first communication. Later, contingent native model integration. Multi-user/multi-server remains deferred.",
        "",
        "**Project control principle:** research before selection; gates rather than fixed commitments; maintain a best-simple-baseline alternative; measure quality per *total* compute, not token count alone.",
        ]
    else:
        lines += [
        "**��� ���?:** ��꟩? E0? ??�?�� ꫢ� � ?? �租� ??��? �����?�?�??��� �� Backlog ����?. ?���� ����? ������� �뢬� ��� ���? �� **�?? �?�� ���?� DEC ?� �� ?�?� �뢦� 맟�?�.**",
        "",
        "**�����:** ?? ���� �럦�? ��? ���� ��꟧ � ?? ?���� ��� �� � ���? LLM ?�?? 矠� ���?�? LoRA? RAG ������?? Cross-RAG ꤟ� � 矠� �����?? �� �� L1/L2/L3? ������ ���� ꥧ�� � ꠢ�? �� ���. ���� �� ����? ꬩ�� �� �?�� ���. ?�?����� � ?맫���? ���� �??���.",
        "",
        "**��� �?�?�:** ���?� ??� �� �뢦��? ??� �?�� ��?��? ��� ���?� ����? ��� ?�?�� ����?�� ��?���� ��?�? �뤬 ??�?� ��?���? **?� �럠� ꥟����?**? �� ��� �㧟� ��?�.",
        ]
    lines += ["", f"## 2. {h['phases']}", ""]
    if lang=="en":
        lines+= ["| Phase | Indicative duration* | Gate | Major outcome | State |","|---|---:|---|---|---|"]
    else:
        lines+= ["| 埪 | ꧢ ��?�?* | ??� | �?�� ���? | ���?� |","|---|---:|---|---|---|"]
    outcome_en={
        "P0":"Snapshot, licensed bilingual golden set, harness, risk/IP gate",
        "P1A":"Rank core models, verify tools and adaptive routing",
        "P1B":"Trained LoRAs, expert-owned RAG, evidence and cache contracts",
        "P1C":"Runnable L1/L2/L3 plus matched-budget empirical acceptance",
        "P2":"Measured and reversible latent/cache/runtime improvements",
        "P3":"Ablated learned architecture / valid negative result, prior-art review",
        "CONT":"Bilingual disclosures, citations, results and contributor policy",
        "FUTURE":"Separate feasibility authorisation, not a current deliverable"}
    outcome_fa={
        "P0":"�����?? ���� ꩤ� �������? ����� �뤬 � ?뢩� ����",
        "P1A":"��?�� 쫢�?�? ������ � Router ��?�?",
        "P1B":"LoRA ���?? RAG ����?? 穟���� ��� � Cache",
        "P1C":"����? L1/L2/L3 � ���?� �� ��?�� �����",
        "P2":"��?��?���? ����/Cache/Runtime �� ���� ���? � ���?��",
        "P3":"�� ?��?���? �� Ablation ?� �?�� ꫢ�? ����? ??�?��",
        "CONT":"�뢬�� �������? ���럧? �?�� � �?��� ꬟�?�",
        "FUTURE":"��� ����? ꫢ�� �?��? �� ���?� ?���?"}
    for p in doc["phases"]:
        du=p["duration_weeks"]
        duration=f"{du[0]}?{du[1]} "+("weeks" if lang=="en" else "���") if du else ("continuous" if p["id"]=="CONT" else "not scheduled") if lang=="en" else ("??����" if p["id"]=="CONT" else "���?��??묧�")
        outcome=(outcome_en if lang=="en" else outcome_fa)[p["id"]]
        lines.append(f"| **{p['id']}** | {duration} | {p['gate']} | {outcome} | {p['state']} |")
    if lang=="en":
        lines+=["","*All durations are provisional, not an approval or promise of delivery. They assume a dedicated researcher and are subject to a fresh hardware/resource and data audit. P2/P3 may be rejected. No fixed dates are assigned to GitHub Milestones until P0 confirms capacity.*"]
    else:
        lines+=["","*��� ꧢ?� �������? �� ��??� ����� ?� ��� ���?�. �� ??��?� ��?� ��� � ?� �� ��?�? �럠� � ���� ����?�? �??���. ��?� ��� P2/P3 �� ���. �� ꬦ�?��� ��?� P0 ���? Milestone� ���?� ���? ��??� ��??���.*"]
    lines += ["", f"## 3. {h['dependencies']}", ""]
    lines += [
        "```mermaid",
        "flowchart LR",
        '    P0["P0: Foundation"] --> P1A["P1-A: Core"]',
        '    P1A --> P1B["P1-B: Experts / RAG"]',
        '    P1B --> P1C["P1-C: L1/L2/L3"]',
        '    P1C --> G1{"G1: Evidence?"}',
        '    G1 -->|Proceed| P2["P2: Latent optimization"]',
        '    G1 -->|Revise / Stop| SIMPLE["Keep best simpler baseline"]',
        '    P2 --> G2{"G2: Measured value?"}',
        '    G2 -->|Proceed| P3["P3: Integrated model research"]',
        '    G2 -->|Reject| SIMPLE',
        '    P3 --> G3{"G3: Novel validated mechanism?"}',
        '    G3 -->|Pass| REVIEW["IP / partner review"]',
        '    G3 -->|Reject| SIMPLE',
        '    PUB["Bilingual science & disclosure control"] -.-> P0',
        '    PUB -.-> P1C',
        '    PUB -.-> P3',
        "```",
        "",
    ]
    if lang=="en":
        lines +=["**Critical dependency chain:** rights-cleared tasks ? verified hardware ? frozen model benchmark ? LoRA/RAG/evidence mechanisms ? runnable L1/L2/L3 ? matched-budget acceptance ? latency/memory bottleneck profiling ? optional latent optimization ? optional new learned architecture. *Do not* train adapters on held-out evaluation sets or start native architecture work before a positive P1/P2 gate."]
    else:
        lines +=["**�?� ퟠ��?? �����?:** ���� ����? �� ���埧� ? ���?�媟� ��??���� ? ��?꟩? ���� 쫢� ? LoRA/RAG/��� ? L1/L2/L3 矠� ���� ? ����� �� ����� ����� ? ?���?� ?��?�� ? ��?��?���? ���� ���?��? ? ??�� �� ����? ꬩ��. ����� Adapter ��? ���� ����� ��?? ?� ���� ��꟩? ��?� ??� �� Gate �㢠� ꤟ� �?��."]
    lines+=["",f"## 4. {h['work']}",""]
    for p in doc["phases"]:
        lines += [f"### {LABELS[lang][p['id']]}", ""]
        packages=[w for w in doc["work_packages"] if w["phase"]==p["id"]]
        for wp in packages:
            deps=", ".join(wp["dependencies"]) or ("None" if lang=="en" else "맟��")
            back=", ".join(wp["legacy_backlog_ids"]) or ("None" if lang=="en" else "맟��")
            estimated=f"{wp['estimated_person_days']} "+("person-days" if lang=="en" else "�婩��") if wp["estimated_person_days"] else ("deferred" if lang=="en" else "����")
            lines+= [
                f"#### {wp['id']} ? {wp['title'][lang]}", "",
                f"**{h['scope']}:** {wp['scope'][lang]}","",
                f"**{h['deliver']}:** {wp['deliverable'][lang]}","",
                f"**{h['accept']}:** {wp['acceptance'][lang]}","",
                f"**{h['needs']}:** {deps} � **{h['backlog']}:** {back}  ",
                f"**{h['role']}:** {ROLE[lang].get(wp['owner_role'],wp['owner_role'])} � **{h['effort']}:** {estimated} � **{h['status_col']}:** `{wp['status']}` (`E0`)","",
            ]
    lines+=["", f"## 5. {h['budget']}", ""]
    for a in doc["assumptions"]:
        lines += [f"- {a[lang]}"]
    total=sum(w["estimated_person_days"] for w in doc["work_packages"])
    actual=[w for w in doc["work_packages"] if w["phase"] not in ("FUTURE","CONT")]
    core=sum(w["estimated_person_days"] for w in actual)
    if lang=="en":
        lines+=["",f"**First-cut effort envelope:** {core} person-days for research phases P0?P3 if all phases pass, plus ongoing publication/governance; **not** funded, assigned or approved. P0?P1C = {sum(w['estimated_person_days'] for w in actual if w['phase'] in ('P0','P1A','P1B','P1C'))} person-days. Detailed estimates require P0 capacity review and explicit contingency; public GitHub issue labels do not constitute funding or engineering assignment."]
    else:
        lines+=["",f"**������ ���?�:** {core} �婩�� ���? P0 �� P3 ��� �� ���� ��� ��� ??�?�? ��?����� ���?� ??���� �뢬��/��?�?�? **���?� ����� ?� �?�� �?��**. P0 �� P1C ����� {sum(w['estimated_person_days'] for w in actual if w['phase'] in ('P0','P1A','P1B','P1C'))} �婩�� ���. ���?� ��?� ?� �� P0? ��?� � ��?�� ���?��? �뤟� �??���."]
    lines+=["",f"## 6. {h['metrics']}",""]
    plan=doc["proposed_experiment_design"]
    if lang=="en":
        lines += [f"- **Proposed gold set:** initial >= {plan['candidate_golden_set_size']} independently adjudicable tasks, >= {int(plan['fa_share_min']*100)}% Persian and >= {int(plan['en_share_min']*100)}% English, including mixed-language and counterexamples. This is an **unapproved planning target**, not a prepared dataset.",
                  "- **Primary outcomes:** held-out correctness; evidence citation faithfulness; accepted task quality at matched total compute.",
                  "- **Secondary outcomes:** abstention/error calibration; cold/warm TTFT; end-to-end p50/p95; peak host/GPU RAM incl. LoRA and KV; total in/out tokens, tensor bytes and cost per correct answer.",
                  "- **Validity:** preregister effect sizes, noninferiority margins and failure thresholds in P0; use paired comparisons and 95% paired bootstrap intervals when appropriate, plus at least three controlled timing repeats; report uncertainty and negative cases. Human/LLM judges require calibration.",
                  "- **No numeric performance target is presently an approved success criterion.** Quality must be protected first, and the measured total-resource trade-off must justify added system complexity."]
    else:
        lines +=[f"- **���� ꩤ� ??��쟧?:** ����� {plan['candidate_golden_set_size']} ?���� 矠� ����? ꫢ�� �� ����� {int(plan['fa_share_min']*100)}? 埩�? � {int(plan['en_share_min']*100)}? ��?�?�? �꩟� �ퟩ� ��??�? � ���?. �?� **�� �����?�?�? ��??�묧�** ���? �� ���� �꟧�.",
                 "- **��� ���?:** ��� ?��� ��? ���� ꫢ��? �埧��? ���럧? ??�?� ��?�� ��?���? ?� �럠� �����.",
                 "- **��� ��?:** ��� ����? TTFT ���/?��? ���?� p50/p95? �?�?�� RAM/VRAM ���� LoRA � KV? ��?� ����?/����?? ��� Tensor � �?�� ��?���? ?��� ��?�.",
                 "- **�㢠��:** ��� �����?? ���?� �� ꤟ� � ������ �?�� �� P0 ??�?��� ���? ��?�� ��? � ���� ??? Bootstrap �� ���� �럫� � ����� �� �?��� ?뢩�?��� ���? ���? ��?���?� � �?��?� ��� ���? ���� �뫟�?/��? ?��?��� ���.",
                 "- **���� �?? �� 㧧? ���?�� ��?�� ?�?�� ���?�?��� �?��.** ��� ??�?� ?���? �?� ���?� ꭩ� ?� �럠� � ????�??."]
    lines+=["",f"## 7. {h['gates']}",""]
    for g in doc["gates"]:
        lines +=[f"### {g['id']} ? {LABELS[lang][g['phase']]}", "",
                f"**{h['accept']}:** {g['criterion'][lang]}", "",
                f"**{h['owner']}:** {g['approval']} � **Fallback:** {g['fallback']}", ""]
    lines+=["",f"## 8. {h['risks']}",""]
    if lang=="en":
        lines += ["| ID | Risk | Initial severity | Mitigation / response |", "|---|---|---|---|"]
    else:
        lines += ["| �럫� | �?�? | ��� ���?� | ?뢩� � �?� |", "|---|---|---|---|"]
    for risk in doc["risks"]:
        lines.append(f"| {risk['id']} | {risk['threat'][lang]} | {risk['severity']} | {risk['treatment'][lang]} |")
    lines+=["",f"## 9. {h['publication']}",""]
    if lang=="en":
        lines+= [
            "Maintain a two-tier evidence/publication policy: **private, access-controlled original experiment and invention records** vs **public bilingual disclosure-safe summaries**. GitHub's public version history is not proof of sole copyright ownership or patent priority, and public disclosure may damage later claims. Do not copy sensitive LDI corpus, model weights, internal infrastructure or unpublished original technical mechanisms into public issues.",
            "",
            "Every public result needs source/revision, rights clearance, independently evaluated grade (E0?E3), baseline, confidence/limitations and the related ADR. Commercial proposals must distinguish rights to original implementation from third-party models, dependencies and methods. Collaborator contribution and licensing rights must be agreed in writing before merging external code/data. No patent registered or commercial product is claimed.",
            "",
            "See [Publication and IP](publication-ip.md), [Contributing](contributing.md), [Security](security.md)."
        ]
    else:
        lines+= [
            "�� �?� �뢬�� ��� ���: **꧟�? ���? ���?� � ������ �����? �� ���? ����? �� ?뢩� �����?** �� ����� **�韭� ������� ����? ?��?�?���**. ���?�?� GitHub �� ���? �륭�� �� ��� ?� ��� ����? ������ �?�� � �嬟? ����? �??��� ����? ��? �� ꥧ�� ?�. ����� ��럧 LDI? ��� ��? �?����� ����? � �?��?�� �����? �뢬�묧� 렟?� �� Issue ����? 穟� �??��.",
            "",
            "� �?�� ����? �� ���/뫦�? ��� �뢬��? ��� ��� E0 �� E3? �� ��? ��?���?� � ADR ꩢ�� ����. �� ����� ����?? �� ??���?���? ��?� ��?� �� �� � ퟠ��?? � ��� ����� ��� ��� ���. ���� ꬟�?� ����� ??� �� ���� ?�/���� �� ���� ?��? ꬦ� ���. �?? ������ ���?��� ?� ꥭ�� ����? ��� ��??���.",
            "",
            "[�?��� �뢬�� � ��??�](publication-ip.md) � [꬟�?�](contributing.md) � [���?�](security.md)."
        ]
    lines+=["",f"## 10. {h['operations']}",""]
    if lang=="en":
        lines+= [
            "- **Daily execution:** one task at a time where practical; note environment/config and result before switching models or experts.",
            "- **Weekly technical review:** update work package state, blockers, next experiments, reproducibility and time/resource consumption.",
            "- **Every two weeks:** owner reviews any changed scope, risk/quality gate and project critical path; no silent moving acceptance thresholds.",
            "- **Monthly public review:** update both languages together, source catalogue, ADRs, negative results and public status without exposing unapproved mechanisms.",
            "- **On each GitHub pull request:** automatic EN/FA structural validation, JSON schema/reference integrity, secret scanning and owner review. A green workflow is not an IP/legal sign-off.",
            "- **State semantics:** `planned`, `ready`, `in_progress`, `blocked`, `review`, `accepted`, `rejected`, `deferred`. Change state only with linked evidence; current roadmap entries remain `planned`.",
        ]
    else:
        lines+= [
            "- **����? ������:** ���?��� �?�?�/쟫�/�� ꬦ� �� ?�?�� �����? ��� ���?� � �?�� ??� �� ��??�.",
            "- **����?�? ��??:** ���?� ����? ���? ����� ��?? ������?� � ꭩ� ���/�럠�.",
            "- **� �� ���:** ����?�? ��? ���? �����? ??� ??�?�/�?�? � �?� �����?? ��??� ?���? ������ �����.",
            "- **���� �� ꦪ� ����?:** �뢬�� ���� �� ����? ��� ���? ADR? �?�� ���? � ���?� ���� �嬟? �?��?�� �?�ꤟ�.",
            "- **���? � Pull Request:** ?뢩� ���?�� ��� ��럧? JSON � �����? ����? Secret � ��??� �?짟���? CI ��� ��� ����? �뢬�� �?��.",
            "- **��韢 ���?�:** `planned`? `ready`? `in_progress`? `blocked`? `review`? `accepted`? `rejected`? `deferred`. ��??� ���?� ��� �� ���? ����?�? ���? ��?? `planned` 쫢�.",
        ]
    lines+=["",f"## 11. {h['first']}",""]
    seq=["DEC-WP-001","DEC-WP-002","DEC-WP-003","DEC-WP-004","DEC-WP-005","DEC-WP-006"]
    for id in seq:
        x=next(p for p in doc["work_packages"] if p["id"]==id)
        lines.append(f"- **{id}** ? {x['title'][lang]}: {x['deliverable'][lang]}")
    if lang=="en":
        lines+=["","**Start gate:** P0 can start without committing to a base model or introducing a new runtime. LDI read-only audit, hardware snapshot and synthetic benchmark design are the first evidence-producing tasks. The roadmap itself is a documented plan (E0), not a completed P0 result."]
    else:
        lines+=["","**�䟪 �?�:** P0 ���� �뢦�� ���? �� ?� 뭠 Runtime ��?� �䟪?�?� ���. ��?�? ���?����? LDI? ��� �럠� � ᩟�? ���� ����? 릫�?� �租꟢ ���?� ����. ��� �?� ����? ᩥ E0 ���? �� �?�� �?�?� P0."]
    lines+=["",f"## 12. {h['sources']}",""]
    refs=[
      ("ISO/IEC/IEEE 29119-1:2022 ? software testing concepts","https://www.iso.org/standard/81291.html"),
      ("NIST AI RMF GenAI Profile ? governance, measurement and risk","https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence"),
      ("GitHub Milestones ? issue tracking and completion","https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones"),
      ("MLflow evaluation datasets ? golden sets, lineage","https://mlflow.org/docs/latest/genai/datasets"),
    ]
    for title,url in refs:lines.append(f"- [{title}]({url})")
    lines+=["",
        "Public linked datasets and references: [research catalogue](../../research/catalogue.json) � [initial experiment register](../../research/experiment-register.json) � [machine-readable roadmap](../../research/roadmap.json).",
        "",
        "**Versioning:** document `DEC-DOC-007`, public roadmap `0.2.0`, created 2026-11-12; detailed implementation and novel algorithms may be withheld pending publication/IP review. No roadmap milestone is declared completed by this version.",
        ""]
    return "\n".join(line.rstrip() for line in lines)

def main()->int:
    p=parse()
    for lang in ("en","fa"):
        file=ROOT/"docs"/lang/"roadmap.md"
        text=render(lang,p)
        file.write_text(text,encoding="utf-8",newline="\n")
        print(f"{file.relative_to(ROOT)}: {len(text)} chars, {len(p['work_packages'])} packages")
    return 0

if __name__=="__main__":
    sys.exit(main())