# Cairnmark-to-Stele Transition Doctrine

Status: v0.1 doctrine  
Issue: #47  
Runtime claim: none

## Purpose

This doctrine defines the transition from Cairnmark to Stele in the certificate-family system.

A Cairnmark is a structured candidate marker. It can preserve evidence, provenance, reasoning context, and non-claims, but it cannot by itself authorize production reliance or Atlas admission.

A Stele is a promoted certificate state. It requires adjudication, reasoning trace, authority evidence, and durable non-claim boundaries.

## State discipline

Valid transition states:

| State | Meaning |
| --- | --- |
| `candidate` | Cairnmark; structured but not adjudicated. |
| `promoted_stele` | Promoted Stele; adjudicated and authority-backed. |
| `rejected` | Candidate or certificate rejected after adjudication. |
| `superseded` | Replaced by a newer certificate or successor state. |

Valid transitions:

```text
candidate -> promoted_stele
candidate -> rejected
candidate -> superseded
promoted_stele -> superseded
```

Invalid transitions include:

- candidate proofpack directly treated as promoted Stele without adjudication;
- undecided certificate admitted by Atlas;
- Pattern C certificate admitted;
- rejected certificate promoted without a new successor record;
- superseded certificate used as current authority without successor chain.

## Required v1.3 fields

Every v1.3 certificate must include:

- `authority_layer`
- `promotion_state`
- `reasoning_trace_ref`
- `cadence_classification`

## Cairnmark rule

A record with `promotion_state: candidate` is a Cairnmark.

Required posture:

- `verdict_status` must remain `undecided` or `review_required`;
- production reliance is not licensed;
- Atlas admission is not licensed;
- reasoning trace may be null, partial, or candidate-level;
- non-claims must state the adjudication boundary.

## Stele rule

A record with `promotion_state: promoted_stele` is a Stele.

Required posture:

- `verdict_status` must be `admitted`;
- `reasoning_trace_ref` must be present;
- `signing_authority_chain` must be present;
- authority layer must be review-backed or stronger;
- non-claims must preserve scope and threshold assumptions.

## Rejected and superseded rules

A rejected record must carry `promotion_state: rejected` and `verdict_status: rejected`.

A superseded record must carry `promotion_state: superseded`, `verdict_status: superseded`, and a successor or supersession reference.

## F4 falsification posture

This doctrine makes F4.x monitorable at the structural level:

- F4.1 reasoning operations conflated with evidence: monitor whether `reasoning_trace_ref` is used as evidence without authority/adjudication context.
- F4.2 Cairnmarks indistinguishable from Steles: monitor `promotion_state` and transition-state discipline.
- F4.3 defeasible support treated as silent authority: monitor `authority_layer`, `promotion_state`, and signing/adjudication fields.

## Non-claims

This doctrine does not adjudicate any live proofpack, promote any certificate, implement runtime certificate transition, implement Atlas admission, or implement capability-tier schemas. It defines structural transition discipline and validation inputs for the certificate-family base schema.
