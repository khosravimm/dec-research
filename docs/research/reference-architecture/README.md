# DEC-CRA v1 — Reference Architecture

Architecture-neutral logical model of DEC's five cognitive capabilities, supporting boundaries and controlled comparison of **Unified**, **Ecosystem** and **Hybrid**.

- [فارسی — معماری مرجع کامل](DEC_CRA_REFERENCE_ARCHITECTURE_FA.md)
- [English — overview](REFERENCE_ARCHITECTURE_EN.md)
- [Machine-readable contracts (JSON Schema)](CONTRACTS.json)
- [Synthetic contract fixtures](SYNTHETIC_CONTRACT_EXAMPLES.json)
- [Requirement/WP traceability](CAPABILITY_IDS.json)
- [Experimental validation plan](VALIDATION_PLAN.md)
- [Decision record](ADR-002-REFERENCE-ARCHITECTURE.md)
- [QA output](QA_RESULTS.json)

## Local self-test

Requires Python 3 and jsonschema >=4.18.

```bash
python3 -m pip install jsonschema
python3 validate_reference.py
```

Passing this test validates the envelope schema, negative fixtures, bounded state transitions, budgets and memory compatibility on synthetic examples. It does **not** validate DEC model/architecture behavior. No system implementation is included.
