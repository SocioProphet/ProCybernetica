# Membrane Boundary Pattern

Status: candidate pattern
Turn: 3 / 28
Owner repository: `SocioProphet/ProCybernetica`
Expected downstream owners: SourceOS, AgentPlane, Policy Fabric, Prophet Platform Standards

## Purpose

A membrane is an active cybernetic boundary.

It is not merely a wall or permission bit. It is a surface that admits, blocks, transforms, logs, redacts, witnesses, and revokes crossings.

## Membrane functions

A membrane can act as:

- boundary;
- privacy surface;
- policy gate;
- session shell;
- sandbox;
- redaction layer;
- projection surface;
- routing filter;
- evidence transformer;
- actuation boundary;
- public/private publication boundary.

## Required membrane record

```yaml
membrane_boundary:
  membrane_id: required
  owner_repo: required
  boundary_kind:
    - policy
    - privacy
    - runtime
    - session
    - source_projection
    - publication
    - network
    - model_route
    - map_layer
    - evidence_export
    - other
  admits: []
  blocks: []
  transforms: []
  logs: []
  witnesses: []
  redacts: []
  revokes: []
  policy_refs: []
  evidence_refs: []
  replay_refs: []
  failure_modes: []
```

## Crossing rule

A consequential crossing should leave a record.

Examples:

| Crossing | Required evidence |
| --- | --- |
| private source -> public summary | redaction policy + source confidence + projection-loss record |
| agent proposal -> repo branch | work order + policy decision + branch evidence |
| runtime dry run -> activation | activation decision + capability grant + replay/evidence artifact |
| raw log -> operator narrative | raw evidence ref + coalescing rule + redaction record |
| map data -> public layer | source license + projection/frequency ledger + uncertainty |
| model route -> provider | policy decision + route evidence + prompt/hash boundary |

## Source-confidence membrane

The Fuller/Synergetics source cards cross several membranes:

```text
image -> OCR -> source-card ledger -> extraction summary -> operational doctrine -> repo artifact
```

Each crossing must preserve source confidence and projection loss.

## SourceOS membrane examples

SourceOS surfaces should treat these as membranes:

- local shell session;
- browser history/event capture;
- redaction tombstone;
- state repair preview;
- local-only HTTP endpoint;
- boot/update receipt;
- remote trust lookup boundary.

## AgentPlane membrane examples

AgentPlane surfaces should treat these as membranes:

- bundle validation;
- executor placement;
- run activation;
- policy admission;
- workspace operation;
- external provider route;
- promotion/reversal;
- replay sealing.

## GAIA membrane examples

GAIA surfaces should treat these as membranes:

- source ingest;
- license/attribution gate;
- projection to tile/layer;
- uncertainty envelope;
- action scenario boundary;
- public layer export.

## Sherlock membrane examples

Sherlock surfaces should treat these as membranes:

- corpus ingest;
- semantic projection;
- ranking;
- snippet generation;
- catalog entry promotion;
- public answer generation.

## Failure modes

- silent crossing;
- unlogged redaction;
- policy decision without receipt;
- public summary without source confidence;
- agent action without scope;
- runtime activation without revocation path;
- projection without declared loss;
- private data leakage;
- false-public artifact classification.

## Conformance questions

1. What membrane was crossed?
2. What was admitted?
3. What was blocked?
4. What was transformed?
5. What was logged?
6. What was redacted?
7. What witnessed the crossing?
8. What can revoke the crossing or downstream authority?
9. What evidence survives public release?
10. What failure mode remains?

## Current status

Candidate pattern. Turn 4 should add a machine-readable profile. Downstream repos should then add concrete examples.
