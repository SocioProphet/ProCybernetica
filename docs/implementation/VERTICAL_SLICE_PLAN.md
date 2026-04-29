# Vertical Slice Implementation Plan

Source basis: `docs/source-captures/BOOK_XI_IMPLEMENTATION_PRACTICUM_CAPTURE.md`.

Status: public implementation plan.

## Principle

The first code path is not an agent runtime.

The first code path is the lawful claim/event/provenance path with schema validation and public-safe fixtures.

## Slice A — Ingest to canonical claims

Goal: one artifact becomes lawful knowledge objects.

Required schemas:

- `artifact_envelope.schema.json`
- `claim.schema.json`
- `provenance_record.schema.json`
- `event_envelope.schema.json` or `trace_event.schema.json`

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
- claim status remains `candidate` or `hypothesis` until validation evidence exists.

## Slice B — Query to justified answer

Goal: one query becomes an answer plus machine-readable justification.

Required schemas:

- `claim.schema.json`
- `observation_envelope.schema.json`
- `artifact_envelope.schema.json`
- future `justification_graph.schema.json`

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

Required fixtures:

- command;
- capability descriptor;
- policy gate;
- denied unsafe action;
- approved bounded action.

Required tests:

- side-effect command requires policy refs;
- capability declares reversibility and approval requirement;
- unsafe call is rejected.

## Slice D — Replay, promotion, and attestation

Goal: a candidate change can be evaluated, replayed, and promoted or quarantined.

Required schemas:

- `replay_envelope.schema.json`
- `evaluation_result.schema.json`
- `promotion_decision.schema.json`
- `artifact_envelope.schema.json`
- future `attestation_statement.schema.json`

Required fixtures:

- replay manifest;
- event log sample;
- evaluation result;
- promotion decision.

Required tests:

- replay manifest validates;
- failed evaluation cannot produce full promotion;
- evidence refs are required;
- quarantine preserves evidence refs.

## Slice E — Mesh coordination

Goal: several lawful nodes coordinate without losing identity, relation, policy, or provenance.

Required schemas:

- `node_descriptor.schema.json`
- `delegation_envelope.schema.json`
- `status_envelope.schema.json`
- `trace_event.schema.json`
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
3. Add synthetic fixtures for Slice A.
4. Add schema validation CLI/tests.
5. Implement minimal claim/event/provenance validation path.
6. Extend to Slice B only after Slice A passes.

## Public-first rule

All fixtures and tests should be public. Use synthetic data where needed. Do not wait for private data to build the public reference path.
