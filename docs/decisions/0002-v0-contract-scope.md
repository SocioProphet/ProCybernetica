# ADR-0002: v0 Contract Scope

Status: proposed

Date: 2026-04-29

## Context

The principal ProCybernetica blueprint corpus has been captured into the repository. The next step is reconciliation: turning captured doctrine into a canonical v0 contract set before runtime implementation expands.

The captured sources agree on a stable outer doctrine: Fractal Nodes, typed envelopes, replay, provenance, promotion law, repository constitutions, Genesis/Inception, secure mesh coordination, and autonomic constitution.

## Decision

v0 should focus on a minimal but complete constitutional loop:

1. identify a node;
2. validate envelopes;
3. record lifecycle transitions;
4. emit events and provenance;
5. replay an episode;
6. evaluate results;
7. issue a promotion or quarantine decision;
8. provide public-safe fixtures and conformance tests.

v0 should not attempt to implement the full mesh, full dashboard, full ontology layer, or full learning mesh before this loop is stable.

## Canonical v0 schema set

The proposed v0 schema set is:

- `node_descriptor.schema.json`
- `artifact_envelope.schema.json`
- `policy_envelope.schema.json`
- `command_envelope.schema.json`
- `delegation_envelope.schema.json`
- `observation_envelope.schema.json`
- `status_envelope.schema.json`
- `trace_event.schema.json`
- `transition_record.schema.json`
- `replay_envelope.schema.json`
- `evaluation_result.schema.json`
- `promotion_decision.schema.json`
- `incident_report.schema.json`
- `claim.schema.json`
- `provenance_record.schema.json`
- `capability_descriptor.schema.json`

Genesis/Inception and mesh/autonomic schemas should be captured in v0 docs and may be added as v0.1/v0.2 schema groups if capacity permits.

## Canonical v0 profiles

The proposed v0 profile set is:

- `controlplane_state_machine.yaml`
- `promotion_policy.example.yaml`
- `bt_semantic_profile.yaml`

K3/Inception lifecycle should be added as a separate profile after the base node lifecycle is reconciled.

## Lifecycle scope

Use the generic Fractal Node lifecycle for v0:

- `unconfigured`
- `configured`
- `inactive`
- `active`
- `degraded`
- `recovery`
- `quarantined`
- `retired`
- `finalized`

Keep twin lifecycle separate:

- `draft`
- `candidate`
- `ready`
- `executing`
- `paused`
- `quarantined`
- `revoked`
- `archived`

## Promotion decision vocabulary

Use these proposed v0 decisions:

- `reject`
- `shadow-only`
- `limited-authority`
- `full-promotion`
- `quarantine`
- `manual-review`
- `rollback-required`
- `revoke-authority`

## Consequences

This makes v0 small enough to implement, test, and publish while remaining faithful to the blueprint.

It also prevents the project from prematurely expanding into broad runtime code before public contracts are stable.

## Open questions

- Should `finalized` and `retired` both remain in v0 node lifecycle?
- Should rollback/revoke remain in `promotion_decision` or move into `incident_report` / `constitutional_verdict`?
- Should Genesis/Inception schemas enter v0 or v0.1?
- Should the Python package name remain `procyber` or become `procybernetica`?

## Source basis

See:

- `docs/reconciliation/SCHEMA_PROFILE_RECONCILIATION.md`
- `docs/source-captures/PROPHET_ARCHITECTURE_SPECIFICATION_CAPTURE.md`
- `docs/source-captures/EXECUTABLE_SPECIFICATION_PACK_CAPTURE.md`
- `docs/source-captures/REFERENCE_IMPLEMENTATION_KIT_CAPTURE.md`
- `docs/source-captures/BOOK_XI_IMPLEMENTATION_PRACTICUM_CAPTURE.md`
