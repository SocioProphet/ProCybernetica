# Epistemic Control Law

Status: v0.1 downstream doctrine binding  
Issue: #42  
Upstream anchor: SocioSphere PR #322 / `standards/epistemic-governance`  
Publication state: public  
Runtime claim: none

## Purpose

This document binds the SocioSphere Epistemic Governance standard into ProCybernetica's doctrine/control-law surface.

SocioSphere owns the standard, protocol surface, migration ledger, topic catalog, run specification, and estate ownership registry. ProCybernetica owns the doctrine that explains why those structures are control law: claims are controlled state; critique is feedback; evidence is promotion substrate; contradiction is bounded uncertainty or reversal trigger; repair is actuation.

## Scope

This is doctrine. It does not implement detectors, counter-tests, replay bundles, policy-as-code, runtime gating, retention policy, telemetry, or release automation.

Downstream implementation remains with the assigned estate owners:

- SocioSphere: standard, protocol surface, registry, workspace governance.
- ProCybernetica: doctrine and epistemic control law.
- Policy Fabric: intervention, retention, drift, and promotion policies as code.
- AgentPlane: executable detector, counter-test, replay, and proof-bundle surfaces.
- SourceOS/sourceos-syncd: local-first discourse events and event-store mapping.
- HolographMe / human-digital-twin: self-owned Reasoning Calibration Projections and dignity-preserving human projections.
- Delivery Excellence: epistemic-governance metrics and release-readiness signals.
- Ontogenesis: claim, evidence, detector, and counter-test ontology.

## Control-law thesis

An epistemic system is a control system over claims.

A claim is not merely text. It is controlled state with lifecycle, authority, evidence, reversibility, and downstream effects. A claim can influence decisions, actions, policies, deployments, model outputs, dashboards, operator trust, and organizational memory. Therefore claims require control law.

The minimum control loop is:

```text
claim -> critique -> counter-test -> evidence -> promotion / hold / reversal -> repair -> replay
```

The loop is lawful only when every transition preserves claim / decision / action separation.

## Core definitions

### Claim

A claim is a structured assertion about a system, event, artifact, person, process, risk, capability, decision, or state of the world.

A claim may be proposed, supported, promoted, challenged, reversed, superseded, or rejected. It may not become canonical merely because it appears in prose, model output, detector output, dashboard text, issue commentary, or operator notes.

### Decision

A decision is an authorized selection among alternatives. It may rely on claims, but it is not identical to the claims it uses.

A decision requires authority, scope, evidence, and review posture.

### Action

An action is an effect-producing operation. It may be based on a decision, but it is not equivalent to the decision.

Actions require policy, authority, side-effect assessment, replayability, and auditability.

### Critique

Critique is feedback applied to claims. It is not hostility; it is the control mechanism that prevents claim state from becoming self-sealing.

Critique may identify missing evidence, fragile inference, unsupported escalation, stale source anchors, small-N risk, detector bias, counterexample pressure, or contradiction.

### Evidence

Evidence is the promotion substrate. It may be direct observation, derived fact, fixture validation, reproducible run output, provenance record, counter-test result, review finding, or audited external artifact.

Reasoning is not itself evidence unless the object under review is the reasoning process. Reasoning organizes evidence; it does not replace it.

### Repair

Repair is actuation in the epistemic control loop. Repair may revise a claim, downgrade status, add missing evidence, attach a counter-test, correct an ontology mapping, reverse a decision, update a detector, or change a promotion rule.

### Contradiction

Contradiction is not automatically failure. It is a control signal.

A contradiction may represent bounded uncertainty, stale evidence, scope mismatch, detector error, ontology drift, adversarial manipulation, or a genuine need for reversal. The system fails only when contradiction is hidden, ignored, or silently normalized.

## Law 1 — Claim / decision / action separation

No claim may be treated as a decision. No decision may be treated as an action. No action may be justified by a claim whose evidence and promotion status are not visible.

This law prevents soft-lane outputs from silently becoming world-changing operations.

## Law 2 — Promotion requires evidence

A claim cannot promote itself. Promotion requires evidence, authority, counter-test posture, and auditability.

A detector finding, model output, or analyst interpretation may open a review lane. It may not become canonical truth without evidence and promotion law.

## Law 3 — Counter-tests are first-class controls

Every detector or critique class must define what would make its finding weaker, false, stale, or out of scope.

A detector that can only accuse but cannot be counter-tested is not an epistemic-governance component. It is an unbounded assertion generator.

## Law 4 — Contradiction must be preserved

Contradiction records must not be erased by cancellation paths, release compensation, dashboard summarization, or policy transforms.

A contradiction may be resolved, bounded, superseded, or escalated. It may not be hidden while its downstream authority remains active.

## Law 5 — Repair must be replayable

Epistemic repair must leave a trace. The system must be able to answer:

- what claim changed;
- why it changed;
- what evidence forced the change;
- what decision or action depended on the earlier claim;
- whether downstream artifacts require reversal, supersession, or notice.

## Law 6 — Human dignity boundary

Reasoning Calibration Projections and human-facing epistemic governance must never reduce a person to a detector object, reputation artifact, or inferred cognitive state without consent, scope, review, and redress boundaries.

Detector findings about people are hypotheses requiring care. They are not accusations, identity judgments, or disciplinary facts without independent process.

## Law 7 — Privacy-tier discipline

Evidence and claim records must preserve publication and privacy boundaries.

If evidence cannot be public because it contains private data, the system should publish the method, schema, synthetic fixture, redacted summary, or provenance posture rather than erase the evidentiary category.

## Soft-lane boundary

Soft-lane outputs include model completions, detector findings, critique notes, heuristic risk flags, dashboard annotations, generated summaries, and operator impressions.

Soft-lane outputs may:

- propose claims;
- request counter-tests;
- flag contradiction;
- recommend evidence preservation;
- request review;
- suggest repair.

Soft-lane outputs may not:

- become canonical truth without promotion;
- authorize action without decision and policy;
- assert actor attribution without discriminating evidence;
- bypass privacy or dignity boundaries;
- hide missing evidence.

## Relationship to falsification doctrine

The unified falsification document defines failure observables for this law. In particular:

- reasoning operations conflated with evidence trigger F4.1;
- soft-lane output promoted without evidence triggers F3.1;
- contradiction hidden by cancellation triggers F8.2;
- human reputation mapping without consent triggers B1.

## Non-claims

This document does not claim that ProCybernetica currently implements the full Epistemic Governance runtime. It defines the doctrine boundary that downstream schemas, fixtures, validators, policy code, replay bundles, and metrics should obey.