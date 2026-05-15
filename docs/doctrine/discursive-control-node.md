# Discursive Control Node

Status: v0.1 downstream doctrine binding  
Issue: #42  
Upstream anchor: SocioSphere PR #322 / `standards/epistemic-governance`  
Publication state: public  
Runtime claim: none

## Purpose

This document defines the Discursive Control Node as the ProCybernetica doctrine object for governed discourse, critique, counter-test, repair, and replay.

A Discursive Control Node is any bounded system component that receives, produces, transforms, evaluates, promotes, reverses, or routes claims. It may be a human review lane, model-assisted detector, issue thread, replay bundle, governance board, release gate, policy agent, dashboard annotation surface, or evidence-review process.

## Scope

This is doctrine. It does not implement a runtime service, detector, message bus, database, agent, or policy engine.

## Node thesis

A discourse surface becomes governable only when it is treated as a control node with explicit inputs, outputs, state, authority, evidence, review posture, and replay path.

Ungoverned discourse tends to collapse four layers:

1. what was said;
2. what was meant;
3. what is evidenced;
4. what may be acted on.

The Discursive Control Node prevents that collapse.

## Minimal node contract

A Discursive Control Node must declare:

- `node_id`: stable identity;
- `node_role`: what kind of discourse/control function it performs;
- `input_classes`: accepted claim, evidence, critique, detector, or review inputs;
- `output_classes`: produced claims, counter-tests, repairs, holds, reversals, or evidence requests;
- `authority_scope`: what the node may influence;
- `non_authority_scope`: what the node must not decide or actuate;
- `evidence_requirements`: what evidence is required for promotion;
- `countertest_requirements`: what would weaken or defeat the output;
- `privacy_tier`: publication and redaction boundary;
- `replay_surface`: how outputs can be re-read, re-run, audited, or reversed.

## Input classes

Permitted input classes include:

- proposed claim;
- detector finding;
- critique note;
- counter-test result;
- evidence receipt;
- contradiction record;
- appeal or challenge;
- repair proposal;
- replay record;
- human review finding;
- release-readiness signal.

Inputs must retain their class. A detector finding is not a promoted claim. A critique note is not evidence. A repair proposal is not a completed repair.

## Output classes

Permitted output classes include:

- `claim_proposed`;
- `claim_held`;
- `claim_supported`;
- `claim_promoted`;
- `claim_reversed`;
- `claim_superseded`;
- `countertest_required`;
- `evidence_required`;
- `repair_required`;
- `review_required`;
- `action_not_authorized`;
- `policy_escalation_requested`.

A node must not emit `claim_promoted` unless it has authority, evidence, counter-test posture, and replay surface for promotion.

## Authority discipline

A Discursive Control Node may influence claim state. It may not automatically authorize external side effects unless it is explicitly bound to a decision and action layer.

The default authority of a discourse node is interpretive, not operational. Operational authority requires a separate policy and action contract.

## Critique as feedback

Critique is the normal feedback path of the node. It can increase quality, reduce overclaim, expose contradiction, request missing evidence, or force repair.

A node that cannot accept critique is not stable. A node that treats critique as hostility rather than feedback is epistemically brittle.

## Counter-test discipline

Every node that emits detector findings or claim evaluations must state what could defeat its output.

A counter-test may be:

- a missing-evidence check;
- a baseline check;
- a small-N check;
- a provenance check;
- a source-independence check;
- a privacy-boundary check;
- a contradictory-evidence check;
- a replay check;
- a human-review check.

## Human dignity boundary

When discourse concerns a person, group, role, or human digital-twin surface, the node must preserve dignity boundaries.

A human-facing node must not:

- infer fixed identity from behavior fragments;
- convert detector output into accusation;
- produce reputation consequences without consent and review;
- hide uncertainty;
- deny appeal or redress when claim state affects a person.

## Privacy and publication boundary

A Discursive Control Node must distinguish:

- public content;
- public-sanitized content;
- public-synthetic content;
- withheld-specific evidence with named reason.

If private evidence is involved, the node should publish the method, schema, redacted summary, or synthetic fixture whenever possible.

## Failure modes

The node is defective if:

- output class is not declared;
- claim, decision, and action are collapsed;
- evidence is missing but promotion occurs;
- critique cannot be represented;
- contradiction is discarded;
- private evidence is exposed;
- human dignity boundary is omitted;
- replay or reversal is impossible.

## Relationship to ProCybernetica falsification

The following falsification observables apply directly:

- F3.1 when soft-lane output promotes without evidence;
- F4.1 when reasoning is treated as evidence;
- F4.3 when defeasible support becomes silent authority;
- F6.1 when private evidence is exposed;
- B1 when human reputation or governance consequence is mapped without consent.

## Non-claims

This document does not define a final JSON Schema for Discursive Control Nodes. It defines doctrine that later schemas, fixtures, and validators may codify after reconciliation.