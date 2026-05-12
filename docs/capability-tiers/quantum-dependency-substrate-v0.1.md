# Quantum Dependency Substrate

**Status:** v0.1 doctrine. Capability tier specification. Opt-in invokable.  
**Date:** May 12, 2026  
**Scope:** Specifies an advanced governance substrate available to users whose governance context demands explicit dependency-control calculus. Not part of the base architecture. Adoption is opt-in at multiple layers — Stele, tenant, deployment — with composition rules defined here.

---

## 1. What this document is

This document defines a capability tier that sits orthogonal to the base seven-layer SocioProphet architecture. The base architecture handles the common governance case with M0–M5 certificate chains, ProCybernetica safety cases, Pneumachinalis reputation, OpsHistory events, and TritFabric Atlas promotion gates.

The capability tier provides additional structural primitives:

- dependency control graphs;
- control reachability records;
- observability partitions;
- shared dependency ancestry;
- dependency cancellation records;
- adaptive feedback loops.

These primitives are for governance contexts where the base architecture's implicit dependency handling is insufficient.

The capability tier is **invoked by reference** from base-architecture artifacts. An artifact in the base architecture is structurally complete without invoking the capability tier. An artifact that invokes the capability tier carries an explicit invocation contract and inherits the tier's additional commitments.

---

## 2. Why a capability tier instead of a constitutional addition

The earlier CI-11 framing would have made dependency-control calculus a constitutional invariant required on every base-architecture artifact at Layer 2 or above. That framing is withdrawn.

The capability-tier framing is correct for three reasons.

First, universal dependency-control calculus would impose substantial schema overhead on the common case. Most certificate-program work, most Pneumachinalis reputation updates, and most OpsHistory events do not need explicit reachability analysis or observability partition accounting.

Second, a universal requirement would conflate capability-tier features with the base architecture. The dependency-control calculus is a structurally heavier governance mechanism, appropriate for specific use cases. Treating it as universal risks either making every user pay the cost or turning the mechanism into a checkbox that is widely invoked but rarely load-bearing.

Third, universal activation would violate the opt-in principle. TritFabric Atlas opt-in, Memory Mesh review-only-by-default, and ProCybernetica review-only proposal mode all express the same constitutional pattern: structural refusal of silent activation.

The base architecture remains lightweight enough for routine governance. The capability tier is available when the governance context warrants the additional cost.

---

## 3. Use cases the capability tier serves

The capability tier is designed for four governance contexts where base-architecture implicit dependency handling is structurally insufficient. These definitions are v0.1 working definitions.

### 3.1 Glass-break governance

Glass-break governance covers decisions where normal governance cadence is too slow but contradictions cannot be silently absorbed.

Examples:

- emergency rollback in production where rollback may invalidate downstream dependencies;
- security incident response where a compromise propagation path must be reconstructed before remediation;
- time-critical safety decisions where the dependency chain back to upstream evidence determines whether unilateral action is allowed.

The dependency calculus is load-bearing because the decision-maker must know, in machine-readable form, what depends on what before acting. Base certificate references are not sufficient because they do not expose reachability structure explicitly.

**Open design question Q1:** Is glass-break primarily about emergency overrides where normal governance is too slow, high-consequence one-shot decisions where contradictions cannot be silently absorbed, multi-stakeholder situations where dependency analysis verifies nobody's interest is silently overridden, or some composition? Resolution expected in v0.2.

### 3.2 Multi-jurisdiction trust-domain composition

This covers contexts where multiple trust domains compose to produce a unified decision.

Examples:

- cross-tenant evidence sharing where evidence produced in one jurisdiction must be evaluated under another jurisdiction's authority chain;
- multi-organization safety cases referencing evidence signed under multiple authority hierarchies with no common root;
- OpsHistory bridge events where information crosses trust-domain boundaries.

The `shared_dependency_ancestry` schema is load-bearing because artifacts signed under different authorities may rest on common upstream evidence.

### 3.3 Planetary-scale coordination

This covers civilizational-scale governance contexts with diverse stakeholders, trust domains, evidence sources, and decision authorities.

Examples:

- climate-scale or biosphere-scale decision-making;
- multi-civilization coordination where evidence semantics differ across stakeholder groups;
- global commons management where adaptive feedback loops must be explicit and auditable.

**Open design question Q2:** What is the empirical structure here: multi-jurisdiction composition, climate-scale coordination, multi-civilization coordination, global commons management, or a composition? Resolution expected as adoption clarifies the dominant use case.

