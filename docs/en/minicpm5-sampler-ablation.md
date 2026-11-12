---
doc_id: DEC-DOC-018
language: en
title: "MiniCPM5-1B: controlled sampling and repetition-loop ablation"
version: 0.1.0
date: 2026-11-12
evidence_level: E1
publication_status: public-research-draft
---

# MiniCPM5-1B: controlled sampling and repetition-loop ablation

**Result:** Sampling parameters materially affected *literal repetition* on the frozen 10-Persian / 10-English general question set. Fixing min_p alone while retaining greedy decoding did not fix the loop. The OpenBMB No-think settings reduced three-word repetition, and adding repetition_penalty=1.05 removed observed three-word repeats in Persian. **None of these settings repaired the observed Persian answer correctness.** This is limited, single-run E1 evidence, not proof of model competence or DEC integration.

## 1. Context and prior experiment correction

The previously published 20-item MiniCPM language run used temperature 0 and did not set min_p or repetition_penalty explicitly. Our installed llama.cpp reports defaults min_p=0.05 and repeat_penalty=1.0. OpenBMB's official llama.cpp cookbook warns min_p=0.05 may cause repetition; it recommends min_p=0.0. For MiniCPM5-1B No-think the vendor recommends temperature=0.7 and top_p=0.95, with optional repetition_penalty=1.05 if repetition occurs. Crucially, temperature=0 means greedy sampling and changing min_p alone may not alter the highest-probability token. Consequently, the cause must be analyzed as a sampler *combination* rather than automatically blaming a single setting.

## 2. Reproducible method

Exactly the same 20 frozen, all-general questions (10 FA, 10 EN; pre-test SHA256 below). Model: official MiniCPM5-1B Q4_K_M, fully SHA256 verified; CPU-only llama.cpp 0.9.0-dev, 4 threads, ctx 2048, Jinja chat-template, No-think/reasoning-off, seed 42, 128-token cap. A single isolated model server was loaded and explicitly warmed before all trials. For each question three profiles were rotated, 60 total requests; server was stopped afterward. No LDI, tool calling or specialist prompt. Directly observed 60/60 successful HTTP requests; timing excludes model load and warmup.

**Model SHA-256:** `81b64d05a23b17b34c475f42b3e72fbde62d4b92cc34541f7a8031d0752deafa`
**Questions SHA-256:** `1fffab3cf5c1fbc7be0eb17406446c52784a0d41c19856c5ed898de8db47bd77`
**Private evidence SHA-256:** `12b141e8893dae3230ab1c09629052af51171409cb63aabf821b1d0f1db56ec0`

## 3. Profile comparison, Persian

| Profile | temperature | top_p | min_p | repeat penalty | Average repeated 3-word fraction | 128-token cap | Median request |
|---|---:|---:|---:|---:|---:|---:|---:|
| S1_minp_zero_only | 0 | 1.0 | 0.0 | 1.0 | 25.85% | 5/10 | 5467.9 ms |
| S2_openbmb_nothink | 0.7 | 0.95 | 0.0 | 1.0 | 3.07% | 7/10 | 5755.6 ms |
| S3_openbmb_nothink_repeat | 0.7 | 0.95 | 0.0 | 1.05 | 0.0% | 7/10 | 5958.0 ms |

### English outcome and length caps

| Profile | English repeated 3-word fraction | English length caps | Median English request |
|---|---:|---:|---:|
| S1_minp_zero_only | 0.34% | 0/10 | 308.6 ms |
| S2_openbmb_nothink | 4.82% | 2/10 | 550.3 ms |
| S3_openbmb_nothink_repeat | 3.06% | 2/10 | 674.5 ms |

The metric is the proportion of three-word sequences already seen earlier in the same generated answer, averaged across ten outputs in each language. It is a diagnostic heuristic; a non-repeating text can still be meaningless. Nearest-rank p95 from ten cases is merely the sample maximum and is not a reliable production latency percentile.

## 4. Selected observed failure cases

For a Persian question about bus arrival time, temperature=0 / min_p=0 still generated a repeated, incoherent phrase until the 128-token cap. The same question with vendor sampling produced a long unrelated explanation; adding a penalty removed repeated three-word patterns but still failed to give 15:25. Thus repetition and correctness are different endpoints.

Several English basic questions remained wrong (e.g., arithmetic answer 12 instead of 17 under both recommended profiles), despite successful HTTP 200 responses. Six or seven Persian cases per profile may reach the length cap, so 'thinking disabled' does not ensure concise instruction following.

## 5. Validity, risks and next gate

The study uses only one seed, one run per profile, one quantized checkpoint and one first-pass reading of correctness; no statistically robust or blinded quality estimate. The vendor-recommended profile changes temperature/top_p/min_p together, so their individual contributions are not isolated. S2 to S3 changes repeat penalty only, but sampling remains stochastic. No formal conclusions on Persian fine-tuning, trainability or tool-use follow. Next gate: test the official FP16/BF16 checkpoint with exact Hugging Face chat template, compare Q4 to reference, repeat with multiple seeds, and evaluate any Persian adaptation against the same held-out cases. Keep MiniCPM5 under investigation rather than prematurely rejecting it.

## 6. Manufacturer and runtime evidence

- [OpenBMB MiniCPM5 llama.cpp deployment — min_p and model-specific sampling](https://github.com/OpenBMB/MiniCPM/blob/main/docs/deployment/llama_cpp.md)
- [OpenBMB MiniCPM5 README — repetition penalty guidance](https://github.com/OpenBMB/MiniCPM/blob/main/README.md)
- [llama.cpp sampling and chat-template options](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)

- [Machine-readable full 60-response artifact](../../research/benchmarks/dec-minicpm5-sampler-ablation-v1.json)
