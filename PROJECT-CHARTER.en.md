# DEC Research — Official Project Charter and Mission

**Version:** 1.0 | **Scope amendment approved:** 16 November 2026 | **Status:** Normative project direction and basis for comparing architectural alternatives.

## Mission statement (owner-approved)

> Research, design, and evaluate an intelligent model or an efficient ecosystem capable of coordinating decision-making, compute allocation, memory, and diverse specializations through its core, while operating on limited resources and supporting Persian and technical tasks.

This is the semantic English translation of the approved Persian statement in [PROJECT-CHARTER.md](PROJECT-CHARTER.md); the Persian wording remains authoritative if interpretive differences arise.

## Scope and decision principles

- The outcome is **not predetermined to be a single standalone model**. A **unified model**, a **coordinated multi-model ecosystem**, and a **hybrid architecture** are all within the research scope.
- The "core" can be a learned internal mechanism, an ecosystem coordination core, or a division of responsibilities between the two. Its placement is decided by research and testing.
- Required measurable capabilities include decision/action selection; adaptive computation; working and long-term memory; specialist selection and composition; resource efficiency; Persian, English and technical task quality.
- Architectural selection must follow evidence E0–E3 and matched tasks, not vendor preference, an existing base model or a single benchmark.
- Benchmark data from a limited set of ready-made LLMs is operational evidence only and cannot replace evaluation of novel architectures, routers, memory or adapters.
- Selecting a base LFM model for training is a **subproject** choice, not a decision about the entire DEC architecture.
- Preserve the research portfolio: old and new models, memory models, different architectures, data/tokenizers, specialist models and model-composition methods.
- Research must lead to falsifiable hypotheses, implementable prototypes and acceptance criteria. Raise documented real constraints with practical alternatives; do not manufacture obstacles.

## Shared comparison criteria

Task completion and quality; decision confidence and errors; memory correctness and continuity; CPU/RAM/latency; scalability; component independence and updateability; Persian/English/code quality; observability and decision traceability; maintainability and total cost of ownership.

## Source precedence

1. [PROJECT-CHARTER.md](PROJECT-CHARTER.md) — authoritative Persian mission and project scope.
2. [ADR-001 English](ADR-001-MODEL-OR-ECOSYSTEM-20261116.en.md) / [Persian](ADR-001-MODEL-OR-ECOSYSTEM-20261116.md) — decision context and alternatives.
3. [Research documents](docs/research/) — catalogues and composition methods.
4. Curated scientific evidence and historical benchmarks, explicitly distinguished by evidence level.
5. GOV-002 collaboration principle — actionable research and avoidance of unsupported obstacles, subject to actual safety and tool constraints.

**Conflict rule:** Earlier statements that treat a single integrated model as the only possible DEC outcome are superseded by this amendment in scope decisions. Original experimental data and research history remain unchanged.
