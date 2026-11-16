# ADR-002 — Technology-neutral DEC Cognitive Reference Architecture
**Date:** 2026-11-16 | **Status:** Proposed for architecture baseline (E0); no production approval | **Supersedes:** none

## Context
The new project charter explicitly allows a unified learned model, an intelligent ecosystem, or a hybrid system. The prior architecture description implies a central controller with a swappable LLM and a future integrated model, but the research covers decisions, adaptive compute, memory, experts, cooperation and tool/evidence handling beyond the nine tested LLMs. A neutral reference is required to compare candidates without assuming a winner.

## Decision
Adopt DEC-CRA v1 as the **logical contract and experimental comparison baseline**:
- Five cognitive capabilities: Decision, Compute Allocation, Memory, Expertise, Collaboration.
- Supporting boundaries: Knowledge/LDI, Tool Execution, Independent Evidence/Verification, Audit and Evaluation.
- Explicit separation of cognitive state and evidence/event planes.
- Canonical, typed versioned contracts, budgeted finite step graph, model/adapter/cache compatibility, replayable trace.
- Three implementation mappings A Unified / B Ecosystem / C Hybrid. All retain the same semantics but may optimize their internal communication differently.
- Architectural and scientific status E0; benchmark E2 of existing LLMs does not decide the architecture.

## Alternatives considered
1. Model-first fixed architecture: rejected **as a premature default**, remains valid candidate A.
2. Agent-orchestration-only ecosystem: rejected **as exclusive mandate**, remains candidate B.
3. Hybrid-only: rejected as predetermined winner, remains candidate C.
4. No contracts and direct experimentation: rejected because comparisons and claims become incomparable; experimentation remains mandatory, now within a common envelope.

## Consequences
- Design can proceed with synthetic contract fixtures before selecting weights or runtime.
- Some models or learned representations cannot satisfy all contract fields internally; an auditable boundary adapter must provide the evidence/metadata envelope without falsely claiming internal introspection.
- Model/router choice, exact tokenizer, transport, data store and runtime remain open.
- Additional implementation cost for versioning and audit; benefit is reproducibility and architecture-neutral measurement.

## Risks / follow-up
- Risk: an external controller prototype could be mistaken for a final commitment to B. Mitigate via explicit A/B/C gates and labels.
- Risk: exposing latent state as if universally portable. Mitigate via compatibility fingerprints and bounded leases.
- Risk: false confidence in schema tests. Mitigate by separating contract success from end-to-end cognitive evaluation.
- Open roadmap issue: P3 label should be neutralized in machine-readable roadmap and bilingual derived docs without changing IDs or history.
- Publish the public design only after redacting machine paths, private data, and unverified vendor performance claims.

## Acceptance (ADR itself)
Reference diagrams, interface schema, threat model, minimum validation protocol and traceability to existing WP/RQ documented and checked. This is a reference approval, not completed model integration or system validation.