### 3.4 Counterfactual and contradiction adjudication

This covers governance contexts where multiple admitted claims about the same target must be reconciled and reconciliation cannot be unilateral.

Examples:

- two independent M1.5 attribution graphs producing contradictory edge claims for the same feature/prompt combination;
- two admitted evidence streams producing conflicting verdicts on the same governance question;
- adversarial audit findings contradicting the original certificate-program verdict.

The `dependency_cancellation_record` schema is load-bearing because contradictions must be explicit and adjudicated, not silently absorbed.

---

## 4. The six capability-tier schemas

Each schema is specified at the level of structural commitments. Full JSON Schema definitions land in `schemas/capability-tier/` after this doctrine is accepted and Q1–Q4 clarify.

### 4.1 `dependency_control_graph.v1.json`

A typed graph whose nodes are artifacts at any layer of the base architecture and whose edges are typed dependency relationships.

Initial edge types:

- `direct_evidence_dependency` — artifact A directly cites artifact B as evidence;
- `transitive_authority` — artifact A inherits authority from artifact B through a signing chain;
- `manifest_digest_chain` — artifact A's manifest digest depends on artifact B's manifest digest by construction;
- `observability_partition_intersection` — artifacts observe overlapping partitions of common upstream material;
- `cancellation_path` — artifacts produce incompatible verdicts and cancellation analysis is required.

The graph has a manifest/latent split: manifest claims are which entities depend on which; latent state is the specific path traversal.

### 4.2 `control_reachability_record.v1.json`

A record specifying, for a given source and target node, whether a dependency path exists, what type the path is, and what authority level the path inherits.

Used to answer: if this Stele is revoked, which downstream Steles must be invalidated?

A reachability record bounds an artifact's authority layer: an artifact reachable from `commonsense_prior` upstream cannot itself claim `institutional_truth` unless the dependency path is broken by an explicit re-grounding step captured in the record.

### 4.3 `observability_partition.v1.json`

A specification of which subset of an upstream artifact a downstream artifact observes.

Two artifacts may reference the same upstream M0 certificate while observing different partitions: one observes only the eval-spec commitment, another only the dataset commitment.

Observability partitions operate on the manifest portion of an artifact and compose with the manifest/latent split. They also compose with Masonmark proofpacks at Layer 2.5, where grounding candidates and chosen entities are partial observations of artifact space.

### 4.4 `shared_dependency_ancestry.v1.json`

A record specifying that two artifacts, despite different signing authorities, share dependency ancestry through common upstream evidence.

This extends authority concentration metrics from counting distinct signers to counting distinct dependency roots.

When invoked, this makes F8.1 directly testable: dependency ancestry concentration above threshold forces structural revision even if signer concentration is below threshold.

### 4.5 `dependency_cancellation_record.v1.json`

A record specifying that two dependency paths produce effects that mutually invalidate.

It captures:

- contradiction target;
- evidence supporting each side;
- adjudicating authority;
- resolution outcome;
- downstream effects.

Composition with the four-valued verdict vocabulary: cancellation between two `admitted` verdicts on contradictory claims cannot silently default to either. It must produce an explicit adjudication record.

### 4.6 `adaptive_feedback_loop.v1.json`

A specification of cybernetic feedback structure:

- which observations feed which control inputs;
- loop time constant;
- stability conditions;
- `loop_gain`.

This is used primarily to make Layer 5 Pneumachinalis reputation feedback auditable, but applies to any closed control loop.

If `loop_gain` exceeds the configured stability threshold, F8.3 is triggered.

---

## 5. Invocation contract

A base-architecture artifact opts into the capability tier by carrying a `capability_tier_invocation` field of the shape defined in `schemas/capability-tier/invocation-contract.v1.json`.

The field is optional on all base-architecture schemas.

Presence means the artifact references capability-tier schemas and inherits the tier's commitments.

Absence means the artifact operates under base-architecture rules only.

When present, the artifact:

- carries explicit references to one or more capability-tier schemas;
- inherits structural commitments for invoked schemas;
- is subject to F8.1, F8.2, and tier-specific falsification observables;
- requires the invoking authority to itself carry capability-tier authorization.

When absent, the artifact:

- operates under base-architecture rules only;
- is not subject to capability-tier falsification observables;
- has no implicit dependency-graph commitments.

---

## 6. Opt-in at multiple layers

### 6.1 Per-Stele opt-in

A specific Stele artifact invokes the capability tier. Other Steles in the same Cairnpath traversal may or may not.

