# Reciprocal Channel Governance

**Status:** Draft v0.1  
**Track:** ProCybernetica frontier governance doctrine  
**Scope:** Doctrine and conformance vocabulary only; downstream runtime implementation remains in owning repositories.

## Purpose

This doctrine establishes reciprocal channel governance for human-machine cybernetic systems.

A cybernetic system does not receive unmediated truth. It receives channel-conditioned signals, percepts, projections, reports, traces, and signs. Those inputs become operationally meaningful only after the system records provenance, confusability, interpretive uncertainty, authority, and repair conditions.

The reciprocal form is essential: humans must reason about machine percepts, and machines must reason about human percepts. Neither side should treat the other's interface rendering as direct access to reality.

## Core rule

No channel-conditioned percept may become durable memory, graph truth, operational claim, policy decision, publication, deletion, or high-risk action without explicit provenance, confidence typing, authority envelope, and repair path.

## Human-machine reciprocal principle

Humans and machines are both channel-conditioned observers.

A machine reading human speech, text, gesture, correction, approval, or refusal must preserve the distinction between signal, percept, interpretant, confidence, authority, and action.

A human reading machine output, including dashboards, summaries, graph projections, confidence scores, CI badges, telemetry alerts, memory cards, and agent reports, must be shown enough channel basis and uncertainty to avoid over-trusting a lossy projection.

## Definitions

### Channel

A governed path by which a human, machine, agent, or system receives, renders, transforms, or acts on information.

Channels include biological sense channels, communication channels, software telemetry channels, connector channels, event streams, model-output channels, memory retrieval channels, graph traversal channels, dashboards, reports, and operational action paths.

### Sense channel

A channel with perceptual semantics: it produces observations or percepts under substrate-specific limits.

Human examples include audition, vision, touch, proprioception, vestibular sensing, interoception, speech perception, text perception, gesture perception, and social perception.

Machine examples include logs, metrics, traces, file diffs, API responses, CI runs, model outputs, embeddings, memory retrievals, graph slices, webhook events, and sensor feeds.

### Signal

The channel substrate before interpretation. Examples include waveform segments, glyphs, pixels, event payloads, log lines, metric samples, file diffs, API responses, sensor packets, and human utterances.

### Percept

The received or extracted form produced by a channel or capture method. A transcript, OCR result, parsed log event, extracted graph edge, model summary, retrieved memory, dashboard panel, and CI badge are percepts, not facts.

### Interpretant

The meaning or actionable reading inferred from a percept. Interpretants may include instruction, claim, preference, threat, approval, refusal, relation, state change, correction, evidence, or action request.

### Confusable

A candidate interpretation that can be mistaken for another under a channel condition. Confusables include homophones, ASR alternatives, OCR lookalikes, Unicode homoglyphs, stale telemetry, flaky CI, model hallucinations, inferred graph edges, ambiguous gestures, social-pragmatic ambiguity, and summary omissions.

### Collapse decision

A governed choice to select one interpretation from a candidate set. Collapse is an accountable action whenever it affects memory, graph state, claims, policy, publication, authorization, or external action.

### Repair event

An active sensing step used to reduce ambiguity or prevent unsafe collapse. Repair events include clarification, rerun, corroboration, reparse, source inspection, alternate-channel confirmation, provenance check, user confirmation, revalidation, and deferral.

### Projection

A lossy rendering of a larger state for human or machine consumption. Summaries, dashboards, graph neighborhoods, embeddings, status reports, memory cards, and agent handoffs are projections. Projections require declared source basis and loss profile before they support consequential decisions.

### Channel authority envelope

The allowed and disallowed effects of a channel. The envelope states whether a channel may display, suggest, write candidate memory, write confirmed memory, create graph edges, propose claims, promote claims, bind policy, trigger actions, publish, delete, or authorize another agent.

## Control principles

### 1. No direct-reality axiom

A cybernetic agent receives mediated measurements, messages, traces, and signs. It does not receive unmediated truth.

### 2. Channel-substrate separation

Audio, text, image, gesture, telemetry, biological state, graph traversal, model output, memory retrieval, and dashboard rendering have different error geometries. Their confidence and authority must not be collapsed into a single generic score.

### 3. Percept/interpretant distinction

The received form and the meant or actionable form are not identical. Systems must preserve the difference between what was captured, what was inferred, and what was confirmed.

### 4. Ambiguity preservation before collapse

Plausible alternatives should be preserved until context, corroboration, repair, or action-risk pressure justifies narrowing.

### 5. Collapse accountability

