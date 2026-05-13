# Prior Synthesis Reconciliation

**Status:** Draft v0.1
**Track:** Reconciliation of prior cybernetic-governance synthesis against the hybrid cybernetic control-plane framing in PR #49
**Purpose:** Preserve the useful content of the prior doctrine/schema work while correcting its shape from a greenfield layered architecture into an estate reconciliation centered on a normalized authority-dependency graph.

---

## 1. Core correction

The prior synthesis was directionally correct but wrong-shaped.

It treated several concepts as new layers, capability tiers, or ProCybernetica-owned schema families. The corrected estate framing from PR #49 says the major planes already exist and have owner repositories. The missing spine is not a new global layer; it is a normalized authority-dependency graph binding trust surfaces, control effects, evidence, cancellation, quarantine, and recovery.

Corrected thesis:

```text
We do not need a new global control plane.
We need a cross-repo authority-dependency graph that makes existing planes interoperable, inspectable, cancellable, and recoverable.
```

---

## 2. Corrected ownership map

| Plane | Canonical owner | Correct role |
|---|---|---|
| Visible cognition/control-loop and trust-surface seed | `SocioProphet/superconscious` | Declares visible cognition, trust surfaces, and control-loop boundaries |
| Estate authority-dependency graph | `SocioProphet/sociosphere` | Owns topology, dependency direction, authority-dependency registry, and operator graph view |
| Cancellation, break-glass, fail-closed law | `SocioProphet/policy-fabric` | Owns admission, inheritance, cancellation, override, revocation, and fail-closed policy semantics |
| Evidence, replay, execution | `SocioProphet/agentplane` | Owns bounded execution, run evidence, replay, placement, and work-order lifecycle |
| Local state integrity and repair binding | `SourceOS-Linux/sourceos-syncd` | Owns local-first state integrity, diagnosis, degraded posture, repair, and host/runtime enforcement |
| Doctrine and conformance vocabulary | `SocioProphet/ProCybernetica` | Owns reconciliation doctrine, conformance language, proof-pack linkage, and public assurance posture |

---

## 3. Vocabulary correction

The prior schema names are useful but should map to the minimal vocabulary from PR #49.

| Prior term | Corrected vocabulary / placement |
|---|---|
| `dependency_control_graph` | SocioSphere `AuthorityDependency` graph, with supporting dependency-control analysis |
| `control_reachability_record` | Reachability view over `AuthorityDependency` edges |
| `observability_partition` | Evidence and operator-view partition on authority dependencies |
| `shared_dependency_ancestry` | Authority-dependency ancestry/concentration analysis |
| `dependency_cancellation_record` | PolicyFabric-owned `CancellationBinding` plus downstream effect semantics |
| `adaptive_feedback_loop` | ControlEffect feedback closure, with evidence and policy admission |
| capability-tier invocation | explicit authority-dependency invocation, not a peripheral capability tier by default |
| Layer 0/1/2/etc. | repo-owned planes in the estate, with ProCybernetica as doctrine host |

Load-bearing minimal vocabulary:

- `AuthorityDependency`
- `ControlEffect`
- `CancellationBinding`

These should become the shared spine. The prior dependency-control schemas can survive as analytical views over these primitives, not as a parallel governance universe.

---

## 4. What stays in ProCybernetica

The following prior work remains correctly placed in ProCybernetica:

- constitutional invariants;
- cybernetic governance fabric doctrine as conformance vocabulary;
- threat model;
- separation of powers;
- proof-pack template;
- gap audit and readiness matrix;
- Birkhoff release-delta doctrine as release-review/conformance doctrine;
- monitor-network/QEC doctrine as monitor topology doctrine;
- PCP replay audit doctrine as assurance doctrine;
- Agentic Ops CMDP/UCO/persona-policy doctrine as control-plane specialization;
- Zachman/AU/Environment/Seven-Model alignment as enterprise ontology doctrine;
- prior synthesis reconciliation itself.

ProCybernetica should not become the runtime registry, graph database, policy engine, execution engine, or local daemon.

---

## 5. What relocates to SocioSphere

SocioSphere should own the estate authority-dependency graph.

Relocated or projected artifacts:

- `AuthorityDependency` registry;
- `ControlEffect` vocabulary registry;
- graph-level dependency direction;
- cross-repo topology;
- authority-dependency validation state;
- operator graph view;
- dependency ancestry/concentration checks;
- cross-repo edge resolution;
- proof-pack graph references;
- AU/Environment/Seven-Model registry views where they represent estate topology.

Prior dependency-control graph work should be reissued as SocioSphere authority-dependency graph schema/registry work.

---

## 6. What relocates to PolicyFabric

PolicyFabric should own cancellation and override semantics.

Relocated or projected artifacts:

