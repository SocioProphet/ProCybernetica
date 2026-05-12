# Unified Falsification Document v1.0

**Status:** v1.0 doctrine. Twenty observables specified with revision direction.  
**Date:** May 12, 2026  
**Scope:** Empirical conditions across the seven-layer SocioProphet architecture plus the quantum dependency substrate capability tier that would force structural revision. Doctrine without falsification conditions is decorative; this document binds doctrine to skin-in-the-game commitments.  
**Review cadence:** Quarterly. Any observable realization triggers same-quarter v1.1 revision. Architectural changes that do not address any listed observable are decorative and should be flagged in PR review.

---

## 1. What this document is

This document specifies twenty observables: empirical conditions across the SocioProphet architecture that would force structural revision. Each observable includes:

- **Condition:** the empirical situation that triggers the observable;
- **Detection mechanism:** how the condition is monitored — continuous, periodic, on-event, or fixture-testable;
- **Revision direction:** what kind of architectural change the observable would force if realized;
- **Severity:** whether realization forces immediate revision (S1), next-cycle revision (S2), or quarterly-review revision (S3);
- **Fixture:** synthetic test case demonstrating the failure mode where applicable.

The observables span:

- layer-boundary observables F1.x, F2.x, F3.x;
- reasoning-operations observables F4.x;
- reputation-substrate observables F5.x;
- operational-event observables F6.x;
- cross-spec observables F7.x;
- capability-tier observables F8.x;
- meta-observables M.x.

---

## 2. Observable severity classification

**S1 — Immediate revision:** The condition, if realized, indicates structural failure that compromises governance integrity. Detection triggers same-week revision of the relevant doctrine, schemas, or composition rules. Production operations affected by the failure must be paused pending revision.

**S2 — Next-cycle revision:** The condition indicates significant misalignment between architecture and empirical reality. Detection triggers next-quarter revision. Production operations may continue with explicit acknowledgment of the deviation.

**S3 — Quarterly-review revision:** The condition indicates a calibration issue or evolving understanding. Detection feeds into quarterly review cycles without immediate intervention.

---

## 3. Layer-boundary observables

### F1.1: Behavioral equivalence classes do not cluster

**Condition:** If, across a representative sample of M0-certified artifacts, behavioral equivalence classes defined by output distributions on the eval spec fail to cluster into discrete patterns and instead form a continuous manifold with no natural decision boundaries, the artifact-to-evidence boundary is structurally wrong.

**Detection mechanism:** Periodic clustering analysis on certified artifacts. Cluster validity indices such as silhouette, Davies-Bouldin, and gap statistic are computed quarterly. Fixture-testable on synthetic behavioral data with known cluster structure.

**Revision direction:** Replace the discrete-equivalence-class abstraction with a continuous-similarity-metric framework. M0 schema would need fundamental restructuring to express behavioral similarity rather than equivalence.

**Severity:** S2.

**Fixture:** `tests/fixtures/falsification/f1-1-cluster-collapse.synthetic.json`.

---

### F1.2: graphbrain-contract artifact identifiers do not survive layer surgery

**Condition:** When `LayerSurgeryPlan` from graphbrain-contract is applied to a NetworkArtifact, if the resulting artifact's content SHA-256 is not derivable from the source artifact identity plus the surgery plan manifest digest, then artifact-layer content addressability is broken.

**Detection mechanism:** Deterministic replay of layer surgery operations across runtime invocations. CI checks that identical surgery operations produce identical content hashes.

**Revision direction:** Either the surgery plan schema must include additional manifest fields to capture the non-determinism source, or the artifact identity must include an explicit nondeterminism flag with bounds on permitted variation.

**Severity:** S1.

**Fixture:** `tests/fixtures/falsification/f1-2-surgery-determinism.synthetic.json`.

---

### F1.3: Multi-encoder artifacts do not decompose cleanly

**Condition:** When ProRepresentation encoder doctrine claims that two encoders applied sequentially produce a composite artifact whose evaluation reports decompose into per-encoder contributions, if the decomposition residual exceeds a configured threshold, default 0.1 of total variance, the compositional encoder framework is structurally inadequate.

**Detection mechanism:** Periodic decomposition analysis on composite encoder artifacts. Residual is computed across the eval spec.

**Revision direction:** Either encoder doctrine must add non-linear composition operators with explicit residual accounting, or graphbrain-contract NetworkArtifact schema must restrict composition to provably decomposable patterns.

**Severity:** S2.

---

