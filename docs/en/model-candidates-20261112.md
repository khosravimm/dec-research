---
doc_id: DEC-DOC-021
language: en
title: "DEC next-generation backbone landscape: tool use, LoRA and latent-state feasibility"
version: 0.1.0
date: 2026-11-12
evidence_level: E0
publication_status: public-research-draft
---

# DEC next-generation backbone landscape: tool use, LoRA and latent-state feasibility

**Status:** Primary-source technical survey of 18 candidates. No new on-host candidate benchmark or final backbone selection is claimed. All *model selection test prompts* will be **English only**; project science documents remain paired Persian/English. Previously run local models are E1 only within their limited test scope; new candidates are E0 source reviews.

## 1. Non-negotiable backbone acceptance gates

The core needs (1) strict English instruction following, (2) structured API tool calling with actual result-driven round trips, (3) correct no-tool decisions, (4) validated arguments/outputs, (5) rights-cleared trainable LoRA/QLoRA checkpoints, (6) switching two genuinely trained adapters without reloading a shared Base, (7) observable hidden states and correct KV/recurrent-state handling, (8) bounded RAM/VRAM/latency, and (9) auditable modification and commercial redistribution rights. Licensing, security and runtime correctness are **hard gates**, not weighted benefits.

## 2. Priority classes

- **Immediate benchmark proposal**: Qwen3.5-2B, MiniCPM5-2B, Granite 4.2-3B, Qwen3.5-4B, Raon-1 nano, QVAC BotPsy-0.8B
- **Existing local comparator**: LFM3-1.7B, Qwen2.5-3B-Instruct
- **Second-wave comparison**: Qwen3-1.7B, Ministral 3 3B Instruct, Gemma 4 E2B-it, Nemotron 3 Nano 4B, K2-Horizon-3.7B, Qwen3-4B-Instruct-2507
- **Method, router or teacher only**: Granite 4.0 H-1B, Ternary Bonsai 2 4B, FunctionGemma 270M, LFM2.5-24B-A2B

## 3. Verified model candidate catalogue

