> **Research note (E0/E2):** Literature and model card claims are differentiated from narrow local benchmarks. No unique DEC architecture has been demonstrated.

# DEC Research — نتایج روش‌های ترکیب چند مدل و چند Adapter (فهرست مستقل)
**نسخه تفکیک‌شده:** 2026-11-16 | **وضعیت:** E0 پژوهشی، بدون اجرای آزمایش ترکیبی جدید
**این سند روش‌ها، معماری اتصال، سیاست Routing، LoRA/QLoRA، ابزارهای ترکیب، ریسک و بنچمارک را پوشش می‌دهد؛ کاتالوگ مدل‌ها جداست:** `MODEL_RESULTS_2026-11-16.md`.

## بررسی فنی تفصیلی
Date: 2026-11-16 UTC. Evidence: E0 (technical source review). No local A/B experiment has run in this study.
Scope: Specialist multi-model selection, sequential agent pipelines, ensemble verification, LoRA switching, weighted composition, trained adapter routing, model-serving backends, CPU constraints, safety, evaluation and ADR. This is a focus area; it does not narrow the larger DEC Research.

## Executive findings
1. A model router (selects between complete models) is distinct from a base-model-shared adapter router (selects a LoRA), from learned per-token expert routing, from adapter merging, and from a multi-stage agent workflow. They are not interchangeable.
2. QLoRA is the training method using a quantized base, not a distinct adapter type. Different base model families or tokenizers cannot normally share the same LoRA safely.
3. CPU-first implementation can start with **llama.cpp server** and a read-only registry of two/three GGUF LoRAs all trained against an EXACT SAME base. Per-request 'lora' weighted scales work but different combinations are not batched in the server.
4. Model-level semantic routing should start with **deterministic signals and cheap classification**; trained cost/quality routing is a separate experimental stage. Avoid spending a 2B inference call to choose another 2B model on every request.
5. Router safety is a new control plane. ACL 2026 Route-to-Rome demonstrates adversarial routing toward high-cost models. Keep allowlisted routes, resource budgets, confidence/OOD abstention, versioned decisions and privilege separation.

## Five distinct architecture patterns and feasibility
|Pattern|Routing granularity|Strength|Risk|CPU deployment maturity|
|---|---|---|---|---|
|Task-to-model|Per request|Distinct architecture, tokenizer, modalities; easy isolation|Memory, model-switch cold start, latency|High with Ollama/llama.cpp gateway, calibrate router|
|Task graph / agent workflow|Per stage/step|Independent specialist OCR→parse→RAG→verify; typed artifacts and audit|Error propagation; total sequential latency|High, but quality must be proved|
|Base + LoRA switching|Per request|One base weights, adapters small, easy isolation|Compatibility & switching; specialist trade-offs|Documented via PEFT and llama.cpp|
|LoRA composition/merging|Weighted per-request or offline merged|Multidomain task, fewer model loads|Interference, numerical/semantic drift|PEFT and llama.cpp, performance dependent|
|Token/layer-level learned adapter routing|Per layer/token|Expert selection without K separate full LMs|Custom kernels, routing training, evaluation complexity|Research-level, no general CPU speed guarantee|

