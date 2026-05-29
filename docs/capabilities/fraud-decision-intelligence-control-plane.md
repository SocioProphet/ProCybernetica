# Fraud Decision Intelligence Control Plane

Status: P0 capability doctrine
Runtime claim: none
Production claim: none
Human-impacting authorization claim: none

## Purpose

This document defines Fraud Decision Intelligence as a governed cybernetic capability family for the Prophet ecosystem.

The capability is not a standalone fraud classifier and not a runtime fraud application. It is a doctrine, contract, evidence, and conformance surface for building fraud decision systems that are portable across industries and governed by explicit claim boundaries.

The seed pattern comes from sanitized enterprise fraud analytics work: population audit, train/test drift review, feature-health and missingness analysis, model-versus-rule comparison, residual-fraud lift, scenario probing, and false-positive root-cause review. No customer-private data, proprietary model artifacts, or client-specific deck content is part of this public doctrine.

## Core thesis

Fraud is an adversarial decision-control problem, not a single prediction problem.

A conformant fraud capability must reason across:

- events;
- entities;
- relationships;
- evidence;
- rules;
- model scores;
- scenario hypotheses;
- control actions;
- human review;
- outcome labels;
- drift;
- feedback;
- governance.

A model score may propose risk. It does not prove fraud, authorize enforcement, or canonize a label.

## Universal objects

### FraudEvent

A bounded unit of activity being evaluated. Examples include an application, transaction, claim, login, refund, account opening, device activation, invoice, ad click, order, wire, credential change, or employee action.

### FraudEntity

An actor, resource, instrument, or infrastructure element connected to events. Examples include customer, account, device, merchant, dealer, provider, employee, vendor, IP address, email, phone, address, payment instrument, identity document, shipping location, wallet, or counterparty.

### FraudRelationship

A typed link among entities or events. Examples include shared device, shared address, shared payment instrument, common provider, common dealer, repeated counterparty, referral path, household relation, infrastructure reuse, or graph-neighborhood relation.

### FraudEvidenceBundle

A bounded evidence package supporting a risk assessment or decision recommendation. It may contain feature values, model scores, rules fired, graph paths, scenario references, analyst notes, source references, and provenance metadata.

### FraudDecisionReceipt

A replayable record of the decision context, recommendation, authorized action, policy boundary, evidence references, and claim limits.

### FraudLabelProvenance

A record describing the origin, confidence, timing, reversibility, and evidence basis of a fraud or non-fraud label.

### FraudFeatureHealth

A record describing availability, missingness, drift, leakage risk, operational availability at decision time, and recommended handling for a feature.

### FraudScenarioCandidate

A bounded hypothesis about a repeatable fraud pattern or control weakness. A scenario candidate is not proof of fraud and must not become a rule, label, or enforcement action without validation.

### FraudControlAction

A policy-authorized action such as allow, deny, hold, review, step-up verification, limit, suspend, monitor, investigate, report, reimburse, claw back, or escalate.

### FraudOutcome

A recorded downstream disposition such as confirmed fraud, confirmed non-fraud, unresolved, prevented loss, actual loss, recovery, customer friction, analyst time, appeal, chargeback, claim denial, regulatory filing, or remediation.

## Industry adapters

The universal object model must support industry-specific profiles without changing the core doctrine.

Initial adapter candidates:

1. Telecom and device fraud: handset financing, activation abuse, dealer fraud, SIM-swap adjacency, synthetic identity, mule identity, account takeover, upgrade abuse.
2. Banking and payments fraud: card-not-present, account takeover, ACH, wire, check, mule accounts, scam payments, synthetic identity, first-party fraud, dispute abuse.
3. Marketplace and commerce fraud: seller fraud, buyer fraud, refund abuse, chargeback abuse, promotion abuse, fake reviews, bot purchasing, reshipping, triangulation fraud.
4. Insurance and healthcare claims fraud: staged claims, inflated claims, duplicate claims, provider billing anomalies, upcoding, phantom billing, referral rings, collusive claim networks.
5. Ad-tech and traffic fraud: click fraud, install fraud, attribution fraud, bot traffic, publisher fraud, device farms.
6. Public-sector and benefits fraud: eligibility manipulation, identity fraud, procurement fraud, grant fraud, vendor collusion, tax-adjacent fraud.
7. Enterprise and internal fraud: expense fraud, payroll fraud, procurement collusion, vendor kickbacks, asset misappropriation, insider abuse.

## Required analytic spine