### F2.1: Certificate verdict resolution exceeds Atlas decision vocabulary

**Condition:** If certificate `verdict_status` produces a value that cannot be cleanly mapped to one of `admit`, `deny`, `admit_with_canary`, or `admit_with_curator_review` via Bridge 3, the four-valued mapping is incomplete.

**Detection mechanism:** Bridge 3 mapping validation in CI. Every certificate with `verdict_status` must successfully map via `verdict_mapping.mapping_rule_applied`.

**Revision direction:** Either extend Atlas decision vocabulary or extend the verdict mapping rules. Both are substantial doctrinal changes.

**Severity:** S1.

**Status:** Closed in v1.0 by Bridge 3 canonical mapping. Continuously monitored.

**Fixture:** `tests/fixtures/falsification/f2-1-verdict-mapping-overflow.synthetic.json`.

---

### F2.2: SHACL shapes cannot express constitutional invariants

**Condition:** If any of CI-1 through CI-10 cannot be expressed as a SHACL constraint that Atlas can evaluate at admission time, the SHACL companion-shape doctrine is incomplete.

**Detection mechanism:** SHACL shape coverage analysis. Each CI must have either a SHACL constraint that expresses it or an explicit non-SHACL Rego stage that runs alongside SHACL with documented composition.

**Revision direction:** Either add SHACL extensions such as SPARQL-based constraints, or formally split the gate layer into SHACL stage plus Rego stage with documented sequencing.

**Severity:** S2.

**Status:** Partial. CI-1, CI-4, and CI-9 are expressible in SHACL. CI-3, CI-5, CI-6, CI-7, CI-8, and CI-10 may require Rego fallback. v1.1 commits to specific coverage after SHACL companion shapes are drafted.

**Fixture:** `tests/fixtures/falsification/f2-2-shacl-incompleteness.synthetic.json`.

---

### F2.3: Eval delta mapping loses Pattern A/B/C resolution

**Condition:** If two M2 implementability certificates with different Pattern classifications, such as A clean versus B partial, map to the same Atlas `decision_outcome` through Bridge 3 `eval_delta_mapping`, the pattern distinction is being silently lost at the gate.

**Detection mechanism:** Bridge 3 mapping validation in CI. Pattern A and Pattern B certificates must produce distinct decision outcomes.

**Revision direction:** Strengthen threshold logic in Bridge 3 to ensure `pattern_classification` produces deterministic decision-outcome differentiation.

**Severity:** S1.

**Status:** Closed in v1.0 by Bridge 3 `thresholds_used` and `delta_satisfies_atlas_gate` fields. Continuously monitored.

---

### F3.1: Downstream components silently override Atlas decisions

**Condition:** If, after Atlas issues a deny decision on a certificate, any downstream component such as memory writeback, agent context hydration, bridge export, or artifact exposure acts on the rejected certificate as if it were admitted, the gate layer is being bypassed.

**Detection mechanism:** Continuous reconciliation between Atlas decision log and downstream component action logs. Discrepancies are S1 events.

**Revision direction:** Implement explicit fail-closed wiring at every downstream component boundary. Components must consult Atlas decisions before acting; absence of admission is structural denial.

**Severity:** S1.

**Fixture:** `tests/fixtures/falsification/f3-1-downstream-override.synthetic.json`.

---

### F3.2: Authority concentration accumulates around a single signer

**Condition:** If, across a representative sample of `promoted_stele` certificates over a quarter, the reputation-weighted authority concentration index exceeds 0.8 for more than 5% of certificates, authority distribution is collapsing toward single-source verification.

**Detection mechanism:** Quarterly concentration audit. Alert threshold at 0.8 hard limit per CI-9; warning threshold at 0.7.

**Revision direction:** Either require additional independent signers on high-concentration certificate kinds, or acknowledge formally that the certificate kind is dependent on a small signer cohort and document the limitation.

**Severity:** S2.

---

## 4. Reasoning-operations observables F4.x

### F4.1: Reasoning operations conflated with evidence

**Condition:** If any certificate or proofpack lacks an explicit `reasoning_trace_ref` after the v1.3 certificate schema bump, reasoning operations are being absorbed into evidence without separability.

**Detection mechanism:** Schema validation on every certificate post-v1.3. Missing or null required field produces validation failure.

**Revision direction:** Enforce v1.3 schema requirements; backfill `reasoning_trace_ref` on existing certificates or mark them superseded.

**Severity:** S2.

**Status:** Pending v1.3 schema bump.

---

### F4.2: Cairnmarks indistinguishable from Steles