### 6.2 Per-tenant opt-in

A tenant configures deployment to enable the capability tier for all Steles produced within tenant scope.

### 6.3 Per-deployment opt-in

A deployment exposes the capability tier at all. Some deployments may ship base architecture only and never expose the capability tier to any tenant.

### 6.4 Composition rule

When opt-ins compose across layers, the most restrictive opt-in wins. A per-Stele opt-in in a tenant that has not enabled the tier defaults to base-architecture-only operation. The invocation contract on the Stele is recorded but not enforced.

**Open design question Q4:** Is per-Stele the right finest grain, or should opt-in operate at sub-Stele granularity, such as per-claim? Resolution expected in v0.2.

---

## 7. Quantum capability semantics

The substrate is called quantum dependency calculus because dependency control with observability partitions and cancellation behavior maps cleanly onto quantum-circuit dependence with observability and interference.

This is not automatically a literal claim that quantum-computational primitives are required.

**Open design question Q3:** Is quantum here:

1. a literal technical claim involving quantum-computational primitives;
2. a formal mathematical correspondence between dependency-control calculus and quantum-circuit dependence;
3. a capability-tier branding choice for a technically classical substrate with stronger composition rules?

Each is legitimate but implies different implementation paths and fidelity requirements. v0.1 leaves the question explicit; v0.2 resolves it based on adoption experience.

---

## 8. Capability-tier falsification observables

### F8.1: Dependency ancestry concentration accumulates around a single evidence source

If multiple artifacts with distinct signing chains rest on common upstream evidence whose `shared_dependency_ancestry` records show concentration above 0.6, multi-party verification has collapsed to single-source verification through indirection.

Forces revision of upstream evidence distribution or formal acknowledgment that artifacts share critical evidence ancestry.

### F8.2: Cancellation paths produce silent contradictions

If two artifacts produce contradictory admitted verdicts on the same target, and no `dependency_cancellation_record` is produced within the configured TTL window, the contradiction is being silently absorbed downstream.

Forces revision of contradiction-detection infrastructure or TTL configuration.

### F8.3: Adaptive feedback loop gain unbounded

If an `adaptive_feedback_loop` record in production shows loop gain above the configured stability threshold for more than one review cadence, the system is at risk of runaway feedback.

Forces damping, gain reduction, loop breaking, or re-engineering.

### F8.4: Capability tier invocation rate exceeds expected baseline

If the rate of `capability_tier_invocation` exceeds configured expected baseline, the tier is being applied beyond intended use or the base architecture is missing support that the capability tier is compensating for.

Forces revision of base architecture or tighter capability-tier adoption guidelines.

---

## 9. What this document does not commit to

This doctrine does not commit to:

- a claim that the quantum-circuit framing is the only valid framing for dependency-control calculus;
- a claim that the four use cases are exhaustive;
- a claim that the six schemas are sufficient;
- a claim that opt-in mechanics are finalized;
- a claim that Q1–Q4 have a single settled answer.

These questions are explicit and tracked. Adoption experience resolves them. v0.2 commits to specific answers where v0.1 leaves them open.

---

## 10. Status

| Item | Status |
|---|---|
| Doctrine version | v0.1 draft |
| Capability tier status | opt-in invokable |
| Six schemas | specified at structural-commitment level |
| Full JSON schemas | pending after doctrine acceptance |
| Invocation contract | drafted in `schemas/capability-tier/invocation-contract.v1.json` |
| Falsification observables | F8.1–F8.4 specified |
| Open design questions | Q1, Q2, Q3, Q4 explicit; resolution in v0.2 |
| Composition with base | invoked by reference; never automatic |
| Composition with base invariants | inherits base invariants when invoked |

---

## 11. Recommended cadence

Quarterly review with explicit revision triggers:

- any of F8.1–F8.4 realized → immediate v0.2 revision;
- any of Q1–Q4 resolved by adoption experience → next-quarter v0.2 revision;
- new capability-tier use case identified → next-quarter v0.2 revision;
- schema-level changes to tier schemas → version bump.

Ownership: same authority that signs M1 composite certificates also signs revisions of this document. This couples capability-tier discipline to production-governance discipline.

---

## 12. Non-claims

This doctrine does not make the capability tier constitutional.

It does not require all base-architecture artifacts to carry dependency-control graphs.

It does not require quantum hardware.

It does not resolve Q1–Q4 in v0.1.

It preserves CI-1 through CI-10 and withdraws the prior CI-11 framing.