A conformant implementation should preserve the following analytic sequence unless a documented exception applies:

1. Population and label contract.
2. Train/test or period-over-period distribution audit.
3. Feature-health and missingness review.
4. Leakage and point-in-time availability review.
5. Current-control baseline comparison.
6. Residual-fraud lift analysis.
7. Scenario discovery and segment probing.
8. False-positive and false-negative root-cause review.
9. Threshold, review-capacity, and intervention simulation.
10. Outcome capture and label-provenance update.
11. Drift, displacement, and adversarial adaptation monitoring.

## Residual-fraud lift

Residual-fraud lift is a first-class capability primitive.

A fraud system must distinguish:

- fraud caught by the incumbent control surface;
- fraud missed by the incumbent control surface;
- fraud caught only by the model or scenario layer;
- fraud caught only by legacy rules;
- fraud caught by both;
- fraud caught by neither;
- false positives created by each control path.

This prevents shallow claims that a model is good merely because it performs well against historical labels that may already encode the incumbent system's biases and blind spots.

## Decision receipt minimum

A FraudDecisionReceipt should include, at minimum:

```json
{
  "decision_id": "fdc_example_001",
  "event_ref": "fraud_event_example_001",
  "entity_refs": ["entity_customer_example", "entity_device_example"],
  "evidence_bundle_ref": "fraud_evidence_bundle_example_001",
  "legacy_rule_outcome": "not_flagged",
  "model_outcome": {
    "score": 0.87,
    "threshold": 0.72,
    "model_id": "example_model_v1"
  },
  "scenario_refs": ["scenario_high_velocity_example"],
  "recommended_action": "manual_review",
  "authorized_action": "manual_review",
  "claim_boundary": "risk_signal_not_proof",
  "label_provenance_ref": null
}
```

## Claim boundaries

The following claims are prohibited unless separately validated and governed:

1. A model score proves fraud.
2. A graph path proves attribution or intent.
3. A public benchmark proves production readiness.
4. A Kaggle-style leaderboard metric proves operational value.
5. A high-risk segment justifies enforcement without policy review.
6. A scenario candidate is a confirmed fraud typology.
7. A weak or delayed label is ground truth without provenance.
8. A feature with unstable missingness is safe without feature-health review.
9. A model-only decision may create human-impacting denial without policy authorization.
10. An analyst note or model explanation may be canonized into memory without review.

## Positive conformance examples

A conformant public-synthetic fixture may show:

- an event scored by legacy rules and a model;
- a feature-health record noting stable and unstable features;
- an evidence bundle referencing model, rule, and graph evidence;
- a decision receipt recommending manual review;
- a label-provenance record added only after a synthetic investigation outcome;
- an explicit claim boundary that the decision is a risk signal, not proof.

## Negative fixture requirements

Future schema/conformance work should reject examples where:

- `model_score` is promoted as proof of fraud;
- `graph_path` is promoted as identity attribution;
- `benchmark_metric` is promoted as production validation;
- `fraud_label` has no provenance;
- `decision_action` is human-impacting without policy authorization;
- `feature_missingness_delta` is material but no feature-health flag exists;
- `memory_writeback` occurs before review;
- `scenario_candidate` is promoted directly into an enforcement rule;
- private customer evidence is included in a public fixture.

## Repository ownership boundaries

ProCybernetica owns this doctrine, claim-boundary law, and conformance posture.

Ontogenesis owns fraud ontology and SHACL shapes.

Semantic SerDes owns portable JSON, JSON-LD, RDF/TTL, and envelope round-trips.

GAIA owns source-pinned external fraud evidence, benchmark manifests, and public corpus curation.

SCOPE-D owns adversarial fraud scenario tests and control-surface stress fixtures.

Agent registry and AgentPlane surfaces own agent admission, permissions, receipts, and execution boundaries.

Model governance ledger owns model validation, model-card, benchmark, drift, and approval records.

Prophet Platform owns downstream runtime implementation, dashboards, services, storage, policy execution, analyst queues, and telemetry.

Alexandrian Academy owns sanitized learning modules and curriculum derived from resolved cases.

Sociosphere owns cross-repository registration and rollout sequencing.

## Non-claims

This document does not implement a model, feature store, fraud detector, graph service, case-management system, runtime policy engine, dashboard, ontology release, or production control. It defines the public doctrine and conformance boundaries for downstream implementation.

This document does not certify any public benchmark, historical client engagement, or Kaggle result as production-valid.

This document does not authorize human-impacting fraud decisions.
