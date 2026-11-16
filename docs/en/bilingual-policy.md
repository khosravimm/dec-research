---
doc_id: DEC-DOC-BILINGUAL-POLICY
language: en
title: "Bilingual documentation: genuine semantic parity and publication quality"
version: 1.0.0
date: 2026-11-16
evidence_level: E0
publication_status: public-research-draft
---

# Bilingual documentation policy — English and Persian

DEC's public technical documentation must be **substantively bilingual**. A Persian suffix, duplicated English file, translated heading, or short Persian abstract beside a complete English dossier is **not** an acceptable full translation.

## Editorial requirements

1. Every public prose dossier requires a real Persian and English equivalent, with direct cross-links. The approved Persian mission is authoritative; the English charter must preserve it faithfully.
2. Both versions must cover the same hypotheses, facts, quantitative findings, uncertainty qualifiers, tables, safety/operational constraints, citations, conclusions and E0–E3 evidence distinctions. Preserve negative results and version history.
3. Translate technical explanations, prose, decision rationale, table headers and non-code cell descriptions. Leave exact machine keys, source URLs, model/checkpoint names, API symbols, command lines, code, metric identifiers, quoted prompts and hashes unchanged where translation would change the artifact.
4. For catalogues, compare the model entries **one-to-one**, including source references and material caveats; a shorter narrative overview is allowed only when clearly labeled as a summary and a complete language counterpart is linked.
5. Changes affecting a scientific claim, architecture decision, contract semantics or acceptance criteria must be applied to both languages in the same commit. Generated reports retain a single machine-readable source and two separately validated renderers.
6. Human semantic review should check mistranslations, dropped qualifiers, numerical units and conflicting source claims. Automated scripts are a guardrail, not a replacement for expert editorial review.

## Automated controls and known limitations

The CI runs [the bilingual audit](../../tools/validate_bilingual_content.py) alongside the existing [public document validator](../../tools/validate_public_docs.py). It detects missing pairs, mostly English Persian prose, inconsistent section and table structure in the core architecture, missing source URLs and unregistered research documents. The JSON report is preserved at [bilingual-audit-20261116.json](../../research/bilingual-audit-20261116.json).

A passing audit is **structural/lexical**; it cannot prove sentence-by-sentence semantic equivalence. Documents dominated by raw English evaluation prompts, field identifiers, code and citations may have lower Persian-character ratios despite valid Persian explanations. Such exceptions require explicit editorial review, not automatic translation or fabricated completion claims.

## Change acceptance

Before merging a new scientific document: verify English/Persian navigation, factual and numeric equivalence, primary sources, link resolution, machine/contract identifier stability and the absence of new security-sensitive content. Retain an audit note or reviewer record where substantive interpretation was checked.
