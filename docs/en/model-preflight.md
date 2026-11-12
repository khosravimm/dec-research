---
doc_id: DEC-DOC-016
language: en
title: "Model core preflight evidence"
version: 0.1.0
date: 2026-11-12
evidence_level: E0
publication_status: public-research-draft
---

# DEC model-only preflight — first executable core screening

**Date:** 2026-11-12. **Status:** E1 preliminary feasibility **for local model inference only**; **DEC cognitive architecture remains E0 and no backbone is selected**. No RAG, adapters, expert council, latent state, training or multitenancy were evaluated.

## Purpose and method

Validate that different candidate small model architectures can load on the available CPU-only inference environment before proposing any integrated DEC experiment or LoRA training. These are **synthetic smoke prompts, not a pre-registered or held-out benchmark**. We compared two straightforward questions: Persian network fundamentals ("In two short Persian sentences, distinguish a layer-2 switch from a router") and English cryptography ("In one short sentence, distinguish hashing and encryption"). Results were read for obvious conceptual adequacy but were **not independently adjudicated**.

Environment: 4 CPU inference threads, context 1024 tokens, seed 42, quantized GGUF models, llama.cpp `0.9.0-dev aa75ff3` for matched screening; process RSS sampled via procfs, wall time **including cold model initialization**. The MiniCPM5 and Qwen3.5 native No-think runs used their relevant chat-template settings and cannot be treated as parameter-identical latency comparisons with the earlier greedy paired run.

| Candidate | Weight size | Observed approximate process RSS | Example cold wall times (FA / EN) | Limited answer observation |
|---|---:|---:|---:|---|
| Qwen2.5:3B Q4 | 1.93 GB | 3.38 GB | 20.93 / 9.79 s | EN hashing answer adequate for prompt; FA network explanation inaccurate |
| MiniCPM5-1B Q4 | 0.688 GB | 1.11 GB | 7.13 / 6.93 s (No-think) | FA response incoherent; EN response contains a false claim about hashing |
| Qwen3.5-0.8B Q4 | 0.533 GB | 0.89 GB | 8.93 / 3.11 s (No-think) | Both short technical responses contain conceptual errors |
| LFM3-1.7B-Base Q4 | 1.10 GB | 1.91 GB | 5.22 s (one completion only) | Model produced raw next-token continuation; **not instruction-quality evaluated** |

**Important diagnostic:** LFM3-Base failed loading with older llama.cpp `0.7.0-dev`, then passed an isolated completion probe with `0.9.0-dev`. Official Liquid AI guidance requires llama.cpp v0.8.0 or later for this architecture. A runtime incompatibility is **not** evidence that a model itself is defective.

**MiniCPM5 detail:** the default thinking path consumed the short output budget before a final answer. We therefore separately tested the model's No-think path using `enable_thinking=false` and native sampling guidance; the observed Persian and English faults persisted in those two examples. The model remains an interesting **architecture/LoRA integration** candidate due to Llama-compatible dense design, not an accepted Persian specialist. <https://github.com/OpenBMB/MiniCPM>

## Weight provenance and rights

| Weight | Source and revision | Verified SHA-256 |
|---|---|---|
| Qwen2.5:3B GGUF | Existing local Ollama content-addressed model | `5ee4f07cdb9beadbbb293e85803c569b01bd37ed059d2715faa7bb405f31caa6` |
| MiniCPM5-1B GGUF Q4 | [OpenBMB official GGUF](https://huggingface.co/openbmb/MiniCPM5-1B-GGUF), commit `5385560dd3e232bcc3577fd9442c332cad2facbd` | `81b64d05a23b17b34c475f42b3e72fbde62d4b92cc34541f7a8031d0752deafa` |
| Qwen3.5-0.8B GGUF Q4 | [Unsloth conversion](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF), commit `6ab461498e2023f6e3c1baea90a8f0fe38ab64d0` | `bd258782e35f7f458f8aced1adc053e6e92e89bc735ba3be89d38a06121dc517` |
| LFM3-1.7B-Base Q4 | [Liquid AI base model](https://huggingface.co/LiquidAI/LFM3-1.7B-Base), local quantized checkpoint | `516b249424778cf3ab61dca89fd12a8da7cea6ba5fa863c6b07a7be68a2d6884` |

OpenBMB MiniCPM5 and original Qwen3.5 model cards state Apache-2.0; LFM3 uses **LFM Open License v1.0**, requiring license-specific review before a commercial derivative. **No third-party weights are redistributed in this repository.**

## Evidence limits and next decisions

Only **two illustrative subject prompts** per instruction model; not a statistical multilingual evaluation or evidence of suitability for deployment. File-level hashes and raw outputs were saved privately in a dated JSON evidence manifest, with no secrets or document corpus captured. **No E2/E3 claim for DEC.**

Next model-only gate: construct a rights-cleared bilingual *technical* gold set with adjudicated oracles and negative/abstention cases; include stronger compact instruction checkpoints such as Qwen3.5-4B and MiniCPM5-2B plus an LFM3 post-trained variant if suitable; then measure matched-budget quality, CPU/RAM, tool compliance and LoRA suitability. The eventual adapter/latent experiment must maintain strict backbone and KV/state compatibility; a successful output from a Base model alone is not a LoRA or cognitive council demonstration.

[Research roadmap](roadmap.md) · [Evaluation method](methods.md) · [Research issue](https://github.com/khosravimm/dec-research/issues/1)