## Evidence and implementation sources — primary
- MoLoRA (ICML 2026): https://proceedings.mlr.press/v306/shah26d.html ; March 2026 first preprint, July conference. Learned per-token routing, Qwen3-1.7B better than 8B on four author-evaluated reasoning tests, not DEC proof. N work vs K*N baseline assumes multiple full replays; does NOT mean zero router overhead.
- LoRA-Mixer (ICLR 2026): https://proceedings.iclr.cc/paper_files/paper/2026/hash/18610cbcd1da57854aa05ebdc5cd3168-Abstract-Conference.html ; attention projection routing, shared reusable LoRA expert units, Routing Specialization Loss, authors report 48% of trainable params of comparator and +3.79/+2.90/+3.95 on selected tasks. Could use already-trained adapters, no guarantee for unrelated LoRA targets.
- MoA heterogeneous mixture of adapters (ACL 2026): https://aclanthology.org/2026.acl-long.965/ ; official code https://github.com/DCDmllm/MoA ; Soft = weighted output of heterogenous adapters; Sparse = selected subset; author's claim negligible degradation, requires independent quality/latency study.
- VIA-SD (ICML 2026): https://proceedings.mlr.press/v306/xian26a.html ; draft model→slim verifier→full verifier tiering, 10–20% over strong speculative decoding baselines in authors' studies; only applies to compatible speculative verification, not generic cross-model debate.
- Model router attack R2A (ACL 2026): https://aclanthology.org/2026.acl-long.2051/ ; adversarial cost escalation, validate router threat model.
- X-LoRA: https://huggingface.co/docs/peft/en/package_reference/xlora ; frozen LoRA experts and trained scalings at token/layer/sequence granularity, requires **two model forwards** at each generation step, often poor for CPU low-latency.
- PEFT multi adapters/activation/hotswap: https://huggingface.co/docs/transformers/peft and https://huggingface.co/docs/peft/package_reference/hotswap ; hotswap targets same/subset layers, LoRA only; mixed adapter types require compatibility https://huggingface.co/docs/peft/developer_guides/mixed_models .
- PEFT add_weighted_adapter SVD/linear/cat/TIES/DARE: https://huggingface.co/docs/peft/en/developer_guides/model_merging and https://huggingface.co/docs/peft/main/package_reference/lora . 'cat' combines rank by SUM, memory may grow; TIES/DARE address merging interference with constraints, no guaranteed improvement.
- llama.cpp server LoRA endpoint and per-request scales: https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md ; GET/POST /lora-adapters, lora [ {id,scale} ], per-request variant disables batching between differing configurations. Check pinned build for exact features.
- vLLM multi-LoRA: https://docs.vllm.ai/en/latest/features/lora/ and https://docs.vllm.ai/en/stable/cli/serve/ ; multi LoRA in batch, dynamic loading docs EXPLICITLY warn against production unless trusted isolated; backend normally GPU, no demonstrated sal-ai CPU suitability.
- SGLang multi-LoRA: https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/lora.mdx ; derived from S-LoRA/Punica (GPU techniques); not CPU fallback assumption.
- S-LoRA (MLSys 2024, older foundational): https://proceedings.mlsys.org/paper_files/paper/2024/hash/906419cd502575b617cc489a1a696a67-Abstract-Conference.html ; thousands of LoRAs, GPU unified paging and batching, not a CPU benchmark.
- RouteLLM older baseline: https://github.com/lm-sys/RouteLLM ; only calibrated on strong/weak pair, sample cost reductions not transferable, and MF router may require external embedding key—verify privacy; supports local integrations with constraints.
- vLLM Semantic Router source: https://vllm-sr.ai/docs/next/overview/semantic-router-overview/ ; separates API gateway, semantic model selection, and inference pool scheduling; policies and multiple model families.
- LiteLLM router: https://docs.litellm.ai/docs/routing ; retry/failover/cooldown and priorities, not by itself a trained domain expert.
- RouterArena evaluation suite: https://github.com/RouteWorks/RouterArena ; benchmark 9 domains, 44 categories, measures cost/latency/robustness/accuracy, not Persian security unless extended.

## Proposed DEC design — research architecture, not implementation claim
```
Client → AuthZ & Data Classification → Structured Input / Capability Detection
       → Policy / Router (cheap rules + calibrated classifier)
              ├─ Translation: Hy-MT2 / PLaMo
              ├─ OCR/Structure: Local Document Intelligence + document parser
              ├─ Retrieval: BGE-M3 + optional Jina Reranker
              ├─ Typed decision: small calibratable task classifier
              ├─ Network/Security: base LLM + security specialist LoRA
              ├─ Persian: SAME base LLM + Persian LoRA (possibly weighted mix if tested)
              └─ Code/Tools: coding model or tool-specialized LoRA
       → Verifier / Evidence Gate → Approved tool actions or user response
       → Trace + Metrics + Source Provenance + Feedback labels
```
The example specialist names are **candidate options**: not assumed downloaded, installed, licensed for deployment, or validated on sal-ai.

**Router actions**: model_id, adapter_ids, adapter_scales, tokenizer/runtime revision, task_type, evidence_refs, hard_cost_budget, privacy class, authorization class, risk/uncertainty. Deny unsafe paths and out-of-scope tool privileges. Rule-based gates operate independently of model's predictions.

