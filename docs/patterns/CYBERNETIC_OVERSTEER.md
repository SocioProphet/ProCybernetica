# Cybernetic Oversteer Pattern

Status: candidate pattern
Turn: 3 / 28
Owner repository: `SocioProphet/ProCybernetica`
Expected downstream owners: `SocioProphet/agentplane`, `SocioProphet/delivery-excellence`, `SocioProphet/prophet-platform`

## Purpose

Cybernetic oversteer occurs when feedback produces oscillation instead of convergence.

In human steering, overcorrection pushes the system past the intended course. In agentic software systems, overcorrection produces plan churn, patch churn, policy flip-flops, and expanding scope after every failure signal.

## Oversteer indicators

```yaml
oversteer_indicators:
  repeated_plan_reversal: true
  patch_churn: true
  issue_churn: true
  branch_churn: true
  oscillating_decisions: true
  policy_flip_flops: true
  repeated_failed_validations: true
  expanding_scope_after_failure: true
  stale_context_reuse: true
  excessive_retry_without_new_evidence: true
```

## Common cases

### Agent patch loop

Symptoms:

- agent repeatedly rewrites the same file;
- each validation failure triggers larger scope;
- branch diverges from main;
- no postcondition evidence accumulates.

Controls:

- stop after bounded attempts;
- require new evidence before retry;
- emit divergence artifact;
- narrow scope;
- escalate to review.

### Review oscillation

Symptoms:

- reviewer asks for A;
- agent changes to B;
- later agent reverts to A;
- no decision record explains the change.

Controls:

- decision log;
- issue owner;
- explicit accepted/rejected alternatives;
- contradiction record.

### Policy flip-flop

Symptoms:

- policy permits action in one step and blocks equivalent action later;
- no state change explains the difference;
- agent bypasses policy by changing surface.

Controls:

- policy decision replay;
- membrane crossing record;
- policy version pin;
- promotion decision review.

### Search/refinement thrash

Symptoms:

- repeated broad search;
- no useful narrowing;
- increasing context volume with decreasing confidence;
- irrelevant sources become accepted because they were retrieved.

Controls:

- evaluated access model;
- source confidence threshold;
- query refinement record;
- stop condition.

## Oversteer record

```yaml
oversteer_record:
  subject_ref: required
  episode_kind: agent_run | pr_review | policy | search | deployment | repair | other
  observed_indicators: []
  attempt_count: required
  evidence_refs: []
  last_new_evidence_at: optional
  damping_action:
    - stop
    - narrow_scope
    - require_review
    - emit_divergence
    - replay
    - quarantine
    - rollback
    - other
  outcome: stabilized | escalated | unresolved | quarantined
```

## Damping rules

A healthy cybernetic loop needs damping.

Recommended defaults:

1. No third retry without new evidence.
2. No scope expansion after failure without explicit approval.
3. No policy bypass by changing execution surface.
4. No merge/promotion if validation failures are unresolved.
5. No repeated agent branch churn without divergence record.
6. No public claim after contradiction without contested-state marker.

## Metrics

Delivery Excellence should track:

- failed validations per accepted artifact;
- retries per work order;
- branch churn per merged PR;
- issue reopen count;
- policy decision reversal count;
- mean time to stabilization;
- entropy introduced per delivery unit.

## Relationship to AgentPlane

AgentPlane should emit or reference oversteer signals when:

- postconditions repeatedly fail;
- divergence artifacts accumulate;
- work orders retry without new evidence;
- policy gates oscillate;
- executor placement changes repeatedly without improved result.

## Relationship to ProCybernetica

ProCybernetica should treat oversteer as a governance concern. A repeated feedback loop without convergence may require:

- manual review;
- limited authority;
- quarantine;
- rollback-required decision;
- concept or claim contested state.

## Current status

Candidate pattern. It becomes operational after AgentPlane examples and Delivery Excellence metrics are added.
