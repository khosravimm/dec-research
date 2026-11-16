# Persian / English / Code tokenizer research for DEC Research
Date: 2026-11-16
Source window: 2026-05-16 to 2026-11-16; older studies clearly marked.
Evidence: E0 source review. No completed measured tokenizer comparison on sal-ai in this report.

## Summary
Tokenizer decisions are architectural: they affect input/output token counts, real context capacity, Unicode fidelity, morphology, vocabulary embedding parameter count, energy/runtime, multilingual transfer, and whether existing model weights remain compatible. **Never replace a pretrained model's tokenizer without training/adjusting token embedding and output head where needed, and testing catastrophic forgetting.**

**Decision pending.** Research three strategies under controlled trials:
1. Maintain existing tokenizer and normalize only in task-appropriate reversible ways (baseline).
2. Extend vocabulary via continued BPE/vocabulary optimization and train new embeddings with continual pretraining; require adequate original-language replay.
3. Build bilingual Persian-English-code tokenizer for a FROM-SCRATCH model, compare baseline BPE/Unigram with morphology-aware, parity-aware, and language-adaptive variants.

## New peer-reviewed studies inside window
|Work|Contribution|Reported result/caveat|DOI/URL|
|---|---|---|---|
|MorphBPE (ACL Findings, July 2026)|Constrain BPE merges to morpheme boundaries, compatible standard inference|Controlled 300M and 1B-from-scratch in EN/RU/HU/AR show morphological coherence and cross entropy improvements; no Persian direct test|https://aclanthology.org/2026.findings-acl.2068/|
|Parity-aware BPE (ACL, July 2026)|Choose merge improving worst-compressed language in each step|Up to 89% lower Gini of per-language token costs in reported experiment, not 89% smaller model or Persian-specific guarantee|https://aclanthology.org/2026.acl-long.342/|
|MUTANT (ACL, July 2026)|Language-aware pre-tokenization and subword/multiword learning|Indic-language fertility 39.5% better than Llama4 and 44% inference throughput gain in own tested comparison; extrapolation to Persian invalid|https://aclanthology.org/2026.acl-long.2146/|
|Vocab Diet (ACL Findings, July 2026)|Vector arithmetic to restructure pretrained vocabulary|10–40% vocabulary slots can be reclaimed and reallocated with limited model degradation in authors' cases|https://aclanthology.org/2026.findings-acl.1618/|
|LangMAP (EMNLP, Oct 2026)|Per-language Unigram distributions over SAME token vocabulary|Better morphology boundary recall; **most downstream LM fine-tuning differences NOT statistically significant**; strong negative qualifier|https://aclanthology.org/2026.emnlp-main.2170/|
|Parallel Tokenizers (EMNLP, Oct 2026)|Language-specific vocabularies aligned via translation lexicon|Improved downstream for 13 low-resource languages in scratch-trained encoders; no proof for decoder LLM or Persian|https://aclanthology.org/2026.emnlp-main.117/|
|Equity with Efficiency (EMNLP, Oct 2026)|Parity-aware vs morphology-driven byte encoding under controlled 1.5B models|Compression parity and task quality show Pareto tradeoff; byte-latent underperforms in studied lower-data training regime|https://aclanthology.org/2026.emnlp-main.1783/|
|One Tokenizer To Rule Them All (ACL, July 2026)|Broad universal tokenizer in pretraining to increase unseen-language adaptability|Up to 20.2% improvement on selected adaptation win rates; not necessarily reason to use universal over Persian-specific for Persian-only|https://aclanthology.org/2026.acl-long.141/|
|TokLens (ACL SRW, July 2026)|6 tokenizer intrinsic metrics, 24 tokenizers, 15 languages|Measures correlate with multilingual outcomes but are NOT substitutes for trained model evaluation|https://aclanthology.org/2026.acl-srw.18/|
|HPLT3-PerRef (Web-as-Corpus, Oct 2026)|Filtered Persian corpus 105.9B tokens, 102.37M documents from 6,144 manual labels|20% filtered as low-quality; dataset tokenizer count depends on tokenizer used. Inspect license/provenance/heldout before training.|https://aclanthology.org/2026.wac-1.6/|

