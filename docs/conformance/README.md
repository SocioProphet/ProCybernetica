# Public Conformance

Status: v0.1 public-review conformance surface  
Epic: #14  
Runtime claim: none

## Purpose

This document records the public conformance surface after the bounded 20-turn integration lane.

ProCybernetica conformance is repository-local and public-first. It validates schemas, profiles, fixtures, proof-pack packaging, assurance traces, estate-alignment references, and Book XI Slice A. It does not implement runtime services owned by AgentPlane, Prophet Platform, SourceOS/SociOS, Ontogenesis, Policy Fabric, Delivery Excellence, HolographMe, or civic-stack downstream systems.

## Conformance ladder

| Level | Meaning | Current status |
| --- | --- | --- |
| C0 | Public docs and source-captures exist. | complete |
| C1 | v0 schemas and profiles are normalized and validated. | complete |
| C2 | Public-synthetic fixtures validate in CI. | complete |
| C3 | Integration maps and ownership boundaries are explicit. | complete |
| C4 | Proof-pack and assurance packaging can cite lower-level evidence. | complete |
| C5 | Downstream runtime adapters are implemented in owning repos. | out of scope for this repository |

## Validation lanes

The repository exposes Makefile targets for each major conformance lane:

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
```

The default CI path runs:

```bash
python -m pytest -q
```

## Public-review invariant

A ProCybernetica public-review artifact is conformant only if it preserves:

- explicit owner boundary;
- schema/profile or doctrine anchor;
- evidence or fixture reference;
- non-claim boundary;
- public/private/redaction posture;
- CI or reviewer validation path.

## Reference CLI posture

There is no single monolithic runtime CLI. The repository-local validators under `tools/cybernetic_governance/` are the public reference validation surface. Each emits JSON and has a Makefile target.

## Non-claims

This conformance surface does not implement production runtime services, deployment services, model execution, agent execution, platform telemetry, ontology release mechanics, civic runtime, or live policy enforcement. It validates public contracts and fixtures only.
