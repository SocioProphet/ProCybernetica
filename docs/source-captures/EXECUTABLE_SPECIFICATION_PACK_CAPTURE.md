# Source Capture: ProCybernetica Volume III — Executable Specification Pack and Conformance Law

Source title: `ProCybernetica_Volume_III_Executable_Specification_Pack.pdf`

Drive source: https://drive.google.com/file/d/1NBf9rTsm8wolTn9JPS_JblMjeqrhy7QO

Capture purpose: preserve the executable specification and conformance-law state from Drive so the public repository can build from the existing source pack rather than inventing contracts ad hoc.

## Document identity

Volume III is titled `Executable Specification Pack and Conformance Law` for the Prophet Ecosystem, Controlplane, ProCybernetica, and EpiCybernetica.

It is prepared as the executable companion to Volume I and Volume II.

It converts architectural doctrine into schemas, profiles, repository law, replay law, and promotion law.

Date: March 7, 2026.

## Abstract capture

Volume I established historical and conceptual lineage. Volume II established normative architecture law through the Fractal Node Contract, Prophet controlplane, and EpiCybernetica loop.

Volume III closes the operational gap by defining machine-readable artifacts, runtime profiles, repository constitutions, conformance criteria, and promotion workflows that convert the theory into an executable engineering program.

The point is not to invent another software stack. It is to legislate a stable contract within which many stacks, planners, repositories, and embodied systems can interoperate without surrendering observability, authority, epistemic discipline, or reversibility.

## Operational thesis

A cybernetic system becomes trustworthy only when its memory, authority, policy, planning, and learning all compile into explicit artifacts that can be validated before execution, inspected during execution, and replayed after execution.

## Scope

This volume applies to every node class in the Prophet ecosystem:

- repositories;
- agents;
- process runners;
- planners;
- executors;
- sensors;
- gateways;
- operator interfaces;
- robots.

A node is any bounded unit of observation, memory, value judgment, behavior generation, or actuation that participates in the authority plane, information plane, or epistemic plane.

## Normative rules captured

1. Every behavior-changing interaction must be represented by a typed envelope with stable identifiers and timestamps.
2. Every node must expose a declared lifecycle state and be externally supervisable.
3. Every durable write must carry provenance metadata sufficient for replay and post-incident review.
4. Every learning update must be bounded by explicit policy and promotion law.
5. Every production capability must pass through replay or shadow evidence before unrestricted deployment.

## Why machine-readable law is necessary

Architectural prose explains intention. Schema and profile law constrain actual behavior.

The source identifies quiet erosion of contract boundaries as a core failure mode:

- planner returns richer objects than expected;
- repository stores context without provenance;
- model update is promoted because it looks better on one benchmark while increasing operator burden;
- behavior changes without a formal admission path.

These are failures of law, not merely failures of code.

## Conformance classes

| Class | Name | Minimum obligations | Typical subjects |
| --- | --- | --- | --- |
| C0 | Schema conformant | validates envelope schemas; emits IDs and timestamps | offline tools, low-risk utilities |
| C1 | Supervised node | lifecycle, status emission, provenance writes, policy refs | repositories, agents, services |
| C2 | Replayable node | deterministic or best-effort replay bundle, pinned dependencies | planners, evaluators, process runners |
| C3 | Production node | replay, shadow evidence, incident hooks, rollback route | live operators, high-authority agents |
| C4 | Safety-critical embodiment | quarantine semantics, guardrails, formal promotion gates | robots, financial/physical actuators |

## Universal machine model and lifecycle algebra

The Fractal Node Contract becomes executable as repeated functional strata:

- identity and lifecycle;
- interfaces and command vocabulary;
- world model and belief state;
- value judgment;
- behavior generation;
- execution and safety guard;
- memory and provenance;
- learning hooks;
- observability.

Lifecycle states are legal states in a supervised automaton. No node changes state by private declaration. The controlplane grants transitions based on policy, health, and evidence.

## Lifecycle rules

1. A node in active state must emit status envelopes at declared cadence.
2. A degraded node must either enter recovery or receive supervisor waiver within a bounded interval.
3. A quarantined node loses all execution authority except explicitly permitted diagnostic verbs.
4. A retired node remains replayable for the retention interval of its incident and promotion history.

## Three-plane architecture

Volume III preserves the distinction between:

- authority tree;
- information graph;
- epistemic plane.

The controlplane controls authority transitions, not truth by fiat.

This prevents both over-centralization and swarm anarchy. The epistemic plane ensures memory is neither erased by authority nor mistaken for truth merely because it exists.

## Envelope family

The canonical envelope family is the spine of the executable specification:

- NodeDescriptor;
- PolicyEnvelope;
- ArtifactEnvelope;
- CommandEnvelope;
- DelegationEnvelope;
- ObservationEnvelope;
- StatusEnvelope;
- ReplayEnvelope;
- IncidentReport;
- EvaluationResult.

The outer envelope family should remain stable for years because tooling, repositories, and conformance harnesses depend on that stability.

## NodeDescriptor capture

NodeDescriptor is the legal identity card of a node.

It fixes:

- class;
- level;
- embodiment;
- lifecycle state;
- parent authority;
- peer groups;
- capabilities;
- command vocabulary;
- resource budget;
- interfaces;
- policy references;
- provenance.

Without a valid NodeDescriptor, a component may exist in source code or container registry but does not yet exist constitutionally inside Prophet.

## ArtifactEnvelope capture

Artifacts are where systems often lose epistemic discipline.

ArtifactEnvelope requires:

- identity;
- type;
- media type;
- creation time;
- producer node;
- subject refs;
- hash;
- storage URI;
- labels;
- confidence;
- policy refs;
- provenance;
- retention class.

