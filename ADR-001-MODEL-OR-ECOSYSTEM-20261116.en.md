# ADR-001 — Architectural scope of DEC Research: Model OR Ecosystem

**Date:** 16 November 2026
**Status:** Accepted — the architectural options remain open; no architecture has yet been selected.
**Type:** Strategic scope and architecture decision
**Authority:** [Project charter](PROJECT-CHARTER.md) / [English translation](PROJECT-CHARTER.en.md)

## Context

Some prior DEC summaries implicitly narrowed the project to developing **one intelligent model**. This prematurely excluded coordinated multi-model and hybrid ecosystems without comparative evidence. The nine-model runtime benchmark was also overemphasized as a basis for evaluating all architecture research.

## Decision

The official mission is:

> Research, design, and evaluate an intelligent model or an efficient ecosystem capable of coordinating decision-making, compute allocation, memory, and diverse specializations through its core, while operating on limited resources and supporting Persian and technical tasks.

The following are **equally valid research options**:

1. **Unified model:** Internal mechanisms for decision, memory, specialized processing and adaptive compute.
2. **Intelligent ecosystem:** A coordinated collection of specialized models and components with a shared cognitive control core.
3. **Hybrid architecture:** Responsibility distributed between the model and its surrounding ecosystem.

## Rejected preconditions

- **Mandatory single unified model:** rejected as a predetermined choice before testing; it remains option 1.
- **Mandatory external orchestration only:** rejected for the same reason; it remains option 2.
- **Architectural decision solely from the nine ready-made LLM benchmark:** rejected. The benchmark remains useful for specific runtime decisions but does not test DEC's underlying architectural hypotheses.

## Consequences

- Continue independent research on adaptive computation, typed decisions, memory, expert/adapter routing, multi-model cooperation, CPU and quantization, Persian/tokenizer, LDI and agentic tool use.
- Prototyping and incremental optimization of each of the three options are permitted without premature lock-in.
- The final choice will follow pre-registered criteria and comparable experiments.
- Historical benchmarks and subproject decisions, including LFM training baselines, retain their original status and must not be promoted to system-wide architecture decisions.

## Acceptance

The mission must appear in the charter and project README, research must reference all three options, and the document must not claim unexecuted architectural experiments as successes.

**Language:** This is the full English counterpart of [ADR-001 Persian](ADR-001-MODEL-OR-ECOSYSTEM-20261116.md), with machine identifiers unchanged.
