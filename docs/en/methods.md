---
doc_id: DEC-DOC-004
language: en
title: "Research methods and evidence"
version: 0.1.0
date: 2026-11-12
evidence_level: E0
publication_status: public-research-draft
---

# Research method and evidence model

## Evidence grades and claims

| Level | Evidence | Permissible claim |
|---|---|---|
| E0 | Theory, prior art, architecture, pre-registered design | Hypothesis / conceptual feasibility |
| E1 | Narrow prototype or controlled synthetic experiment | Initial technical feasibility in tested configuration |
| E2 | Initial real-world deployment data | Limited operational findings; not generalized |
| E3 | Repeated, predefined tests on declared environment | Repeatable claims only within measured scope |

A cited paper is strong evidence **for the paper's own experimental configuration**, not automatically E1/E2 DEC evidence. E1 requires executing DEC's own chosen variant. Record negative results and deviations.

## Research-before-design cycle

Problem definition → inspect prior project decisions → primary-source research → candidate taxonomy → compare alternatives → prototype/baseline → measurement and independent review → decision record (ADR) → staged integration. Reject custom mechanisms when an existing mature solution can meet the same requirements with lower risk.

## Review hierarchy and confidence

Start with publications of original methods (ICML/ICLR/ACL etc.), official model cards, repository source, pinned commits and official runtime documentation. Independently verify claims of performance, licensing, model-language support and hardware compatibility. Mark unreviewed links explicitly; citation **does not** imply reproduction.

## Experimental validity controls

Pre-register task sets and evaluation rubrics before model tuning; isolate development, validation and held-out test data; make Persian technical questions, mixed-language retrieval, contradiction, abstention and failure injection explicit. Use at least one domain expert/reference adjudicator for high-consequence claims. Measure judge agreement if using an LLM-as-judge.

## Decision record format

Each ADR: question; owner/authority; options and counterfactual; evidence links, versions and date; chosen/rejected choices; expected effect; safety/quality gate; rollback; open uncertainty. An ADR is **not** proof of a running implementation.

## Data inclusion and publication

Publish only independently licensed and non-sensitive fixtures. Do not rehost proprietary books/standards, unpublished model weights, private infrastructure descriptions, secrets or raw internal logs. Public citations may link to original external sources without copying full protected content.
