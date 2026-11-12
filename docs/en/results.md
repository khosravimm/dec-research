---
doc_id: DEC-DOC-009
language: en
title: "Results and limitations"
version: 0.1.0
date: 2026-11-12
evidence_level: E0
publication_status: public-research-draft
---

# Results register — no DEC performance results yet

**Status (2026-11-12): E0 only.** This public repository records an architecture hypothesis, external literature and a test plan. **No DEC runtime, fully trained expert adapter, native integrated model, comparative DEC benchmark or independent replication has been delivered.**

| Claim / output | Current evidence | Status | What would change the status |
|---|---|---|---|
| Small base model selected | Comparative candidates from official repos | **Not selected** | Pinned same-hardware FA/EN benchmark with resource and quality scores |
| LoRA expert training improves quality | Other projects show feasibility | **Not tested in DEC** | Controlled A2 versus A3 with held-out tasks |
| Three-level adaptive router saves compute | Architecture/routing prior art | **Not tested in DEC** | Equal-budget A4/A5/A6 comparison |
| Shared bounded latent memory works | Published LatentMAS/LatCom/C2C references | **Not tested in DEC** | Compatible A6/A7 implementation and measured tensors/quality |
| Council is better than one expert | Research hypothesis | **Not established** | Held-out, matched resource and retrieval comparison |
| Native new architecture invented | Owner long-term aspiration | **Not established** | Distinct trained mechanism, ablation, prior-art and IP assessment |
| Multiuser/multiserver readiness | Design seams only | **Deferred** | Separate future scope and tests |

## Reporting template

Every future public result must include `experiment_id`, date, environment, model/adapter hashes, corpus/fixtures, code commit, baseline, null hypothesis, measurements with denominators and intervals, negative cases, reviewer, limitations, reproducibility instructions, evidence artifact hash, disclosure/rights approval, and a decision of adopted/rejected/deferred.

Vendor benchmark scores and prior-paper improvements are **not DEC observations**. They may appear in [research landscape](research-landscape.md) with citations, but not in this table as achievements.
