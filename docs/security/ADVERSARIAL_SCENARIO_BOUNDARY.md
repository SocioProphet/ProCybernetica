# Adversarial Scenario Boundary Doctrine

**Status:** Draft v0.1  
**Track:** Security, assurance, and downstream runtime governance  
**Purpose:** Define the boundary between attack-technique mappings, governed adversarial scenarios, authority, evidence, promotion, memory, and downstream execution surfaces.

---

## 1. Purpose

This doctrine extends `docs/security/THREAT_MODEL.md` with the scenario-level boundary needed by SCOPE-D, Ontogenesis, Prophet Workspace, Memory Mesh, Prophet Platform, and GAIA.

MITRE ATT&CK, MITRE ATLAS, D3FEND, local SourceOS/SCOPE-D techniques, and related taxonomies are useful controlled vocabularies. They are not complete scenario models. A mapped technique is not authority, proof, attribution, scenario completeness, claim promotion, or permission to execute.

The governing object for platform work is therefore the adversarial scenario: a composition record that binds objective, topology, channel substrate, interface crossing, authority, safety boundary, evidence, technique annotations, runtime decisions, memory effects, claim-promotion state, consequence, abstention rules, and non-claims.

---

## 2. Controlling rule

A technique mapping may annotate a scenario. It must not substitute for scenario governance.

This rule applies to ATT&CK, ATLAS, D3FEND, OWASP, CAPEC, CWE, CVE, SourceOS-local technique identifiers, and any later generated import lane.

A technique mapping does not establish:

- authorization to observe, probe, execute, mutate, deliver, collect, or destroy;
- engagement authorization;
- production/live-target permission;
- attribution;
- evidence sufficiency;
- claim-promotion eligibility;
- memory writeback eligibility;
- reportability;
- product safety posture;
- completeness of a scenario.

---

## 3. Required scenario semantics

A governed adversarial scenario should declare or reference:

- scenario identity and version;
- scenario class;
- adversarial objective or defensive hypothesis;
- target topology;
- channel substrates;
- interface crossings;
- authority envelope;
- safety boundary references;
- capability exposure;
- human interpretation risk;
- machine interpretation risk;
- trust-edge usage;
- boundary events;
- evidence records;
- attack-technique annotations, when applicable;
- control references;
- proof references;
- runtime-decision receipt references;
- memory effects;
- claim-promotion state;
- consequence model;
- abstention rules;
- counterfactual branches;
- semantic non-claims;
- redaction state.

SCOPE-D owns the executable JSON contract for this scenario composition object. Ontogenesis owns RDF/SHACL semantic projection. ProCybernetica owns this doctrine and the promotion/authority/evidence boundary. Downstream platform and workspace repositories consume these contracts without weakening them.

---

## 4. Repository ownership

### 4.1 ProCybernetica

ProCybernetica owns doctrine, promotion law, authority boundaries, evidence boundaries, publication boundaries, non-claim discipline, and public-review conformance posture.

This repository does not own SCOPE-D runtime execution, Ontogenesis semantic release discipline, Memory Mesh durable writeback, Prophet Workspace channel implementations, Prophet Platform runtime services, or GAIA curation vault mechanics.

### 4.2 SCOPE-D

SCOPE-D owns Wargames execution contracts, boundary events, evidence records, coverage claims, runtime decision receipts, safety-boundary fixtures, dry-run/live-read-only gates, proof artifacts, and report-only/synthetic run outputs.

SCOPE-D should define the machine-checkable adversarial scenario composition schema and validators that bind these existing records into a scenario object.

### 4.3 Ontogenesis

Ontogenesis owns ontology-native representation of agentic purple-team loops, ATT&CK/ATLAS/local technique alignment, SHACL gates, and semantic export surfaces.

Ontogenesis should extend the existing agentic-purple-team/MITRE alignment surface rather than create a disconnected duplicate ontology.

### 4.4 Memory Mesh

Memory Mesh owns durable memory proposal and writeback governance.

Scenario learning, memory effects, and post-run memory updates must route through review-only proposal contracts unless a later approved governance flow explicitly permits durable writeback.

### 4.5 Prophet Workspace

Prophet Workspace owns workspace product semantics and capability contracts for mail, calendar, contacts, files, documents, chat, rooms, meetings, admin, audit, policy, and search.

Workspace channels are governed substrates. They are not neutral transports. Interface crossings such as email-to-ticket, chat-to-agent-action, calendar-to-policy-exception, and document-to-memory must be modelable as scenario surfaces.

### 4.6 Prophet Platform

Prophet Platform owns runtime services, deployment topology, platform contracts, telemetry, APIs, dashboards, and operator surfaces that consume upstream standards.

Platform integration must consume scenario objects as governed inputs. It must not treat ATT&CK coverage, model summaries, or synthetic run artifacts as standalone production findings.

### 4.7 GAIA World Model

GAIA owns external source pinning, provenance, manifests, file hashes, attributable source records, and reproducible curation reports for public evidence used by scenario work.

GAIA evidence may support a scenario. It does not itself promote a claim.

---

## 5. Non-claims

The following are explicitly non-claims:

- An ATT&CK mapping is not proof of compromise.
- An ATT&CK mapping is not authorization to execute a procedure.
- An ATT&CK mapping is not engagement authorization.
- An ATT&CK mapping is not attribution.
- A synthetic scenario is not production observation.
- A dry-run receipt is not evidence of live execution.
- A model-generated summary is not source evidence.
- A public threat report is not local evidence unless pinned, classified, and related to a scenario record.
- A memory effect is not durable memory writeback.
- A learning recommendation is not canonized doctrine.
- A scenario report is not claim promotion unless promotion gates pass.
- A dashboard coverage cell is not safety assurance.