## Comparative decision matrix (pre-benchmark qualitative)
|Criterion|Multiple models|One base + switched LoRAs|Learned token-level MoLoRA|
|---|---|---|---|
|Different architectures/modalities|Yes|No, unless base supports them|No, constrained base|
|Resident memory on CPU|Many weights or cold swaps|Single base + small adapters|Single base + adapters, router+kernel overhead|
|Independent update/retrain|Strong|Strong within shared base|Possible, but router transfer must be validated|
|Specialist failure isolation|Strong|Partial shared base|Weak shared representation|
|Tool/data policy separation|Can run separate service identities|Must enforce externally|Must enforce externally|
|Operational maturity|High|Medium/high depending runtime|Research|
|Decision traceability|Per-request, easy|Per-request, easy|Per-token requires heavier traces|
|Best initial research role|Cross-modal & independent experts|Security/Persian adapters|Later research comparator|

## Benchmarks / verification plan
**Baselines**: (A) single best general model; (B) a model selected by deterministic task rule; (C) cheap classifier route with abstention; (D) base+one LoRA; (E) base+2 weighted LoRAs; (F) offline PEFT merge (TIES/DARE/SVD), (G) trained MoLoRA/LoRA-Mixer only after baseline proves potential.
**Same domain corpus**: Persian/English network and security source QA, command reasoning, Python validity, instruction schema, routing ambiguous prompts, document OCR→RAG→answer, mixed code+Persian, malicious prompt injection, route-cost manipulation.
**Metrics**: task completion, false acceptance, source faithfulness, calibrated route accuracy, OOD abstention, token usage, TTFT/p50/p95 latency, throughput, cold/warm swap time, total RSS/adapter bytes/KV, cost per successfully answered task, privacy & access violations, end-to-end trace completeness.
**Testing integrity**: fixed seeds, repeated real workloads, equal answer budgets, exact base/adapter hashes, source splits and unique held-out tasks. Model cold/warm control, no external network calls without consent. No claims of E2/E3 until corresponding experimental evidence exists.

## Recommendations — conditional research decisions
Phase P0: no new architecture code. Inspect existing DEC code/ADRs and current Ollama model inventory. Define task taxonomy, labeled routing dataset, capability matrix and security gate; use rule-based multi-model pipeline as baseline.
Phase P1: isolate a CPU runner (llama.cpp) and select ONE base model demonstrably compatible with LoRA adapters; train 2 specialist adapters (Persian+network-security) with shared provenance and frozen base; compare single vs weighted combinations. Allow rollback to base-only.
Phase P2: assess PEFT merges, cheap learned router and per-request adapter switch.
Phase P3: prototype MoLoRA or LoRA-Mixer only if measured synergy and latency show material benefit; test against simple workflow with two independent models and a verifier.
These are proposed experiments, not finished implementation, and require dataset and host compatibility validation.

## Critical misconceptions / constraints
- Choosing an adapter trained under QLoRA is still selecting a LoRA; quantized base affects model deployment configuration.
- Adapter changes *during generation* and per-token gating are not free dynamic switches in stock llama.cpp/vLLM and cannot be inferred from per-request APIs.
- Model merge between arbitrary different vocabularies/architectures is generally invalid; adapter merge requires exact compatible base and inspected target modules.
- Several GPU-serving papers report excellent scaling, but CPU-only sal-ai may be dominated by memory bandwidth and model swap.
- Router model may itself be larger/slower than task; compare against simple regular expressions and classical classifiers.
- Collaboration quality can degrade due to error propagation and consensus bias; do not assume N agents beats one well-chosen expert.


## شواهد سایر روش‌ها و فناوری‌های مرتبط در کاتالوگ اولیه
- LoRA-Mixer — ICLR 2026: https://proceedings.iclr.cc/paper_files/paper/2026/hash/18610cbcd1da57854aa05ebdc5cd3168-Abstract-Conference.html
- MoLoRA — ICML 2026: https://proceedings.mlr.press/v306/shah26d.html
- MoA — ACL 2026: https://aclanthology.org/2026.acl-long.965/
- LayerRoute — Dynamic layer skipping with LoRA: https://arxiv.org/abs/2609.13682
- MobileMoE — internal expert routing, distinct from external model routing: https://arxiv.org/abs/2605.27358
- KV1 — KV Cache quantization, not adapter selection: https://huggingface.co/klein-ml/KV1-1.2B
- MorphBPE / ParityBPE / vocabulary expansion: see `PERSIAN_TOKENIZER_RESEARCH_2026-11-16.md`.
- Rayline ARC, Strands Decider, LemonDecider, OpenThai-SystemOne are **model artifacts** catalogued in the model report; their use as Routing decision components remains a **method** in this document.
- Original mixed chronicle kept untouched: `SLM_CATALOG_2026-11-16.md`.
