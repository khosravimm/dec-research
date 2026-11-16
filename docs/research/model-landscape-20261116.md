> **Research note (E0/E2):** Literature and model card claims are differentiated from narrow local benchmarks. No unique DEC architecture has been demonstrated.

# DEC Research — نتایج شناسایی و بررسی مدل‌ها (فهرست مستقل)
**نسخه تفکیک‌شده:** 2026-11-16 | **منبع اصلی:** `SLM_CATALOG_2026-11-16.md` (آرشیو دست‌نخورده)
**دامنه:** مدل‌های عمومی و تخصصی، ایرانی و بین‌المللی، معماری‌های مدل، وزن‌ها و نسخه‌ها؛ بازه جست‌وجو: 2026-05-16 تا 2026-11-16، موارد قدیمی‌تر به‌عنوان baseline.
**سطح شواهد:** عمدتاً E0، مبتنی بر مدل‌کارت و گزارش سازنده. اعداد آزمون سایر مدل‌ها آزمایش مستقل محلی نیست.
**این گزارش شامل روش‌های ترکیب مدل‌ها یا Adapterها نیست.** مرجع جداگانه آن `COMPOSITION_METHODS_RESULTS_2026-11-16.md` است.

## وضعیت آزمون محلی
- MiniCPM5-2B Q4_K_M در sal-ai: 74 درخواست، 44 PASS خودکار، 20 FAIL (12 کنترل Thinking خاموش + 8 اصلی)، 10 MANUAL_REVIEW. 52 درخواست اصلی با Thinking روشن: 44 PASS / 8 FAIL؛ نتایج کیفی جدا از آزمون خودکار.
- فایل اولیه و کامل نتایج: `[internal evidence file; not part of the public repository]`؛ سایر نتایج با شاخص یکسان فقط بعد از تأیید کیفیت، قابل مقایسه‌اند.

## جدول‌های اصلی مدل‌ها به تفکیک دور پژوهش
توجه: جدول‌های زیر عیناً از کاتالوگ قبلی استخراج شده‌اند تا ادعاهای منبع حفظ شوند؛ تعارض‌ها و اصلاحات نسخه‌های بعدی در فایل آرشیوی باقی مانده‌اند. خواننده باید به آخرین اصلاحیه مراجعه کند و صحت نسخه/مجوز را پیش از استقرار دوباره بررسی کند.

### A — عمومی و اولویت‌دار برای بنچمارک CPU
|توسعه‌دهنده|مدل|پارامتر|معماری/قابلیت|منبع رسمی|اولویت|
|---|---|---|---|---|---|
|OpenBMB|MiniCPM5-2B|2.52B|Dense; thinking, tools, 131K|https://huggingface.co/openbmb/MiniCPM5-2B|P0: آزمون در sal-ai|
|Liquid AI|LFM3-1.7B|1.7B|Hybrid; CPU inference|https://huggingface.co/LiquidAI|Baseline نصب‌شده|
|SparkLLM/XHToken|Spark-X2.6-1.7B|1.7B|Hybrid sliding/full attention, GGUF/Base|https://huggingface.co/XHToken/Spark-X2.6-1.7B|P0|
|SparkLLM/XHToken|Spark-X2.6-4B|4.1B|Hybrid sliding/full attention, GGUF/Base|https://huggingface.co/XHToken/Spark-X2.6-4B|P0|
|IBM|Granite 4.2-3B|3B|Dense; flexible reasoning, tool use; Apache-2.0|https://www.ibm.com/granite/docs/models/granite/|P0|
|IFM/MBZUAI|K2-Horizon-0.9B|0.9B|Dense; teacher distillation; 128K; open training|https://huggingface.co/IFM/K2-Horizon-0.9B|P1; serving compatibility check|
|IFM/MBZUAI|K2-Horizon-3.7B|3.7B core; total may differ|Dense, native 512K context; open training, check total memory|https://huggingface.co/IFM/K2-Horizon-3.7B|P1|
|NVIDIA|Nemotron Labs Dory1.0-4B|4B|Latent-recurrent looped depth, adjustable internal compute, GGUF Q5_K_M; up to 256K; OpenMDW 1.1|https://huggingface.co/nvidia/NVIDIA-Nemotron-Labs-Dory1.0-4B-GGUF|P0 architecture research|
|Gensyn|Open-1B SFT/Base|1B class|Open training research, multiple checkpoints; verify exact parameter count|https://huggingface.co/Gensyn/open-1b-sft|P1 training study|
|Swiss AI|Apertus 1.5-8B|8B|Multimodal, optional thinking, training transparency, Apache-2.0|https://huggingface.co/blog/swiss-ai/apertus-v15-release-notes|P2 RAM-heavy baseline|

