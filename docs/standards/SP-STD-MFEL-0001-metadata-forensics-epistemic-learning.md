# SP-STD-MFEL-0001 — Metadata Forensics and Epistemic Learning

Status: v0.1 public-safe standard  
Issue: #52  
Publication state: public  
Runtime claim: none

## Purpose

SP-STD-MFEL-0001 defines the public, evidence-preserving standard for learning from metadata-forensics artifacts and epistemic-threat artifacts without collapsing observation, analysis, suspicion, attribution, or conclusion.

The standard exists because metadata artifacts are easy to overread. A plist key, Spotlight record, microstackshot summary, FileProvider churn event, or rhetorical artifact can be real and still not license actor attribution, compromise attribution, remote exfiltration, or coordinated-threat conclusions.

## Scope

This standard applies to public-safe analysis of:

- macOS metadata artifacts, including Core Spotlight, Notes indexing, FileProvider/iCloud/CloudKit churn, CoreSuggestions adjacency, SpotlightKnowledge processing, boot/reset seams, kernel-panic seams, and microstackshot/resource-pressure summaries;
- epistemic-threat artifacts, including anti-verification rhetoric, self-sealing narrative construction, conspiracy-style evidence inversion, and rhetorical patterns that degrade evidence-seeking behavior;
- mixed cases where local metadata and rhetorical artifacts are used together in a case review.

## Non-scope

This standard does not implement endpoint detection, surveillance, actor attribution, live incident response, malware classification, model training on private content, or production telemetry collection.

It does not allow raw private logs, credentials, account identifiers, device identifiers, private messages, or user content to be committed to the public repository.

## Five-layer rule

Every MFEL case must keep these layers separate:

1. `observed_fact` — what was directly observed or sanitized from source material;
2. `derived_fact` — what was deterministically or boundedly derived from observations;
3. `interpretation` — what the facts may mean, including alternative explanations;
4. `hypothesis` — a candidate explanation with support, negative evidence, and missing evidence;
5. `prohibited_conclusion` — a conclusion the case explicitly does not license.

A standard-conforming case must not collapse these layers. A local indexing artifact may be an observed fact. A possible exfiltration path is a hypothesis. A remote-exfiltration conclusion is prohibited unless discriminating evidence exists.

## Redaction boundary rule

Every MFEL case must declare a `redaction_boundary` with:

- classification: `public`, `public-sanitized`, or `public-synthetic`;
- private-evidence policy;
- public substitute type;
- withheld fields.

Withholding private evidence does not permit vague conclusions. If the public artifact cannot show a necessary evidentiary layer, the case must name the missing evidence rather than imply it.

## Hypothesis discipline

Every suspicious or high-risk hypothesis must include:

- `negative_evidence` — evidence or considerations that weaken the hypothesis;
- `missing_evidence` — evidence that would be needed before promotion;
- `prohibited_conclusions` — claims that are not licensed by the current record.

The schema enforces this for `risk_level: suspicious` and `risk_level: high`.

## Actor-attribution discipline

Actor attribution is prohibited unless it carries:

- actor label;
- attribution basis;
- confidence bound;
- evidence references;
- non-claims.

Unsupported attribution must fail validation. A case may say that actor evidence is absent. It may not imply a real actor from aggregate diagnostics alone.

## Public-safe examples

This standard defines three initial public-safe examples:

- `examples/mfel/notes-spotlight-indexing.sanitized.yaml`;
- `examples/mfel/corespotlight-plist.sanitized.yaml`;
- `examples/mfel/qanon-rhetorical-construction.sanitized.yaml`.

The first two are sanitized macOS metadata cases. The third is a synthetic rhetorical fixture. None describe a live incident, identify a real actor, publish raw private logs, or claim endpoint compromise.

## Schema family

The v0.1 MFEL schema family is isolated under:

```text
schemas/mfel/
```

Current schemas:

- `observation.schema.json` — complete case record with five-layer separation;
- `hypothesis.schema.json` — reusable evidence-bound hypothesis record;
- `evidence-graph.schema.json` — graph structure connecting observations, derivations, interpretations, hypotheses, and prohibited conclusions.

The MFEL namespace is intentionally separate from unresolved core governance schema namespaces. MFEL may reference broader ProCybernetica doctrine, but it does not replace the core controlplane envelope family.

## Validation requirements

A conforming validation lane must check that:

- all MFEL schemas are valid JSON Schema 2020-12;
- all public examples validate;
- layer collapse fails validation;
- suspicious/high-risk hypotheses without negative and missing evidence fail validation;
- unsupported actor attribution fails validation;
- evidence-graph node IDs agree with their declared layers.

The test entrypoint is:

```bash
python -m pytest -q tests/mfel/test_schema_examples.py
```

The default repository test suite should also execute this file.

## Prohibited conclusions

Standard-conforming reports must explicitly prohibit conclusions that the record does not support. Common prohibited conclusions include:

- remote exfiltration from local indexing artifacts alone;
- coordinated compromise from plist churn alone;
- actor attribution from aggregate diagnostics alone;
- rhetorical-actor attribution from synthetic fixtures;
- surveillance or model-training claims from public-safe examples.

## Downstream integration targets

MFEL should later provide adapter or ontology mappings for:

- `SourceOS-Linux/sourceos-syncd` local-first event/evidence models;
- `SocioProphet/sociosphere` case triage and governance workflow;
- `SocioProphet/ontogenesis` evidence/claim ontology and SHACL/JSON-LD vocabulary;
- `HolographMe` human digital twin dignity and consent boundaries;
- Holmes/SlashTopics topic and rhetoric fixtures for evidence-bound model training.

Downstream integration must preserve redaction, consent, non-attribution, missing-evidence, and prohibited-conclusion semantics.

## Non-claims

This standard does not claim that any included example is a live incident. It does not claim compromise, exfiltration, actor identity, coordinated operation, or production runtime readiness. It defines public evidence discipline for case learning.
