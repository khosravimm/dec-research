---
doc_id: DEC-DOC-010
language: en
title: "Reproducibility and evaluation contracts"
version: 0.1.0
date: 2026-11-12
evidence_level: E0
publication_status: public-research-draft
---

# Reproducibility contract

## Intended artifacts

An accepted experiment should publish (where permitted): dataset/fixture ID and SHA256, trained model + LoRA revision **identifier** and primary source (not redistributed unlicensed weights), runtime/container versions, CPU/GPU information at safe non-identifying granularity, command configuration, random seeds, test inputs and reference adjudication policy, raw numeric results, calculation scripts, known failures, and a declared evidence level.

## Required schemas

The [experiment register](../../research/experiment-register.json) is machine-readable and contains a **bilingual** task label, status, linked paper references and evaluation metrics. The source [catalogue](../../research/catalogue.json) is a bilingual pointer index and does not contain downloaded copyrighted documents or third-party code.

For future run `RUN-ID`, minimum fields are `experiment_id`, `run_id`, `dataset_sha256`, `runtime_revision`, `model_revision`, `adapter_revision`, `config_sha256`, `task_count`, `correct_count`, `error_count`, `latency_ms_p50`, `latency_ms_p95`, `ttft_ms`, `peak_rss_bytes`, `peak_vram_bytes`, `token_prefill`, `token_generated`, `tensor_transfer_bytes`, `evaluator`, `limitations` and `evidence_grade`.

No numeric metric may be filled with guessed or synthetic values without an explicit *simulated* label. Use null/unknown instead of zero when absent. Repeat tests across planned settings and show variance. A failure to reproduce is publishable information.

## Integrity and timing

Use Git commits for public trace, plus dated file manifests with SHA256. Git revision hashes and commit timestamps help trace versions but are not independent certified proof of invention ownership or earliest priority. Preserve raw traces privately where publishing them would reveal secrets, personal data, unpublished methods or copyrighted corpora.

## Scientific robustness

Treat authors' paper scores as external reported findings; only data produced by the DEC harness may be marked E1/E2/E3. Quality comparisons must control for total compute, retrieval corpus, input length, prompt template and specialist adapter state. Summarize negative cases, strong baselines and potential confounders.
