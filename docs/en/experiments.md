---
doc_id: DEC-DOC-006
language: en
title: "Experimental protocol"
version: 0.1.0
date: 2026-11-12
evidence_level: E0
publication_status: public-research-draft
---

# Pre-registered laboratory study protocol

## Research question and units of comparison

The experimental unit is a **case** (one frozen task with a reference result, evidence corpus and adjudication rubric). Compare identical tasks, evidence access and hardware limits. Each run has immutable IDs, model and adapter revision hashes, quantization, prompts, dataset version and measured conditions. No pilot is deemed successful before the protocol is fixed.

## Arms (planned, E0)

| Arm | Configuration | Controlled variable |
|---|---|---|
| A0 | One small model, direct | Minimum cost |
| A1 | Same model + own RAG | Retrieval effect |
| A2 | Same model + role prompt + same RAG | Prompt specialization |
| A3 | Same model + trained role LoRA + same RAG | LoRA added value |
| A4 | Single expert with deeper structured Thinking/tools | Deliberation versus direct |
| A5 | Fixed panel of 2–3 experts, typed event exchange | Council benefit and baseline overhead |
| A6 | Adaptive L1/L2/L3 council, typed exchange | Routing and stop benefit |
| A7 | Same adaptive council, bounded compatible latent exchange | Latent communication marginal benefit |
| A8 | Larger reference model under declared total resource budget | Scale contrast |
| A9 | Native integrated architecture (future conditional) | New computation versus best modular baseline |

A7/A9 are not runnable until a compatible representation and measurable mechanism exist. **No experiment arm has been executed**.

## Dataset

Stratify held-out bilingual tasks: Persian/English network/security incident analysis, technical troubleshooting, code tasks, management trade-offs, cross-domain disagreements, malicious/untrusted retrieval, evidence insufficiency and abstention. Store task ID, language, difficulty, correct reference, reproducible fixtures, source rights, sensitivity tier, and independent reviewers. No confidential organisational records in the public fixtures.

## Outcomes

Primary: factual correctness and evidence faithfulness (with independent adjudication). Secondary: appropriate abstention, disagreement detection, task-level utility, token in/out, cold/warm TTFT, p50/p95 end-to-end latency, tokens/s, peak RAM/VRAM incl. KV/LoRA, Tensor bytes, cache correctness and energy per accepted answer if measurable.

## Confounders and acceptance

Hold hardware, context length, generation settings, retrieval budget and benchmark fixed; compare quality at matched total inference budget in addition to raw latency; evaluate multiple seeds or controlled repeats and report uncertainty/confidence intervals, failures and tool-call parsing errors. Define numeric success thresholds **before** training or observing held-out results; until then they are open. Incompatibility, missing rights, poor Persian quality, leakage or excessive memory constitute legitimate rejection. See [experiment register](../../research/experiment-register.json).

No E1+ result currently exists in the public research record.