**Condition:** If any artifact at Layer 2.5 or above appears without explicit `promotion_state`, or with a value outside `candidate`, `promoted_stele`, `rejected`, or `superseded`, the Adjudication Plane is being bypassed.

**Detection mechanism:** Continuous schema validation. Field absence or invalid value is S1.

**Revision direction:** Enforce v1.3 schema requirements; reject artifacts that fail to declare promotion state.

**Severity:** S1.

**Status:** Pending v1.3 schema bump.

---

### F4.3: Defeasible support treated as silent authority

**Condition:** If any certificate or proofpack with `authority_layer: commonsense_prior` is referenced by a downstream artifact in a way that treats it as `institutional_truth`, the authority hierarchy is collapsing.

**Detection mechanism:** Cross-reference analysis between `authority_layer` of contributing evidence and `authority_layer` claimed by downstream Steles.

**Revision direction:** Strengthen authority translation rules in Bridge 1 and Bridge 2 to enforce CI-3, authority bounded by lowest input.

**Severity:** S2.

---

## 5. Reputation-substrate observables F5.x

### F5.1: Reputation does not predict contribution quality

**Condition:** If, across a representative sample of agents in the same role/domain cell over a quarter, rank correlation between prior-period reputation and observed contribution quality in the current period falls below configured threshold, default Spearman rho = 0.3, the reputation calculation is not predictive.

**Detection mechanism:** Quarterly correlation analysis per role/domain cell with minimum cell size for statistical power.

**Revision direction:** Either revise Pneumachinalis reputation formula or acknowledge that reputation is backward-looking accounting without predictive validity.

**Severity:** S2.

**Fixture:** `tests/fixtures/falsification/f5-1-reputation-non-predictive.synthetic.json`.

---

### F5.2: Stake-based authority creates concentration rather than distributing it

**Condition:** If, across a representative sample of stake commitments over a quarter, the Gini coefficient of stake distribution increases monotonically across quarters, the stake mechanism is reinforcing existing reputation rather than distributing authority.

**Detection mechanism:** Quarterly Gini coefficient computation on stake holdings. Trend analysis across quarters.

**Revision direction:** Revise stake economics or acknowledge that stakes function as wealth accumulation rather than authority distribution.

**Severity:** S2.

---

### F5.3: Certificate events do not produce meaningful delta-H at reputation layer

**Condition:** If, across a representative sample of certificate-bearing microbeat events over a quarter, the median `delta_h_attributed` value is statistically indistinguishable from zero, certificate events are not moving the knowledge state.

**Detection mechanism:** Quarterly entropy delta analysis. Per-event delta-H distribution analyzed for central tendency and dispersion.

**Revision direction:** Either revise the H(K) entropy functional or acknowledge that certificates contribute to reputation dimensions not captured by knowledge entropy.

**Severity:** S2.

---

## 6. Operational-event observables F6.x

### F6.1: Redaction propagation latency exceeds tombstone TTL

**Condition:** If, in any rolling seven-day window, more than 5% of issued redaction tombstones fail to invalidate downstream context packs within the configured TTL, the redaction cascade is structurally broken.

**Detection mechanism:** Continuous redaction propagation monitoring.

**Revision direction:** Increase redaction lane priority and ensure cascade infrastructure meets TTL, or extend TTL with documented operational consequences.

**Severity:** S1.

**Fixture:** `tests/fixtures/falsification/f6-1-redaction-latency.synthetic.json`.

---

### F6.2: Policy decision consistency drifts across topology profiles

**Condition:** If the same `event_class` receives materially different policy decisions across topology profiles for reasons not explained by topology metadata, PolicyFabric is deciding on unstated grounds.

**Detection mechanism:** Quarterly cross-topology decision audit.

**Revision direction:** Make topology-conditional policy logic explicit in policy reference schema and document which topologies materially affect which decision families.

**Severity:** S2.

---

### F6.3: Agent grants become stale faster than reputation decay

**Condition:** If median agent grant TTL is shorter than median reputation half-life in the same domain, the system is throttling agent access before reputation evidence can accumulate.

**Detection mechanism:** Periodic cross-cell analysis of grant TTL distributions and reputation decay parameters.

**Revision direction:** Align grant TTL with reputation decay parameters, or accept that grant TTL is a security control independent of reputation dynamics.

**Severity:** S2.

---

### F6.4: Bridge isolation fails in measurable cases

**Condition:** If cross-tenant or cross-trust-domain leakage is detected through bridge events, the trust-domain model is wrong.

