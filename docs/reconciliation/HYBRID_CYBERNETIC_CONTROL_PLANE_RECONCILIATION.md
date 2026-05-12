# Hybrid Cybernetic Control Plane Reconciliation

Status: draft v0.1  
Owner: ProCybernetica reconciliation lane  
Scope: Superconscious, SocioSphere, Policy Fabric, AgentPlane, SourceOS, and ProCybernetica control-plane alignment

## Purpose

This document reconciles the existing SocioProphet / SourceOS control-plane work into a single hybrid cybernetic control-plane doctrine.

The result is not a new global control plane and not a replacement for existing authority repositories. The estate already contains the major planes. The missing work is to make authority propagation, observable effects, cancellation, quarantine, and evidence uniform across those planes.

Core conclusion:

```text
We already have the planes.
We now need the authority-dependency graph that binds them.
```

## Corrected framing

Earlier drafts risked presenting the hybrid control plane as greenfield. That is wrong.

The corrected architecture is:

```text
Superconscious governs the visible cognition/control loop.
ProCybernetica codifies public cybernetic doctrine and conformance law.
SocioSphere records estate topology, dependency direction, and operator-facing control graph state.
Policy Fabric owns admission, inheritance, cancellation, break-glass, promotion, and fail-closed policy law.
AgentPlane owns bounded execution, placement, replay, and evidence artifacts.
SourceOS owns local trust, state integrity, service posture, repair, and host/runtime enforcement.
```

The hybrid control plane is therefore a cross-repo system of systems. It must be reconciled, not centralized.

## Existing anchors

### Superconscious

Primary role: visible governed cognition/control loop.

Current anchors:

- `README.md`
- `ARCHITECTURE.md`
- `THREAT_MODEL.md`
- `TRUST_SURFACE.yaml`
- `docs/trust-surface-protocol.md`
- `schemas/trust-surface.schema.json`

Key doctrine:

- no invisible authority;
- safe operational traces rather than raw private reasoning traces;
- policy admission before tools, memory, model routes, side effects, or egress;
- deterministic M1 posture with no network, no model calls, no side effects, no shell execution, and local artifacts only;
- adapter boundaries for policy, agent grants, model routing, runtime, tools, memory, evidence, workspace, approval, and benchmarking.

Superconscious should be treated as the control-loop and trust-surface seed, not as the canonical schema owner or execution authority.

### ProCybernetica

Primary role: public cybernetic doctrine, reconciliation, source capture, conformance law, and reference implementation scaffold.

Current anchors:

- `README.md`
- `docs/START_HERE.md`
- `docs/BLUEPRINT_POSITIONING.md`
- `docs/BLUEPRINT_PROVENANCE.md`
- `docs/CAPTURE_STATUS.md`
- `docs/source-captures/`
- `docs/PROGRAM_STATUS.md`

Key doctrine:

- every meaningful component is a control node with explicit identity, lifecycle, interfaces, memory, world model, value judgment, behavior generation, execution, learning, coordination, and observability;
- authority, command, promotion, and actuation must be typed, policy-bound, replayable, and auditable;
- soft, learned, heuristic, or proposal lanes do not become canonical truth or world-changing action without validation, evidence, and promotion law;
- the Prophet estate should be a hierarchy-and-graph of lawful control nodes, not an unstructured swarm.

ProCybernetica should own reconciliation doctrine and conformance vocabulary, not runtime placement.

### SocioSphere

Primary role: estate control graph, workspace topology, registry state, validation lanes, readiness, and operator control surface.

Current anchors:

- `docs/architecture/estate-control-graph.md`
- `registry/dependency-graph.yaml`
- `docs/integrations/GAIA_OFIF_MESHLAB_GOVERNANCE.md`
- `docs/integration/sourceos-substrate-control-plane.md`
- `registry/repository-ontology.yaml`
- `registry/epistemic-governance.yaml`

Key doctrine:

- implementation stays in owning component repos;
- SocioSphere records topology, dependency direction, validation state, hardening posture, workspace state, and cross-repo control graph;
- agentic work must pass through AgentPlane work-order semantics and Policy Fabric gates;
- semantic, identity-sensitive, deployment, runtime, and evidence surfaces must not define parallel governance stacks.

SocioSphere is the natural home for the estate authority-dependency graph.

### Policy Fabric

Primary role: policy-as-code, semantic validation, admission, promotion, inheritance, break-glass, cancellation, and fail-closed posture.

Current anchors:

- `README.md`
- `docs/TRUST_AND_SECURITY_MODEL.md`
- `docs/specs/agent_reliability_overrides.md`
- `contracts/policy_fabric_agent_inheritance_profile_v1.schema.json`
- `contracts/policy_fabric_break_glass_override_v1.schema.json`
- `examples/sourceos/sourceos-repo-context-read-only.policy.json`
- `tools/validate_agent_reliability_overrides.py`

Key doctrine:

