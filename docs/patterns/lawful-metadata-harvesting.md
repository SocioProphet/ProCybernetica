# Lawful Metadata Harvesting

Status: v0 doctrine pattern
Owner surface: ProCybernetica / SourceOS State Integrity / AgentPlane / Policy Fabric / Sherlock

## Purpose

Lawful metadata harvesting is the governed observation pattern for pulling structured metadata from an external repository without confusing collection with truth, authority, or promotion.

The seed example is OAI-PMH, where a harvester sends typed HTTP requests such as `ListRecords`, receives batches of records, and follows opaque `resumptionToken` continuation cursors until the final response returns an empty token. The protocol supplies a useful extraction grammar. It does not by itself supply trust, provenance, replay, authorization, or promotion law.

This pattern turns a resumable metadata pull into a cybernetic evidence chain:

```text
external repository
  -> protocol request
  -> batch response
  -> receipt seal
  -> policy decision
  -> replay manifest
  -> search packet
  -> validation report
  -> promotion decision
```

## Boundary rule

A continuation cursor is not evidence by itself.

For OAI-PMH specifically, `resumptionToken` is a flow-control cursor. It must be treated as opaque data. It must not be interpreted as a cryptographic proof, an authorization grant, a stable ordering proof, or a semantic claim about the repository. ProCybernetica evidence begins only when the request, response, cursor state, actor identity, policy decision, and previous receipt hash are sealed into an auditable receipt.

## Required actors

Every lawful harvest must name at least these actors or actor references:

- `source_repository`: the external repository or data provider.
- `harvester_actor`: the import bridge, agent, or service performing the harvest.
- `policy_authority`: the Policy Fabric or equivalent authority that approved or denied the harvest scope.
- `execution_authority`: the AgentPlane or equivalent runner that can replay the harvest run.
- `promotion_authority`: the gate that decides whether harvested records may become durable operational state.

The harvester is an observation actor. It is not automatically an authority over the truth of the harvested content.

## Required evidence objects

A lawful harvest must produce:

1. `HarvestPlan` — endpoint, verb, metadata prefix, date/set scope, privacy class, retention class, and allowed maximums.
2. `PolicyDecision` — a policy decision reference covering the harvest plan.
3. `HarvestRun` — run identity, actor identity, execution environment, status, and replay reference.
4. `HarvestBatchReceipt` — one receipt per request/response batch.
5. `HarvestLedgerRoot` — the terminal hash binding the batch receipts.
6. `ValidationReport` — structural, semantic, and policy validation results.
7. `PromotionDecision` — explicit decision for any record promoted into Memory, Knowledge Graph, GAIA, SourceOS durable state, or another canonical substrate.

## Receipt requirements

Each batch receipt must bind:

- protocol and verb;
- endpoint identity;
- harvester actor identity;
- policy decision reference;
- request hash;
- response hash;
- record count;
- previous resumption-token hash, when present;
- next resumption-token hash, when present;
- previous receipt hash;
- current receipt hash;
- observation timestamp;
- classification and handling tags.

Raw secrets, credentials, private tokens, and private endpoint parameters must not be exposed in default public receipts. Cursor values should normally be hashed, not stored raw.

## Promotion law

No harvested record may become canonical truth or durable operational state merely because it was returned by a repository.

Promotion requires:

- a valid receipt chain;
- a policy decision allowing the target promotion surface;
- a validation report reference;
- source and record identifiers;
- classification and handling tags;
- a promotion decision with an explicit outcome.

Allowed promotion outcomes are:

- `promoted` — admitted to the target substrate under policy.
- `denied` — rejected by policy, validation, trust, or scope constraints.
- `deferred` — retained as evidence but not promoted.

## Required anomaly classes

Implementations must be able to represent at least:

- `bad_resumption_token`
- `expired_resumption_token`
- `resumption_token_loop`
- `missing_final_empty_token`
- `unexpected_empty_batch`
- `record_count_regression`
- `response_hash_mismatch_on_replay`
- `endpoint_identity_changed`
- `metadata_prefix_changed`
- `deleted_record_without_policy`
- `overscope_attempt`
- `unbounded_harvest_blocked`
- `rate_limit_or_throttle_detected`
- `non_monotone_datestamp_observed`
- `cursor_semantics_overassumed`
- `suspicious_tokenized_pagination_pattern`

An implementation must not hide these anomalies inside generic transport failure logs. They are governance-relevant observations.

## Stack alignment

### ProCybernetica

Defines the doctrine, schema, fixtures, conformance gates, and promotion law.

### SourceOS State Integrity / `sourceos-syncd`

Runs the harvester as an `import_bridge` actor and emits canonical local-first state events. Harvest state is not hidden background sync; it is inspectable, typed, replayable, and repairable.

### Policy Fabric

Authorizes endpoint, verb, metadata format, date/set window, maximum batch behavior, retention class, privacy class, and promotion target.

### AgentPlane

Runs the harvest bundle and emits validation, placement, run, replay, promotion, and reversal artifacts.

### Sherlock / Sherlock Search

Indexes receipt packets, normalized metadata records, anomaly packets, and promotion decisions. Search must preserve policy decision refs, evidence refs, freshness, classification, and sensitivity ceiling.

### SocioSphere

Surfaces harvest plans, current cursor state, receipt health, anomaly status, replay status, and promotion decisions as operator-facing control state.

### Memory Mesh / Knowledge Graph / GAIA

Receive only promoted records with receipt and validation lineage. Raw harvest output must not bypass promotion law.

## Minimal conformance invariant

A lawful metadata harvest is invalid if any of these are true:

1. A batch receipt lacks a policy decision reference.
2. A receipt chain skips or rewrites a previous receipt hash without an anomaly.
3. A resumption-token hash repeats in a way that indicates a loop and no `resumption_token_loop` anomaly is recorded.
4. The run is marked completed without a terminal empty-token state.
5. A record is promoted without a validation report reference.
6. A record is promoted without a target-specific policy decision.
7. Raw cursor values or private request parameters are published in a public receipt.

## Non-goals

This pattern is not an OAI-PMH implementation guide.
It is not a crawler framework.
It is not a license to exfiltrate metadata.
It is not a claim that repository output is true.
It is not a substitute for source evaluation, validation, or promotion governance.

## First implementation cut

The first cut should include:

- a JSON schema for a lawful metadata harvest evidence envelope;
- one valid OAI-PMH-style three-batch fixture;
- invalid fixtures for missing policy decision, token loop without anomaly, and promotion without validation;
- a validator script that enforces structural and cross-field invariants;
- downstream binding issues for SourceOS, Policy Fabric, AgentPlane, Sherlock, and SocioSphere.
