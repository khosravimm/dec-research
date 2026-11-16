# DEC Cognitive Reference Architecture — v1 (English index)

Technology-neutral reference design for DEC's five cognitive capabilities and a fair comparison of **Unified**, **Ecosystem** and **Hybrid** options. The Persian and English documents must be semantically equivalent in coverage, design claims and evidence limitations; a translated filename or header is not sufficient.

| Subject | English | Persian |
|---|---|---|
| Full architecture | [Reference architecture](DEC_CRA_REFERENCE_ARCHITECTURE_EN.md) | [معماری مرجع](DEC_CRA_REFERENCE_ARCHITECTURE_FA.md) |
| Validation plan | [Validation plan](VALIDATION_PLAN.md) | [برنامهٔ آزمون](VALIDATION_PLAN_FA.md) |
| Architecture decision | [ADR-002](ADR-002-REFERENCE-ARCHITECTURE.md) | [ADR-002 فارسی](ADR-002-REFERENCE-ARCHITECTURE_FA.md) |
| Brief overview | [English summary](REFERENCE_ARCHITECTURE_EN.md) | — |

**Language-neutral machine artifacts:** [JSON Schema](CONTRACTS.json), [synthetic fixtures](SYNTHETIC_CONTRACT_EXAMPLES.json), [capability/WP index](CAPABILITY_IDS.json), [QA output](QA_RESULTS.json), [test runner](validate_reference.py).

Requires Python 3 and `jsonschema>=4.18`. `python3 validate_reference.py` tests the schema and synthetic invariants, **not the cognitive performance of a model**.

Identifiers, model names, JSON keys, code and research IDs remain unchanged across languages. Explanatory narrative, decision rationale, headings and non-code tables are localized.