**Detection mechanism:** Continuous leakage monitoring using synthetic tracer probes in bridge channels.

**Revision direction:** Architectural revision of the bridge layer and re-derivation of trust-domain boundaries with formal isolation guarantees.

**Severity:** S1.

**Fixture:** `tests/fixtures/falsification/f6-4-bridge-leakage.synthetic.json`.

---

## 7. Cross-spec observables F7.x

### F7.1: Bridge schemas do not compose under updates

**Condition:** If a v1.1 update to any of the three bridge schemas breaks references in fixtures from other specs that do not co-update, the bridge layer is too tightly coupled.

**Detection mechanism:** CI on schema version bumps. New bridge versions must not break existing positive fixtures from referenced specs.

**Revision direction:** Establish explicit versioning policy with deprecation windows. Bridge schemas must support old and new referenced-spec versions during deprecation.

**Severity:** S2.

---

### F7.2: Authority translation produces inconsistent layers

**Condition:** If the same actor in the same context produces different `authority_layer` values across OpsHistory grants, Pneumachinalis reputation records, and certificate signing authorities, authority translation rules are inconsistent.

**Detection mechanism:** Cross-spec authority audit.

**Revision direction:** Implement a unified authority resolution service or formally specify which spec is authoritative for which authority decisions.

**Severity:** S1.

**Fixture:** `tests/fixtures/falsification/f7-2-authority-inconsistency.synthetic.json`.

---

### F7.3: Replay determinism varies across layers

**Condition:** If a Pneumachinalis microbeat event bit-exactly replays but the OpsHistory event it references has a manifest digest that diverges under replay, or vice versa, the manifest/latent split is being applied inconsistently across layers.

**Detection mechanism:** Cross-layer replay validation. Manifest digest consistency checked across spec boundaries.

**Revision direction:** Unified manifest specification across all specs, documenting manifest versus latent fields at each layer.

**Severity:** S1.

---

### F7.4: Cadence inheritance breaks

**Condition:** If a microbeat-rate event references a macrobeat-only schema that is not available in any beacon for its stream, cadence rules are being violated.

**Detection mechanism:** Continuous cadence validation.

**Revision direction:** Strengthen the wire layer beacon resolution. Macrobeat artifacts must be explicitly published to beacons before microbeats can reference them.

**Severity:** S2.

---

## 8. Capability-tier observables F8.x

These apply only to artifacts that invoke the quantum dependency substrate capability tier through the invocation contract. Base-architecture-only operations are not subject to F8.x.

### F8.1: Dependency ancestry concentration accumulates around a single evidence source

**Condition:** If multiple artifacts with distinct signing chains in capability-tier invocations rest on common upstream evidence whose `shared_dependency_ancestry` records show concentration above 0.6, multi-party verification has collapsed to single-source verification through indirection.

**Detection mechanism:** Periodic ancestry concentration analysis on capability-tier-invoking artifacts.

**Revision direction:** Distribute upstream evidence sources, or formally acknowledge that artifacts share critical evidence ancestry as a known limitation in non-claims.

**Severity:** S2.

---

### F8.2: Cancellation paths produce silent contradictions

**Condition:** If two artifacts in the base architecture produce contradictory admitted verdicts on the same target, and no `dependency_cancellation_record` is produced within the configured TTL window when the capability tier is invoked for that target, the contradiction is being silently absorbed.

**Detection mechanism:** Contradiction monitoring on capability-tier-invoked target classes.

**Revision direction:** Strengthen contradiction-detection infrastructure and revise TTL window if needed.

**Severity:** S1.

---

### F8.3: Adaptive feedback loop gain unbounded

**Condition:** If any `adaptive_feedback_loop` record in production shows loop gain above the configured stability threshold for more than one review cadence, the cybernetic system is at risk of runaway feedback.

**Detection mechanism:** Continuous loop gain monitoring on capability-tier-invoked feedback loops.

**Revision direction:** Damping, gain reduction, or loop-breaking with explicit external adjudication.

**Severity:** S1.

**Fixture:** `tests/fixtures/falsification/f8-3-feedback-loop-unbounded.synthetic.json`.

---

### F8.4: Capability tier invocation rate exceeds expected baseline

**Condition:** If the rate of `capability_tier_invocation` across production artifacts exceeds configured expected baseline, default 5% of routine governance artifacts, the tier is being applied to use cases it was not designed for, or the base architecture is missing structural support.

**Detection mechanism:** Quarterly invocation rate analysis.