### B — تخصصی عامل، برنامه‌نویسی، مستندات
|توسعه‌دهنده|مدل|پارامتر|کاربرد تخصصی|منبع رسمی|اولویت|
|---|---|---|---|---|---|
|Microsoft|FrogNano-4B-2609|4B|Repository-level software agent, RL post-training, text-only intended use|https://huggingface.co/microsoft/FrogNano-4B-2609|P1 coding-agent|
|Microsoft|Mage-VL-Cowork|4B class|GUI+terminal computer use, visual policy|https://huggingface.co/microsoft/Mage-VL-Cowork|P2 vision-agent|
|Microsoft|Fara1.5-4B|4B class|Vision/browser agent, not general SLM|https://huggingface.co/microsoft/Fara1.5-4B|P2|
|Ai2|TMax-2B and TMax-4B|2B/4B|Terminal agents fine-tuned via DPPO, Apache-2.0|https://huggingface.co/allenai/tmax-2b|P1 agent benchmark|
|Ai2|Bolmo-1B|1B|Byte-level model retrained from an older baseline; pretrained research, not conventional SLM chat|https://huggingface.co/allenai/Bolmo-1B|P2|
|Ai2|AstaBrief-8B|8B|Scientific cited reporting, open training data|https://huggingface.co/blog/allenai/astabrief|P2 LDI/RAG|
|H Company|Holo-3.1-0.8B|0.8B class|Multimodal computer-use (released in June)|https://huggingface.co/Hcompany/Holo-3.1-0.8B|P1 specialized agent|
|H Company|Holotron4 Nano|30B total/3B active class|Multimodal MoE; total memory significant|https://huggingface.co/Hcompany/Holotron4-30B-A3B|P2 CPU impractical compared to dense 3B|
|Upstage|Solar Mini 4|~35B total/~3B active (vendor claim)|MoE agent/multilingual; total memory significant|https://huggingface.co/upstage|P2 architecture evaluation|

### Addendum — deeper search, 2026-11-16 (v3, additive)
| Developer | Model/research | 2026 source | Role | caveat |
|---|---|---|---|---|
|Meta|MobileMoE-S/M/L Base, SFT, QAT (NINE released checkpoints)|https://huggingface.co/facebook/models|P0 architecture and CPU runtime lab|FAIR NC license; custom runtime; not Ollama-ready by default; 8k context; English focus|
|Apple|AFM 3 Core 3B Dense|https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models|Important architecture reference|Proprietary, no official downloadable weights established|
|Apple|AFM 3 Core Advanced, 20B total / 1–4B active|https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models|P0 architectural research on prompt-wise expert paging and variable active compute|Proprietary / hardware restricted, not sal-ai benchmark candidate|
|Kog AI|Laneformer 2B (2.3B)|https://huggingface.co/blog/kogai/kog-laneformer-2b-the-latency-first-model|P1 coding and low-latency system architecture|4k context; benefits depend on custom Kog runtime; tokenizer Llama2 license|
|Norwegian National Library (NbAiLab)|Borealis 2 E2B preview|https://huggingface.co/NbAiLab/borealis2-e2b-preview|P2 regional multilingual and controlled pretraining evaluation|Preview, NB license, narrow Nordic language focus|
|FrontiersMind|Lumma-Fev-4B-v2|https://huggingface.co/blog/FrontiersMind/lumma-fev-27b-v2|P1 typed probability decision head (non-generative!) for DEC architecture|Not a chatbot/LLM baseline; company/benchmarks relatively unestablished|
|JOSIE-2 community researchers|JOSIE-2 2B/4B/9B|https://huggingface.co/blog/Goekdeniz-Guelmez/josie-2-technical-report-curated-post-training-for|P2 compact curated posttraining experiment|Derivative of Qwen3.5; claims require independent audit|

