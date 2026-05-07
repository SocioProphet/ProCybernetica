# Systema v0 Conformance

Status: candidate conformance spine
Turn: 3 / 28
Owner repository: `SocioProphet/ProCybernetica`

## Purpose

This document defines the first public conformance spine for Systema.

Systema v0 conformance is intentionally small. It does not require every downstream runtime to be complete. It requires that doctrine, claims, projections, membranes, agent actions, metrics, and manuals expose enough structure to be inspected, reviewed, and improved.

## Conformance classes

### S0 — Source-aware

The artifact identifies its source posture.

Required:

- source refs where applicable;
- source confidence if source-derived;
- quote boundary if using source text;
- candidate status for unreviewed extraction;
- no low-confidence OCR as authoritative quotation.

### S1 — Projection-aware

The artifact declares representation boundaries.

Required:

- source surface;
- target surface;
- preserved information;
- lost or distorted information;
- confidence effect;
- review requirement.

### S2 — Triangulated

The artifact or claim has at least three stabilizers.

Required, depending on context:

- assertion + evidence + independent witness;
- implementation + test + provenance;
- actor + policy + receipt;
- artifact + hash + replay;
- model output + source + verifier.

### S3 — Membrane-accounted

The artifact identifies boundaries crossed.

Required:

- admitted inputs;
- blocked inputs/actions;
- transformations;
- logs;
- redactions;
- witness/receipt;
- revocation or rollback path.

### S4 — Tensegrity-stabilized

The system declares local compression members and continuous tension members.

Required:

- compression members;
- tension members;
- stability rule;
- failure modes;
- evidence refs.

### S5 — Metric-accounted

The artifact declares useful output and resource/entropy burden.

Required:

- service/capability output;
- denominator;
- baseline;
- uncertainty;
- evidence refs;
- entropy burden where material.

### S6 — Manualized

The artifact is independently buildable, testable, repairable, and revisable.

Required:

- purpose;
- parts/dependencies;
- build steps;
- validation steps;
- repair steps;
- failure modes;
- known limitations;
- revision history;
- public-safe evidence examples.

## Minimal v0 public-review target

Systema v0 public-review readiness requires:

| Class | Required for v0 public review? |
| --- | --- |
| S0 Source-aware | yes |
| S1 Projection-aware | yes |
| S2 Triangulated | yes for consequential claims/actions |
| S3 Membrane-accounted | yes for boundary-crossing artifacts |
| S4 Tensegrity-stabilized | yes for runtime/agent/system claims |
| S5 Metric-accounted | yes for performance claims |
| S6 Manualized | yes for mature artifacts; candidate for early doctrine |

## Repository expectations

### ProCybernetica

Must provide:

- source-confidence doctrine;
- projection-loss doctrine;
- anti-pattern catalog;
- conformance spine;
- profile layer;
- manual commons.

### Ontogenesis

Must provide:

- concept-entry model;
- source-anchored concept records;
- SHACL gates;
- vocabulary drift detector;
- concept promotion lifecycle.

### Sherlock

Must provide:

- evaluated access result model;
- catalog entries;
- source confidence;
- projection-loss and usefulness fields.

### GAIA

Must provide:

- world-pattern inventory doctrine;
- data tetrahedron model;
- geodesic route relation;
- projection/frequency ledger;
- livingry/resource coordination examples.

### AgentPlane

Must provide:

- tensegrity runtime contract;
- capability-radius examples;
- oversteer indicators;
- evidence/replay linkage.

### SourceOS surfaces

Must provide:

- membrane/state-integrity mapping;
- canonical event evidence;
- repair and redaction evidence;
- operator narrative.

### Delivery Excellence

Must provide:

- Dymaxion metric;
- entropy ledger;
- verified capability per resource burden.

### Platform Standards

Must provide:

- triangulated evidence pattern;
- membrane boundary standard;
- periodic experience standard;
- PR/release templates.

### Prophet Platform

Must provide:

- runtime bridge for Systema evidence refs;
- service-level consumption of upstream contracts;
- smoke validation path.

## Conformance checklist

A Systema artifact should answer:

1. What is it?
2. What source or prior artifact does it derive from?
3. What confidence level applies?
4. What projection occurred?
5. What evidence triangulates it?
6. What membrane was crossed?
7. What authority radius applies?
8. What compression and tension members stabilize it?
9. What resource burden and entropy does it introduce?
10. What manual or validation path lets another party reproduce it?

## Non-conformance examples

- a public claim with no source ref;
- an OCR-derived quote with no confidence state;
- a dashboard metric with no projection-loss disclosure;
- an agent action with no policy decision or receipt;
- a runtime activation with no revocation path;
- a performance claim with no denominator;
- a concept with no owner, aliases, allowed uses, or forbidden uses;
- a catalog item with no validation or availability state;
- a release with no manual or failure-mode section.

## Current status

Candidate conformance spine. Turn 4 should add profiles. Turn 5 should create downstream issues. Later turns should add examples, fixtures, and validators.
