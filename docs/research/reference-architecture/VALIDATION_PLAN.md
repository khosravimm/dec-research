# DEC-CRA v1 — Validation Plan and Architecture Decision Gates
**Status:** Proposed protocol E0; no measured integration success.
**Baseline:** GitHub roadmap 2026-11-12 (35 work packages), project charter 2026-11-16.
**Primary rule:** Same data, constraints and task-success definition for Unified (A), Ecosystem (B) and Hybrid (C). No default winner.

## 1. Two distinct validation levels
### Contract validation (can run before any LLM)
- Schema validation: every envelope has schema_version, kind and matching payload type.
- Reject invalid action/unknown enum, out-of-range confidence, negative budgets, arbitrary fields, malformed revision handles.
- Referential integrity: every source/decision/action/ref in a trace must point to an artifact of permitted class.
- Case lifecycle: legal transitions only, monotonically increasing sequence, no success without verified receipt for effectful tool action.
- Memory compatibility: no KV/latent handle reuse across mismatched model/tokenizer/adapter/runtime fingerprint; expired leases invalid.
- Resource control: consumed budget cannot exceed allocated hard ceilings; stop/timeout is explicit outcome.
- Audit integrity: event hashes reproducible; trace interruption and tampering detected.
Passing these proves only contracts and harness correctness, **not** model reasoning or architecture efficacy.

### Cognitive/system evaluation (must be executed on real workloads)
- A0: best single model + fixed budget; A1: same model with extra thinking under equal total CPU budget.
- B0: deterministic task router + specialized tools/models (ecosystem), event-based working memory.
- B1: calibrated small decider/router + model selection and abstain.
- B2: multi-expert L1/L2/L3 council with independent reviews on trigger.
- C0: shared base + per-request LoRA + external knowledge and tools.
- C1: shared backbone with trained token/layer adapter or expert gating, after viable common base and kernel are available.
- A2: custom unified learned decision/compute/memory blocks; research spike, not required to label P1 achieved.
All options must be compared to cost/quality baselines appropriate to their actual capacities, avoiding artificial symmetric architecture constraints that render one option infeasible.

## 2. Measurable evaluation design
Pre-register before runs: held-out case IDs, label policy, model/checkpoint/tokenizer/adapter hashes, test sequence, cold/warm conditions, n samples, real CPU/RAM budget, permitted external tools, and evaluation algorithm.
**Dataset strata**: Persian technical networking/security, English programming/API, mixed Persian-English logs/JSON, source-based QA, tabular documents, contradictory evidence, confidence/OOD, tool failure and adversarial prompt injection.
**Prevent leakage**: split by source document/time and near-duplicate groups; do not tune on held-out final set.
**Judging**: reference computations, tool receipts and domain adjudication; blind manual judge for nuanced content. Report uncertainty intervals and conflicts, not a single weighted grade absent agreed criteria.

| Hypothesis | Experimental contrast | Primary metrics | Fail / rollback criteria |
|---|---|---|---|
| H-DECISION | rules vs decider vs LLM-router | task-conditioned route accuracy, Brier/ECE, abstention and incremental latency | worse end-to-end success or unbounded routing cost |
| H-COMPUTE | fixed budget vs model adaptive/depth/early stop | completed-task quality per CPU-sec, p95 latency, token efficiency | same quality lower reliability, final answer truncation |
| H-EXPERT | base+prompt/RAG vs LoRA selection/merge/learned routing | independent held-out success, negative transfer, RSS, update cost | regression on code/English or higher cost without benefit |
| H-MEMORY | structured events vs RAG vs bounded latent memory | long-horizon precision/recall, forgetting, poisoning resilience, cache validity | incorrect attribution or cross-revision state reuse |
| H-COLLAB | single extra reasoning vs independent specialists | fully verified result / total cost, disagreement handling | no incremental gain at matched budget |
| H-ARCH | A vs B vs C on comparable workflows | quality/cost Pareto, audit completion, maintenance complexity | fails objective acceptance gates; preserve alternate |

