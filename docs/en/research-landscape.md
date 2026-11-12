---
doc_id: DEC-DOC-005
language: en
title: "Research landscape and real-world reference projects"
version: 0.1.0
date: 2026-11-12
evidence_level: E0
publication_status: public-research-draft
---

# Research landscape and candidate comparison

This is a **curated technical landscape** compiled from original publications, model cards, official documentation and public source repositories as of 2026-11-12. It is not a systematic meta-analysis or independent demonstration of those projects' benchmark claims. See the bilingual [machine-readable source catalogue](../../research/catalogue.json).

## Compact model cores and neural architectures

| Candidate | Relevance to DEC | Caveat |
|---|---|---|
| [MiniCPM5 1B/2B](https://github.com/OpenBMB/MiniCPM) | Standard dense Llama-compatible checkpoints, documented LoRA/QLoRA, Think modes, GGUF and reported teacher distillation | No built-in multi-role shared latent council; Persian unverified |
| [Qwen3.5 0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B) | Hybrid Gated DeltaNet/attention compact model | Model/runtime LoRA and Persian performance must be assessed |
| [Granite 4.0 H](https://huggingface.co/ibm-granite/granite-4.0-h-1b) | Mamba-2 plus attention for compact reasoning and tool/routing roles | Recurrent state is not equivalent to Transformer KV |
| [LFM3](https://huggingface.co/LiquidAI/LFM3-1.7B) | Shared backbone family with specialized variants | Model-specific licensing and training/runtime access require validation |
| [RWKV-7](https://github.com/BlinkDL/RWKV-LM) / [Mamba](https://github.com/state-spaces/mamba) | Efficient recurrent state architecture | Not interchangeable with standard LoRA Transformer hidden states |
| [BitNet](https://github.com/microsoft/BitNet) | Native low-bit weights and custom kernels | Native ternary architecture is not a generic Q4 conversion |

**Screening rule:** availability of public weights/source does **not** prove suitability or accuracy in a Persian/English technical benchmark, nor feasible training on a 6GB-class GPU.

## Latent collaboration and memory

- [LatentMAS (ICML 2026)](https://proceedings.mlr.press/v306/zou26k.html): public shared-latent memory experiments.
- [Interlat (ACL 2026)](https://aclanthology.org/2026.acl-long.1248/): hidden-state communication and alignment for agents.
- [LatCom (EMNLP 2026)](https://aclanthology.org/2026.emnlp-main.1068/): compression of expensive cross-agent latent communication.
- [Cache-to-Cache (ICLR 2026)](https://proceedings.iclr.cc/paper_files/paper/2026/hash/474ada926b331d78f06d95e8913111cc-Abstract-Conference.html): trainable KV projection/fusion in tested model pairs; **distributed cross-server experiments are deferred**.
- [LRAgent (ICML 2026)](https://proceedings.mlr.press/v306/jeon26b.html): LoRA-specific KV duplication and base sharing.
- [Agent Primitives](https://github.com/haibojin001/AgentPrimitives): Review/Vote/Plan/Organize modules communicating via compatible KV; end-to-end demo status must be checked.
- [LatentMAS-SLoRA](https://github.com/Arifuzzamanjoy/latent_mas_slora): executable research code for per-role LoRA switching and latent message exchange, **with untrained bundled role adapters**. Published small benchmark not a DEC result.

These projects show partial feasibility but none is a ready DEC system or a validated new integrated model with collaborative latent cognition.

## Tools and software products

- [PEFT](https://github.com/huggingface/peft) + [Unsloth](https://github.com/unslothai/unsloth) + [TRL](https://huggingface.co/docs/trl/main/index): LoRA training, parameter-efficient adaptation and post-training research.
- [llama.cpp](https://github.com/ggml-org/llama.cpp): local GGUF CPU serving; [vLLM](https://github.com/vllm-project/vllm), [SGLang](https://github.com/sgl-project/sglang): optimized model serving, typically with hardware-specific features.
- [LangGraph](https://github.com/langchain-ai/langgraph), [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), [CrewAI](https://github.com/crewAIInc/crewAI): robust structured agent coordination but **not** automatically latent transport.
- [LMCache](https://github.com/LMCache/LMCache): tiered KV cache reuse for compatible runtime/requests; **not** shared neural deliberation.
- [pgvector](https://github.com/pgvector/pgvector), [LightRAG](https://github.com/HKUDS/LightRAG): retrieval backends to compare with existing document-intelligence assets rather than replace them prematurely.
- [AutoGen](https://github.com/microsoft/autogen), [LoRAX](https://github.com/predibase/lorax) and [S-LoRA](https://github.com/S-LoRA/S-LoRA) have repository maintenance/archival warnings; use them as historical references, not defaults.

## Prior-art significance and qualification

The potential unique DEC contribution is **not** the LoRA, MoE, cache sharing, latent message or orchestration concepts individually: all have significant prior art. Any later claim must isolate a distinct trainable integrated mechanism and independently demonstrate its effect. Avoid public disclosure of unfiled technical inventions without prior legal review. Research names and cited code are not adopted components until version, licensing, hardware and reproducibility tests pass.

## References and raw results

See [catalogue](../../research/catalogue.json), [planned experiments](../../research/experiment-register.json), [methods](methods.md) and [results](results.md). Every catalogued item is E0 in the DEC context, irrespective of external paper evidence quality.