When a system selects one interpretation from several candidates, and that selection affects a durable or consequential sink, the selection must be recorded as a collapse decision.

### 6. Repair as active sensing

Repair is not an afterthought. Clarification, rerun, corroboration, re-ingestion, alternate-channel confirmation, and deferral are part of cybernetic sensing.

### 7. Human-facing legibility

Machine percepts must be rendered so humans can correctly reason about source basis, uncertainty, coverage gaps, staleness, inferred status, and allowed use.

### 8. Action authority bounded by channel certainty

High-risk actions require stronger channel certainty, stronger provenance, and stronger repair than reversible or low-risk actions.

### 9. Projection accountability

A projection must declare its source channels, projection method, loss mode, omissions, freshness window, and allowed/disallowed decisions before it is used for governance or action.

### 10. Memory and graph sinks are high consequence

Durable memory writes and graph edge creation require stricter gates than transient conversation state because they contaminate future perception, retrieval, planning, and authority.

### 11. Power-aware channel governance

Some channels become institutional authority surfaces. Dashboards, model summaries, graph edges, alerts, and agent reports can dominate human judgment. Channel governance must prevent weak percepts from becoming official reality through fluency, visualization, or repetition alone.

### 12. Privacy and observer-profile limits

Observer profiles may be used only to improve safety, accessibility, repair, and interpretability. They must remain scoped, revisable, auditable, and minimally invasive. Sensitive identity claims require explicit authorization or a stronger lawful basis.

## Required channel record fields

A governed channel record should declare at least:

- `channel_id`
- `channel_class`
- `substrate`
- `producer`
- `consumer`
- `capture_method`
- `trust_boundary`
- `known_confusability_modes`
- `confidence_type`
- `provenance_ref`
- `allowed_sinks`
- `disallowed_sinks`
- `repair_protocols`
- `expiry_policy`
- `promotion_rules`

## Required collapse record fields

A collapse decision should declare at least:

- `collapse_id`
- `source_observation_ref`
- `candidate_interpretants`
- `selected_interpretant_ref`
- `decision_basis`
- `confidence_type`
- `authority_envelope_ref`
- `downstream_sink`
- `reversibility`
- `repair_events`
- `residual_uncertainty`

## Downstream implications

### Memory Mesh

No durable memory without channel lineage. Memory records should distinguish observed, inferred, confirmed, operational, stale, contested, and superseded memory.

### Entity graph

No durable graph edge without evidence class, source channel, promotion state, temporal scope where relevant, and allowed consumers. Inferred edges must not masquerade as confirmed edges.

### Holography and projection systems

No projection without source basis and loss profile. Dashboards, summaries, graph slices, memory cards, embeddings, and agent handoffs must declare coverage and omission boundaries.

### Prophet Platform

Runtime ingestion, normalization, memory-write gates, graph-write gates, action gates, and human-facing uncertainty rendering should consume this doctrine as implementation law.

### Superconscious

Superconscious may coordinate channel-aware agent behavior, preserve alternates, and trigger repair, but it does not own this doctrine. It must cite ProCybernetica and downstream formalizations as authority.

### GAIA world-model layer

External-world evidence must be tagged by source channel, provenance, freshness, confusability class, and corroboration status.

### SCOPE-D and Wargames

Adversarial validation should include ASR confusion, OCR confusables, Unicode homoglyphs, prompt injection, poisoned memory, graph edge poisoning, forged logs, stale telemetry, malicious projections, and over-authoritative agent reports.

### Alexandrian Academy

Humans need literacy for reading machine percepts. Training material should teach how to inspect source basis, projection loss, confidence type, and allowed use.

## Non-claims

This document does not implement runtime services, memory services, graph services, platform orchestration, telemetry collection, model execution, agent execution, or live policy enforcement.

This document does not claim that all human senses are reducible to machine channels, or that machine channels are equivalent to biological perception.

This document does not endorse a fixed count of human senses. It uses sense-channel as an operational category for mediated observation and error analysis.

This document does not permit inferred human affect, stress, identity, disability, health status, or protected traits to be stored or acted upon without appropriate authorization, scope, and safety controls.

## Minimum conformance posture

A downstream system is minimally channel-governed only if it can answer:

1. What channel produced this percept?
2. What confusables were possible?
3. What interpretant was selected?
4. Was a collapse decision made?
5. What provenance supports the selection?
6. What authority does the channel have?
7. What sinks may this percept affect?
8. What repair path exists?
9. What uncertainty remains?
10. How is the result rendered legibly to humans or machines?
