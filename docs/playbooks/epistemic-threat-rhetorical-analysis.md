# MFEL Playbook — Epistemic-Threat Rhetorical Analysis

Status: v0.1 public-safe playbook  
Standard: SP-STD-MFEL-0001  
Runtime claim: none

## Purpose

This playbook defines how ProCybernetica analyzes epistemic-threat and anti-verification rhetorical artifacts while preserving evidence boundaries, non-attribution discipline, and human dignity.

It is intended for public, public-sanitized, or public-synthetic fixtures. It does not authorize surveillance, platform monitoring, actor attribution, content takedown, or model training on private content.

## Scope

The playbook covers rhetorical patterns such as:

- self-sealing claims;
- anti-verification instructions;
- evidence inversion;
- failed-prediction absorption;
- insider-only knowledge framing;
- delegitimization of external review;
- social-pressure substitution for evidence;
- narrative escalation without discriminating evidence.

The playbook can describe QAnon-style rhetorical construction as a pattern class. It must not use a synthetic pattern fixture to attribute conduct to a real person, group, account, or coordinated operation.

## Case format

Every rhetorical-analysis case should validate against:

```text
schemas/mfel/observation.schema.json
```

Specific hypotheses may additionally validate against:

```text
schemas/mfel/hypothesis.schema.json
```

Graph relations may validate against:

```text
schemas/mfel/evidence-graph.schema.json
```

## Five-layer workflow

### 1. Observed facts

Record only what the artifact says or does structurally.

Examples:

- the text instructs readers to distrust external verification;
- the text reframes failed prediction as deeper concealment;
- the text implies hidden knowledge is available only to in-group participants;
- the fixture is synthetic and has no real source account.

Do not record motive, actor identity, operation status, radicalization effect, or group membership as observed facts unless those are directly evidenced.

### 2. Derived facts

Derived facts describe bounded rhetorical structure.

Examples:

- the artifact contains an anti-verification loop;
- the artifact treats external rebuttal as confirmation;
- the artifact uses identity pressure to replace evidence;
- the artifact lacks provenance to a real actor.

A derived fact must name the transform or analytic rule used.

### 3. Interpretation

Interpretation explains possible meaning and risk while naming alternatives.

Alternative explanations may include:

- fiction;
- satire;
- puzzle rhetoric;
- ordinary in-group slang;
- synthetic training fixture;
- political persuasion without self-sealing structure;
- artifact stripped of context.

Interpretation is not proof of influence, actor intent, or operation status.

### 4. Hypothesis

A hypothesis is a candidate explanation.

Suspicious or high-risk hypotheses must include negative evidence and missing evidence.

Examples of missing evidence for actor-operation claims:

- public documented source;
- account-level evidence;
- distribution graph;
- coordination evidence;
- independent corroboration;
- chain of custody.

### 5. Prohibited conclusion

A rhetorical-analysis case must explicitly prohibit unsupported conclusions.

Common prohibited conclusions:

- attributing synthetic text to a real actor;
- inferring coordinated operation from rhetorical form alone;
- inferring individual belief state from a single artifact;
- inferring extremist identity from pattern similarity alone;
- training on private content without consent and redaction.

## Actor-attribution rule

Actor attribution is not a rhetorical classification. A case may classify text as anti-verification rhetoric without naming an actor.

Actor attribution requires:

- attribution basis;
- confidence bound;
- evidence references;
- non-claims;
- redaction and consent boundary where humans are implicated.

Unsupported attribution must fail validation under `schemas/mfel/hypothesis.schema.json`.

## Human dignity boundary

When rhetorical artifacts concern a person, group, or community, the analyst must avoid converting a pattern label into an accusation, identity judgment, score, or governance consequence.

A rhetorical fixture is evidence for a pattern taxonomy only within its declared scope. It is not a reputation record.

## Public-safe examples

Reference fixture:

```text
examples/mfel/qanon-rhetorical-construction.sanitized.yaml
```

This fixture is synthetic. It tests schema discipline for self-sealing, anti-verification rhetoric. It does not describe a live post, real account, real group, or coordinated operation.

## Review checklist

A rhetorical-analysis case is not standard-conforming unless:

- [ ] the artifact source class is public, sanitized, or synthetic;
- [ ] observed facts describe text structure only;
- [ ] derived facts name the analytic transform;
- [ ] interpretations list alternative explanations;
- [ ] high-risk hypotheses include negative and missing evidence;
- [ ] actor attribution is absent or evidence-bound;
- [ ] prohibited conclusions are explicit;
- [ ] non-claims state what the fixture does not prove.

## Non-claims

This playbook does not claim to detect extremism, classify people, identify actors, infer intent, or measure persuasion. It defines evidence-bound rhetorical-analysis discipline for public-safe MFEL cases.
