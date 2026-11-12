---
doc_id: DEC-DOC-007
language: en
title: "Research roadmap"
version: 0.1.0
date: 2026-11-12
evidence_level: E0
publication_status: public-research-draft
---

# Research roadmap — staged and evidence-gated

## P0 — Audit and study preregistration

Verify original internal candidate LDI/retrieval APIs without exporting its private corpus; inventory the experimental host/resources and existing model artifacts; curate licensable bilingual network/security/software/management questions; freeze datasets, metrics, hypotheses and acceptance rules. Status: **planned**.

## P1 — Reproducible modular prototype

Compare Qwen3.5 0.8B, MiniCPM5-1B, Granite H-1B, LFM3-1.7B and historical controls where hardware permits; test tool templates, role prompt versus trained LoRA and RAG, council controller and the L1/L2/L3 routing baseline. Capture real memory and latency. Status: **not yet implemented**.

## P2 — Local neural-state optimization

Only after P1 results: profile hidden-state transfer, adapter-specific cache correctness, LatentMAS-SLoRA, Agent Primitives, LatCom and learned projection/compression. Compare against **short typed-event** handoff and simple local memory. Do not assume latent is faster. Status: **conditional / not started**.

## P3 — Integrated architecture hypothesis

Only after sufficient P1/P2 evidence: test learned sparse expert routing, state-space alternatives, teacher/student distillation and compact cognitive workspace. Keep frozen modular baseline and ablation. Check prior art and publication rights before posting novel implementation details. Status: **future conditional**.

## Explicitly deferred

Concurrent independent user sessions, tenant isolation, multiserver Cache-to-Cache and production rollout require separate architecture and safety assessment after real lab success. They are **not** scheduled P1 deliverables.

## Publication maturity

v0.1.0 is a **research dossier**, not a software release. Milestones upgrade only on links to reproducible evidence. Reject weak paths and publish their failures where rights permit.
