> **Research note (E0/E2):** Literature and model card claims are differentiated from narrow local benchmarks. No unique DEC architecture has been demonstrated.

# MobileMoE – Technical review of primary paper (Meta AI, arXiv 2605.27358)
Date: 2026-11-16. Evidence: E0 for architecture and interpretation; E2-like published experimental evidence on specified devices, not independently reproduced. Earlier catalog entries remain unchanged; this document adds corrections.

## Primary sources
- Main primary paper (28 pages): https://arxiv.org/pdf/2605.27358 ; submitted 2026-05-26, PDF dated May 27.
- Hugging Face official org: https://huggingface.co/facebook/models
- Official instruction-tuned card: https://huggingface.co/facebook/MobileMoE-S-SFT
- Official QAT card: https://huggingface.co/facebook/MobileMoE-M-QAT
- Official Base card: https://huggingface.co/facebook/MobileMoE-M-Base
- ExecuTorch official runtime repository: https://github.com/pytorch/executorch
- Quantized custom MoE operation documentation: https://github.com/pytorch/executorch/tree/main/examples/models/llama
- Counter-evidence on other MoE+hardware pairing: https://arxiv.org/abs/2606.21428

## Model scales (official Meta model cards)
|Scale|Active|Total|Layers|Width|Q/KV heads|Routed expert|top-k|Shared|INT4 static weight GB|Context|
|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
|S|272M|1.3B|20|768|12/4|60|4|1|0.68|8192|
|M|528M|2.8B|26|1024|16/4|60|4|1|1.48|8192|
|L|922M|5.3B|32|1280|20/4|60|4|1|2.75|8192|

Meta released nine checkpoints (S/M/L each of Base, instruction SFT, INT4 QAT) on Hugging Face in August 2026. IMPORTANT CORRECTION: official weights ARE AVAILABLE; earlier catalog said unverified. License FAIR Noncommercial Research, not OSI or Apache-2.0. English-focused; do not assume Persian performance. Base is not instruction-tuned.

## Design, scaling and implementation findings
1. Paper Eq. (1) models training loss jointly as a function of active parameters, training tokens, expert count, expert granularity and shared experts; optimizing under memory and compute budgets includes weights plus KV cache (Eqs. 4/5). Memory proxy excludes some transient inference costs.
2. Controlled model-selection study finds moderate expert sparsity E=8 superior to excessive sparsity (diminishing benefit beyond E=8). Dividing into granularity g=8 gives 60 fine-grained routed experts plus 4 active top-k and shared expert; group count vs flattened expert count must not be confused.
3. Sigmoid gating, normalized top-k selection, auxiliary-loss-free bias-based expert balancing with lambda 1e-3, router z-loss 1e-4, FP32 routing stabilize training.
4. Pretraining ~6 trillion tokens at 2048 context, mid-training ~500B tokens at 8192, SFT >80M samples (~126B tokens) at 8192, QAT ~21B tokens, with mixed code/math/knowledge and instructions.
5. BF16 training; QAT uses symmetric groupwise INT4 weight quantization (group size 32) and INT8 dynamic activations, router FP32. Paper's BF16 SFT to INT4 QAT aggregate accuracy drop ~2–3 points on its 14-benchmark average, not zero loss.
6. Mobile inference uses ExecuTorch XNNPACK with a custom fused MoE FFN kernel: grouped GEMM, token rearrangement by expert, fused top-k/dispatch/gate+up/SwiGLU/down/weighted scatter. On Arm, the op uses optimized torchao (NEON i8mm/dotprod); generic x86 fallback supports numerical testing but not necessarily the speedups.
7. Hardware from paper: Samsung Galaxy S25 Snapdragon 8 Elite CPU 4 threads; iPhone 16 Pro A18 Pro CPU 2 threads; additionally Apple GPU via MLX. These are not sal-ai Xeon results.
8. At similar INT4 static weight footprint to MobileLLM-Pro, MobileMoE-S reported prefill speedups 1.8–3.8x and decode 2.2–3.4x depending on hardware/backend/context; specific table scores and caveats matter. The S model is close to dense baseline overall QAT benchmark accuracy: 44.0% vs 45.5%, not strictly better quality.
9. Peak RSS under realistic 8k prompts on Samsung S25: S 1.49 GB, M 2.77 GB, L 4.71 GB. Do not treat 0.68/1.48/2.75 GB model weight memory as real peak RAM. Dummy repeated-token prompts understate MoE RSS by up to 1.2–2.1x, because fewer distinct experts are activated.
10. Context 8192 only; no demonstrated 128k context or language-specialization in Persian. Custom model code/trust_remote_code increases supply-chain surface; pin commits/review code/sandbox.

## Experimental results interpretation
Paper reports both 14 foundational benchmarks and advanced instruction/code/math benchmarks; compare only matched formats, precision, prompt templates and eval harness. Base vs SFT vs QAT figures cannot be used interchangeably. Table 6 reports QAT aggregate 44.0/52.5/57.8 for S/M/L vs 45.5 MobileLLM-Pro; corresponding BF16 SFT 46.7/55.3/60.1.

## Counterevidence and boundary of validity
2026-06-19 empirical paper https://arxiv.org/abs/2606.21428 found OLMoE-1B-7B slower and more energy hungry than matched dense on two different devices under llama.cpp. This does not disprove MobileMoE-specific fused runtime results, but it demonstrates that 'fewer active parameters' does NOT imply fast edge inference without right backend/weight paging/memory bandwidth.

## DEC Research decision / benchmark gate
- Distinguish research value from commercial deployment: FAIR NC restricts intended license scope; legal review required before production/commercial usage.
- Priority: S-SFT, M-SFT for qualitative Persian/network-security baseline; S-QAT, M-QAT for runtime/memory, M-Base only for pretraining/adapters.
- First verify Meta model code with isolated Transformers CPU inference and compare outputs on 5 prompts; no official universal Ollama GGUF availability confirmed; do NOT claim Ollama speed parity.
- Follow with same source prompts but split by route: CPU transformers reference, ExecuTorch optimized path (only on supported platform), accuracy, TTFT, decode tok/s, RSS under realistic prompts, 512/2k/8k context, expert activation distribution, and task formatting.
- For adapting to Persian security tasks: validate tokenizer token/character ratios, LoRA support for MoE/expert routing, contamination/leakage safeguards, Base vs SFT, non-English degradation, and training resource feasibility.
- Consider architecture for adaptive task routing without assuming any expert is an independent deliberative CPU: these are learned nonlinear sub-networks selected per token, not separately accountable decision modules.