### Addendum — fourth source verification, 2026-11-16 (v4)
|Developer|Model|Size and architecture|Official distribution|License|DEC R&D class / gate|
|---|---|---|---|---|---|
|JetBrains|Mellum2.1-12B-A2.5B-Thinking|12B total, 2.5B active, 64 experts top-8, 28 layers, 131,072 context, sliding 1024 on 3/4 layers|Official Q4_K_M GGUF 8.1GB, MXFP4_MOE GGUF 7.0GB; model + MTP head|Apache-2.0|P0 coding-agent CPU research, CPU inference verified **by vendor instructions only**, not yet on sal-ai; full MoE weight footprint matters|

### Addendum — sixth systematic discovery, 2026-11-16
|Developer|Model|Scope & distinguishing architecture|Weights / license|Fit / caveat|
|---|---|---|---|---|
|Tencent Hunyuan|Hy-MT2-1.8B|Specialist multilingual translation incl Persian; reports 33 translation languages; AngelSlim 1.25-bit Q: vendor claims 440MB and 1.5x speed|Official BF16, GGUF, 2-bit, 1.25-bit GGUF; Apache-2.0|**P0 for Persian LDI OCR→translation**; assess EN↔FA fidelity/terminology, not general reasoning|
|Preferred Networks + NICT|PLaMo 3 Translate 0.8B & 2B|53 supported languages incl Persian; glossary/context-aware; supports long combined in+out up to 32768 tokens|Official BF16, GGUF, MLX, NVFP4; PLaMo Community License|**P0/P1 for Persian translation**; community license can require registration/agreement for commercial use; custom_code execution review|
|Preferred Networks + NICT|PLaMo 3 0.8B Finance Instruct|Finance-domain 0.8B variant, not general cybersecurity model|Official org listing, details not deeply checked|P2 domain-specialization comparison; not a new base family|
|Bilibili Index Team|Index-Translate-2B|Qwen3.5-based translation model 150 languages, glossary/style/JSON/markdown constraints; has visual-translation companion|Official model weights, Apache-2.0|**P0 for OCR postprocessing / EN↔FA if supported**; 150-language claim does not by itself establish measured Persian quality|
|Bilibili Index Team|Index-Translate-Omni-2B|Text+image translation and Chinese-English speech/ASR built on Index-Translate family|Official weights; card lists no explicit license, verify before use|P1 multimodal translation; **NOT equivalent to multilingual speech across 150 languages**|
|Amazon|ALoDLM-1.7B|Adaptive looped masked diffusion model built from Qwen3; persistent latent state, token-wise compute allocation and learned halting|Official weights + code; CC-BY-NC-4.0|**P0 architecture research**; not normal autoregressive Ollama workflow; no established CPU speedup|
|Amazon / Strands Agents|Strands Decider 2B (Qwen3.5 v1 2610)|LoRA on Qwen3.5-2B-Base plus typed readout; yes/no, multiclass, ordinal score, calibrated confidence|Official adapter, recipe, data and code; Apache-2.0; `strands-decider` supports CPU|**P0 for DEC architecture** as internal independent decision stage; not a text-generation replacement|
|NVIDIA|Nemotron 3.5 Parse 0.631B|Vision encoder + 10-layer mBART; page text, reading order, table/chart, bbox, semantic classes; MTP drafter optional|Official weights+code; OpenMDW-1.1|**P0 LDI OCR/document parsing**; vendor performance on H100/H200, CPU operation untested|
|Baidu|Unlimited-OCR-2|Document OCR vision-language; multimodal structured extraction|Official safetensors and custom code; MIT|P1 LDI comparative OCR; size, CPU cost and Persian quality require validation|
|Jina AI|jina-ocr-v1|Multilingual OCR/document understanding; custom DeepSeek-VL-derived architecture|Official safetensors; CC-BY-NC-4.0|P1 research OCR only due license; CPU and Persian performance untested|

