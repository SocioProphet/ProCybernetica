# Synergetic Cybernetics Anti-Patterns

Status: candidate doctrine
Turn: 3 / 28
Owner repository: `SocioProphet/ProCybernetica`
Related files:

- `docs/integration/SYSTEMA_PATTERN_INVENTORY_CONTROL.md`
- `docs/source-captures/FULLER_SYNERGETICS_COMPLETION_CAPTURE.md`
- `docs/doctrine/SYNERGETIC_CYBERNETICS_ALIGNMENT.md`
- `docs/evidence/SOURCE_CONFIDENCE_AND_PROJECTION_LOSS.md`

## Purpose

This document records failure modes for Systema.

A doctrine is incomplete unless it defines how it fails. These anti-patterns prevent the estate from converting source fragments, projections, metaphors, agent outputs, and dashboards into false authority.

## Governing rule

A Systema artifact is suspect when it increases apparent coherence while reducing source traceability, reviewability, reversibility, or evidence strength.

## Anti-pattern catalog

### Static snapshot fallacy

Treating a dynamic system as a frozen state.

Symptoms:

- dashboards without valid-time or transaction-time;
- memory packs without freshness horizon;
- repo inventories without update cadence;
- agent plans that ignore drift;
- claims that do not expire, refresh, or become stale.

Controls:

- periodic experience profile;
- replay window;
- drift indicator;
- freshness horizon;
- state transition record.

### Flat-map fallacy

Treating a projected representation as the world.

Symptoms:

- embedding similarity presented as truth;
- map layer presented without projection or distortion;
- dashboard rollup without uncertainty;
- OCR treated as exact text;
- summary treated as source.

Controls:

- projection-loss record;
- source confidence record;
- drilldown to source;
- confidence badge;
- forbidden promotion without review.

### Token-word fallacy

Treating words as interchangeable tokens rather than shared experience contracts.

Symptoms:

- same term means different things across repos;
- prompt vocabulary drifts from schema vocabulary;
- UI label does not match ontology class;
- policy term has no operational definition;
- alias becomes a new concept without review.

Controls:

- concept dictionary entry;
- alias registry;
- vocabulary drift detector;
- allowed and forbidden use fields.

### Search-result fallacy

Treating retrieval as evaluation.

Symptoms:

- search returns similar text without trust basis;
- no usefulness or availability signal;
- no provenance refs;
- no public release posture;
- no reproduction path.

Controls:

- catalog-as-access-device result;
- evaluated result fields;
- source confidence;
- reproducibility and cost/burden fields.

### Untriangulated claim fallacy

Promoting a claim on assertion alone.

Symptoms:

- claim has no source;
- implementation has no test;
- artifact has no hash;
- agent output has no verifier;
- policy decision has no receipt.

Controls:

- assertion + evidence + independent witness;
- implementation + test + provenance;
- actor + policy + receipt;
- artifact + hash + replay.

### Unbounded agent fallacy

Giving an agent tools without declaring reach, membrane, evidence, and revocation.

Symptoms:

- tool grants without scope;
- cross-repo mutation without work order;
- runtime side effects without receipt;
- no action radius;
- no revocation path.

Controls:

- capability-radius class;
- membrane boundary record;
- policy decision refs;
- replay envelope;
- revocation rule.

### Compression-without-tension fallacy

Adding services, repos, agents, models, or tools without continuous policy/evidence/provenance tension.

Symptoms:

- new runtime has no policy link;
- new schema has no owner;
- new service emits no receipts;
- new model route has no replay or evaluation;
- new repo has no conformance path.

Controls:

- tensegrity runtime contract;
- declared compression member;
- declared tension members;
- stability and failure-mode rules.

### Dymaxion slogan fallacy

Claiming more-with-less without denominator, baseline, or evidence.

Symptoms:

- vague efficiency claim;
- no resource denominator;
- no baseline;
- no uncertainty;
- no receipts.

Controls:

- Dymaxion service metric;
- verified capability per resource;
- entropy adjustment;
- evidence refs.

### Catalog rot

Letting a registry become an unevaluated dump.

Symptoms:

- tools listed without status;
- no availability signal;
- no owner;
- no validation command;
- no revision history;
- stale entries stay visible as authoritative.

Controls:

- catalog entry lifecycle;
- usefulness and readiness fields;
- review cadence;
- deprecation state.

### Manual gap

Having architecture without buildable, repairable, testable instructions.

Symptoms:

- no quickstart;
- no validation command;
- no known limitations;
- no repair steps;
- no failure modes;
- no public-safe evidence example.

Controls:

- manual commons gate;
- release readiness checklist;
- failure-mode section;
- repair plan.

### Source laundering

Promoting weak extraction, visual inference, or OCR fragments into authoritative doctrine.

Symptoms:

- source confidence absent;
- quote boundary absent;
- low-confidence text quoted as exact;
- visual diagram interpreted without uncertainty;
- user extraction treated as source text.

Controls:

- source-confidence record;
- quote boundary;
- review state;
- candidate-only default;
- independent verification for load-bearing quotation.

### Analogy-as-proof

Using useful design analogy as evidence for mathematical, scientific, legal, or operational truth.

Symptoms:

- Fuller term used as proof;
- metaphor replaces validation;
- concept similarity replaces causal evidence;
- design doctrine bypasses tests.

Controls:

- claim level;
- allowed use / forbidden use;
- proof boundary;
- validation requirement.

### Cybernetic oversteer

Feedback causes oscillation rather than convergence.

Symptoms:

- repeated plan reversals;
- patch churn;
- issue churn;
- policy flip-flops;
- agent retries with expanding scope;
- repeated failed validation loops.

Controls:

- oversteer indicators;
- damping rule;
- escalation threshold;
- stop condition;
- postcondition / divergence evidence.

### Phase-parity loss

A source anchor or invariant is lost as an idea moves through phases.

Symptoms:

- concept becomes schema but loses source refs;
- fixture loses claim level;
- implementation loses policy refs;
- release loses validation evidence;
- public claim loses uncertainty.

Controls:

- phase parity check;
- source anchor preservation;
- evidence refs at every phase;
- projection-loss update.

## Review questions

A reviewer should ask:

1. What is being represented?
2. What is the source?
3. What changed during representation?
4. What evidence triangulates the claim?
5. What membrane was crossed?
6. What authority radius applies?
7. What tension members stabilize the component?
8. What entropy does this introduce?
9. What manual lets another party reproduce it?
10. What failure mode would invalidate it?

## Current status

These anti-patterns are candidate conformance controls. They become validated when downstream profiles, examples, and tests land in the owning repos.
