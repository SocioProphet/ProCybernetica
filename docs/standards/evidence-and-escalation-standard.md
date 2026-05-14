# Evidence and Escalation Standard

Status: v0.1 public-safe doctrine capture  
Issue: #58  
Publication state: public  
Runtime claim: none

## Purpose

This standard codifies neutral decision-theoretic escalation discipline for coordinated-compromise, influence, security, and epistemic-threat hypotheses.

The controlling rule is simple: no default escalation, and no attribution without discriminating evidence. A report may preserve suspicion, uncertainty, and risk posture, but it may not collapse observation into actor attribution, coordinated-compromise finding, or incident escalation merely because the facts are unusual, clustered, or emotionally salient.

## Scope

This standard applies when ProCybernetica records or reviews claims about suspicious activity, coordinated compromise, abnormal metadata, rhetorical manipulation, tool misuse, governance-control failure, or adversarial influence.

It is a doctrine and assessment contract. It is not a live detection engine, a threat-intelligence feed, a surveillance system, or an attribution oracle.

## Publication boundary

Assessment examples in this repository must be public, public-sanitized, or public-synthetic. Raw private logs, customer data, user-private evidence, live telemetry, credentials, and sensitive deployment details are excluded unless they are sanitized into a public-safe representation.

A public-safe assessment may publish method, schema, hypothesis structure, synthetic fixture, redacted evidence summary, and prohibited-conclusion discipline without publishing private evidence.

## Core rule

Escalation requires all of the following:

1. a complete or explicitly bounded hypothesis space;
2. calibrated, bounded, or honestly unknown denominators;
3. an explicit dependency model;
4. discriminating evidence that favors one hypothesis over plausible alternatives;
5. an explicit loss matrix separating harm prevention from evidentiary certainty.

If these are missing, the assessment may recommend dominant-strategy mitigations, monitoring, preservation, or review. It may not assert actor attribution, coordinated compromise, or incident certainty.

## Required layers

### 1. Observed facts

Observed facts are directly available records, events, artifacts, statements, timestamps, hashes, or measurements. They must be separated from interpretation.

Examples:

- a file exists at a path;
- a workflow failed at a named step;
- a metadata index contains a named field;
- a message contains a quoted phrase;
- a process emitted a diagnostic.

Observed facts do not, by themselves, identify intent, actor, coordination, or compromise.

### 2. Derived facts

Derived facts are deterministic transformations of observed facts: counts, joins, hashes, schema-validation results, time deltas, graph edges, or normalized labels.

Derived facts must name the transform used. If the transform depends on assumptions, the assumptions must be explicit.

### 3. Interpretations

Interpretations explain what observed and derived facts may mean. Interpretations remain defeasible. They must carry confidence language and alternative explanations.

### 4. Hypotheses

A hypothesis is a candidate explanation. Every high-risk hypothesis must include:

- what would make it more likely;
- what would make it less likely;
- what evidence is missing;
- what benign or mundane alternatives remain live.

### 5. Conclusions

Conclusions are permitted only when the evidence supports them under the declared hypothesis space, denominator model, dependency model, and loss matrix.

Unsupported conclusions must be recorded as prohibited conclusions, not silently omitted.

## Hypothesis-space rule

An assessment must not compare a suspicious hypothesis only against nothing. It must compare against plausible alternatives.

Minimum alternatives for coordinated-compromise or influence claims include:

- normal system behavior;
- local misconfiguration;
- product or platform churn;
- user action;
- automation side effect;
- indexing or caching artifact;
- benign correlation;
- third-party service behavior;
- adversarial action without coordination;
- coordinated adversarial action.

If alternatives cannot be enumerated fully, the assessment must state that the hypothesis space is incomplete.

## Denominator rule

An assessment must identify the denominator for the claim when a rate, anomaly, clustering, or probability judgment is implied.

Valid denominator states are:

- `calibrated`: grounded in a known baseline or sample frame;
- `bounded`: not fully calibrated, but bounded by a stated population, window, or process;
- `unknown`: denominator is not known, and probabilistic escalation is prohibited.

Unknown denominators do not block defensive mitigations. They do block confident anomaly claims.

## Dependency rule

The assessment must model dependence among evidence items.

Repeated observations from one source, pipeline, indexer, tool, policy, or actor may not be counted as independent corroboration unless independence is shown. Common-cause explanations must remain live until ruled out.

## Discriminating-evidence rule

Evidence is discriminating only when it changes the relative plausibility of one hypothesis against specific alternatives.

Non-discriminating signals may justify preservation, monitoring, hardening, or additional review. They do not justify attribution or coordinated-compromise conclusions.

## Loss-matrix rule

Risk response and truth claim must be separated.

A high-loss scenario may justify defensive action under uncertainty. It does not license overstating evidence. The assessment must state whether the recommendation is based on evidence strength, loss avoidance, reversibility, legal duty, or operator preference.

## Permitted recommendation classes

- `observe`: continue collecting public-safe evidence;
- `preserve`: preserve records without escalating the claim;
- `mitigate_dominant_strategy`: take low-regret protective action that is beneficial across hypotheses;
- `request_review`: send to a human or specialist reviewer;
- `escalate_security_review`: escalate process, not attribution;
- `escalate_incident`: declare incident handling only when evidence and loss criteria support it;
- `hold_claim`: block publication or promotion of unsupported claim;
- `revise_doctrine`: revise schema, threshold, or doctrine if the assessment exposes a control-law gap.

## Prohibited moves

A standard-conforming assessment must not:

- infer actor attribution from aggregate diagnostics alone;
- infer coordination from correlation alone;
- treat private suspicion as public fact;
- treat absence of benign proof as proof of compromise;
- treat repeated observations from one pipeline as independent corroboration;
- publish raw private telemetry as public evidence;
- hide missing evidence when recommending escalation;
- collapse mitigation into truth claim.

## Required assessment fields

A conforming assessment should include:

- assessment identity and version;
- subject and scope;
- publication state;
- observed facts;
- derived facts;
- hypotheses and alternatives;
- denominator model;
- dependency model;
- discriminating evidence;
- missing evidence;
- loss matrix;
- recommendation;
- prohibited conclusions;
- claim boundary;
- redaction boundary.

## Relation to ProCybernetica

This standard supports the ProCybernetica hard/soft-lane boundary. Soft-lane suspicion, critique, model output, analyst interpretation, or detector findings can propose attention and mitigation. They cannot promote themselves into canonical claims, actor attribution, or world-changing action without evidence, review, and promotion law.

## Non-claims

This standard does not claim that every suspicious pattern is benign. It also does not claim that every unresolved hypothesis should be ignored. It requires the repository to preserve uncertainty while still allowing proportionate, reversible, and public-safe mitigations.