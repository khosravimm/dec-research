---
doc_id: DEC-DOC-002
language: en
title: "Research problem and questions"
version: 0.1.0
date: 2026-11-12
evidence_level: E0
publication_status: public-research-draft
---

# Problem statement and falsifiable hypotheses

## Core question

Can a **small, swappable language backbone** augmented with independently trained expert adapters, domain RAG, adaptive reasoning and bounded shared latent state provide more accurate, evidence-grounded interdisciplinary decisions at an acceptable end-to-end compute cost than simpler alternatives?

This is not equivalent to: *Can a small model become as good as a large model in all tasks?* A useful result may be narrower: which task types benefit from which path, under what cost/quality envelope?

## Research questions (RQ)

| ID | Testable question |
|---|---|
| RQ-01 | Which small base offers reliable Persian/English technical understanding and controllable inference on target hardware? |
| RQ-02 | Does a domain LoRA improve quality beyond role prompting + the same retrieved documents? |
| RQ-03 | Can an adaptive route choose L1/L2/L3 better than fixed compute allocation? |
| RQ-04 | How can the model pause at *valid action boundaries* to request and use new external evidence? |
| RQ-05 | Can a bounded latent workspace improve cooperation relative to concise typed event transfer? |
| RQ-06 | Which hidden-state, retrieval-embedding or KV interfaces are compatible across role adapters and model versions? |
| RQ-07 | Does a council outperform longer single-agent thinking when total compute and evidence are equal? |
| RQ-08 | Can any validated council behavior be distilled into a unified learned architecture without losing rare-case criticism or abstention? |

## Hypotheses / alternatives

**H1:** LoRA adds measurable domain capability beyond prompt-only and RAG-only controls. **Null:** No improvement outside noise or equivalent-quality cost.

**H2:** Adaptive L1/L2/L3 routing improves quality per unit cost. **Null:** A single model with a fixed deeper compute budget is as effective.

**H3:** Latent-first bounded communication improves end-to-end metrics. **Null:** A short typed message costs less and performs as well; large tensors can erase token savings.

**H4:** Joint learned memory/expert routing retains council benefits in a smaller integrated model. **Null:** Distillation causes collapse of dissent, overfitting or capability loss.

All statements are **E0 propositions**, not achieved results. Hypotheses must be rejected when tests fail. Results require an immutable data/evidence trail.