The artifact store is not a file share. It is an evidence organ.

## Command and Delegation capture

A command is an authority-bearing event, not just a function call.

CommandEnvelope represents directed action with issuer, receiver, verb, parameters, constraints, deadlines, expected artifacts, and policy references.

DelegationEnvelope transfers bounded authority with scope, rollback ownership, cost/risk ceilings, required artifacts, and explanation level.

Many planner bugs are actually delegation bugs: work is handed off without clear authority budget, rollback owner, or typed expectations.

## Observation, Status, Replay, Incident, Evaluation

Observation and Status close the online loop.

Replay, Incident, and Evaluation close the offline and governance loops.

Together they make the system falsifiable: what came in, what was believed, what happened, why it happened, and whether the result satisfies promotion law.

Replayability is first-class. The moment a node gains consequential authority, it must gain the ability to explain and replay.

## Repository constitutions

Repository law is where cybernetic architecture becomes more than orchestration.

Each repository class is a node with:

- command vocabulary;
- policy references;
- retention doctrine;
- freshness doctrine;
- incident hooks.

Repository mesh exists because not all memory is the same.

Volume III includes reference DDL for:

- node_registry;
- artifact_store;
- policy_registry;
- event_log;
- replay_manifest;
- incident_log;
- evaluation_run;
- trust_registry;
- semantic_entity;
- semantic_relation;
- memory_invalidation.

## Planning allocation

Planner methods are allocated by horizon and uncertainty:

- symbolic planning for strategic/supervisory horizons;
- belief-space reasoning for uncertain task horizons;
- behavior trees for execution orchestration and recovery;
- MPC/local optimizers for primitive/actuator horizons;
- learned policies and VLA models as priors, proposal generators, or local controllers inside policy and safety envelopes.

## Behavior-tree semantic profile

The source pins BT semantics:

- root-to-leaf sequential tick model;
- explicit halt required;
- subtree-local blackboard by default;
- shared keys require declaration;
- sequence/fallback/parallel semantics;
- idempotent leaf reentry requirement;
- leaf status events;
- recovery policy references;
- recovery retry budget;
- tick trace and leaf-action correlation ID.

BT semantics must not be assumed accidentally. Alternative semantics require a declared profile.

## Plugin law

Planner plugins include POMDP, MPC, RL, VLA/foundation models, and symbolic planners.

Every plugin must answer:

- what problem class it solves;
- what evidence it emits;
- how stable it is under replay;
- whether it can be wrapped by policy and guardrails.

## EpiCybernetica and truth maintenance

Memory is not truth.

A record may be stale, forged, low-confidence, superseded, or context-bound.

The epistemic plane manages comparison, conflict detection, confidence propagation, challenge cases, and admissibility of belief change.

Learning is permitted only under declared budget:

- compute budget;
- risk budget;
- reversibility budget;
- operator burden budget;
- uncertainty budget.

## Learning promotion gates

| Gate | Question | Artifact |
| --- | --- | --- |
| G1 | What exact component changed? | artifact envelope + version pins |
| G2 | What evidence supports the change? | evaluation result + replay bundles |
| G3 | Did policy or safety regress? | policy gate report |
| G4 | Can change be rolled back? | rollback plan artifact |
| G5 | Did operator burden increase? | human factors review |
| G6 | Did disagreement or drift increase? | epistemic delta report |
| G7 | Is improvement durable across challenge cases? | evaluation corpus replay summary |

## Replay as constitutional evidence

Replay is described as the minimum viable scientific method for an operating cybernetic system.

It reconstructs:

- observation stream;
- belief updates;
- planner alternatives;
- chosen action;
- policy gates;
- emitted artifacts.

Replay may be deterministic or best-effort, but must be honest about determinism class.

## Incident law

An incident is any episode where safety, policy, latency, cost, epistemic integrity, or operator burden crossed a declared threshold.

Incident records include severity, owner, evidence refs, immediate actions, and root-cause hypotheses.

Incident closure is not the same as explanation. A contained incident may remain epistemically unresolved.

Hidden patching is prohibited: every mitigation that changes behavior must itself become an artifact.

## Security and quarantine

Security is a set of typed threat surfaces:

- prompt/tool injection;
- stale or forged memory;
- rogue delegation;
- unsafe model drift;
- latency or partial failure.

The countermeasure is layered authority, stable contracts, provenance, replay, and quarantine semantics.

A quarantined component should lose execution authority before it loses observability.

## Promotion sequence

Default promotion order:

1. schema validation;
2. unit and contract testing;
3. scenario replay;
4. closed-loop simulation;
5. shadow deployment;
6. limited-authority live operation;
7. full promotion.

A planner cannot self-promote merely because it predicts its own success.

## Reference implementation blueprint

The implementation should ship in three coupled layers:

1. specification pack: schemas, profiles, DDL, fixtures;
2. runtime enforcement adapters: validation middleware, migration tooling, admission checks, BT profile validation, replay ingestion;
3. domain-specific node implementations conforming to common law.

The constitutional layer changes slowly. The application layer changes quickly.

## Migration path for existing stacks

Migration begins with inventory, not rewrite.

Sequence:

1. inventory services, repositories, agents, operators, embodied systems;
2. derive provisional NodeDescriptor, lifecycle state, command vocabulary, repository dependencies, incident history;
3. wrap current message types inside canonical envelopes;
4. enforce repository constitutions and replay law;
5. activate planner/BT profile enforcement;
6. enable promotion ladder.

## Capture status

Captured into GitHub as structured source-state. This is not a replacement for the original Drive PDF. It is the repo-local executable-spec capture used to make ProCybernetica self-contained enough to build from.
