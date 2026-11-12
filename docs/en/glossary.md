---
doc_id: DEC-DOC-014
language: en
title: "Glossary and definitions"
version: 0.1.0
date: 2026-11-12
evidence_level: E0
publication_status: public-research-draft
---

# Glossary

| Term | DEC usage and boundary |
|---|---|
| DEC | Working title: Deliberative Expert Council; *not* a new model architecture or registered mark |
| Small backbone | Shared and swappable generative base neural model |
| Expert package | Logical role LoRA + controller + dedicated RAG + retrieval policy + version metadata |
| LoRA / QLoRA | Parameter-efficient weight adaptation / low-bit training method; not guaranteed memory sharing |
| RAG | External retrieval for factual grounding; a vector embedding is not a neural continuation state |
| Hidden state | Model intermediate activation from a particular layer and version |
| KV cache | Layer-/position-specific attention keys and values; requires exact compatibility to reuse |
| Latent workspace | Proposed bounded internal state buffer/handles; not yet DEC implemented |
| Latent-first | Prefer to avoid unnecessary decoding/re-tokenization **when verified** beneficial |
| Expert council | Dynamically activated roles that may challenge or revise with evidence; not forced consensus |
| Evidence ledger | Structured IDs, claims, source references, model versions, tests and uncertainties |
| Think / No Think | Template/model-dependent reasoning mode, not proof of direct control of private model internals |
| P1/P2/P3 | Modular experimental PoC; measured runtime fusion; conditional native model research |
| E0/E1/E2/E3 | Theoretical, synthetic prototype, limited real operation, repeated predefined evidence in-scope |
| IP / chain of title | Legally supported rights and provenance, distinct from a GitHub username or repository |
