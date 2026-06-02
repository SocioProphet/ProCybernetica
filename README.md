# ProCybernetica

ProCybernetica is the public codification surface for an existing cybernetic-control blueprint: doctrine, schemas, profiles, source captures, reconciliation records, conformance law, assurance packaging, and reference validation scaffolding for governed cybernetic systems.

This repository was codified from the existing ProCybernetica Drive corpus. Drive remains the source archive. GitHub is now the public, self-contained, executable-specification target for the v0 public-review state.

## Current status

Current mode: stable public-review state after the bounded 20-turn integration lane.

The core public-review surface now includes:

- estate integration maps;
- reconciled v0 schemas and profiles;
- cybernetic-governance schemas, fixtures, and validators;
- certificate v1.3 and Cairnmark-to-Stele transition doctrine;
- SHACL companion coverage;
- Human Protection Layer reconciliation;
- AgentPlane governance binding schemas;
- proof-pack assurance schemas;
- civic-stack assurance bindings;
- lawful-learning conformance smoke;
- Book XI Slice A public-synthetic ingest-to-claims fixture;
- estate-alignment follow-up fixtures;
- CI observation receipts;
- Sovereign Validation Fabric schema and fixture conformance;
- Effective Authority Architecture hardening doctrine.

Start with:

1. [`docs/START_HERE.md`](docs/START_HERE.md)
2. [`docs/INTEGRATION_STATUS.md`](docs/INTEGRATION_STATUS.md)
3. [`docs/PUBLIC_REVIEW_CHECKLIST.md`](docs/PUBLIC_REVIEW_CHECKLIST.md)
4. [`docs/conformance/README.md`](docs/conformance/README.md)
5. [`docs/implementation/VERTICAL_SLICE_PLAN.md`](docs/implementation/VERTICAL_SLICE_PLAN.md)
6. [`docs/security/EFFECTIVE_AUTHORITY_ARCHITECTURE.md`](docs/security/EFFECTIVE_AUTHORITY_ARCHITECTURE.md)
7. [`AGENTS.md`](AGENTS.md)

## What ProCybernetica is

ProCybernetica is not a generic application repository. It is the operational cybernetic framework for the Prophet ecosystem: a disciplined control fabric in which repositories, agents, process runners, planners, executors, gateways, sensors, operator interfaces, hosts, services, and embodied systems can all be treated as lawful control nodes.

The companion epistemic discipline is EpiCybernetica: the governance, critique, replay, assurance, contradiction-handling, and re-anchoring loop that keeps the operational system from becoming opaque, self-justifying, or unbounded under adaptation.

The repository starts from four core commitments:

1. Every meaningful component is a node with explicit identity, lifecycle, interfaces, memory, world model, value judgment, behavior generation, execution, learning, coordination, and observability.
2. Commands, authority, promotion, and actuation must be typed, policy-bound, replayable, and auditable.
3. Learned, heuristic, or soft-lane outputs may propose changes, but they do not become canonical truth or world-changing action without validation, evidence, and promotion law.
4. The Prophet ecosystem should be built as a hierarchy-and-graph of fractal control nodes, not as an unstructured swarm of agents or passive services.

## Repository mode

The capture/reconciliation foundation is complete enough for public review. The repository now exposes executable public conformance lanes rather than only source captures.

The correct next sequence is:

1. Preserve public-review stability.
2. Keep CI and fixture lanes green.
3. Add future Book XI slices after Slice A.
4. Add G7+ theorem-adjacent colimit/evidence-cocone work as a separate tranche.
5. Push downstream runtime adapters into their owning repositories, not into ProCybernetica.
6. Promote effective-authority hardening from doctrine to schemas, fixtures, validators, and downstream manifests.

## Canonical program tracks

### 1. Doctrine as code

The doctrinal corpus becomes concrete contracts: JSON Schemas, YAML profiles, semantic contracts, lifecycle profiles, replay envelopes, promotion decisions, policy envelopes, assurance schemas, SHACL companions, and conformance tests.

### 2. Reference validation kit

The public executable target is a compact validation kit: schema bundle, profile validators, fixture validators, proof-pack validators, HPL reconciliation checks, lawful-learning smoke checks, and Book XI Slice A validation.

### 3. Prophet Platform integration

Prophet Platform should consume ProCybernetica standards as its production runtime law. ProCybernetica defines the contracts; Prophet Platform implements services, storage, orchestration, telemetry, policy, dashboards, and deployment surfaces.

### 4. Agent and repository governance

GitHub repositories, pull requests, agents, tool invocations, branches, merges, workflow runs, and deployments should be modeled as Fractal Nodes and governed by replay, policy, evidence, and promotion law.

### 5. Effective Authority hardening

SourceOS, Bear Browser, Prophet Platform, AgentPlane, model/control-plane repos, workspace/search/world-model surfaces, and research/proof repos should converge on one Effective Authority Architecture: every repo declares what it can observe, what it can act on, what can leave the machine or workspace boundary, and what proves disabled machinery actually stopped.

### 6. Curriculum and standards publication

The ProCybernetica books, preludes, blueprints, and implementation practicum become a public educational and standards surface for cybernetic systems engineering.

## Public conformance

The main conformance entrypoint is:

```bash
python -m pytest -q
```

Representative Makefile lanes include:

```text
v0-schemas-ci
profiles-ci
cybernetic-governance-ci
dependency-control-ci
agentic-ops-ci
bridges-ci
certificate-v13-ci
shacl-ci
agentplane-binding-ci
proof-pack-ci
lawful-learning-ci
hpl-ci
book-xi-slice-a-ci
civic-stack-ci
estate-alignment-followups-ci
svf-ci
```

## Public-first trust posture

This repository is public-first. The blueprint, doctrine, captures, schemas, profiles, examples, tests, methodology, validation checks, and reference fixtures should be public by default.

The only narrow exclusions are credentials, secrets, customer/user private data, live private telemetry, sensitive deployment configuration, legally restricted third-party material, or evidence that must be sanitized before publication.

The burden of justification is on withholding, not publishing. See [`docs/PUBLICATION_BOUNDARY.md`](docs/PUBLICATION_BOUNDARY.md), [`docs/PUBLICATION_MATRIX.md`](docs/PUBLICATION_MATRIX.md), and [`docs/decisions/0001-public-first-transparency.md`](docs/decisions/0001-public-first-transparency.md).

## Non-claims

Public-review readiness is not production-readiness. This repository does not implement production runtime services, deployment services, model execution, agent execution, platform telemetry, ontology release mechanics, civic runtime, live policy enforcement, human-impacting authorization, or downstream runtime adapters. Those remain in the owning repositories.
