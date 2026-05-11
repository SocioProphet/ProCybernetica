# Governance Fabric Threat Model

## Purpose

This document defines the first threat model for the Cybernetic Governance Fabric.

The threat model anchors every schema, monitor, release gate, evidence receipt, and promotion decision. Without a threat model, governance artifacts become activity logs rather than security controls.

## Protected assets

### Authority assets

- authority graph;
- role assignments;
- delegation chains;
- emergency authority;
- promotion permissions;
- publication authority.

### Runtime assets

- agent execution traces;
- tool scopes;
- sandbox boundaries;
- irreversible-action controls;
- rollback paths;
- runtime secrets and credentials.

### Evidence assets

- evidence receipts;
- replay plans;
- source locks;
- certificate fragments;
- off-history records;
- incident records;
- public evidence bundles.

### Privacy assets

- user data;
- private prompts;
- sensitive trace content;
- redacted evidence;
- sealed witness material;
- zero-knowledge commitments.

### Monitor assets

- monitor configuration;
- monitor output;
- meta-monitor reports;
- alert routing;
- syndrome-decoder state;
- monitor independence claims.

## Threat classes

### T1 — Hidden authority lane

An actor creates an undeclared path to approve, execute, suppress, or promote without the authority graph seeing it.

Controls:

- authority-chain schema;
- no-action-without-trace invariant;
- hidden-lane monitor;
- promotion-decision evidence references.

### T2 — Promotion by prose

An artifact is promoted based on explanation, confidence, or consensus without digital evidence.

Controls:

- evidence-receipt requirement;
- promotion-decision schema;
- no-promotion-by-prose invariant;
- CI fixture validation.

### T3 — Trace suppression

A governed action occurs without a trace or with a selectively incomplete trace.

Controls:

- agent-action-trace schema;
- append-only evidence ledger;
- off-history retention;
- monitor-of-monitors report.

### T4 — Tool-scope escalation

An agent obtains tool authority broader than the declared permission scope.

Controls:

- tool-permission-scope schema;
- runtime sandbox;
- irreversible-action approval;
- least-authority default.

### T5 — Monitor capture

The actor being monitored can disable, rewrite, bypass, or blind its monitor.

Controls:

- monitor independence declaration;
- QEC-style monitor redundancy;
- syndrome decoder;
- meta-monitor report.

### T6 — Evidence forgery

An actor modifies, fabricates, reorders, or selectively omits evidence fragments.

Controls:

- content hashes;
- ledger events;
- source-lock manifest;
- cryptographic receipts;
- post-quantum receipt roadmap.

### T7 — Off-history deletion

Rejected or failed candidates are deleted, making selection bias invisible.

Controls:

- off-history evidence schema;
- append-only ledger;
- rejected-candidate retention policy;
- audit of superseded fragments.

### T8 — Goodharted metric

A metric becomes a target and is optimized in a way that undermines the underlying safety property.

Controls:

- anti-Goodhart invariant;
- held-out evidence;
- adversarial evaluation;
- off-target audit;
- metric retirement policy.

### T9 — Privacy overcollection

The system collects raw private data when a commitment, hash, redaction, or aggregate would suffice.

Controls:

- privacy/evidence minimization invariant;
- redaction metadata;
- zero-knowledge receipt option;
- sealed witness path.

### T10 — Supply-chain drift

The code, model, dataset, schema, prompt, tool, or dependency differs from the one used in the certificate.

Controls:

- source-lock schema;
- artifact manifest;
- CI hash checks;
- dependency provenance.

### T11 — Emergency-power normalization

Emergency authority becomes an undeclared ordinary path.

Controls:

- emergency-power trace;
- time bounds;
- post-use review;
- exclusion from promotion precedent unless ratified.

### T12 — Human approval fatigue

Human approvers approve without meaningful review because the request volume or interface makes refusal costly.

Controls:

- approval-volume metrics;
- fatigue flag;
- sampled review;
- separation of approval and promotion;
- human-factors audit.

## Adversary models

### Internal negligent actor

Mistakes, overbroad approvals, missing evidence, accidental schema drift.

### Internal malicious actor

Deliberate hidden authority, evidence tampering, tool-scope escalation, off-history deletion.

### External attacker

Prompt injection, supply-chain compromise, credential theft, monitor evasion, artifact poisoning.

### Model/agent misbehavior

Sycophancy, deception, hidden objective, monitor gaming, refusal bypass, over-refusal, capability regression.

### Colluding monitors

Multiple monitors fail or collude, producing a false syndrome pattern.

## Threat-model acceptance criterion

Every Tier 1 schema must identify which threat classes it mitigates. Every promotion decision must state which threat classes remain unresolved.

## Non-claim boundary

This is a doctrine threat model. It does not claim a deployed detection system or exhaustive threat taxonomy.
