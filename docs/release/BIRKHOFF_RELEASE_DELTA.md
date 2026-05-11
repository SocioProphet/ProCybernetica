# Birkhoff Release-Delta Governance

**Status:** Draft v0.1
**Track:** Tier 2 formal foundation, Tier 1 release discipline
**Purpose:** Define an operational release-delta method that separates compensating counter-terms from genuine behavioral changes.

---

## 1. Purpose

A release diff tells us what files changed. It does not tell us what behavior changed.

A benchmark result tells us whether some observed scores changed. It does not tell us which changes were absorbed by compensating adjustments, which changes created new behavior, and which changes represent doctrine-level shifts.

Release-delta governance must answer:

- what changed;
- what observable behavior remained stable;
- what hidden compensations preserved that stability;
- what behavior genuinely changed;
- what changes are non-renormalizable and require doctrine-level review;
- which changes may be promoted.

This document introduces Birkhoff-style release-delta decomposition as an operational governance method.

---

## 2. Scope

This doctrine applies to material changes in model versions, fine-tunes, system prompts, developer prompts, policies, reward or rubric functions, monitor thresholds, tool permissions, memory policies, schemas, runtime harnesses, evaluator suites, deployment profiles, and publication boundaries.

The doctrine also applies to changes that appear small. A small textual diff can carry a large behavioral delta. A large code diff can carry a small behavioral delta. The gate must reason about behavior, authority, monitoring, evidence, and risk rather than file size.

---

## 3. Core intuition

A release often contains both counter-terms and renormalized contributions.

A counter-term is an adjustment that compensates for another change to keep observable behavior stable. It may be benign, but it is always governance-relevant because it can hide the true behavioral movement of a release.

A renormalized contribution is the genuine behavior change that survives at the declared observation scale after compensations are accounted for.

Example: a prompt update weakens refusal behavior, while a monitor threshold is tightened to keep benchmark violations low. A naive release report says the prompt changed, the monitor changed, and tests pass. A Birkhoff-style release report says the prompt weakening is the risky term, the monitor tightening is a counter-term, observed benchmark stability is not evidence of unchanged safety, and the renormalized contribution may include increased reliance on monitor blocking.

---

## 4. Release-delta objects

### 4.1 Bare update

The raw set of changes.

Required fields:

- `release_delta_id`
- `source_version`
- `target_version`
- `changed_artifacts`
- `change_type`
- `actor`
- `authority_chain_id`
- `declared_intent`
- `risk_tier`
- `autonomy_tier`

### 4.2 Observable signature

The behavior measured at the chosen scale.

Required fields:

- `eval_results`
- `monitor_alert_changes`
- `policy_decision_changes`
- `tool_action_changes`
- `latency_changes`
- `privacy_changes`
- `safety_case_changes`
- `incident_changes`

### 4.3 Counter-term

A compensating adjustment that preserves or restores an observable.

Required fields:

- `counter_term_id`
- `compensates_for`
- `artifact`
- `mechanism`
- `observables_preserved`
- `risk_created`
- `review_required`
- `evidence_receipt_ids`

### 4.4 Renormalized contribution

The genuine observed behavioral change after counter-terms are accounted for.

Required fields:

- `contribution_id`
- `affected_behavior`
- `scale`
- `risk_delta`
- `capability_delta`
- `safety_delta`
- `evidence_receipt_ids`

### 4.5 Non-renormalizable change

A change that cannot be absorbed by finite counter-terms under the existing doctrine.

Examples:

- changes what counts as authority;
- removes trace requirement;
- allows promotion without evidence;
- alters publication boundary;
- gives agents power to modify monitors;
- changes privacy classification rules.

Required fields:

- `non_renormalizable_change_id`
- `reason`
- `doctrine_section`
- `required_review`
- `promotion_blocked`

---

## 5. Operational decomposition algorithm

### Step 1 — Collect raw delta

Inputs include git diff, model version diff, prompt diff, policy diff, schema diff, monitor configuration diff, eval suite diff, and deployment configuration diff.

Output: `bare_update`.

### Step 2 — Classify changed artifacts

Classes include model, prompt, policy, monitor, evaluator, runtime, tool scope, memory, schema, deployment, and publication.

Output: artifact classification map.

### Step 3 — Determine declared observables

The release author must declare which observables are expected to remain stable and which are intended to change.

Observables include refusal behavior, safe-completion behavior, tool-action decisions, prompt-injection defense, privacy handling, monitor recall, latency, capability score, incident rate, and user-facing behavior.

Output: observable signature target.

### Step 4 — Run baseline and target evaluations

Run evals on source version, target version, ablated target without each compensating change where feasible, target with previous monitor where feasible, target with previous policy where feasible, and target with previous prompt where feasible.

Output: comparative evidence.