## 3. Minimal falsifiable vertical slice
Example case: "Given network change ticket and vendor document excerpt, determine impact of a subnet/routing change, request evidence if needed, produce a reversible change plan with citations."
- Step 1 Accept CaseRequest and create trace and budget snapshot.
- Step 2 Decision chooses L1 answer, L2 retrieval/tool or L3 second expert.
- Step 3 Allocator sets time/token/RSS/step ceilings and halting criteria.
- Step 4 Knowledge interface retrieves cited vendor standards/source IDs from LDI.
- Step 5 Expert invocation returns candidate plan with explicit uncertainty.
- Step 6 Verifier checks subnet arithmetic, configuration consistency, evidence references and tool-result receipts.
- Step 7 Report answer/deferral and trace with cost, divergences, dissent and source revisions.
This is a **proposed example**; no real change to network equipment or evidence of execution is implied.

## 4. Acceptance gates (thresholds set before experiment)
**G-CRA-SCHEMA:** 12 typed payloads and realistic positive/negative contract fixtures pass validation. Every payload type represented.
**G-CRA-TRACE:** deterministic replay of state machine; all expected transitions logged; invalid transition and missing tool receipt fail.
**G-CRA-BUDGET:** over-budget actions are denied with reason; bounded iteration.
**G-CRA-EVIDENCE:** no successful claim without backing source or validated deterministic check; disagreements visible.
**G-CRA-A/B/C:** each feasible candidate has reproducible build, task-suite, raw traces and comparable budget accounting.
**G-CRA-DECISION:** architecture choice cites pre-registered criteria and leaves rejected options, costs, uncertainty and rollback path.

Note G-CRA-SCHEMA is possible with synthetic fixtures. G-CRA-A/B/C cannot be claimed passed until actual model/ecosystem experiments occur.

## 5. Research sequencing without premature lock-in
1. Freeze reference contracts and starter dataset, validate schemas and a synthetic trace.
2. Build explicit event-based ecosystem as an **experimental harness**, not selected winner.
3. Train a small typed decision model vs deterministic baseline and investigate budget routing.
4. Verify LoRA/data/KB and memory operations independently, preserving real source provenance.
5. Prototype bounded latent state and internal learned experts/compute if implementation availability allows.
6. Compare completed task success per resource, then select or combine architecture with an ADR.

## 6. ADR and roadmap risks
- Charter 2026-11-16 leaves A/B/C open; official P3 label "Integrated Model Research" still implies A only. Update roadmap JSON plus derived English/Farsi docs as a dedicated tracked change, not a silent rename.
- Public DEC GitHub E0 plans and private sal-ai E2 model benchmarks are **distinct** repositories of evidence; do not inflate the public system status.
- Tool calls require separate execution policy; model decisions are proposals, not receipt of completed effects.
- Switching tokenizer/LoRA/revision invalidates unspecified memory compatibility; universal latent interoperability is not assumed.
- Deployment of learned memory and routing remains research, so memory persistence and calibration are unproven.

## 7. Traceability
| Contract/capability | Main work packages | Existing research question |
|---|---|---|
| DecisionProposal & Compute Allocation | WP-008,009,016,023,025 | RQ-03,04 |
| ExpertInvocation/Result | WP-007,011,014,017 | RQ-01,02,07 |
| MemoryHandle, state and compatibility | WP-013,020,021,022 | RQ-05,06 |
| KnowledgeRequest/Result | WP-002,010,012 | RQ-02,05 |
| ToolAction/Receipt | WP-008,012,016 | RQ-04 |
| EvidenceEvent/CaseResult | WP-005,012,018,019,027 | RQ-07,08 |
| Architecture alternatives and learning | WP-027,028,029,031 | RQ-08 and mission amendment |

## 8. Deliverable state
Reference architecture, contracts, experiment design and decision record are **design outputs**. Any implementation, model training, runtime benchmark, or architecture selection must be stated separately with evidence and reproducible raw artifacts.
