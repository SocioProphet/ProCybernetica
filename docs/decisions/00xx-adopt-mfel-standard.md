# Decision: Adopt SP-STD-MFEL-0001 Metadata Forensics and Epistemic Learning

Status: accepted v0.1  
Date: 2026-05-15  
Issue: #52  
Decision scope: public-safe MFEL standard, schemas, examples, and test harness

## Context

ProCybernetica needs a public standard for learning from metadata-forensics and epistemic-threat artifacts without turning local diagnostics, sanitized metadata, or rhetorical pattern fixtures into unsupported claims.

The motivating cases include macOS metadata artifacts such as Core Spotlight plist diagnostics, Notes Spotlight indexing, FileProvider/iCloud/CloudKit churn, CoreSuggestions adjacency, SpotlightKnowledge processing, boot/reset seams, kernel-panic seams, and microstackshot/resource-pressure summaries. The same discipline is needed for epistemic-threat artifacts such as QAnon-style anti-verification rhetoric and self-sealing narrative construction.

These artifacts are useful for learning and governance only if they preserve the difference between observation, derivation, interpretation, hypothesis, and prohibited conclusion.

## Decision

Adopt SP-STD-MFEL-0001 as a public-safe standard under:

```text
docs/standards/SP-STD-MFEL-0001-metadata-forensics-epistemic-learning.md
```

Adopt the isolated schema namespace:

```text
schemas/mfel/*
```

Initial schemas:

- `schemas/mfel/observation.schema.json`
- `schemas/mfel/hypothesis.schema.json`
- `schemas/mfel/evidence-graph.schema.json`

Initial examples:

- `examples/mfel/notes-spotlight-indexing.sanitized.yaml`
- `examples/mfel/corespotlight-plist.sanitized.yaml`
- `examples/mfel/qanon-rhetorical-construction.sanitized.yaml`

Initial validation:

- `tests/mfel/test_schema_examples.py`

## Rationale

MFEL is a case-analysis and evidence-discipline standard. It is not a core controlplane envelope family and does not need to wait for the unresolved `governance-fabric` versus `cybernetic-governance` namespace decision recorded in `docs/reconciliation/SCHEMA_PROFILE_RECONCILIATION.md`.

The isolated `schemas/mfel/*` namespace lets MFEL proceed without mutating unresolved governance schemas or certificate-family schemas.

The five-layer model is adopted because it prevents common evidence errors:

- treating a local metadata observation as a compromise finding;
- treating a derived correlation as actor attribution;
- treating interpretation as evidence;
- treating a hypothesis as a conclusion;
- omitting the conclusions the public record does not license.

## Consequences

MFEL cases must include:

- observed facts;
- derived facts;
- interpretations;
- hypotheses;
- prohibited conclusions;
- redaction boundary;
- negative evidence;
- missing evidence;
- non-claims.

Suspicious and high-risk hypotheses must include `negative_evidence` and `missing_evidence`.

Unsupported actor attribution must fail validation.

Public examples must remain sanitized or synthetic. They must not contain raw private logs, private note content, account identifiers, device identifiers, handles, group names, or private messages.

## Alternatives considered

### Encode MFEL into core governance schemas immediately

Rejected for v0.1. Core governance namespace decisions are still unresolved. MFEL should not force those decisions.

### Publish playbooks without schemas

Rejected. Playbooks alone would not enforce layer separation, missing-evidence discipline, or unsupported-attribution rejection.

### Delay MFEL until full schema freeze

Rejected. MFEL is independent enough to proceed as a separate namespace, and it directly supports public evidence discipline.

## Non-claims

This decision does not claim live endpoint telemetry, incident status, actor attribution, compromise finding, surveillance capability, production runtime readiness, or model-training authorization.

It adopts a public-safe standard and validation lane for disciplined case learning.
