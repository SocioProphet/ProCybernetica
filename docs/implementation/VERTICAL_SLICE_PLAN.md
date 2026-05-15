# Book XI Vertical Slice Implementation Plan

Source basis: `docs/source-captures/BOOK_XI_IMPLEMENTATION_PRACTICUM_CAPTURE.md`.

Status: public implementation plan.

## Principle

The first code path is not an agent runtime.

The first code path is the lawful claim/event/provenance path with schema validation and public-safe fixtures.

This plan assumes the stabilized v0 surface is available:

- v0 schemas and profiles are validated;
- Human Protection Layer reconciliation is complete;
- AgentPlane governance binding schemas are available for future proof-pack exhibits;
- proof-pack assurance schemas are available for future reviewer-facing packaging.

## Slice A — Ingest to canonical claims

Goal: one artifact becomes lawful knowledge objects.

Required schemas:

- `artifact_envelope.schema.json`
- `claim.schema.json`
- `provenance_record.schema.json`
- `event_envelope.schema.json`

Required fixtures:

- synthetic artifact envelope;
- candidate claim;
- validated claim;
- provenance record;
- ingest event.

Required tests:

- artifact validates;
- claim validates;
- provenance validates;
- event validates;
- every claim has provenance;
- every claim declares schema and ontology version;
- heuristic output enters as `candidate` or `hypothesis`;
- validated claim derives from candidate claim and cites provenance;
- event cites artifact and provenance references.

Implementation in #8:

- `tests/fixtures/book-xi/slice-a-ingest-to-claims.synthetic.json`
- `tools/cybernetic_governance/validate_book_xi_slice_a.py`
- `tests/test_book_xi_slice_a.py`
- Makefile targets `book-xi-slice-a-fixtures` and `book-xi-slice-a-ci`

## Slice B — Query to justified answer

Goal: one query becomes an answer plus machine-readable justification.

Required schemas:

- `claim.schema.json`
- `observation_envelope.schema.json`
- `artifact_envelope.schema.json`
- future `justification_graph.schema.json`
- proof-pack artifact-entry schema for reviewer-facing citation packets

Required fixtures:

- query observation;
- retrieved claims;
- answer artifact;
- justification graph fixture.

Required tests:

- answer has supporting claims;
- evidence references are preserved;
- confidence does not replace claim status.

## Slice C — Plan to safe side effect

Goal: soft-lane plan becomes bounded action only through capability gateway.

Required schemas:

- `command_envelope.schema.json`
- `capability_descriptor.schema.json`
- `policy_envelope.schema.json`
- `transition_record.schema.json`
- Human Protection Layer status/trust-surface doctrine
- AgentPlane action-dispatch/tool-grant schemas where AgentPlane is involved

Required fixtures:

- command;
- capability descriptor;
- policy gate;
- denied unsafe action;
- approved bounded action.

Required tests:

- side-effect command requires policy refs;
- capability declares reversibility and approval requirement;
- unsafe call is rejected;
- human-impacting actions respect HPL policy-status boundaries.

## Slice D — Replay, promotion, and attestation

Goal: a candidate change can be evaluated, replayed, and promoted or quarantined.

Required schemas:

- `replay_envelope.schema.json`
- `evaluation_result.schema.json`
- `promotion_decision.schema.json`
- `artifact_envelope.schema.json`
- certificate v1.3 base schema;
- proof-pack assurance schemas;
- AgentPlane proof-pack exhibit schema where run capsules are involved.

Required fixtures:

- replay manifest;
- event log sample;
- evaluation result;
- promotion decision;
- proof-pack scorecard or disposition fixture.

Required tests:

- replay manifest validates;
- failed evaluation cannot produce full promotion;
- evidence refs are required;
- quarantine preserves evidence refs;
- proof packs cite lower-level evidence rather than becoming raw evidence stores.

## Slice E — Mesh coordination

Goal: several lawful nodes coordinate without losing identity, relation, policy, or provenance.

Required schemas:

- `node_descriptor.schema.json`
- `delegation_envelope.schema.json`
- `status_envelope.schema.json`
- `trace_event.schema.json`
- dependency-control transport channel schema;
- future mesh schemas from Volumes VI–VIII.

Required fixtures:

- repository node;
- planner node;
- operator node;
- delegation envelope;
- status event;
- operator review event.

Required tests:

- every node has descriptor;
- delegation has scope and authority;
- status reports preserve lifecycle and health;
- trace can reconstruct the multi-node flow.

## Implementation order

1. Complete v0 schema family.
2. Complete v0 profiles.
3. Reconcile HPL and publication boundaries.
4. Add synthetic fixtures for Slice A.
5. Add schema validation CLI/tests.
6. Implement minimal claim/event/provenance validation path.
7. Extend to Slice B only after Slice A passes.

## Public-first rule

All fixtures and tests should be public. Use synthetic data where needed. Do not wait for private data to build the public reference path.

## Non-claims

This plan does not implement a generic agent runtime, query runtime, planner runtime, capability gateway, replay service, mesh coordination runtime, database, object store, lexical index, vector index, or graph database.