---
doc_id: DEC-DOC-013
language: en
title: "Security and public disclosure controls"
version: 0.1.0
date: 2026-11-12
evidence_level: E0
publication_status: public-research-draft
---

# Security and safe public disclosure

**DEC PoC trust model:** one local trusted cognitive domain and one active case at a time. Trusted specialists can share necessary domain knowledge and bounded latent state without imposing a separate heavyweight authorization request per tensor. Trust in the local orchestration components does **not** turn untrusted retrieved content into executable instructions.

## Boundary controls

External documents, imported LoRA weights, tools and model packages enter via a controlled source boundary; actions and data leaving the local domain require appropriate permission. Keep all credentials, tokens, key material, infrastructure hostnames/IPs, VPN profiles, raw monitoring logs, model training data without publication rights, security architecture of real institutions, secrets and collaborator confidential files **out of Git and out of Git history**.

Review all publication candidates before their first commit. Removing a secret in a later commit is not sufficient if it was ever public. Do not publish raw embeddings, latent states or cache dumps produced from sensitive inputs; their opaque shape is not privacy protection.

## Public report procedure

Use a GitHub Issue for **non-confidential** security concerns. For suspected sensitive disclosure, do not paste exploit payloads or secrets into public Issues. Request a private contact route using a generic issue without details. A formal vulnerability intake address is not available yet; do not invent one.

Future multiuser/multitask isolation is a separate post-PoC security project, not an implemented assurance.