- authored policy is the intent layer;
- compiled plans must faithfully reflect authored policy;
- generated reports and manifests are part of the control surface;
- secrets are references only;
- lower scopes may tighten controls but may not weaken higher scopes;
- break-glass overrides require bounded scope, human approval, expiry, audit reference, and signature object.

Policy Fabric should own cancellation and override semantics, not execution.

### AgentPlane

Primary role: execution control plane, placement, run evidence, replay, guarded invocation, and agentic work-order lifecycle.

Current anchors:

- `README.md`
- `docs/agentic-pr-control-plane-v0.md`
- `docs/integration/network-native-assistant-evidence.md`
- `schemas/`
- `examples/`
- `runners/`
- `tools/`

Key doctrine:

- execution is evidence-producing work;
- bundles are validated, placed, run, evidenced, and made replayable;
- implementation, review, merge, and ledger authority must be separated;
- evidence contracts should not mutate firewall state, install mesh components, contact model providers, invoke native assistants, or store credentials unless an explicit executor path performs a policy-approved action.

AgentPlane should emit authority-dependency evidence, not decide policy.

### SourceOS / sourceos-syncd

Primary role: local-first state integrity, event envelope, service posture, state health, repair planning, local enforcement, and attestable diagnosis.

Current anchors:

- `docs/specs/sourceos-control-plane-integration.md`
- `docs/specs/sourceos-state-integrity-report.md`
- `docs/canonical-event-envelope.md`
- `schemas/sourceos-event.schema.json`
- `schemas/sourceos.event.v0.1.schema.json`

Key doctrine:

- every event must include actor, authority domain, declared capability, policy decision, causal parent, resource cost, privacy class, retention class, and remediation;
- raw logs are evidence, but product surfaces should expose typed, coalesced, causally linked events with operator narratives;
- local-first daemons must explain owned state, freshness, invariants, policy, repair safety, and trust posture;
- degraded diagnosis should map to safe controller action or explicit manual decision.

SourceOS should bind authority dependencies to local state integrity and repair posture.

## Reconciled control-plane law

The shared control-plane law should be:

```text
No invisible authority.
No control effect without declared authority.
No authority without policy admission.
No policy admission without evidence obligations.
No cross-plane propagation without dependency topology.
No cancellation without downstream effect semantics.
No recovery without attestation, drift reconciliation, and prove-clean posture where applicable.
```

## Missing spine: authority-dependency graph

The current estate has:

- trust surface declaration;
- topology and dependency graph registration;
- policy inheritance and break-glass contracts;
- execution and replay evidence;
- state integrity and local repair reports;
- public cybernetic doctrine.

It does not yet have a single normalized contract that says:

```text
This actor or component may affect that target
through this authority surface,
under this policy,
with this evidence,
subject to these cancellation and recovery rules.
```

This is the authority-dependency graph.

The authority-dependency graph is not just a dependency graph. It is a cybernetic control graph. Each edge must say what kind of influence can propagate and how that influence is observed, denied, cancelled, quarantined, or repaired.

## Proposed minimal vocabulary

Do not introduce a large greenfield object universe. Add only the missing binding vocabulary.

### AuthorityDependency

Declares a lawful influence path between an authority source and an affected target.

Required conceptual fields:

```text
source_ref
target_ref
authority_surface_ref
control_effect_refs
policy_refs
evidence_requirement_refs
cancellation_binding_refs
trust_surface_refs
owner_repo
status
```

### ControlEffect

Describes what can actually change.

Allowed first tranche effect classes:

```text
read
write
execute
route
publish
persist_memory
promote
merge
deploy
replicate
quarantine
revoke
repair
model_route
network_egress
credential_access
browser_control
terminal_control
host_mutation
```

### CancellationBinding

Maps policy decisions, break-glass expiry, revocation, degraded mode, quarantine, prove-clean, and state-integrity diagnosis onto downstream authority dependencies.

Required conceptual fields:

```text
trigger
action
scope
revoked_capabilities
blocked_effects
evidence_preservation
recovery_requirements
prove_clean_requirements
owner_repo
```

## Repository ownership for missing bindings

### ProCybernetica

Owns this reconciliation doctrine and conformance language.

Recommended additions:

```text
docs/reconciliation/HYBRID_CYBERNETIC_CONTROL_PLANE_RECONCILIATION.md
docs/conformance/authority-dependency-control-law.md
```

### SocioSphere

Owns the estate authority-dependency graph.

Recommended additions:

```text
docs/architecture/authority-dependency-graph.md
registry/authority-dependencies.yaml
schemas/authority-dependency.schema.json
tools/validate_authority_dependencies.py
```

### Superconscious

Extends trust surfaces with affected control effects and authority dependencies.

Recommended additions:

```text
docs/trust-surface-authority-dependencies.md
schemas/trust-surface-authority-dependency.schema.json
examples/TRUST_SURFACE.with-authority-dependencies.yaml
```

### Policy Fabric

Owns cancellation and override binding semantics.

Recommended additions:

```text
docs/specs/cancellation_binding.md
contracts/policy_fabric_cancellation_binding_v1.schema.json
examples/policy_fabric_cancellation_binding_example.json
tools/validate_cancellation_binding.py
```