### Addendum — seventh systematic review (2026-11-16): original DEC Research scope preserved
|Lab / company|Candidate|Architecture/features|Weights and restrictions|DEC hypothesis|
|---|---|---|---|---|
|Nanbeige (Kanzhun/China)|Nanbeige4.2-3B|Looped Transformer; trained from scratch on 28T tokens; loopSplit, mHC/depth attention, concat n-gram embeddings; configurable thinking and XML/JSON tools; 256K advertised context|HF official weights, Apache-2.0, Transformers trust_remote_code; https://huggingface.co/Nanbeige/Nanbeige4.2-3B ; Base https://huggingface.co/Nanbeige/Nanbeige4.2-3B-Base|P0 **novel architecture** and training on limited params; CPU support/actual RSS/latency unverified|
|Ant Group inclusionAI|Ling-3.0-tiny|7.9B total / 1.3B active, KDA/MLA hybrid 3:1, 128 routed experts with top-8 plus 1 shared, fast/thinking modes|Official MIT weights, GGUF Q4_K_M 4.82GB; https://huggingface.co/inclusionAI/Ling-3.0-tiny and https://huggingface.co/inclusionAI/Ling-3.0-tiny-GGUF|P0 CPU hybrid MoE, agentic usage; compare real CPU not vendor Mac/DGX speed|
|Ant Group inclusionAI|LemonDecider 4B v3|Qwen3.5-4B-derived typed decision backbone, 255-option readout; no free-text generation, calibrated scalar inherited; 8192 token input per chunk, recursive question bisection|Official published Apache-2.0 weights with MIT code notices, custom Transformers; https://huggingface.co/inclusionAI/LemonDecider|P0 **model / task / adapter routing** component; probabilities NOT automatically calibrated in our domains|
|Ant Group inclusionAI|SingGuard-2B|Multimodal text/image risk classifier with **runtime policy supplied as input**, fast early judgment + optional deeper reasoning|Official Apache-2.0, GGUF Q4_K_M 1.11 GB plus multimodal projector; https://huggingface.co/inclusionAI/SingGuard-2b-GGUF|P1 policy gating, sandbox policy versioning; not equivalent to an external security policy enforcement engine|
|Tencent|WeVisDoc-2B / 4B|Qwen3-VL-derived page image→Markdown, LaTex tables / text; vendor OmniDocBench v1.6 reports 95.06 (2B) / 95.38 (4B)|Official Apache-2.0 model weights, official execution path is vLLM/GPU; https://huggingface.co/tencent/WeVisDoc-2B|P1 LDI OCR/layout; **do not infer CPU support or Persian OCR quality**|
|Ant Group inclusionAI|SingVL-S1-4B|VLM 4B-class model published in Ant official org; recent Nov 2026 repository|Official weights catalog https://huggingface.co/inclusionAI/models ; deeper card verification required|Discovery queue, not an approved CPU model|
|Xiaomi|MiMo series recent releases|Model family includes massive MoE and smaller 9B distill derivatives|Must inspect official model card individually; do not equate active with resident memory|Architecture and distillation track, not auto-install|