| Candidate | Architecture / size | Declared license | Potential DEC role | Uncertainty or risk |
|---|---|---|---|---|
| [Qwen3.5-2B](https://huggingface.co/Qwen/Qwen3.5-2B) | 2B dense/hybrid | Apache-2.0 | Compact agent contender with separate Base checkpoint for LoRA | Hybrid DeltaNet/Attention state and PEFT support require targeted tests |
| [MiniCPM5-2B](https://huggingface.co/openbmb/MiniCPM5-2B) | 2.52B dense Llama | Apache-2.0 | Primary dense multi-LoRA research candidate with official PEFT recipes | Vendor SGLang tool parser and GGUF conversion need separate verification |
| [Granite 4.2-3B](https://huggingface.co/ibm-granite/granite-4.2-3b) | 3B dense Transformer | Apache-2.0 | Agentic dense candidate with configurable thinking and transparent architecture | Thinking budget/parser and local LoRA feasibility are untested |
| [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) | 4B hybrid DeltaNet | Apache-2.0 | Stronger-capacity tool/instruction comparator | 6GB training and state access are not yet validated |
| [Raon-1 nano](https://huggingface.co/KRAFTON/Raon-1-nano) | 3.1B total / 1.5B effective, hybrid | Apache-2.0 | New Nov 11 2026 hybrid with recurrent state and English tools | New release, custom code and LoRA/state compatibility untested |
| [QVAC BotPsy-0.8B](https://qvac.tether.io/models/botpsy) | 0.8B Qwen3.5 derivative | Apache-2.0 | Nov 11 specialist tool executor / lightweight router candidate | Tool specialization does not prove general shared-core reasoning |
| [LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) | 1.73B tri-hybrid | LFM Open License v1.0 | Observed DEC comparator, 11/12 tool score and shared family Base | Commercial licence terms and latent/LoRA behavior need formal gate |
| [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) | 1.7B dense Transformer | Apache-2.0 | Simpler dense latent/LoRA reference than newer hybrid backbones | DEC actual tool-call score is unknown |
| [Ministral 3 3B Instruct](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512) | 3.4B language + 0.4B vision | Apache-2.0 | Dense function-calling competitor with separate Base checkpoint | Real memory and multimodal runtime requirements need measuring |
| [Gemma 4 E2B-it](https://huggingface.co/google/gemma-4-E2B-it) | 5.1B total / 2.3B effective | Apache-2.0 | New function-calling PLE architecture candidate | Effective 2B does not mean 2B storage; 6GB training unverified |
| [Nemotron 3 Nano 4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16) | 3.97B Mamba-2 + Attention | NVIDIA Nemotron Open Model License | English-focused agent with Mamba2 state reference | GPU-oriented runtime and special license require a gate |
| [K2-Horizon-3.7B](https://huggingface.co/IFM/K2-Horizon-3.7B) | 3.7B core dense; embeddings extra | Apache-2.0 | Open research baseline with training/eval code and tool parser | High thinking token budget and H200-serving advice are resource mismatches |
| [Granite 4.0 H-1B](https://huggingface.co/ibm-granite/granite-4.0-h-1b) | ~1.5B total hybrid Mamba2 | Apache-2.0 | Compact recurrent-state architecture/router comparator | Mamba recurrent state differs from KV; adapter switching not verified |
| [Ternary Bonsai 2 4B](https://huggingface.co/prism-ml/Ternary-Bonsai-2-4B-gguf) | 4.21B ternary language; 0.95–1.15GB weights | Apache-2.0 | Very low-weight-memory research, not a proven trainable backbone | Custom kernels/fork; LoRA and reproducibility unproven |
| [FunctionGemma 270M](https://deepmind.google/models/gemma/functiongemma/) | 270M specialized tool model | Gemma terms | Tiny customizable tool router, not a general council core | Gemma-specific licence; needs fine-tune and independent test |
| [LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) | 24B total / ~2.45B active MoE | LFM Open License v1.0 | Teacher and MoE reference, not a 6GB-first trainable core | All 24B parameters still need storage; 2B active is not 2B total |
| [Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) | 4B dense Transformer | Apache-2.0 | Mature dense PEFT and tool reference against new hybrids | LoRA on 6GB GPU may require offload |
| [Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) | 3B dense Transformer | qwen-research | DEC 22/24 control only, commercial licensing unresolved | Official qwen-research licence: verify local lineage and commercial rights |

## 4. What DEC E1 experiments already establish

The existing 24-case English DEC test observed 22/24 for a locally stored Qwen2.5:3B weight and 20/24 for LFM3-1.7B, with 10/10 positive tool cycles for both. These are single-run E1 outcomes using simple synthetic tools. **The local Qwen2.5 weight origin and exact rights must be mapped to an official repository and revision.** The official Qwen2.5-3B-Instruct card declares qwen-research, so the historically top-scoring checkpoint should not be presumed commercially unrestricted.

## 5. Architectural implications and decision risks

**Dense vs hybrid:** Dense MiniCPM5-2B, Granite 4.2-3B, Qwen3-1.7B and Qwen3-4B offer more straightforward first experiments for adapter swapping and hidden-state collection. Qwen3.5, Raon, Granite Hybrid and LFM3 have recurrent/DeltaNet/Mamba/convolution paths with a distinct internal-state contract; none grants cross-adapter KV or recurrent-state correctness automatically.

**Real LoRA support:** PEFT supports installing and switching adapters on a shared base, but adapter type, target modules, rank, exact backbone revision and state semantics must be verified. Loading a GGUF model is not proof of a 6GB GPU QLoRA training path; training should use a properly supported Safetensors checkpoint.

**Latent research:** Transformers' output_hidden_states=True exposes layer outputs, but passing them as useful inter-expert messages and reusing KV/SSM state after changing LoRA is not automatically valid. LatentMAS-SLoRA is a promising research prototype, but its bundled role adapters are untrained, so it does not prove the value of trained LoRA experts.

**Commercial rights:** Apache-2.0 still entails notices, provenance and third-party supply-chain obligations. Liquid's LFM Open License v1.0 requires enterprise licensing for production by businesses above $10M annual revenue. Official Qwen2.5-3B-Instruct is qwen-research. NVIDIA and Gemma legacy weights have their own terms. Ownership of DEC's original code/research does not imply ownership of third-party model weights.

## 6. Recommended staged shortlists

**Agent core:** benchmark Qwen3.5-2B, Granite 4.2-3B, Qwen3.5-4B and newly released Raon-1 nano versus the existing LFM3-1.7B control. **Multi-LoRA / latent substrate:** validate two trained adapters first on dense MiniCPM5-2B and Qwen3-1.7B, then repeat on hybrid Qwen3.5-2B. **Lightweight tool router:** compare new BotPsy-0.8B with FunctionGemma 270M. Avoid assuming one optimal architecture before controlled evidence.

## 7. Proposed acceptance experiment

First verify exact repository revision, SHA256 and weights license. Use at least 40 English exact-instruction and 40 English tool scenarios including no-tool negatives, ambiguous tools, invalid arguments, conflicting requirements and multi-step calls. Repeat with at least three seeds and independent adjudication. For surviving candidates, train two genuine rights-cleared LoRAs and prove one-time base loading, adapter switching, state isolation, KV/SSM and hidden-state correctness, peak RAM/VRAM and rollback. Do not upload raw third-party weights or private records to public GitHub. These are proposed future thresholds, not observed results.

No DEC final base is selected. Manufacturer-reported benchmark scores are not interchangeable with the DEC hardware/runtime or the owner's English-only tool criteria.

## 8. Primary technical references

- https://huggingface.co/docs/transformers/peft
- https://huggingface.co/docs/peft/main/quicktour
- https://huggingface.co/docs/transformers/main_classes/output
- https://github.com/Arifuzzamanjoy/latent_mas_slora
- https://huggingface.co/blog/LiquidAI/lfm3
- https://huggingface.co/blog/ibm-granite/granite-4-2

### Research evidence and reproducibility
- [Prior five-model English tools/instructions E1 test](model-english-instruction-tools.md)
- [Machine-readable catalogue](../../research/model-candidates-20261112.json)