### AgentPlane

Emits execution evidence that a run used, attempted, or was blocked from using declared authority dependencies.

Recommended additions:

```text
docs/integration/authority-dependency-evidence.md
schemas/authority-dependency-evidence.schema.v0.1.json
examples/authority-dependency-evidence.example.json
```

### SourceOS / sourceos-syncd

Binds authority dependencies to local state integrity, degraded state, repair plans, quarantine, and attestation.

Recommended additions:

```text
docs/specs/authority-dependency-state-integrity-binding.md
examples/authority-dependency-state-integrity-report.example.json
```

## Minimum valid authority-dependency edge

A valid first-tranche authority dependency should answer:

1. What is the source actor, repo, service, agent, workload, or node?
2. What target may it affect?
3. Which declared trust surface grants the possible authority?
4. Which control effects are possible?
5. Which policy admits or denies those effects?
6. Which evidence proves use, denial, or non-use?
7. Which cancellation binding revokes or neutralizes the dependency?
8. Which repository owns the edge?
9. Which system renders it to the operator?
10. Which validator blocks incomplete or unsafe declarations?

## Example conceptual edge

```yaml
schema_version: "0.1"
kind: AuthorityDependency
metadata:
  id: agentplane-guarded-invocation-to-sourceos-network-door
  owner_repo: SocioProphet/agentplane
spec:
  source_ref:
    repo: SocioProphet/agentplane
    kind: guarded_invocation
  target_ref:
    repo: SourceOS-Linux/sourceos-syncd
    kind: network_door_plan
  authority_surface_refs:
    - SocioProphet/superconscious:TRUST_SURFACE.yaml#agent_orchestrator
  control_effect_refs:
    - route
    - network_egress
  policy_refs:
    - SocioProphet/policy-fabric:sourceos.repo_context.read_only
  evidence_requirement_refs:
    - SocioProphet/agentplane:NetworkDoorPlanEvidence
  cancellation_binding_refs:
    - SocioProphet/policy-fabric:break_glass_expired
    - SourceOS-Linux/sourceos-syncd:state_integrity_unsafe
  status: draft
```

This is illustrative only. The canonical schema belongs in SocioSphere after this reconciliation is accepted.

## Validation expectations

A first validator should fail when:

- an authority dependency has no source or target;
- a runtime-bearing source has no trust-surface reference;
- a control effect lacks a policy reference;
- an execution, route, model-route, network-egress, credential-access, browser-control, terminal-control, or host-mutation effect lacks evidence requirements;
- a revocable effect lacks cancellation bindings;
- a cancellation binding does not preserve evidence;
- a recovery path lacks attestation, drift reconciliation, or prove-clean posture where applicable;
- owner repo and implementation repo are ambiguous;
- prose-only authority is used instead of machine-readable references.

## Open questions

1. Should `AuthorityDependency` live as a SocioSphere registry contract or a future SourceOS canonical spec?
2. Should trust-surface authority dependencies be embedded inside `TRUST_SURFACE.yaml` or stored as a separate sidecar file?
3. Should Policy Fabric own all cancellation bindings or only policy-originated cancellation bindings?
4. Should AgentPlane evidence reference authority dependencies by URI, hash, or registry id?
5. Should SourceOS state-integrity reports include live authority-dependency status or only local consequences?
6. Which repo owns the cross-repo validator that verifies all declared references resolve?

## Near-term sequence

1. Accept or revise this reconciliation in ProCybernetica.
2. Open SocioSphere authority-dependency graph issue.
3. Open Superconscious trust-surface authority dependency issue.
4. Open Policy Fabric cancellation binding issue.
5. Open AgentPlane authority-dependency evidence issue.
6. Open SourceOS state-integrity binding issue.
7. Add one thin fixture per repo before expanding schemas.
8. Add cross-repo validation only after the first fixtures exist.

## Readiness estimate

Current estate readiness after reconciliation:

```text
Conceptual architecture: 80%
Superconscious cognition/control loop: 65%
Trust surface protocol: 60%
AgentPlane evidence/execution: 70%
Policy Fabric admission/cancellation primitives: 60%
SocioSphere estate graph/topology: 60%
SourceOS state integrity/local loop: 55%
Unified authority-dependency contract: 15%
Cross-repo validator coverage: 25%
Operator/UI rendering of dependency/cancellation graph: 20%
Overall hybrid cybernetic control-plane readiness: 47%
```

## Final doctrine

The hybrid cybernetic control plane is not a single controller. It is a reconciled estate discipline:

```text
Global doctrine and intent remain public and reviewable.
Cognition is visible and trace-producing.
Trust surfaces are explicit.
Policy admission is machine-checkable.
Execution is evidence-producing and replayable.
Topology is registry-backed.
Local state is diagnosable and repair-aware.
Authority propagates only through declared dependencies.
Unsafe influence is cancelled, quarantined, or degraded with evidence preserved.
```

The next implementation target is therefore not another control-plane manifesto. It is the first authority-dependency graph fixture and validator.