### Addendum — eighth research sweep (2026-11-16): edge startups, China, memory, runtime
| Maker / region | Model | Verified technical evidence | Limitation / DEC priority | Primary source |
|---|---|---|---|---|
| Prism ML / US | Ternary-Bonsai-2 (2B, 4B, 9B) | 2B-class VLM with ternary language weights. 2B GGUF language portion: PTQ1_0 0.43 GB; PQ2_0 0.52 GB; Q2_0 0.55 GB compared with ~3.8 GB FP16. Custom kernels do not expand weights to FP16. | Apache-2.0; CPU via llama.cpp advertised, exact build and vision-tower RAM need tests. **P0 quantization**. | https://huggingface.co/prism-ml/Ternary-Bonsai-2-2B-gguf |
| Klein ML / startup | KV1-1.2B | Based on Liquid LFM2.5-1.2B; KV-cache-aware training for BQ2_0 2.5-bit/value. At 32K context KV cache 384 MiB → 60 MiB (per sequence); BF16 weights remain unaffected. | Inherits LFM Open License; needs custom KV1.cpp backend (not stock Ollama); author's 75.8% score-retention aggregate conceals much weaker MMLU-Pro. **P0 memory efficiency**. | https://huggingface.co/klein-ml/KV1-1.2B |
| MemTensor / China | MemT-1.0-Nano | 36B total/3B active; persistent native-memory blocks plus local and hyper-memory, gating of read/write/forget; claims ~66× reduced memory-state footprint vs full-context KV at 128K history. | 36B model weights still required; Apache-2.0; custom Transformers code, CPU efficiency unverified. **P0 memory architecture, not small deployed footprint**. | https://huggingface.co/MemTensor/MemT-1.0-Nano |
| KRAFTON / South Korea | Raon-1-mini-preview | 30B-A4B sparse MoE + linear attention from scratch; official GGUF/MLX and Apache-2.0 weights; Korean/English specialization. | Preview; ~29B total resident weights; not a dense 4B. **P1 regional agent & architecture**. | https://huggingface.co/KRAFTON/Raon-1-mini-preview |
| Ant Group inclusionAI / China | Ming-3.0-tts-0.5B | Dense 0.5B-class TTS backbone, DiT/audio tokenizer/speaker encoder, 7 vendor-listed languages. | MIT, custom runtime; **Persian not in official 7 languages**, not currently valid Persian TTS candidate. | https://huggingface.co/inclusionAI/Ming-3.0-tts-0.5B |
| Ant Group inclusionAI / China | Ming-3.0-asr-tiny | Context-aware Chinese/English ASR with hotword hints; model-card lists ~9B parameters despite tiny branding. | MIT, 17.8GB repo, no official Persian support; not a sub-1B model. | https://huggingface.co/inclusionAI/Ming-3.0-asr-tiny |
| Tencent / China | Hy-Memory-30B-A3B | MoE specializing in memory-writing and persistent-fact selection for agents. | Apache-2.0; 30B total weights, not light CPU baseline. **P1 memory policy**. | https://huggingface.co/tencent/Hy-Memory-30B-A3B |
| Academic | LayerRoute | Input-adaptive layer skipping jointly trained with low-rank adaptation on Qwen2.5-0.5B; 21.5k router + ~1.08M LoRA params, ten seeds, reported speedup 1.02–1.06× (mean 1.04×). | Paper dated Sep 12, 2026; gains modest and not equivalent to model/adapter selection; independent CPU replication needed. | https://arxiv.org/abs/2609.13682 |

### Addendum — ninth sweep (2026-11-16): Iranian/Persian model engineering
| Maker | Model | Implementation / reproducibility | Gate | Primary source |
|---|---|---|---|---|
| Sina Meraji / IbnSina | IbnSina-1.5B | 1.48B Llama-compatible 28 layers, native Persian-focused byte-level BPE 32768, context 2048, GGUF Q4_K_M ~904MB. Creator reports 36.7B training tokens and ~51.5k instruction conversations, Muon+AdamW and pretraining from random init. Apache-2.0 weights/code. | P0 Persian tokenizer and local CPU baseline; author evaluation multiple-choice scores near chance (31.8% ParsiNLU-MC, 26.8% PersianMedQA), NOT reliable Persian security expert. Claims of 46B tokens elsewhere need distinction from exact 36.7B training run. | https://huggingface.co/ibnsina-llm/ibnsina-1.5b |
| Sina Meraji / IbnSina | IbnSina-3B | 3B Qwen3-style architecture trained from scratch (not fine-tuned Qwen weights), 40 layers, d2560, GQA 20/4, 2048 context; 99.6B pretraining tokens, checkpoints, optimizer shards, tokenizers, SFT variants, MANIFEST.sha256, GGUF Q4 ~1.81GB, Apache-2.0. | P0 from-scratch research and benchmark; checkpoint author reports one seed failing to reproduce 2026 September SFT v2.1 gains; do not claim performance superiority. | https://huggingface.co/ibnsina-llm/ibnsina-3b-checkpoints |
| Aria Haman Mehr Parseh / Haman Labs | Haman Graph-LLM 125M | 124,978,951 unique params, 10-layer decoder + GCN static lexical graph 31,995 nodes, context 256, from scratch ~396.9M token-exposures. Custom Rakhshai runtime, published model/dataset/graph/checkpoints, Haman Model License 1.0, CPU CLI. Released 2026-07-15. | P0 **graph-neural hybrid architecture** for DEC research; cannot serve as general assistant (256 context); creator's "first native architecture" claim scoped and not independently established. | https://huggingface.co/aria-haman/haman-fa-article-graph-llm-125m |
| Arad Manamnaoon (individual) | Persian GPT 110M | 110.4M, decoder-only 12 layers, trained from scratch on ~244M Persian Wikipedia tokens, context 1024; BPE32k, safetensors and training details; author claims test PPL14.52. | P1 reproducible small-model teaching baseline; not instruction-tuned or secure factual system; license/data provenance CC-BY-SA-3.0 requires review. | https://huggingface.co/aradmanamnaoon/persian-lm-from-scratch |
| Dibachain / DibaAi | Diba-2B | Persian/web coding focus, claims GGUF Q4 1.2GB and ~18 tok/s four-core CPU, Apache-2.0. Its different Diba-Base card still says weights 'coming soon'. Dataset DiLLM.nano ~1.02M documents, ~379M tokens. | P1 conditional: verify actual downloadable GGUF/model files, revisions, reproducibility and functional independent tests before including performance comparisons. | https://huggingface.co/DibaAi/Diba-2B |
| JibayAi | Jibay 2 | 2B Qwen3-derived, claims public open release June 2026 after initial May 2025. | P2 verification queue: author claims on proprietary Jibay5 (97% GPQA Diamond outperforming GPT-6 Astra) are **unverified**, and must not be repeated as fact. Check repository actual model artifacts and licenses. | https://huggingface.co/JibayAi/Jibay_2 |

