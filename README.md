# DEC Research — Deliberative Expert Council

**Public bilingual research programme / برنامه پژوهشی عمومی دوزبانه**

[فارسی](README.fa.md) · [English](README.md)

> **Status (12 Nov 2026):** Research architecture and literature review, **E0**. No implemented or benchmark-validated DEC, production service, trained specialist LoRA or demonstrably novel neural model is claimed. DEC is a working name, not a claim of registered invention.

## Purpose

We are investigating whether a **small, swappable language model** can solve difficult interdisciplinary tasks by combining specialized LoRA adapters, expert-owned retrieval, adaptive reasoning, a shared bounded *latent* working memory and evidence-grounded collaboration. The long-term hypothesis is that **measured, successful mechanisms** could be integrated into a genuinely new model/runtime architecture, not merely packaged as independent agents.

### Three adaptive reasoning levels

| Level | Mechanism | Intended benefit |
|---|---|---|
| L1 | One specialist, direct answer | Avoid unnecessary compute |
| L2 | One specialist with iterative thinking, tools and retrieval | Improve complex single-domain solutions |
| L3 | Dynamic council of specialists with evidence, challenge and revision | Improve cross-domain correctness, not forced consensus |

**Latent-first, not latent-only:** avoid needless hidden-state → text → token roundtrips where measured to be effective; maintain an auditable structured evidence lane. Retrieval embeddings, hidden states and KV cache are **not interchangeable**.

## Full scientific and delivery roadmap

[Detailed roadmap (English)](docs/en/roadmap.md) and [Persian roadmap](docs/fa/roadmap.md) track **35 packages linked to 39 earlier research tasks**, eight decision gates, twelve risks, reproducible acceptance criteria, and provisional effort. The shared [machine-readable plan](research/roadmap.json) generates both versions. This is E0 planning, not implementation.

## Operational status / P0

[First controlled P0 integration check](docs/en/progress.md): read-only LDI API smoke passed; real DEC model experiments are not yet performed. Two P0 work packages are in progress; G0 is still open.

## Model core execution / exploratory E1 preflight

[CPU-only model preflight](docs/en/model-preflight.md): Qwen2.5:3B, MiniCPM5-1B, Qwen3.5-0.8B and LFM3-1.7B-Base were probed locally with pinned weights. No model selected, Persian technical performance remained problematic in the tiny sample, and DEC architecture remains E0.

## Repeatable general-language model benchmark

[20-question warm-loaded bilingual evaluation](docs/en/model-warmloaded-general20.md) replaces the rejected two-question decision basis: 10 Persian and 10 English **general** tasks per instruction model, with a separate load, verified warm-up, 60 saved answers, reference judgments, and post-load latencies. Results are E1 and **do not select a DEC core**.

## MiniCPM5 repetition diagnosis

[Controlled 60-request sampler ablation](docs/en/minicpm5-sampler-ablation.md) compares min_p-only greedy, manufacturer-recommended No-think, and No-think with repetition_penalty=1.05 on the same frozen general bilingual questions. Literal Persian loops declined, but correctness remained inadequate. This E1 observation does **not** approve or reject MiniCPM5 as DEC backbone.

## Liquid AI candidate models — load and thinking-budget diagnostics

[Full-load general bilingual screening of LFM3-1.7B and LFM2.5-1.2B-Thinking](docs/en/liquid-warmloaded-general20.md) records 40 requests after warm-up with model-specific settings. Many LFM2 Thinking requests exhausted the 512-token budget before a final answer; no fair final-answer accuracy ranking or DEC core selection follows.

## English-only instruction following and real tool-call testing

[English-only 24-case tool and instruction evaluation](docs/en/model-english-instruction-tools.md) supersedes Persian-language criteria for this research track. The suite includes 12 exact English instructions and 12 structured function-calling/no-tool cases per model, with 120 saved results across five pinned models, loaded and warmed before all questions. Scores are E1 and include both the original rule and a transparent posthoc fixture-aligned correction; no DEC core accepted.

## Research stages

**P1: modular laboratory proof** → **P2: measured runtime/latent integration** → **P3: conditional investigation of a native learned integrated architecture**. No multi-tenant/multi-user/multi-server implementation is in current scope. Evidence gates and negative results are mandatory.

## Read the bilingual research documentation

| Topic | English | فارسی |
|---|---|---|
| Vision and scope | [Vision](docs/en/vision.md) | [چشم‌انداز](docs/fa/vision.md) |
| Problem and research questions | [Problem](docs/en/problem.md) | [صورت مسئله](docs/fa/problem.md) |
| Conceptual architecture | [Architecture](docs/en/architecture.md) | [معماری](docs/fa/architecture.md) |
| Prior art and alternatives | [Research landscape](docs/en/research-landscape.md) | [مرور پژوهش‌ها](docs/fa/research-landscape.md) |
| Study methodology and evidence | [Methods](docs/en/methods.md) | [روش‌شناسی](docs/fa/methods.md) |
| Experimental protocol | [Experiments](docs/en/experiments.md) | [آزمایش‌ها](docs/fa/experiments.md) |
| Roadmap | [Roadmap](docs/en/roadmap.md) | [نقشه راه](docs/fa/roadmap.md) |
| Decisions and changes | [Decisions](docs/en/decisions.md) | [تصمیم‌ها](docs/fa/decisions.md) |
| Results and limitations | [Results](docs/en/results.md) | [نتایج](docs/fa/results.md) |
| Reproducibility and benchmarking | [Reproducibility](docs/en/reproducibility.md) | [بازتولیدپذیری](docs/fa/reproducibility.md) |
| Publication, IP and licensing | [Publication & IP](docs/en/publication-ip.md) | [انتشار و مالکیت فکری](docs/fa/publication-ip.md) |
| Collaboration | [Contributing](docs/en/contributing.md) | [مشارکت](docs/fa/contributing.md) |
| Privacy and trust boundary | [Security](docs/en/security.md) | [امنیت](docs/fa/security.md) |
| Terms | [Glossary](docs/en/glossary.md) | [واژه‌نامه](docs/fa/glossary.md) |

Machine-readable bilingual records: [research catalogue](research/catalogue.json) · [experiment register](research/experiment-register.json).

## Participation

Academic collaborators, independent researchers, engineers and potential industrial partners are welcome to open a **GitHub Issue** proposing a replicable study, paper, experiment, artifact or collaboration. Prefer specific evidence, baselines, measurements and links. This repository **does not currently accept external code/data contributions under an open-source license** until rights and license conditions are determined. See [contributing](docs/en/contributing.md) and [publication/IP](docs/en/publication-ip.md). No commercial return or institutional sponsorship is implied.

## Disclosure and rights

Public does not automatically mean open source. **No repository-wide reuse/redistribution license has been granted at this stage**; third-party papers/code retain their original licenses. Only sanitized research material is published. Unreleased inventions, credentials, internal infrastructure and raw third-party documents are not published. See [publication policy](docs/en/publication-ip.md) and [security policy](docs/en/security.md).

## Provenance

Public research documents were prepared from a larger, separately governed AI-LAB conceptual research workspace. They are **curated public summaries**, not exports of lab state, private code or unreleased original methods. Machine-readable experiment status starts as `planned`, and results remain `not_run` until an actual logged reproduction exists.

**Maintainer account:** [@khosravimm](https://github.com/khosravimm). For questions and collaboration use repository Issues; please do not send confidential material in public posts.