---

## 6. Safety and authority requirements

A scenario must fail closed when authority is absent, ambiguous, expired, or insufficient for the requested action class.

The following action classes require explicit authority and safety-boundary treatment before any downstream runtime can treat them as executable, even in limited form:

- live target access;
- network access;
- command execution;
- credential access;
- payload delivery;
- state mutation;
- destructive behavior;
- deployment;
- external tool invocation;
- memory writeback;
- claim promotion;
- public report publication.

If a scenario is synthetic, redacted, report-only, dry-run, or learning-mode, downstream systems must preserve that state in receipts, reports, dashboards, memory proposals, and platform surfaces.

---

## 7. Evidence and promotion requirements

Evidence must remain distinct from authority.

A scenario may reference direct evidence, corroborating evidence, contradictory evidence, absent-expected evidence, summary evidence, or proof digests. Promotion rules must distinguish these roles.

Summary-only or model-generated evidence must not promote to a finding without corroborating/direct evidence and an explicit promotion decision.

Public-source evidence from GAIA or other curation lanes must remain source-pinned and provenance-classified. External public intelligence may support a hypothesis, but it must not automatically become local observation or local attribution.

Promotion by prose is forbidden. Promotion must be typed, evidence-linked, and reviewable.

---

## 8. Memory requirements

Memory is state, not authority.

Scenario memory effects must be explicit. Examples include:

- false continuity;
- stale policy resurrection;
- entity merge error;
- identity split;
- malicious or lossy summary;
- privilege hidden in context;
- poisoned embedding;
- sandbox-to-canon leakage;
- invalid claim promotion.

A scenario may recommend a learning update. That recommendation must not become durable memory unless routed through Memory Mesh review-only proposal governance or a later explicitly approved writeback flow.

---

## 9. Channel and interface requirements

Channel substrates must be represented when they affect trust, interpretation, authority, auditability, or consequence.

Relevant substrates include email, SMS, voice, video, calendar, chat, ticketing, browser, GitHub, CI/CD, API, OAuth, documents, model context, vector memory, agent tool calls, dashboards, report exports, support portals, vendor consoles, and workspace workrooms.

Interface crossings are first-class scenario events when meaning, authority, or evidence changes while moving between substrates. Examples:

- email becomes ticket;
- chat request becomes agent tool call;
- document summary becomes memory proposal;
- GitHub issue becomes branch/CI activity;
- vendor message becomes policy exception;
- synthetic artifact becomes report export;
- dashboard cell becomes executive decision.

These crossings are attack surfaces even when each individual action looks normal.

---

## 10. Abstention requirements

Abstention is a valid and sometimes required control outcome.

A governed system should abstain from:

- attribution when evidence is insufficient;
- execution when authority is insufficient;
- memory writeback when evidence or tenant scope is insufficient;
- claim promotion when non-claims are unresolved;
- publication when redaction/publication boundary review has not passed;
- dashboard elevation when a record is synthetic, dry-run, or report-only;
- tool invocation when capability exposure is ambiguous.

An abstention result should emit a receipt or reviewable trace where the owning contract requires one.

---

## 11. Minimum implementation path

The minimum compliant implementation path is:

1. ProCybernetica records this scenario boundary doctrine.
2. SCOPE-D adds a Wargames adversarial scenario composition schema above existing boundary/evidence/coverage/receipt contracts.
3. SCOPE-D adds semantic validators and negative fixtures that reject ATT&CK-only completeness, synthetic promotion, summary-only finding promotion, and memory-writeback bypass.
4. Ontogenesis extends the existing agentic-purple-team/MITRE alignment ontology with scenario/channel/interface/memory/consequence/abstention semantics.
5. Memory Mesh adds a scenario-learning binding that routes learning into review-only proposal governance.
6. Prophet Workspace adds channel-substrate/interface-crossing contracts for workspace surfaces.
7. Prophet Platform adds a scenario-reference binding before any operator UI.
8. GAIA adds source-pinning support for public security-intelligence sources used by generated imports or scenario evidence.

---

## 12. Acceptance criteria for downstream work

A downstream implementation is aligned with this doctrine only if:

- ATT&CK/ATLAS/local technique mappings are treated as annotations;
- scenario records include safety, evidence, authority, non-claims, and redaction state;
- synthetic/dry-run/report-only status cannot be hidden in exports;
- memory updates route through Memory Mesh governance;
- workspace channel/interface crossings are explicit when relevant;
- model-generated summaries are not treated as source evidence;
- public-source intelligence is pinned before being used as evidence support;
- runtime/platform surfaces preserve blocked, abstained, and review-required outcomes;
- reports state what is not claimed.

---

## 13. Relationship to the threat model

This doctrine is subordinate to and extends `docs/security/THREAT_MODEL.md`.

The threat model identifies authority attacks, runtime attacks, monitoring attacks, evidence attacks, promotion attacks, release attacks, publication attacks, and required controls. This document defines the scenario-level composition boundary that allows those controls to be applied coherently across SCOPE-D Wargames contracts, Ontogenesis semantic alignment, Memory Mesh learning governance, workspace substrates, platform runtime, and GAIA source curation.
