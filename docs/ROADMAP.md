# ProCybernetica Roadmap

This roadmap converts the Drive corpus into public repository work streams. It is intentionally implementation-oriented.

## v0.1.0 — Constitutional runtime skeleton

Goal: prove that ProCybernetica can run as executable doctrine, not only prose.

Deliverables:

- schema bundle for core envelopes;
- lifecycle state-machine profile;
- validation CLI;
- supervisor service;
- replay runner;
- promotion gate;
- sqlite or JSONL reference persistence;
- examples and smoke tests.

Acceptance criteria:

- `procyber validate` validates a node descriptor against schema;
- `procyber state-demo` registers a node and performs legal transitions;
- illegal transitions fail explicitly;
- `procyber replay-demo` replays an event log into an evaluation result;
- promotion gate emits `reject`, `shadow-only`, `limited-authority`, `full-promotion`, or `quarantine`;
- tests cover validation, lifecycle, replay, and promotion.

## v0.2.0 — Fractal Node Contract pack

Goal: make the node contract complete enough for repositories, agents, process runners, and platform services.

Deliverables:

- `node_descriptor.schema.json`;
- `command_envelope.schema.json`;
- `delegation_envelope.schema.json`;
- `observation_envelope.schema.json`;
- `status_envelope.schema.json`;
- `artifact_envelope.schema.json`;
- `trace_event.schema.json`;
- reference examples for repository, agent, process, planner, gateway, and operator nodes.

Acceptance criteria:

- every example validates;
- schemas distinguish authority from information;
- lifecycle and command vocabulary are explicit;
- status and observation envelopes preserve provenance references.

## v0.3.0 — Genesis/Inception/K3 lifecycle

Goal: codify seed formation and runtime twin instantiation.

Deliverables:

- Genesis Seed schema;
- Inception Request schema;
- Twin Runtime Descriptor schema;
- K3 bridge lifecycle profile;
- verification and quarantine states;
- examples for deployment twin, audit twin, research twin, and repository twin.

Acceptance criteria:

- seeds are versioned and policy-bound;
- inception requires actor, project, trust domain, runtime, region, memory scope, and provider profile;
- K3 transitions produce replayable evidence;
- actuation is denied before `TWIN_READY` and policy pass.

## v0.4.0 — Prophet Platform integration contract

Goal: define how production platform services consume ProCybernetica law.

Deliverables:

- controlplane API contract;
- memory-plane integration guide;
- telemetry and OpenTelemetry mapping;
- policy-engine integration guide;
- workflow/orchestration integration guide;
- dashboard contract for scoring, drift, contradiction, and promotion state.

Acceptance criteria:

- Prophet Platform can import schemas and profiles as a standards package;
- no doctrinal duplication is required in Prophet Platform;
- service responsibilities are mapped to Fractal Node classes;
- production data remains outside the public repo.

## v0.5.0 — GitHub and agent governance

Goal: model repositories, PRs, branches, workflows, Codex/Copilot/Claude agents, and deployment actions as governed nodes.

Deliverables:

- GitHub Repository Node example;
- Pull Request Process Node example;
- Agent Node example;
- Merge/Promotion policy example;
- branch fan-out and remerge guidance;
- agent delegation and review contract.

Acceptance criteria:

- repository state can be represented as node memory and lifecycle;
- PR state can be replayed and promoted;
- agent tool authority is bounded by policy envelope;
- merge decisions are represented as promotion decisions with evidence.

## v0.6.0 — SourceOS and trust substrate integration

Goal: connect boot, host, build, and deployment evidence to ProCybernetica evidence law.

Deliverables:

- SourceOS evidence adapter contract;
- boot receipt artifact envelope;
- build attestation artifact envelope;
- host lifecycle node example;
- policy examples for deployment gate and rollback.

Acceptance criteria:

- boot/build/deploy receipts can be referenced by replay and promotion decisions;
- host changes are modeled as gated actuation;
- SourceOS remains implementation substrate, ProCybernetica remains governing contract.

## v1.0.0 — Public standard and conformance suite

Goal: publish a stable public standard with a working reference implementation and test suite.

Deliverables:

- stable schema versioning;
- conformance harness;
- public examples;
- curriculum index;
- reference implementation docs;
- platform integration guide;
- security and publication boundary guide.

Acceptance criteria:

- outside implementers can validate a node implementation against ProCybernetica contracts;
- Prophet Platform can consume the standard directly;
- examples cover repository, agent, process, platform service, and host-trust embodiments;
- documentation clearly distinguishes doctrine, reference code, and production bindings.