| Organization | Model / contributions | Why retained | Source |
|---|---|---|---|
| Part AI | Dorna and Dorna2: Persian adaptation of Llama3/3.1 8B, GGUF; Tooka-SBERT 0.1B/0.4B semantic models and Persian benchmark ecosystem | Production-style localization, retrieval/embedding baseline; Dorna release older than six months | https://huggingface.co/PartAI |
| University of Tehran | PersianMind-7B: Llama2 adaptation with Persian token extension, noncommercial terms | Comparative continual pretraining / tokenizer research; older than window | https://huggingface.co/universitytehran/PersianMind-v1.0 |
| Hooshvare Research Lab | ParsBERT, GPT2-fa, token-classification/sentiment, summarization | Strong Persian understanding baselines for **router, document tagging, LDI**; most models from 2020–23 | https://huggingface.co/HooshvareLab/models |
| Hezar AI | Persian-focused BERT, OCR models/datasets, parsynth-ocr-4m released/updated around October 2026 | Important LDI Persian OCR dataset candidate; inspect dataset consent/licensing and training/test leakage | https://huggingface.co/hezarai |
| Darsadi research lab | Zagros-1.0-Quick 30.5B MoE, 8 experts top-2, Apache-2.0 | Iranian/Persian-centric MoE, however release **Sep 2025**, outside current window and far from small total-weight | https://huggingface.co/darsadilab/zagros-1.0-quick |

