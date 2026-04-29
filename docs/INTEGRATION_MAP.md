# ProCybernetica Integration Map

This map defines how ProCybernetica relates to the rest of the Prophet and SocioProphet software estate.

The key separation is simple: ProCybernetica defines the public control law and reference machinery. The platform and product repositories implement it in production contexts.

## Repository responsibility model

### ProCybernetica

Role: doctrine, standards, schemas, profiles, conformance tests, reference implementation, examples, and public curriculum.

Owns:

- Fractal Node Contract;
- Genesis Seed Contract;
- Inception/Twin Runtime Contract;
- K3 bridge lifecycle profile;
- command, delegation, observation, status, policy, replay, incident, evaluation, and promotion envelopes;
- reference supervisor;
- replay harness;
- promotion gate;
- conformance tests;
- public doctrine and textbook index.

Does not own:

- production credentials;
- customer data;
- live telemetry;
- deployment-specific policy secrets;
- private operating records.

### prophet-platform

Role: production runtime implementation of ProCybernetica law.

Should consume:

- schemas from `ProCybernetica/schemas`;
- lifecycle and promotion profiles from `ProCybernetica/profiles`;
- conformance tests from `ProCybernetica/tests`;
- integration guidance from `ProCybernetica/docs`.

Should implement:

- controlplane API;
- lifecycle supervisor service;
- event/replay service;
- memory adapters;
- policy engine integration;
- telemetry integration;
- dashboard integration;
- production storage;
- operational access control.

### agent-plane

Role: embodiment layer for agents, tool execution, delegation, and agentic workflows.

Should consume:

- Agent Node descriptor profile;
- command envelope;
- delegation envelope;
- observation envelope;
- status envelope;
- replay envelope;
- promotion and quarantine policy.

Should implement:

- agent lifecycle;
- tool authority boundaries;
- delegation records;
- replayable agent traces;
- agent promotion/quarantine;
- bounded tool invocation policy.

### socioprophet / SocioProphet product repositories

Role: product and application surfaces that use the ProCybernetica/Prophet Platform control law.

Should consume:

- platform services that implement ProCybernetica contracts;
- dashboard and evidence surfaces;
- public doctrine as product vocabulary where useful.

Should implement:

- user-facing workflows;
- customer experiences;
- application-specific surfaces;
- product dashboards;
- domain adapters;
- value propositions and packaging.

### SourceOS-Linux / SourceOS-Boot / SourceOS-Spec / nlboot

Role: host, boot, image, trust, and attestation substrate.

Should produce:

- boot receipts;
- build attestations;
- image lifecycle records;
- host evidence;
- deployment evidence;
- rollback evidence.

ProCybernetica should consume those as evidence-bearing artifacts in replay, promotion, and incident records.

### standards and knowledge repositories

Role: ontology, policy, semantic, and governance standards that ProCybernetica can reference.

Should align through:

- ontology identifiers;
- policy references;
- SHACL/JSON Schema references where applicable;
- standards documentation;
- conformance expectations.

## Control mapping

| Estate object | ProCybernetica node class | Primary actuation | Primary risk | Required governance |
| --- | --- | --- | --- | --- |
| GitHub repository | repository | branch, commit, merge, tag, release, quarantine | stale/conflicting truth | provenance, replay, branch policy, promotion |
| Pull request | process | review, update, merge, close, rebase | unsafe promotion | evaluation, CI, reviewer evidence, promotion decision |
| Agent | agent | tool call, patch, delegation, explanation | hallucination, misdelegation | tool policy, trace, replay, authority envelope |
| Workflow run | process | start, retry, cancel, checkpoint | partial completion, deadlock | event log, retry policy, replay |
| Deployment | actuator/process | deploy, rollback, promote | production mutation | approval, evidence bundle, rollback path |
| Host/image | process/repository | build, sign, boot, update | trust break, supply chain drift | attestation, receipt, SLSA/in-toto-style evidence |
| Dashboard | gateway/operator | show, filter, explain, escalate | false confidence | provenance, source confidence, contradiction flags |
| Platform service | executor/gateway | process command, update memory, emit status | opaque side effect | typed envelopes, telemetry, policy pass |

## Integration principle

No repository should reimplement ProCybernetica doctrine privately unless it is experimenting ahead of the standard. Production repositories should import, vendor, or synchronize the public contracts and report deviations back to this repository.

## Minimal runtime path

The smallest useful cross-repo path is:

1. `ProCybernetica` defines a `NodeDescriptor`, `CommandEnvelope`, `ReplayEnvelope`, `EvaluationResult`, and `PromotionDecision`.
2. `prophet-platform` exposes a service that validates those envelopes and records event evidence.
3. `agent-plane` emits agent traces and delegation envelopes.
4. GitHub workflows emit repository and PR process events.
5. SourceOS/boot repositories emit host/build/deployment evidence.
6. Prophet Platform joins the evidence and exposes dashboard views.
7. Promotion gates decide whether a proposal remains shadow-only, becomes limited authority, is fully promoted, or is quarantined.

## Rule for implementation

The standard must stay small enough to execute and strict enough to govern. Complexity belongs behind adapters; constitutional surfaces belong in this repository.
