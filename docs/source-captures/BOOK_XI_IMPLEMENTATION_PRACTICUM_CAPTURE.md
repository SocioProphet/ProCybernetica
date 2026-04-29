# Source Capture: ProCybernetica Book XI — Implementation Practicum

Source title: `ProCybernetica_Book_XI_Implementation_Practicum.pdf`

Drive source: https://drive.google.com/file/d/1t0z9YZm7oW3OOgUnAQdcEU3Vnqx1y7eG

Capture purpose: preserve the implementation-practicum blueprint inside GitHub so engineers and agents can build from the vertical-slice doctrine already present in the source corpus.

## Document identity

Book XI is titled `Implementation Practicum`.

The practicum converts earlier doctrine into worked vertical slices.

The reader is meant to learn how to make:

- one artifact become claims;
- one query become a justified answer;
- one plan become a safe side effect;
- one change become a promoted capability;
- many lawful nodes become a replayable mesh.

## Practicum stance

Book XI is deliberately procedural.

Earlier books provide theory, grammar, and constitutional doctrine. Book XI walks through end-to-end slices that can be implemented, tested, replayed, and evaluated.

It does not try to build the whole ecosystem at once. It isolates recurring slices:

- ingest;
- query;
- act;
- replay/promote;
- mesh-coordinate.

Each slice is small enough to implement and reason about, but rich enough to expose the architecture's invariants.

## Why practicum is necessary

A cybernetic course fails if it remains only descriptive.

The architecture matters only if a practitioner can build a minimal vertical slice that respects its laws.

Standards become useful here:

- JSON Schema gives validity language;
- managed lifecycles and executors make runtime progression explicit;
- policy bundles let law travel with the system;
- traces, metrics, and logs share correlation context;
- provenance and attestation make promotion auditable.

## Vertical Slice A — Ingest to canonical claims

Goal: one incoming artifact becomes lawful knowledge objects:

- stored evidence;
- candidate claims;
- mapped entities;
- validated claims;
- indexes;
- events;
- provenance.

Minimum durable objects:

- raw artifact;
- provenance record;
- candidate claims;
- committed claims;
- emitted events.

The source defines a `Claim` interface with:

- id;
- subject;
- predicate;
- object;
- status;
- ontology_ref;
- schema_ref;
- provenance_refs;
- derived_from;
- transaction_time.

Claim statuses include:

- candidate;
- validated;
- derived;
- hypothesis;
- stale;
- retracted.

Practicum law:

- every claim must have provenance;
- every claim must declare schema and ontology version;
- heuristic outputs enter as candidate or hypothesis rather than validated truth.

Implementation note: start boring on purpose. Use one relational database as source of truth for claims, events, policies, and evaluations; one object store for artifacts; one lexical index; one vector index; and graph projections generated from relational source.

## Vertical Slice B — Query to justified answer

Goal: a query becomes an answer plus machine-readable justification.

The justification is part of the answer contract, not decoration.

The query pipeline is explicitly hybrid:

1. normalize objective;
2. expand through mediator;
3. retrieve from lexical, graph, vector, and structured sources;
4. plan bounded reasoning steps;
5. execute processors under policy;
6. synthesize answer and explanation.

Key practicum lesson: confidence must never replace claim status.

A highly ranked answer candidate is not the same thing as a validated claim.

This distinction prevents elegant self-deception.

## Vertical Slice C — Plan to safe side effect

Goal: turn plans into external effects without allowing soft-lane proposals to become ungoverned actions.

The source defines a `CapabilityDescriptor` with:

- id;
- input_schema;
- output_schema;
- reversible;
- approval_required;
- policy_scope;
- external_system.

Processors reason. Capabilities act.

Mixing the two is how systems accidentally send nonsense to production systems.

Non-negotiables:

- capability gateways;
- idempotency keys;
- approval checks;
- policy gating;
- capability typing;
- observability.

## Vertical Slice D — Replay, promotion, and attestation

Goal: govern change.

A new prompt, rule, model, extractor, or processor becomes promotable only through replay, evidence, and attestation.

Replay means deterministic re-execution over a frozen corpus or trace set.

Evidence means metrics, diffs, operator notes, and failure-catalog comparisons.

Attestation records who built or approved the candidate, what inputs were used, and where the bundle was registered/logged.

Relevant standards:

- JSON Schema 2020-12;
- OPA bundles;
- Rekor transparency log;
- SLSA and in-toto provenance/layout concepts;
- OpenTelemetry trace context;
- SCITT transparency-service and receipt concepts.

Minimal promotion gate:

| Input | Evidence | Decision | Output |
| --- | --- | --- | --- |
| candidate bundle | replay score + regressions + policy diff | reject / quarantine / promote | new hard-lane version |
| new extractor | precision/recall drift + operator notes | sandbox or approve | processor release |
| new planner step | latency + policy violations + rollback proof | approve only if bounded | planner catalog update |

## Vertical Slice E — Mesh coordination

Goal: join several lawful nodes into one replayable mesh.

Identity, relation, policy, and observability must survive every hop.

A complete slice should demonstrate:

- one node ingests;
- another plans;
- a third explains;
- a fourth authorizes or actuates;
- every event preserves routing identity, replay key, policy context, and causal trace context.

Mesh completion criterion: a practicum slice is finished when many lawful nodes can coordinate, replay, and explain the same end-to-end case without losing identity, relation, policy, or provenance.

## Suggested reference implementation

The source names this minimal module map:

```text
schemas/
  claim.schema.json
  event.schema.json
  processor.schema.json
  capability.schema.json

core/
  claims/
  events/
  provenance/
  policy/
  runtime/
  truth_maintenance/

processors/
  extraction/
  retrieval/
  graph_traversal/
  rule_inference/
  llm_proposal/
  validation/
  explanation/

services/
  ingest/
  query/
  planner/
  mediator/
  capability_gateway/
  replay/
  evaluate/
  operator/
```

The source states: the first code to write is not an agent runtime. It is the schema pack plus claim/event/provenance path.

This is important for this repository because early runtime scaffolding should remain provisional until capture and reconciliation are complete.

## Exercises and lab prompts

The source proposes:

1. define one artifact schema, one claim schema, and one provenance object;
2. build minimal ingest slice producing candidate claims and one validated claim;
3. build justification graph for a query answer with provenance on every node;
4. create one policy gate blocking unsafe capability call;
5. add replay and compare two processor versions against the same corpus.

The point is not one massive demo. The point is to force every major doctrine to survive contact with an implementable slice.

## Codification implications

Book XI should drive:

- `schemas/claim.schema.json`;
- `schemas/event.schema.json`;
- `schemas/processor.schema.json`;
- `schemas/capability.schema.json`;
- claim/event/provenance core backlog;
- justified-answer contract;
- capability gateway design;
- replay/promotion/attestation path;
- mesh coordination vertical-slice tests;
- public practicum exercises.

## Capture status

Captured into GitHub as structured source-state. This is not a replacement for the Drive PDF. It records the practicum and vertical-slice implementation blueprint.