### Addendum — eleventh sweep, 2026-11-16: small specialist models and verified serving constraints
| Maker/region | New candidate | Task / architecture | Availability / license / key caveat | Primary source |
|---|---|---|---|---|
| Jina AI / Germany | jina-reranker-v3.5 | **0.6B listwise reranker** built on Qwen3-0.6B, hybrid 3L2G, jointly ranks query and multiple documents, max context 131K | Official BF16 and GGUF; BEIR 63.20 nDCG@10, MIRACL 74.11, vendor reported; license must be checked at pinned repo revision. P0 for LDI/RAG compared with bge-m3 and reranker baseline. | https://huggingface.co/jinaai/jina-reranker-v3.5 |
| Rayline / startup | ARC-1.0 | **0.6B reported model artifact**, Qwen3.5-0.8B backbone with shared frozen 12 layers and specialized success, token usage, reasoning, PII, operation, domain and question heads | Apache-2.0 weights; proprietary production training data; stock vLLM **cannot** serve custom architecture, vllm-arc plugin only stage 1. Author-reported task-economics depend on cloud pool and price. P0 routing research, not immediate drop-in. | https://huggingface.co/rayline-ai/ARC-1.0 |
| iApp / Thailand | OpenThai-SystemOne | **0.8B typed decision model**, Qwen3.5-0.8B text tower and SlotHead for up to 255 alternatives, score/yes-no/choice; independent open reimplementation | Apache-2.0; Thai/English training and 5B Thai continued-pretraining tokens; Persian/OOD decision calibration unknown. P1 compare with ARC/Strands/Lemon. | https://huggingface.co/iapp/OpenThai-SystemOne |
| MinimaLabs / startup | KLM 1.6 | **99M BASE model**, Gated-DeltaNet hybrid; extension to 100B LR-decay tokens from KLM1.5 checkpoint | Apache-2.0; not instruction-tuned, evaluation zero-shot multiple choice; custom architecture and `trust_remote_code`. P1 teaching/architecture, **not security agent**. | https://huggingface.co/MinimaLabs/KLM-1.6 |
| iApp / Thailand | OpenThai2.0 OCR Text | **1.02M-parameter two-part OCR**, PP-OCRv6-tiny detector plus 587K Thai CTC line recognizer; ONNX/OpenVINO CPU | Apache-2.0; vendor measures ~0.39s/A4 page, ~450MB RAM per worker, **Thai+English only**, not Persian OCR. P0 architecture/CPU pipeline design. | https://huggingface.co/iapp/OpenThai2.0-OCR-Text |
| iApp / Thailand | OpenThai2.0 OCR Markdown | **630.8M VLM document parser**, full Thai fine-tune of NVIDIA Nemotron 3.5 Parse; layout, HTML tables, Markdown | OpenMDW-1.1 inherited, GPU official serving, Thai+English only; not a Persian OCR candidate without training. P1 LDI cross-language training example. | https://huggingface.co/iapp/OpenThai2.0-OCR-Markdown |
| Alibaba Logics / China | Logics-Parsing-V3 | **Document-level state-recurrent parser**; maintains hierarchical state across pages, merges cross-page text/tables, visual-text links; released Sep 22 2026 | Official model repo and report; 0.8B figure comes from third-party catalog and must be confirmed in primary card/config before size claim. P0 LDI architecture. | https://huggingface.co/Logics-MLLM/Logics-Parsing-V3 |
| Uraion Labs / startup | Uraion-Agent-Small | Qwen3.5-2B specialized for tool calls with **QLoRA** and merged adapter; official code/data recipe | Apache-2.0. **Published GGUF has known invalid tensor-shape errors**; publisher recommends regenerating via NF4→FP32→GGUF. CPU NF4 slow. P2 until valid GGUF rechecked; claimed tool ability unverified independently. | https://huggingface.co/UraionLabs/Uraion-Agent-Small |

## یافته‌های مدل بدون جدول مستقل در کاتالوگ اولیه
- `LiquidAI/d1-2B`: مدل تصمیم‌گیری تخصصی از خانواده LFM3؛ https://huggingface.co/LiquidAI/d1-2B
- `MiniCPM5-2B`: نسخه GGUF رسمی https://huggingface.co/openbmb/MiniCPM5-2B-GGUF
- `Kog Laneformer 2B`: مطالعه معماری و تأخیر https://huggingface.co/kogai/laneformer-2b-it
- `TinyLM 275M`: مطالعه مدل کوچک پایه https://huggingface.co/Shiv-22/tinylm
- `MobileMoE S/M/L`: وزن‌های Base/SFT/QAT منتشر شده‌اند؛ اصلاحیه مدل‌کارت بر خلاف یادداشت نخست که انتشار وزن را تأییدنشده می‌دانست؛ https://huggingface.co/facebook/models

## گزارش‌های اختصاصی مدل‌ها
- `MOBILEMOE_TECHNICAL_REVIEW_2026-11-16.md`: مقاله و پیاده‌سازی MobileMoE.
- `PERSIAN_TOKENIZER_RESEARCH_2026-11-16.md`: پژوهش Tokenizer فارسی (روش تحقیق زبان، نه مدل ترکیبی).
- برای موارد توصیفی بدون جدول، تناقضات مجوز، اصلاحیه‌ها و منابع: `SLM_CATALOG_2026-11-16.md` آرشیو اصلی.
