# Source Capture: ProCybernetica Volume IV Reference Implementation Kit

Source title: `ProCybernetica_Volume_IV_Reference_Implementation_Kit.pdf`

Drive source: https://drive.google.com/file/d/1r2eN2S5J4ojfzkNjrZqZ50i770kaeaMd

Capture purpose: preserve the current implementation-kit state from Drive so the repository can later build the reference runtime from an existing specification rather than inventing a new one.

## Document identity

Volume IV is titled `Reference Implementation Kit and Runtime Services`.

It is positioned as the runnable bridge from architectural law to executable controlplane behavior for the Prophet ecosystem.

The volume converts the constitutions of Volumes I through III into a functional reference kit: schemas, validators, supervisor service, repository adapter, replay harness, promotion gate, planner registry, and smoke tests.

The goal is not a finished platform. The goal is a lawful implementation skeleton that can be executed, audited, criticized, and extended.

## Implementation thesis

The central claim is that a cybernetic system is only as serious as its lawful runtime.

If envelopes are not validated, node transitions are not supervised, artifacts are not replayable, and promotion is not gated, then the system may be clever, but it is not governed.

The smallest operational subset must preserve:

- typed envelopes;
- schema bundle;
- lifecycle state machine;
- supervisor;
- promotion gate;
- repository adapter;
- replay harness;
- planner registration.

The implementation principle is to make architectural law visible all the way down to code.

## Kit architecture

The kit is organized so a reader can move from constitution to runtime without navigating a maze of abstractions.

The source divides the implementation into these layers:

| Layer | Purpose | Primary files |
| --- | --- | --- |
| schemas | Typed contract for consequential messages and state records | `schemas/*.schema.json` |
| profiles | Semantic pinning for lifecycle and behavior-tree interpretation | `profiles/*.yaml` |
| runtime package | Validators, supervisor, promotion gate, replay runner, repositories | `prophet_reference_kit/*` |
| examples | Pinned sample artifacts and event logs | `examples/*` |
| tests | Smoke validation and behavior checks | `tests/*` |

The implementation principle is fractal continuity. Repositories, agents, and planners do not get unrelated implementation philosophies. They share one lawful outer surface and can specialize internally.

## Schema bundle capture

The implementation kit defines a stable name-to-schema mapping and validation entry point.

The source schema map includes:

- `node_descriptor`;
- `artifact_envelope`;
- `policy_envelope`;
- `command_envelope`;
- `delegation_envelope`;
- `observation_envelope`;
- `status_envelope`;
- `replay_envelope`;
- `incident_report`;
- `evaluation_result`;
- `transition_record`;
- `promotion_decision`;
- `trace_event`.

The source makes a key doctrinal point: validation is not just input hygiene. It is the first operational expression of epistemic humility. The system does not know what a payload means unless the payload presents itself lawfully.

## Envelope roles

| Envelope | Runtime role | Failure if absent |
| --- | --- | --- |
| NodeDescriptor | Identity and admission contract | orphan nodes and unverifiable capabilities |
| CommandEnvelope | Authorized imperative action | unbounded side effects and unclear issuer |
| DelegationEnvelope | Bounded task transfer | implicit authority leakage |
| ReplayEnvelope | Pinned reconstruction manifest | debugging without evidence |
| PromotionDecision | Post-evaluation authority verdict | shadow promotion and untracked risk |

## Lifecycle algebra and supervisor service

The supervisor is the runtime organ that gives the controlplane a spine.

It maintains node descriptors, evaluates lifecycle events against the state machine profile, performs transitions, and records transition events as first-class evidence.

A node cannot quietly become active. It must pass through lawful transitions.

The source emphasizes that authority-tree and information-graph are different. Supervisor transitions act on the authority plane. Peer exchange does not silently rewrite authorization.

## Repository adapters and active memory

The reference kit includes a lightweight SQLite repository and JSONL event log.

These are not intended as high-scale production stores. Their purpose is to preserve constitutional semantics while remaining runnable in a notebook, workstation, or CI job.

Repositories are not passive buckets. They are constitutional organs that preserve lawful memory classes and retrieval surfaces.

The SQLite adapter persists node descriptors and artifact envelopes. The JSONL event log preserves chronological execution evidence. Together they provide a minimal split between stateful memory and temporal trace.

## Replay harness

Replay is described as a decisive boundary. Without replay, errors become folklore. With replay, they become evidence.

The reference replay runner loads a replay manifest, pins an event log, reconstructs observed event types, and emits an evaluation result.

The source clarifies that the point is not narrow determinism. The point is replayability under declared conditions: version pins, context windows, policy bundles, and data references sufficient to interpret drift.

## Promotion gate and quarantine

The promotion gate consumes evaluation results, checks them against policy thresholds, and emits a typed decision:

- reject;
- shadow-only;
- limited-authority;
- full-promotion;
- quarantine.

This is the legal border between experimentation and operational trust.

Quarantine is not an embarrassing stopgap. It is constitutive. It halts a subject without deleting evidence of why it was halted.

