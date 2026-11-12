# Research publication changelog / تاریخچه انتشار پژوهش

[English](CHANGELOG.md) · [فارسی](CHANGELOG.fa.md)

## 0.2.5 — 2026-11-12

- User rejected previous two-question model evaluation; publish a new 20-question per model (10 FA, 10 EN) all-general benchmark after verified full loading and explicit warm-up.
- Tested 3 instruction models, all 60 calls succeeded; retain 60 full answers, reference cases, per-language scores, CPU RSS and post-warm-up timings.
- Results are scoped E1 first-pass review; model selection and DEC architecture tests remain pending.

## 0.2.4 — 2026-11-12

- Add bilingual model-only CPU preflight report for four locally tested weight families, verified hashes, tool versions, narrow method and negative findings.
- MiniCPM5-1B and Qwen3.5-0.8B official/traceable GGUF files installed in isolated model research storage, without modifying running inference services.
- E1 applies only to model load/inference feasibility; DEC remains E0, no backbone accepted.

## 0.2.3 — 2026-11-12

- P0 execution **started**: controlled read-only existing LDI integration smoke produced six successful API responses with no corpus mutation.
- WP-002/WP-003 now in progress; P0 gate not accepted. Published bilingual sanitized progress document; DEC performance remains E0.
- Public roadmap activity states require an explicit evidence link.

## 0.2.2 — 2026-11-12

- Align provisional phase durations with person-day capacity assumptions: P0 5-7, P1A 4-6, P1B 6-8, P1C 6-8, conditional P2 10-14 and P3 12-20 weeks. No date commitments or test-status changes.

## 0.2.1 — 2026-11-12

- Correct Windows encoding corruption in the Persian roadmap, 35 public GitHub issue titles/bodies and 8 milestone names.
- Add actual Unicode integrity checks and link every work package to its tracking issue.
- All 39 historical research IDs remain mapped; experiments unchanged, E0.

## 0.2.0 — 2026-11-12

- Detailed English/Persian roadmap: 35 work packages, mapped to 39 historical task identifiers, phased dependencies, provisional effort, outputs, acceptance tests, 8 gates and 12 risks.
- Single bilingual JSON roadmap source, reproducible renderer and roadmap integrity validation in CI.
- All cognitive experiments and implementation remain planned or deferred (E0).

## 0.1.0 — 2026-11-12

- Initial public, sanitized **E0** DEC research dossier.
- Bilingual scientific problem, architecture, literature, hypotheses, reproducibility, planned experiments and current results (none).
- Publication/IP rights policy, collaboration guide, provenance declaration and machine-readable bilingual indices.
- The separately governed AI-LAB laboratory remains private; there was **no DEC execution, software release or invention registration**.