## Important studies before six-month window (foundational baselines)
- Embedding Relearning and Swapping, EACL March 2026: train embeddings for custom tokenizer while freezing base and then evaluate English forgetting; up to 20% reported on some tasks, not uniform: https://aclanthology.org/2026.eacl-long.357/
- Teaching Old Tokenizers New Words, EACL March 2026: continued BPE merges on targeted data, adding reachable tokens; leaf-based pruning: https://aclanthology.org/2026.findings-eacl.341/
- Vocabulary Expansion with 0.01GB, Computational Linguistics March 2026: evaluate initialization + continued training in small data regime: https://aclanthology.org/2026.cl-1.9/

## Persian projects
- IbnSina-3B, canonical training tokenizer archived under `base/tokenizer_TRAINING.tar.gz`, `tokenizer.pkl` MD5 7e262b94 and `token_bytes.pt`. **Must not silently use pilot `v1_32k` tokenizer**, or compare token counts with the wrong version. Model context 2048; https://huggingface.co/ibnsina-llm/ibnsina-3b-checkpoints
- Persian LLM Token Bench repository: https://github.com/abebr/persian-llm-token-bench, limited-size demo results; **treat as small, uncontrolled third-party evaluation, not authoritative full-domain ranking**. Claims Gemma2 vs Mistral 3× are conditional on its short sample and versions; need reproducibility/real dataset.
- Hazm, Parsivar normalizers: do not normalize indiscriminately; some remove vowel marks or rewrite digits, which changes cited source and security identifiers. https://github.com/ICTRC/Parsivar/blob/master/parsivar/normalizer.py

## Linguistic and security-specific acceptance gates
- Unicode: Arabic Yeh U+064A vs Persian Yeh U+06CC, Arabic Kaf U+0643 vs Persian Keheh U+06A9, ZWNJ U+200C, tatweel, diacritics, Arabic/Persian/Latin digits, right-to-left marks, mixed-script text; preserve semantics and reversible mapping.
- Morphology: `می‌روم`, `نمی‌توانستیم`, `کتاب‌هایمان`, `آسیب‌پذیری‌ها`, compounds, colloquial and formal differences, compound Persian-Arabic terms.
- Domains: Persian natural language, English standards, command lines, IPv4/IPv6, CIDR, CVE-YYYY-NNNN, URLs, OS paths, JSON/YAML, network interface names and tool invocations. **Normalize prose only; preserve code, hashes, IDs, commands and raw evidence exactly.**
- Bidirectional: parallel EN/FA technical texts and aligned terms; check inverse language effect, English/code degradation and language-switch task prompts.
- Metrics: tokens per word (declare splitting convention), chars per token, UTF-8 bytes per token, ZWNJ penalty, morphology boundary F1, roundtrip error rate, sequence length p50/p95/p99 by domain, vocab utilization, low-frequency fragmentation, total embedding weight bytes, inference TTFT/TPS/peak RSS, trained-model held-out metrics, regression tests on English/code.
- Leakage: train/validation/holdout source splits by documents and time, avoid near-duplicate leakage, pin tokenizer revisions, corpus hashes, version changes and authorization.
- Model integration: new token IDs must have correctly initialized embeddings and tied/untied LM head, call resize/reinitialize as appropriate; LoRA on attention alone does not teach new embedding IDs; require continued embedding training, replay, eval.
- Quantified acceptance gates are to be **pre-registered** after corpus baseline, not invented post hoc; do not claim 20% improvement without actual protocol results.

## First experimental design (not yet executed)
1. Select real Persian books/LDI documents and paired English network/security text; add natural mixed-script conversation and source logs. Curate document-level train/dev/test with provenance.
2. Use verified local tokenizer implementations from LFM3, MiniCPM5, Qwen3.5, Gemma and IbnSina; compare on one frozen corpus. Never equate corpus-specific fertility with generative capability.
3. Train BPE32k/BPE64k/Unigram32k, MorphBPE/Parity-BPE if official implementation valid, balanced Persian–English–code data. Keep vocabulary and sampling controlled.
4. Only after intrinsic metrics: train equal-capacity 100–300M pilot model from scratch OR adapt a compatible small pretrained baseline with vocabulary changes plus embedding training. Measure retained English/code ability.
5. Make decision with cost/quality tradeoffs, reproducibility, rollback and security gate. Keep the main model and training pipeline unchanged until controlled study succeeds.

Public note: tokenizer design and comparisons remain an E0 research plan; no complete experiment is claimed.