## Planner registry

The kit does not implement all planners. It implements planner registration.

The purpose is to make planners nameable, inspectable, and bound to regimes and maximum authority.

Symbolic planners, behavior-tree executors, MPC modules, POMDP solvers, and learned proposal models can all enter the controlplane as declared instruments with known regimes and admission limits.

## CLI surface

The source describes a CLI exposing three baseline operations:

1. validate a payload against a schema;
2. run a state-machine demonstration;
3. execute replay-to-promotion demonstration.

These are not flashy demos. They prove that legal surfaces and runtime services are coupled.

The intended operator commands are:

```bash
python -m prophet_reference_kit.cli validate examples/node_descriptor.example.json --schema node_descriptor
python -m prophet_reference_kit.cli state-demo
python -m prophet_reference_kit.cli replay-demo
PYTHONPATH=. python -m unittest discover tests -v
```

## Deployment topologies

The same kit can inhabit:

- single-node laboratory setup;
- clustered service mesh;
- hybrid embodied edge deployment.

Across these topologies, transport and persistence may change. Typed envelopes, external supervision, replay evidence, and bounded promotion must not change.

## Anti-patterns and countermeasures

| Anti-pattern | Why dangerous | Countermeasure |
| --- | --- | --- |
| opaque side effects | state changes occur without replayable evidence | typed envelopes and event log |
| silent schema drift | nodes interpret payloads differently | schema bundle with canonical names |
| unversioned prompts or models | behavior cannot be traced to a pinned subject | replay manifest with version pins |
| planner without policy envelope | optimization outruns authority | promotion gate and planner registry |
| health without replay evidence | status becomes theater | incident-linked telemetry and replay |

## Current limits named by source

The source explicitly says Volume IV is not completion.

It does not yet provide:

- distributed consensus;
- remote attestation;
- policy compilation;
- high-volume telemetry ingestion;
- rich scenario simulation;
- formal temporal logic checks;
- deep planner implementations;
- domain-specific command vocabularies.

Those limits are deliberate. The reference kit should be small enough to audit and fork.

## File manifest captured from source

The source names this intended file set:

```text
README.md
examples/evaluation.example.json
examples/events.example.jsonl
examples/node_descriptor.example.json
examples/replay.example.json
profiles/bt_semantic_profile.yaml
profiles/controlplane_state_machine.yaml
profiles/promotion_policy.example.yaml
prophet_reference_kit/__init__.py
prophet_reference_kit/cli.py
prophet_reference_kit/controlplane/__init__.py
prophet_reference_kit/controlplane/promotion_gate.py
prophet_reference_kit/controlplane/state_machine.py
prophet_reference_kit/controlplane/supervisor.py
prophet_reference_kit/envelope_io.py
prophet_reference_kit/paths.py
prophet_reference_kit/planners/__init__.py
prophet_reference_kit/planners/registry.py
prophet_reference_kit/replay/__init__.py
prophet_reference_kit/replay/runner.py
prophet_reference_kit/repositories/__init__.py
prophet_reference_kit/repositories/event_log.py
prophet_reference_kit/repositories/sqlite_repo.py
prophet_reference_kit/schema_bundle.py
prophet_reference_kit/validate.py
prophet_reference_kit/version.py
pyproject.toml
schemas/artifact_envelope.schema.json
schemas/command_envelope.schema.json
schemas/delegation_envelope.schema.json
schemas/evaluation_result.schema.json
schemas/incident_report.schema.json
schemas/node_descriptor.schema.json
schemas/observation_envelope.schema.json
schemas/policy_envelope.schema.json
schemas/promotion_decision.schema.json
schemas/replay_envelope.schema.json
schemas/status_envelope.schema.json
schemas/trace_event.schema.json
schemas/transition_record.schema.json
sql/prophet_repository_ddl.sql
tests/test_replay_and_promotion.py
tests/test_state_machine.py
tests/test_validation.py
```

## Next implementation steps captured from source

- replace local repository with replicated adapters while preserving envelope law;
- add a controlplane service API using the same schema bundle and state machine;
- formalize planner plugin manifests and benchmark suites;
- extend replay into a scenario and red-team harness;
- introduce signatures, attestations, and stronger provenance for high-trust deployments;
- connect the implementation kit to later doctrine on cybernetic consciousness versus model fluency.

## Codification implications

This source should drive GitHub work after the source-capture phase:

1. Preserve the manifest and contracts as issue-backed implementation scope.
2. Avoid premature divergence in package naming, schema names, or CLI verbs unless deliberately chosen.
3. Build from the captured kit skeleton rather than inventing an unrelated runtime.
4. Keep reference implementation small, auditable, and doctrinally legible.
5. Treat code as executable capture of the existing doctrine, not as a replacement for source capture.

## Capture status

Captured into GitHub as structured source-state. This is not a replacement for the original Drive PDF. It is the repo-local capture used to make ProCybernetica self-contained enough to build from.
