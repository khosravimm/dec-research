#!/usr/bin/env python3
"""Render public bilingual DEC roadmap from the authoritative validated JSON."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "research/roadmap.json").read_text(encoding="utf-8"))

STRINGS={
"en":{
"title":"Detailed research and implementation roadmap",
"intro":"This is the controlled, versioned research and delivery plan (E0). No DEC model, LoRA specialization, complete three-level council, benchmark result or new architecture is claimed to have been implemented.",
"status":"Current state and scope","phases":"Phases and estimated durations","flow":"Critical path and dependencies","work":"Work breakdown and acceptance contracts","resources":"Resource estimates and assumptions","metrics":"Measurement and statistical validity","gates":"Evidence gates (Go/No-go)","risks":"Risk register","governance":"Research, publication, IP and change governance","next":"Immediate action sequence","refs":"Normative and technical references",
"phase":"Phase","duration":"Estimated duration","gate":"Gate","state":"State",
"scope":"Scope/method","deliver":"Deliverable","accept":"Acceptance evidence","deps":"Dependencies","legacy":"Historical backlog IDs","role":"Accountable role","effort":"Estimated effort","issue":"GitHub tracking issue","time_unit":"weeks","days":"person-days","none":"None","not_scheduled":"Not scheduled","continuous":"Continuous",
"crit":"The critical path is: legally usable bilingual benchmark and actual hardware audit -> fair small-model core selection -> real LoRA and RAG + typed evidence protocol -> executable L1/L2/L3 -> matched-budget independent acceptance -> conditional latent/cache optimization -> conditional native learned model architecture. Do not switch to an advanced phase before its evidence gate.",
"estimate":"Phase and work-package estimates are provisional planning assumptions for one focused full-time research engineer plus occasional evaluation and legal review. They are not funded commitments or project deadlines; P2/P3 might be rejected. Replan after P0 based on resource constraints and measured bottlenecks.",
"metrics_text":"Proposed pre-registered evaluation (NOT yet approved): at least 160 independently reviewable FA/EN cases, at least 40% Persian and 30% English, with mixed-language and negative/abstention examples. Compare quality and evidence faithfulness at matched total compute. Capture p50/p95 end-to-end time, TTFT cold/warm, peak RAM/VRAM including adapters/KV, total prefill/output tokens, tensor bytes, failures and abstention. Preregister minimal useful improvement and noninferiority margins in P0. Use paired tests, uncertainty estimates (e.g. 95% paired bootstrap when appropriate), and at least three timing repeats. Missing metrics are unknown, never zero.",
"publication":"Public work is bilingual and source-linked, with an explicit E0-E3 evidence grade and outcome even when negative. Novel mechanisms, unfiled IP, private LDI corpus, sensitive infrastructure, unlicensed data and implementation details requiring clearance remain private. GitHub commits do not prove ownership or patent rights. Publication has its own legal review gate. Do not promise commercial value or open-source licences.",
"cadence":"Daily: complete one traceable task/test before switching context. Weekly: update blockers, evidence, performance and work-package states. Fortnightly: owner gate and resource review. Monthly: bilingual publication after source/rights checks. Status changes require a linked experiment/result or decision, never a cosmetic percentage.",
"first_intro":"Begin with P0: governance, read-only LDI audit, verified compute/model inventory, evaluation gold set, reproducibility harness and rights/prior-art review. The roadmap is not proof that these tasks are already done.",
"footer":"All work packages remain planned; deferred future items have not been authorized. This document is generated from research/roadmap.json, not hand-edited."
},
"fa":{
"title":"\u0631\u0648\u062f\u0645\u067e \u062c\u0627\u0645\u0639 \u067e\u0698\u0648\u0647\u0634 \u0648 \u0627\u062c\u0631\u0627\u06cc DEC",
"intro":"\u0627\u06cc\u0646 \u0646\u0633\u062e\u0647\u060c \u0628\u0631\u0646\u0627\u0645\u0647 \u06a9\u0646\u062a\u0631\u0644\u200c\u0634\u062f\u0647 \u067e\u0698\u0648\u0647\u0634 \u0648 \u0627\u062c\u0631\u0627 \u0628\u0627 \u062f\u0631\u062c\u0647 \u0634\u0648\u0627\u0647\u062f E0 \u0627\u0633\u062a. \u0647\u06cc\u0686 \u0645\u062f\u0644 DEC\u060c \u0645\u062a\u062e\u0635\u0635 LoRA \u0622\u0645\u0648\u0632\u0634\u200c\u062f\u06cc\u062f\u0647\u060c \u0634\u0648\u0631\u0627\u06cc \u06a9\u0627\u0645\u0644 \u0633\u0647\u200c\u0633\u0637\u062d\u06cc\u060c \u0628\u0646\u0686\u0645\u0627\u0631\u06a9 \u0639\u0645\u0644\u06cc \u06cc\u0627 \u0645\u0639\u0645\u0627\u0631\u06cc \u0639\u0635\u0628\u06cc \u062c\u062f\u06cc\u062f\u06cc \u062f\u0631 \u0627\u06cc\u0646 \u0645\u0631\u062d\u0644\u0647 \u0627\u062c\u0631\u0627 \u0648 \u0627\u062b\u0628\u0627\u062a\u200c\u0634\u062f\u0647 \u0627\u0639\u0644\u0627\u0645 \u0646\u0645\u06cc\u200c\u0634\u0648\u062f.",
"status":"\u0648\u0636\u0639\u06cc\u062a \u0645\u0648\u062c\u0648\u062f \u0648 \u062f\u0627\u0645\u0646\u0647","phases":"\u0641\u0627\u0632\u0647\u0627 \u0648 \u0645\u062f\u062a\u200c\u0647\u0627\u06cc \u0628\u0631\u0622\u0648\u0631\u062f\u06cc","flow":"\u0645\u0633\u06cc\u0631 \u0628\u062d\u0631\u0627\u0646\u06cc \u0648 \u0648\u0627\u0628\u0633\u062a\u06af\u06cc\u200c\u0647\u0627","work":"\u0633\u0627\u062e\u062a\u0627\u0631 \u0634\u06a9\u0633\u062a \u06a9\u0627\u0631 \u0648 \u0645\u0639\u06cc\u0627\u0631\u0647\u0627\u06cc \u067e\u0630\u06cc\u0631\u0634","resources":"\u0628\u0631\u0622\u0648\u0631\u062f \u0645\u0646\u0627\u0628\u0639 \u0648 \u0645\u0641\u0631\u0648\u0636\u0627\u062a","metrics":"\u0633\u0646\u062c\u0634 \u0648 \u0627\u0639\u062a\u0628\u0627\u0631 \u0622\u0645\u0627\u0631\u06cc","gates":"\u062f\u0631\u0648\u0627\u0632\u0647\u200c\u0647\u0627\u06cc \u062a\u0635\u0645\u06cc\u0645 \u0648 \u0634\u0648\u0627\u0647\u062f","risks":"\u062f\u0641\u062a\u0631 \u0631\u06cc\u0633\u06a9","governance":"\u062d\u0627\u06a9\u0645\u06cc\u062a \u067e\u0698\u0648\u0647\u0634\u060c \u0627\u0646\u062a\u0634\u0627\u0631\u060c \u062d\u0642\u0648\u0642 \u0648 \u062a\u063a\u06cc\u06cc\u0631","next":"\u062a\u0631\u062a\u06cc\u0628 \u0627\u0642\u062f\u0627\u0645\u200c\u0647\u0627\u06cc \u0641\u0648\u0631\u06cc","refs":"\u0645\u0646\u0627\u0628\u0639 \u0647\u0646\u062c\u0627\u0631\u06cc \u0648 \u0641\u0646\u06cc",
"phase":"\u0641\u0627\u0632","duration":"\u0645\u062f\u062a \u0628\u0631\u0622\u0648\u0631\u062f\u06cc","gate":"\u06af\u06cc\u062a","state":"\u0648\u0636\u0639\u06cc\u062a",
"scope":"\u062f\u0627\u0645\u0646\u0647 \u0648 \u0631\u0648\u0634","deliver":"\u062e\u0631\u0648\u062c\u06cc \u0642\u0627\u0628\u0644 \u062a\u062d\u0648\u06cc\u0644","accept":"\u0634\u0627\u0647\u062f \u067e\u0630\u06cc\u0631\u0634","deps":"\u067e\u06cc\u0634\u200c\u0646\u06cc\u0627\u0632","legacy":"\u0634\u0646\u0627\u0633\u0647 \u0627\u0642\u062f\u0627\u0645 \u0642\u0628\u0644\u06cc","role":"\u0646\u0642\u0634 \u0645\u0633\u0626\u0648\u0644","effort":"\u0646\u0641\u0631\u0631\u0648\u0632 \u0628\u0631\u0622\u0648\u0631\u062f\u06cc","issue":"\u0645\u0633\u0626\u0644\u0647 \u0642\u0627\u0628\u0644 \u067e\u06cc\u06af\u06cc\u0631\u06cc \u062f\u0631 GitHub","time_unit":"\u0647\u0641\u062a\u0647","days":"\u0646\u0641\u0631\u0631\u0648\u0632","none":"\u0646\u062f\u0627\u0631\u062f","not_scheduled":"\u0632\u0645\u0627\u0646\u200c\u0628\u0646\u062f\u06cc\u200c\u0646\u0634\u062f\u0647","continuous":"\u067e\u06cc\u0648\u0633\u062a\u0647",
"crit":"\u0645\u0633\u06cc\u0631 \u0628\u062d\u0631\u0627\u0646\u06cc: \u062f\u0627\u062f\u0647 \u0645\u0631\u062c\u0639 \u062f\u0648\u0632\u0628\u0627\u0646\u0647 \u062f\u0627\u0631\u0627\u06cc \u062d\u0642 \u0627\u0633\u062a\u0641\u0627\u062f\u0647 \u0648 \u0645\u0645\u06cc\u0632\u06cc \u0648\u0627\u0642\u0639\u06cc \u0633\u062e\u062a\u200c\u0627\u0641\u0632\u0627\u0631 \u2190 \u0627\u0646\u062a\u062e\u0627\u0628 \u0645\u062f\u0644 \u06a9\u0648\u0686\u06a9 \u0628\u0627 \u0622\u0632\u0645\u0648\u0646 \u0645\u0646\u0635\u0641\u0627\u0646\u0647 \u2190 LoRA \u0648\u0627\u0642\u0639\u06cc \u0648 RAG \u0648 \u0642\u0631\u0627\u0631\u062f\u0627\u062f \u0634\u0648\u0627\u0647\u062f \u2190 L1/L2/L3 \u0642\u0627\u0628\u0644 \u0627\u062c\u0631\u0627 \u2190 \u062a\u0635\u0645\u06cc\u0645 \u0645\u0628\u062a\u0646\u06cc \u0628\u0631 \u0633\u0646\u062c\u0634 \u0628\u0627 \u0645\u0646\u0627\u0628\u0639 \u0628\u0631\u0627\u0628\u0631 \u2190 \u0628\u0647\u06cc\u0646\u0647\u200c\u0633\u0627\u0632\u06cc \u0646\u0647\u0641\u062a\u0647 \u0648 Cache \u0641\u0642\u0637 \u062f\u0631 \u0635\u0648\u0631\u062a \u0645\u0646\u0641\u0639\u062a \u2190 \u067e\u0698\u0648\u0647\u0634 \u0645\u0634\u0631\u0648\u0637 \u0645\u0639\u0645\u0627\u0631\u06cc \u062f\u0631\u0648\u0646\u06cc \u06cc\u0627\u062f\u06af\u0631\u0641\u062a\u0646\u06cc. \u0639\u0628\u0648\u0631 \u0627\u0632 \u0641\u0627\u0632 \u0628\u062f\u0648\u0646 \u0634\u0648\u0627\u0647\u062f \u06af\u06cc\u062a \u0645\u062c\u0627\u0632 \u0646\u06cc\u0633\u062a.",
"estimate":"\u0645\u062f\u062a \u0641\u0627\u0632\u0647\u0627 \u0648 \u0646\u0641\u0631\u0631\u0648\u0632 \u0628\u0633\u062a\u0647\u200c\u0647\u0627 \u0641\u0631\u0636 \u0627\u0648\u0644\u06cc\u0647 \u0628\u0627 \u0638\u0631\u0641\u06cc\u062a \u06cc\u06a9 \u067e\u0698\u0648\u0647\u0634\u06af\u0631 \u062a\u0645\u0627\u0645\u200c\u0648\u0642\u062a \u0645\u062a\u0645\u0631\u06a9\u0632 \u0628\u0647 \u0647\u0645\u0631\u0627\u0647 \u062f\u0627\u0648\u0631\u06cc \u0641\u0646\u06cc \u0648 \u062d\u0642\u0648\u0642\u06cc \u0645\u0642\u0637\u0639\u06cc \u0627\u0633\u062a\u061b \u0646\u0647 \u0628\u0648\u062f\u062c\u0647 \u0645\u0635\u0648\u0628 \u06cc\u0627 \u0645\u0648\u0639\u062f \u062a\u0639\u0647\u062f\u0622\u0648\u0631. P2 \u06cc\u0627 P3 \u0645\u0645\u06a9\u0646 \u0627\u0633\u062a \u0631\u062f \u0634\u0648\u0646\u062f. \u067e\u0633 \u0627\u0632 P0 \u0628\u0627\u06cc\u062f \u0645\u062a\u0646\u0627\u0633\u0628 \u0628\u0627 \u0638\u0631\u0641\u06cc\u062a \u0648\u0627\u0642\u0639\u06cc \u0648 \u06af\u0644\u0648\u06af\u0627\u0647\u200c\u0647\u0627 \u0628\u0627\u0632\u0628\u0631\u0646\u0627\u0645\u0647\u200c\u0631\u06cc\u0632\u06cc \u06a9\u0631\u062f.",
"metrics_text":"\u0637\u0631\u062d \u067e\u06cc\u0634\u0646\u0647\u0627\u062f\u06cc \u067e\u06cc\u0634\u200c\u062b\u0628\u062a \u0622\u0632\u0645\u0648\u0646 (\u0647\u0646\u0648\u0632 \u062a\u0635\u0648\u06cc\u0628 \u0646\u0634\u062f\u0647): \u062d\u062f\u0627\u0642\u0644 \u06f1\u06f6\u06f0 \u067e\u0631\u0648\u0646\u062f\u0647 \u0642\u0627\u0628\u0644 \u062f\u0627\u0648\u0631\u06cc \u0645\u0633\u062a\u0642\u0644 \u0641\u0627\u0631\u0633\u06cc \u0648 \u0627\u0646\u06af\u0644\u06cc\u0633\u06cc\u060c \u0628\u0627 \u062f\u0633\u062a\u200c\u06a9\u0645 \u06f4\u06f0\u066a \u0641\u0627\u0631\u0633\u06cc \u0648 \u06f3\u06f0\u066a \u0627\u0646\u06af\u0644\u06cc\u0633\u06cc \u0648 \u0645\u0648\u0627\u0631\u062f \u062f\u0648\u0632\u0628\u0627\u0646\u0647\u060c \u0645\u0646\u0641\u06cc \u0648 \u0627\u0645\u062a\u0646\u0627\u0639. \u0645\u0642\u0627\u06cc\u0633\u0647 \u0635\u062d\u062a \u0648 \u0648\u0641\u0627\u062f\u0627\u0631\u06cc \u0628\u0647 \u0634\u0648\u0627\u0647\u062f \u0628\u0627 \u06a9\u0644 \u0645\u0646\u0627\u0628\u0639 \u0628\u0631\u0627\u0628\u0631. \u062b\u0628\u062a \u062a\u0623\u062e\u06cc\u0631 \u0646\u0647\u0627\u06cc\u06cc p50/p95\u060c TTFT \u0633\u0631\u062f \u0648 \u06af\u0631\u0645\u060c \u0628\u06cc\u0634\u06cc\u0646\u0647 RAM/VRAM \u0634\u0627\u0645\u0644 LoRA \u0648 KV\u060c \u062a\u0648\u06a9\u0646\u060c \u062d\u062c\u0645 Tensor\u060c \u062e\u0637\u0627 \u0648 \u0627\u0645\u062a\u0646\u0627\u0639. \u062f\u0631 P0 \u062d\u062f\u0627\u0642\u0644 \u0628\u0647\u0628\u0648\u062f \u0627\u0631\u0632\u0634\u0645\u0646\u062f \u0648 \u062d\u062f \u0645\u062c\u0627\u0632 \u0627\u0641\u062a \u067e\u06cc\u0634\u200c\u062b\u0628\u062a \u0634\u0648\u062f. \u0622\u0632\u0645\u0648\u0646 \u062c\u0641\u062a\u06cc \u0648 \u0628\u0631\u0622\u0648\u0631\u062f \u0639\u062f\u0645\u200c\u0642\u0637\u0639\u06cc\u062a (\u0627\u0632 \u062c\u0645\u0644\u0647 \u0628\u0627\u0632\u0647 \u06f9\u06f5\u066a Bootstrap \u062c\u0641\u062a\u06cc \u062f\u0631 \u0635\u0648\u0631\u062a \u062a\u0646\u0627\u0633\u0628) \u0648 \u062f\u0633\u062a\u200c\u06a9\u0645 \u0633\u0647 \u062a\u06a9\u0631\u0627\u0631 \u06a9\u0646\u062a\u0631\u0644\u200c\u0634\u062f\u0647 \u0632\u0645\u0627\u0646 \u0627\u062c\u0631\u0627 \u0634\u0648\u062f. \u0645\u0642\u062f\u0627\u0631 \u0646\u0627\u0645\u0648\u062c\u0648\u062f\u060c \u0645\u062c\u0647\u0648\u0644 \u0627\u0633\u062a \u0646\u0647 \u0635\u0641\u0631.",
"publication":"\u0627\u0646\u062a\u0634\u0627\u0631 \u0639\u0645\u0648\u0645\u06cc \u0628\u0627\u06cc\u062f \u0641\u0627\u0631\u0633\u06cc \u0648 \u0627\u0646\u06af\u0644\u06cc\u0633\u06cc\u060c \u062f\u0627\u0631\u0627\u06cc \u0645\u0646\u0628\u0639\u060c \u0631\u062f\u0647 \u0634\u0648\u0627\u0647\u062f E0 \u062a\u0627 E3 \u0648 \u0646\u062a\u0627\u06cc\u062c \u0645\u0646\u0641\u06cc \u0645\u0639\u062a\u0628\u0631 \u0628\u0627\u0634\u062f. \u0633\u0627\u0632\u0648\u06a9\u0627\u0631 \u0627\u062d\u062a\u0645\u0627\u0644\u06cc \u0627\u0628\u062f\u0627\u0639\u06cc\u060c \u0627\u062e\u062a\u0631\u0627\u0639 \u062b\u0628\u062a\u200c\u0646\u0634\u062f\u0647\u060c \u0627\u0633\u0646\u0627\u062f \u062e\u0635\u0648\u0635\u06cc LDI\u060c \u0632\u06cc\u0631\u0633\u0627\u062e\u062a \u062d\u0633\u0627\u0633\u060c \u062f\u0627\u062f\u0647 \u0641\u0627\u0642\u062f \u0645\u062c\u0648\u0632 \u0648 \u062c\u0632\u0626\u06cc\u0627\u062a \u0646\u06cc\u0627\u0632\u0645\u0646\u062f \u062a\u0635\u0648\u06cc\u0628 \u062f\u0631 \u0645\u062e\u0632\u0646 \u062e\u0635\u0648\u0635\u06cc \u0628\u0645\u0627\u0646\u0646\u062f. Commit \u06af\u06cc\u062a\u200c\u0647\u0627\u0628 \u0633\u0646\u062f \u0642\u0637\u0639\u06cc \u0645\u0627\u0644\u06a9\u06cc\u062a \u06cc\u0627 \u062d\u0642 \u0627\u062e\u062a\u0631\u0627\u0639 \u0646\u06cc\u0633\u062a. \u0647\u0631 \u0627\u0646\u062a\u0634\u0627\u0631 \u06af\u06cc\u062a \u062d\u0642\u0648\u0642\u06cc \u0645\u0633\u062a\u0642\u0644 \u062f\u0627\u0631\u062f \u0648 \u0627\u0631\u0632\u0634 \u062a\u062c\u0627\u0631\u06cc \u06cc\u0627 \u0645\u062c\u0648\u0632 \u0645\u062a\u0646\u200c\u0628\u0627\u0632 \u0646\u0628\u0627\u06cc\u062f \u0628\u062f\u0648\u0646 \u0645\u0628\u0646\u0627 \u0627\u062f\u0639\u0627 \u0634\u0648\u062f.",
"cadence":"\u0631\u0648\u0632\u0627\u0646\u0647: \u062a\u06a9\u0645\u06cc\u0644 \u06a9\u0627\u0631 \u06cc\u0627 \u0622\u0632\u0645\u0648\u0646 \u0645\u0634\u062e\u0635 \u0628\u0627 Trace \u067e\u06cc\u0634 \u0627\u0632 \u062a\u063a\u06cc\u06cc\u0631 \u0632\u0645\u06cc\u0646\u0647. \u0647\u0641\u062a\u06af\u06cc: \u06af\u0632\u0627\u0631\u0634 \u0645\u0627\u0646\u0639\u060c \u0634\u0648\u0627\u0647\u062f\u060c \u06a9\u0627\u0631\u0627\u06cc\u06cc \u0648 \u0648\u0636\u0639\u06cc\u062a \u0628\u0633\u062a\u0647\u200c\u0647\u0627. \u0647\u0631 \u062f\u0648 \u0647\u0641\u062a\u0647: \u0645\u0631\u0648\u0631 \u06af\u06cc\u062a\u200c\u0647\u0627 \u0648 \u0645\u0646\u0627\u0628\u0639 \u062a\u0648\u0633\u0637 \u0645\u0627\u0644\u06a9. \u0645\u0627\u0647\u0627\u0646\u0647: \u0627\u0646\u062a\u0634\u0627\u0631 \u062f\u0648\u0632\u0628\u0627\u0646\u0647 \u067e\u0633 \u0627\u0632 \u06a9\u0646\u062a\u0631\u0644 \u0645\u0646\u0628\u0639 \u0648 \u062d\u0642 \u0627\u0641\u0634\u0627. \u062a\u063a\u06cc\u06cc\u0631 \u0648\u0636\u0639\u06cc\u062a \u0641\u0642\u0637 \u0628\u0631 \u0627\u0633\u0627\u0633 \u0646\u062a\u06cc\u062c\u0647 \u06cc\u0627 \u062a\u0635\u0645\u06cc\u0645 \u067e\u06cc\u0648\u0646\u062f\u062e\u0648\u0631\u062f\u0647 \u0627\u0633\u062a\u060c \u0646\u0647 \u062f\u0631\u0635\u062f \u0638\u0627\u0647\u0631\u06cc.",
"first_intro":"\u06a9\u0627\u0631 \u0631\u0627 \u0627\u0632 P0 \u0622\u063a\u0627\u0632 \u0645\u06cc\u200c\u06a9\u0646\u06cc\u0645: \u062d\u0627\u06a9\u0645\u06cc\u062a\u060c \u0645\u0645\u06cc\u0632\u06cc \u0641\u0642\u0637\u200c\u062e\u0648\u0627\u0646\u062f\u0646\u06cc LDI\u060c \u0645\u0648\u062c\u0648\u062f\u06cc \u0648\u0627\u0642\u0639\u06cc \u0645\u062f\u0644 \u0648 \u0645\u0646\u0627\u0628\u0639\u060c \u062f\u0627\u062f\u0647 \u0645\u0631\u062c\u0639\u060c \u0627\u0628\u0632\u0627\u0631 \u0628\u0627\u0632\u062a\u0648\u0644\u06cc\u062f \u0648 \u06a9\u0646\u062a\u0631\u0644 \u0645\u0646\u0627\u0628\u0639 \u0648 \u062d\u0642\u0648\u0642. \u062e\u0648\u062f \u0631\u0648\u062f\u0645\u067e \u0628\u0647 \u0645\u0639\u0646\u0627\u06cc \u062a\u06a9\u0645\u06cc\u0644 \u0627\u06cc\u0646 \u0627\u0642\u062f\u0627\u0645\u0627\u062a \u0646\u06cc\u0633\u062a.",
"footer":"\u062a\u0645\u0627\u0645 \u0628\u0633\u062a\u0647\u200c\u0647\u0627 \u062f\u0631 \u0648\u0636\u0639\u06cc\u062a \u0628\u0631\u0646\u0627\u0645\u0647\u200c\u0631\u06cc\u0632\u06cc\u200c\u0634\u062f\u0647\u200c\u0627\u0646\u062f \u0648 \u0645\u0648\u0627\u0631\u062f \u0622\u06cc\u0646\u062f\u0647 \u0645\u062c\u0648\u0632 \u0627\u062c\u0631\u0627 \u0646\u062f\u0627\u0631\u0646\u062f. \u0627\u06cc\u0646 \u0633\u0646\u062f \u0627\u0632 research/roadmap.json \u062a\u0648\u0644\u06cc\u062f \u0645\u06cc\u200c\u0634\u0648\u062f \u0648 \u0646\u0628\u0627\u06cc\u062f \u062f\u0633\u062a\u06cc \u0628\u0627 \u0645\u0646\u0628\u0639 \u0627\u0635\u0644\u06cc \u0645\u062a\u0641\u0627\u0648\u062a \u0634\u0648\u062f."
}
}
PHASE_OUTCOME={
"en":{"P0":"Verified environment, benchmark and governance","P1A":"Core, tool and router baseline","P1B":"Specialist LoRA, RAG and evidence transport","P1C":"Runnable three-level cognition and acceptance","P2":"Measured local latent/state integration","P3":"Optional learned model architecture","CONT":"Continuous bilingual public science","FUTURE":"Deferred expansion"},
"fa":{"P0":"\u0645\u062d\u06cc\u0637 \u0645\u0639\u062a\u0628\u0631\u060c \u062f\u0627\u062f\u0647 \u0622\u0632\u0645\u0648\u0646 \u0648 \u062d\u0627\u06a9\u0645\u06cc\u062a","P1A":"\u0645\u0628\u0646\u0627\u06cc \u0647\u0633\u062a\u0647\u060c \u0627\u0628\u0632\u0627\u0631 \u0648 Router","P1B":"LoRA\u060c RAG \u0648 \u0645\u0633\u06cc\u0631 \u0634\u0648\u0627\u0647\u062f","P1C":"\u0646\u0645\u0648\u0646\u0647 \u0633\u0647\u200c\u0633\u0637\u062d\u06cc \u0648 \u067e\u0630\u06cc\u0631\u0634","P2":"\u0627\u062f\u063a\u0627\u0645 \u0645\u062d\u0644\u06cc \u0646\u0647\u0641\u062a\u0647 \u0648 Cache \u0628\u0627 \u0633\u0646\u062c\u0634","P3":"\u0645\u062f\u0644 \u062f\u0631\u0648\u0646\u06cc \u0622\u0645\u0648\u0632\u0634\u200c\u067e\u0630\u06cc\u0631 \u0645\u0634\u0631\u0648\u0637","CONT":"\u0627\u0646\u062a\u0634\u0627\u0631 \u0639\u0644\u0645\u06cc \u062f\u0648\u0632\u0628\u0627\u0646\u0647 \u067e\u06cc\u0648\u0633\u062a\u0647","FUTURE":"\u062a\u0648\u0633\u0639\u0647 \u0645\u0639\u0648\u0642"}
}
def render(lang):
 s=STRINGS[lang]
 out=[
 "---", "doc_id: DEC-DOC-007", f"language: {lang}",
 f"title: \"{s['title']}\"", f"version: {data['version']}",
 f"date: {data['created_at']}", "evidence_level: E0",
 "publication_status: public-research-draft", "---","",
 "# "+s["title"],"",s["intro"],"",
 "## 1. "+s["status"],""
 ]
 if lang=="en":
  out+=["**E0 facts:** Public research dossier exists; 39 previously planned internal tasks are mapped to 35 packages. No DEC performance tests have been executed.", "",
        "**Scope:** one trusted local cognitive domain, one active case; shared swappable LLM, role LoRA, own RAG and opt-out authorized Cross-RAG, three L1/L2/L3 levels, evidence-preserving latent-first communication; future integration conditioned on experiments. Multiuser/multiserver explicitly deferred.",""]
 else:
  out+=["**\u0648\u0627\u0642\u0639\u06cc\u062a E0:** \u067e\u0631\u0648\u0646\u062f\u0647 \u067e\u0698\u0648\u0647\u0634\u06cc \u0639\u0645\u0648\u0645\u06cc \u0648\u062c\u0648\u062f \u062f\u0627\u0631\u062f \u0648 \u06f3\u06f9 \u0627\u0642\u062f\u0627\u0645 \u0642\u0628\u0644\u06cc \u0628\u0647 \u06f3\u06f5 \u0628\u0633\u062a\u0647 \u06a9\u0627\u0631\u06cc \u0646\u06af\u0627\u0634\u062a \u0634\u062f\u0647\u200c\u0627\u0646\u062f\u061b \u0647\u0646\u0648\u0632 \u0628\u0646\u0686\u0645\u0627\u0631\u06a9 \u0627\u062c\u0631\u0627\u06cc\u06cc DEC \u0646\u062f\u0627\u0631\u06cc\u0645.","",
        "**\u062f\u0627\u0645\u0646\u0647:** \u06cc\u06a9 \u062d\u0648\u0632\u0647 \u0634\u0646\u0627\u062e\u062a\u06cc \u0645\u062d\u0644\u06cc \u0645\u0648\u0631\u062f \u0627\u0639\u062a\u0645\u0627\u062f\u060c \u06cc\u06a9 \u067e\u0631\u0648\u0646\u062f\u0647 \u0641\u0639\u0627\u0644\u060c LLM \u06a9\u0648\u0686\u06a9 \u0642\u0627\u0628\u0644 \u062a\u0639\u0648\u06cc\u0636\u060c LoRA\u060c RAG \u0627\u062e\u062a\u0635\u0627\u0635\u06cc \u0648 Cross-RAG \u0645\u062c\u0627\u0632 \u0648 \u0642\u0627\u0628\u0644 \u062e\u0627\u0645\u0648\u0634\u06cc\u060c \u0633\u0647 \u0633\u0637\u062d L1/L2/L3 \u0648 \u0627\u0631\u062a\u0628\u0627\u0637 \u0646\u0647\u0641\u062a\u0647 \u0647\u0645\u0631\u0627\u0647 \u0634\u0648\u0627\u0647\u062f. \u0627\u062f\u063a\u0627\u0645 \u0622\u062a\u06cc \u0645\u0634\u0631\u0648\u0637 \u0627\u0633\u062a\u061b \u0686\u0646\u062f\u06a9\u0627\u0631\u0628\u0631\u0647 \u0648 \u0686\u0646\u062f\u0633\u0631\u0648\u0631\u06cc \u0645\u0639\u0648\u0642\u200c\u0627\u0646\u062f.",""]
 out+=["## 2. "+s["phases"],"",
       "| "+s["phase"]+" | "+s["duration"]+" | "+s["gate"]+" | "+s["state"]+" | "+("Outcome" if lang=="en" else "\u0646\u062a\u06cc\u062c\u0647") +" |",
       "|---|---:|---|---|---|"]
 for p in data["phases"]:
  d=p["duration_weeks"]
  duration=(f"{d[0]}-{d[1]} "+s["time_unit"]) if d else (s["continuous"] if p["id"]=="CONT" else s["not_scheduled"])
  out.append(f"| {p['id']} | {duration} | {p['gate']} | {p['state']} | {PHASE_OUTCOME[lang][p['id']]} |")
 out+=["","## 3. "+s["flow"],"",
 "```mermaid",
 "flowchart LR",
 ' A["P0: foundation"] --> B["P1A: core"]',
 ' B --> C["P1B: LoRA/RAG"]',
 ' C --> D["P1C: L1/L2/L3"]',
 ' D --> G1{"G1 acceptance?"}',
 ' G1 -->|yes| E["P2: latent optimization"]',
 ' G1 -->|no| X["Keep simpler baseline"]',
 ' E --> G2{"G2 measured benefit?"}',
 ' G2 -->|yes| F["P3: integrated model"]',
 ' G2 -->|no| X',
 ' F --> G3{"G3 native value?"}',
 ' G3 -->|no| X',
 ' G3 -->|yes| IP["IP/partner review"]',
 "```","",s["crit"],"",
 "## 4. "+s["work"],""
 ]
 for p in data["phases"]:
  out+=["### "+p["id"]+" \u2014 "+p["name"][lang],""]
  for w in [w for w in data["work_packages"] if w["phase"]==p["id"]]:
   out+=["#### "+w["id"]+" \u2014 "+w["title"][lang],""]
   if w.get("github_issue"):
    out+=["**"+s["issue"]+":** ["+w["id"]+"]("+w["github_issue"]+")",""]
   out+=["**"+s["scope"]+":** "+w["scope"][lang],"",
         "**"+s["deliver"]+":** "+w["deliverable"][lang],"",
         "**"+s["accept"]+":** "+w["acceptance"][lang],"",
         "**"+s["deps"]+":** "+(", ".join(w["dependencies"]) or s["none"]),"",
         "**"+s["legacy"]+":** "+(", ".join(w["legacy_backlog_ids"]) or s["none"]),"",
         "**"+s["role"]+":** "+w["owner_role"]+" | **"+s["effort"]+":** "+str(w["estimated_person_days"])+" "+s["days"]+" | **"+s["state"]+":** "+w["status"]+" (E0)",""]
 out+=["## 5. "+s["resources"],"",s["estimate"],""]
 for v in data["assumptions"]:out+=["- "+v[lang]]
 subtotal=sum(w["estimated_person_days"] for w in data["work_packages"] if w["phase"] not in ("CONT","FUTURE"))
 p1=sum(w["estimated_person_days"] for w in data["work_packages"] if w["phase"] in ("P0","P1A","P1B","P1C"))
 out+=["",("**Planning envelope:** " if lang=="en" else "**\u0628\u0631\u0622\u0648\u0631\u062f \u0627\u0648\u0644\u06cc\u0647:** ")+str(subtotal)+" "+s["days"]+" (P0-P3 if all gates pass); P0-P1C: "+str(p1)+" "+s["days"]+". No funded commitment.","",
       "## 6. "+s["metrics"],"",s["metrics_text"],"",
       "## 7. "+s["gates"],""]
 for g in data["gates"]:
  out+=["### "+g["id"]+" / "+g["phase"],"",
        "**"+s["accept"]+":** "+g["criterion"][lang],"",
        "**"+s["role"]+":** "+g["approval"],"",
        ("**Fallback:** " if lang=="en" else "**\u0628\u0627\u0632\u06af\u0634\u062a \u06cc\u0627 \u062a\u0648\u0642\u0641:** ")+g["fallback"],""]
 out+=["## 8. "+s["risks"],"",
       "| ID | "+("Risk" if lang=="en" else "\u0631\u06cc\u0633\u06a9")+" | "+("Severity" if lang=="en" else "\u0634\u062f\u062a")+" | "+("Response" if lang=="en" else "\u06a9\u0646\u062a\u0631\u0644")+" |",
       "|---|---|---|---|"]
 for r in data["risks"]:
  out += ["| "+r["id"]+" | "+r["threat"][lang]+" | "+r["severity"]+" | "+r["treatment"][lang]+" |"]
 out+=["","## 9. "+s["governance"],"",s["publication"],"",s["cadence"],"",
       "## 10. "+s["next"],"",s["first_intro"],""]
 for w in data["work_packages"][:6]:
  out+=["- **"+w["id"]+"** \u2014 "+w["title"][lang]+": "+w["deliverable"][lang]]
 out+=["","## 11. "+s["refs"],"",
  "- [ISO/IEC/IEEE 29119-1:2022 \u2014 Software testing](https://www.iso.org/standard/81291.html)",
  "- [NIST AI RMF Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)",
  "- [GitHub Milestones](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones)",
  "- [MLflow evaluation datasets](https://mlflow.org/docs/latest/genai/datasets)","",
  "- [Research catalogue / \u06a9\u0627\u062a\u0627\u0644\u0648\u06af](../../research/catalogue.json)",
  "- [Experiments / \u0622\u0632\u0645\u0627\u06cc\u0634\u200c\u0647\u0627](../../research/experiment-register.json)",
  "- [Machine-readable roadmap / \u0631\u0648\u062f\u0645\u067e \u0645\u0627\u0634\u06cc\u0646\u200c\u062e\u0648\u0627\u0646](../../research/roadmap.json)","",s["footer"],""]
 return "\n".join(out)

for lang in ("en","fa"):
 path=ROOT/"docs"/lang/"roadmap.md"
 content=render(lang)
 path.write_text(content,encoding="utf-8",newline="\n")
 assert chr(0xfffd) not in content
 if lang=="fa":assert sum(0x600<=ord(c)<=0x6ff for c in content)>1000
 print(lang,"utf8_ok, packages",len(data["work_packages"]),"chars",len(content))