- `CancellationBinding` schema;
- break-glass expiry behavior;
- revocation semantics;
- degraded mode semantics;
- fail-closed mapping;
- safe-completion policy transformations;
- policy-originated control-effect denial;
- downstream cancellation propagation rules.

Prior dependency-cancellation and release-counterterm material should feed PolicyFabric when it determines how a control effect is cancelled or neutralized.

---

## 7. What relocates to AgentPlane

AgentPlane should own execution evidence and replay.

Relocated or projected artifacts:

- `agentplane_run_capsule`;
- `agentplane_tool_grant`;
- `agentplane_action_dispatch`;
- authority-dependency evidence emitted by runs;
- per-step UCO attribution;
- loop-detector signals;
- off-history evidence at execution time;
- operator readout;
- proof-pack runtime exhibits;
- persona-policy consumption at execution time.

AgentPlane should emit evidence that a run used, attempted to use, or was blocked from using declared authority dependencies. It should not decide the policy law.

---

## 8. What relocates to SourceOS / sourceos-syncd

SourceOS should own local state-integrity and repair bindings.

Relocated or projected artifacts:

- authority-dependency local consequences;
- degraded-state diagnosis;
- repair-plan binding;
- local evidence persistence;
- local replay posture;
- local quarantine posture;
- state-health and freshness reports;
- prove-clean or attest-clean binding where applicable.

The Environment/Aperture event spine should eventually persist through SourceOS local-first state integrity.

---

## 9. What waits for Superconscious

Superconscious remains under construction. Do not modify its implementation surface from this branch.

Future dependency issue only when concrete contracts are ready:

- trust-surface authority-dependency extension;
- visible cognition/control-loop evidence mapping;
- affected ControlEffect references;
- adapter-boundary references for policy, tools, memory, model routes, runtime, evidence, workspace, approval, and benchmarking.

---

## 10. How the new enterprise and agentic ops work fits

The Zachman/AU/Environment/Seven-Model alignment does not replace the authority-dependency graph. It supplies the enterprise ontology used to type graph nodes, evidence, proof packs, organizations, services, sites, environment regimes, and events.

The Agentic Ops CMDP/UCO/persona-policy work does not replace AgentPlane. It supplies a deterministic control policy and budget/substrategy selection layer that AgentPlane can consume when executing governed runs.

Correct placement:

| Artifact family | Doctrine host | Runtime / registry owner |
|---|---|---|
| AU / Environment / Seven-Model ontology | ProCybernetica | SocioSphere + Prophet Platform + SourceOS |
| Agentic Ops persona policy | ProCybernetica | AgentPlane + Prophet Platform |
| Proof pack | ProCybernetica | Prophet Platform + SocioSphere |
| AuthorityDependency graph | ProCybernetica doctrine only | SocioSphere |
| CancellationBinding | ProCybernetica doctrine only | PolicyFabric |
| Execution evidence | ProCybernetica doctrine only | AgentPlane |
| Local state integrity | ProCybernetica doctrine only | SourceOS |

---

## 11. Branch hygiene consequence

The current PR branch should not carry unrelated falsification/transition/capability-tier work unless explicitly reframed under this reconciliation.

Unrelated tranche families should be split into separate PRs:

- M-series transition/Cairnmark-to-Stele work;
- unified falsification observables;
- bridge-schema tranche;
- capability-tier invocation contracts.

The cybernetic-governance PR should contain only:

- doctrine and conformance alignment;
- core Tier 1 schema base;
- proof-pack template;
- AgentPlane binding;
- Agentic Ops persona-policy control plane;
- enterprise ontology/AU/Environment alignment;
- prior synthesis reconciliation.

---

## 12. Immediate next steps

1. Finish branch hygiene.
2. Update `CAPTURE_INDEX.md` to remove off-scope references and add this reconciliation artifact.
3. Keep PR #49 as the estate-level correction source.
4. Treat PR #25 as the prior-synthesis capture branch that must be reconciled before merge.
5. Open SocioSphere authority-dependency graph issue after PR #49 lands.
6. Open PolicyFabric cancellation binding issue after graph vocabulary stabilizes.
7. Open AgentPlane authority-dependency evidence issue after core authority-dependency references stabilize.
8. Open SourceOS state-integrity binding issue after first graph fixture exists.
9. Keep Superconscious untouched until a concrete trust-surface extension issue is needed.

---

## 13. Non-claims

This document does not claim the prior synthesis was useless.

It does not claim PR #49 obsoletes all prior files.

It does not implement the authority-dependency graph.

It does not move implementation into ProCybernetica.

It records the correction: prior work must be reinterpreted as doctrine and schema runway for a cross-repo authority-dependency graph, not as a new centralized cybernetic layer.