**Revision direction:** Either revise base architecture or restrict capability-tier adoption guidelines.

**Severity:** S3.

---

## 9. Meta-observables M.x

### M.1: Six-layer decomposition is the wrong cut

**Condition:** If, across F1.x through F7.x, more than 30% of S1/S2 conditions are realized in a single quarter, the layer decomposition may be fundamentally wrong.

**Detection mechanism:** Quarterly aggregate analysis.

**Revision direction:** Architectural review of layer decomposition. The seven-layer architecture may need restructuring.

**Severity:** S2.

**Fixture:** `tests/fixtures/falsification/m-1-layer-decomposition-wrong.synthetic.json`.

---

### M.2: Falsification observables not empirically testable

**Condition:** If more than 25% of observables lack fixture-testable detection mechanisms after v1.1, the falsification doctrine is decorative.

**Detection mechanism:** Coverage analysis of fixture/test infrastructure.

**Revision direction:** Add empirical test infrastructure for each observable; downgrade or remove observables that resist operationalization.

**Severity:** S1.

---

### M.3: Falsification document ossifies

**Condition:** If two consecutive quarterly review cycles produce zero revisions despite at least one realized observable, the review process has lost adversarial integrity.

**Detection mechanism:** Quarterly review meta-analysis.

**Revision direction:** Rotate review authority and introduce adversarial reviewers from outside the architecture's authoring team.

**Severity:** S2.

---

## 10. Observable cross-references

Summary CI coverage:

| Constitutional invariant | Observables |
|---|---|
| CI-1 manifest/latent split | F1.2, F7.3 |
| CI-2 cadence separation | F7.4 |
| CI-3 authority stratification | F4.3, F7.2 |
| CI-4 Cairnmark/Stele | F4.2 |
| CI-5 fail-closed | F2.1, F2.3, F3.1 |
| CI-6 dry-run discipline | F4.2, F4.3 indirectly |
| CI-7 redaction cascade | F6.1 |
| CI-8 consent typed event | F3.1, F6.4 |
| CI-9 authority concentration | F3.2, F8.1 |
| CI-10 falsification observables | M.1, M.2, M.3 |

Layer coverage:

| Layer | Observables |
|---|---|
| Layer 0 wire | F7.3, F7.4 |
| Layer 1 runtime | F3.1, F6.x |
| Layer 2 artifact | F1.1, F1.2, F1.3 |
| Layer 2.5 reasoning ops | F4.x |
| Layer 2.75 operational events | F6.x |
| Layer 3 evidence | F2.x, F4.x |
| Layer 4 gate | F2.x, F3.x |
| Layer 5 reputation | F5.x |
| Capability tier | F8.x |
| Cross-layer | F7.x |
| Meta | M.x |

---

## 11. Quarterly review process

The falsification document is reviewed quarterly.

**Detection owners:** Continuous monitoring per observable. Owners are named in `docs/falsification/observable-owners.md`. Owners report realized observables within 72 hours of detection.

**Review chair:** Rotates quarterly among the certificate-program authority chain. The chair compiles realized observables, schedules revision sessions, and produces the v1.x revision document.

**Adversarial reviewer:** External to the certificate-program authoring team. Responsible for arguing that listed observables miss important failure modes or current monitoring is insufficient.

**Sign-off authority:** Same authority that signs M1 composite certificates. v1.x revisions require their signature for adoption.

---

## 12. What this document does not commit to

The falsification doctrine is conservative about claims:

- twenty observables are not exhaustive;
- severity classifications are calibration choices;
- detection mechanisms are minimum viable;
- revision directions are starting points, not exhaustive;
- realized observables may produce other revisions with explicit justification.

---

## 13. Status

| Field | Status |
|---|---|
| Document version | v1.0 |
| Observables specified | 20 |
| Meta-observables | 3 |
| Fixture coverage | 10 observables have synthetic fixtures planned or captured |
| Remaining observables | Continuous monitoring or periodic-audit observables |
| Constitutional invariant coverage | CI-1 through CI-10 covered |
| Layer coverage | Every layer plus capability tier has at least one observable |
| Cross-spec coverage | F7.x addresses bridge composition risks |
| Review cadence | Quarterly; immediate revision on S1 realization |

---

## 14. Non-claims

This document does not implement monitoring, fixtures, or CI by itself.

It does not claim the twenty observables are exhaustive.

It does not claim that thresholds are final.

It binds the architecture to explicit revision triggers so doctrine cannot self-stabilize around its own assumptions.