### Step 5 — Identify compensating pairs

Find changes where artifact A moves an observable away from target, artifact B moves it back, the final metric appears stable, and removing B exposes A's effect.

These are candidate counter-terms.

### Step 6 — Compute renormalized contribution

After accounting for counter-terms, classify remaining behavior changes.

Output: `renormalized_contribution` records.

### Step 7 — Check renormalizability

A release is non-renormalizable if finite compensating changes cannot preserve constitutional invariants.

Red flags include hidden authority lane, trace removal, monitor self-modification, promotion-by-prose path, public/private evidence collapse, unbounded tool permission, and evaluator self-promotion.

### Step 8 — Gate promotion

Promotion decision may be allow, allow with monitoring, allow with degraded autonomy, quarantine, require doctrine review, or reject.

---

## 6. Schema obligations

### `counter_term.v1.json`

Minimum fields:

- `counter_term_id`
- `release_delta_id`
- `compensates_for`
- `artifact_ref`
- `mechanism`
- `observables_preserved`
- `risk_created`
- `review_required`
- `evidence_receipt_ids`

### `renormalized_contribution.v1.json`

Minimum fields:

- `contribution_id`
- `release_delta_id`
- `affected_behavior`
- `scale`
- `risk_delta`
- `capability_delta`
- `safety_delta`
- `evidence_receipt_ids`

### `release_delta_report.v1.json`

Minimum fields:

- source and target versions;
- changed artifacts;
- declared intent;
- risk and autonomy tier;
- observed behavior deltas;
- counter-terms;
- renormalized contributions;
- non-renormalizable changes;
- evidence receipts;
- promotion recommendation;
- non-claims.

---

## 7. Examples

### Example 1 — Safe release

Change: prompt clarifies refusal language. Eval suite unchanged. Monitor unchanged.

Observed: refusal accuracy improves, helpful safe-completion rate unchanged, and no hidden compensating change detected.

Result: no counter-terms, one renormalized contribution, promotion allowed.

### Example 2 — Counter-term release

Change: prompt weakens refusal, monitor threshold tightened.

Observed: benchmark violation rate unchanged.

Ablation: target prompt with old monitor increases violations; old prompt with new monitor overblocks benign requests.

Result: monitor threshold is a counter-term compensating prompt weakening. Promotion requires review and likely blocks until the prompt update is corrected.

### Example 3 — Non-renormalizable release

Change: tool permission policy lets agents modify monitor configuration.

Observed: tests pass.

Result: violates constitutional invariant, is non-renormalizable, requires doctrine-level review, and normal release promotion is blocked.

---

## 8. Gate policy

### Green

No constitutional invariant affected; no high-risk counter-terms; renormalized contribution matches declared intent; evals pass; monitor stable.

### Yellow

Counter-terms present but declared; risk low or medium; mitigation recorded; additional monitoring required.

### Red

Hidden counter-term, high or critical risk, failed safety eval, missing evidence, or unclear causal attribution.

### Black

Non-renormalizable change, hidden authority lane, trace removal, promotion-by-prose path, monitor self-modification path, or privacy boundary collapse.

Black releases cannot be promoted under ordinary release process. They require constitutional or doctrine review.

---

## 9. Relationship to causal monitoring

A counter-term is not merely correlated compensation. It should be supported by intervention.

Required evidence for high-risk counter-term:

- remove compensating artifact and observe behavior;
- hold compensating artifact while reverting original change;
- estimate causal effect;
- record uncertainty.

---

## 10. Relationship to safety cases

A cybernetic safety case must include release-delta status.

Required fields:

- current release delta;
- counter-terms;
- renormalized contributions;
- non-renormalizable changes;
- review decision;
- residual risk.

A safety case that omits release-delta effects is incomplete.

---

## 11. Tests

- B-1 hidden counter-term: risky prompt weakening plus monitor tightening. Expected: counter-term detected.
- B-2 stable metric false assurance: benchmark score stable but risk shifts from model behavior to monitor blocking. Expected: governance-dependence shift recorded.
- B-3 non-renormalizable change: trace requirement weakened. Expected: release blocked.
- B-4 declared safe change: safe-completion wording improved without compensation. Expected: promotion allowed.

---

## 12. Implementation plan

Phase 1: manual release-delta report with required fields.

Phase 2: automated artifact classification from git, model, prompt, policy, and monitor diffs.

Phase 3: ablation harness for prompt, policy, monitor combinations.

Phase 4: causal effect estimation and counter-term ranking.

Phase 5: Birkhoff-style decomposition visualized in dashboard.

---

## 13. Closing rule

A release is not safe because its diff is small.

A release is safe enough only when the fabric can say what changed, what was compensated, what genuinely moved, what did not move, and what cannot be promoted under existing law.
