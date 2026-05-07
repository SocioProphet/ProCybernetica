# Source Confidence and Projection Loss

Status: candidate evidence doctrine
Turn: 2 / 28
Owner repository: `SocioProphet/ProCybernetica`

## Purpose

This document defines the evidence posture for source-derived doctrine in Systema.

It exists because the Fuller/Synergetics source-card package contains mixed-confidence material: visual-only cards, sparse OCR, partial OCR, near-verbatim fragments, diagrams, and manual-review candidates. Systema must not turn weak extraction into authoritative doctrine.

## Rule

A representation is not the source.

A source image, OCR fragment, transcript, summary, concept record, ontology node, search result, dashboard card, embedding, map tile, or agent memory is a projection of some prior surface.

Every projection can preserve information, lose information, distort information, or create false confidence.

## Source confidence scale

| Level | Meaning | Allowed use |
| --- | --- | --- |
| A | manually verified against source artifact or stable published text | load-bearing quotation, reviewed concept definition |
| B | mostly usable OCR/text with review still required | provisional paraphrase, candidate concept support |
| C | partial OCR or near-verbatim fragments | candidate doctrine only |
| D | sparse OCR or primarily visual/diagram source | visual/source anchor only |
| E | visual-only or low OCR | manual review required before any textual claim |

## Review states

| State | Meaning |
| --- | --- |
| `unreviewed` | extracted or inferred, not manually checked |
| `candidate` | plausible but not load-bearing |
| `manually_reviewed` | human checked against visible source or trusted transcript |
| `independently_verified` | confirmed against independent source or stable publication |
| `rejected` | extraction or interpretation failed review |
| `contested` | conflicting evidence or unresolved interpretation |

## Quote boundary

Every source-derived statement should identify its quote boundary:

| Boundary | Meaning |
| --- | --- |
| `exact` | exact quotation verified at sufficient confidence |
| `near_verbatim` | close OCR/manual transcription, still subject to review |
| `paraphrase` | meaning-preserving restatement |
| `operational_translation` | doctrine translated into system design language |
| `analogy` | conceptual similarity, not proof |
| `unsupported` | not admissible |

## Source confidence record

Recommended record shape:

```yaml
source_confidence_record:
  source_ref: required
  source_kind: image | pdf | transcript | book | patent | lecture | marginalia | diagram | manual | other
  extraction_confidence: A | B | C | D | E
  review_state: unreviewed | candidate | manually_reviewed | independently_verified | rejected | contested
  quote_boundary: exact | near_verbatim | paraphrase | operational_translation | analogy | unsupported
  extracted_by: required
  reviewed_by: optional
  review_date: optional
  uncertainty_notes: required_if_not_A
  promoted_claim_refs: []
  prohibited_uses: []
```

## Projection-loss record

Recommended record shape:

```yaml
projection_loss_record:
  projection_id: required
  source_surface: required
  target_surface: required
  transformation:
    - OCR
    - summarization
    - paraphrase
    - embedding
    - ontology_mapping
    - map_projection
    - dashboard_aggregation
    - model_inference
    - code_generation
    - other
  preserves: []
  loses: []
  distortion_risks: []
  confidence_effect: required
  evidence_refs: []
  review_required: boolean
```

## Mandatory projection-loss cases

Projection-loss reporting is required when a transformation affects:

- public claims;
- promotion decisions;
- scoring or dashboard results;
- ontology assertions;
- source quotations;
- agent memory;
- GAIA map/world-model layers;
- Sherlock catalog results;
- runtime or policy actions;
- legal, safety, deployment, or trust posture.

## Common projection risks

| Risk | Description | Control |
| --- | --- | --- |
| OCR hallucination | OCR creates plausible but false text | source confidence and manual review |
| summary overreach | summary claims more than source supports | claim boundary and source refs |
| analogy laundering | metaphor becomes implied proof | quote boundary and claim level |
| flat-map fallacy | representation is mistaken for territory | projection-loss record |
| embedding opacity | vector similarity hides source reasoning | source/citation requirements |
| dashboard false confidence | aggregation suppresses uncertainty | confidence badges and drilldown |
| stale projection | representation no longer matches source | valid-time and transaction-time checks |
| vocabulary drift | same term means different things across repos | concept dictionary and drift gate |

## Claim promotion interaction

A claim may not move from `candidate` to `validated` unless source confidence and projection-loss posture are compatible with the claim's use.

Minimum rule:

```text
candidate claim + low source confidence -> stays candidate
candidate claim + manual review + evidence refs -> may become reviewed
reviewed claim + independent witness + validation -> may become validated
validated claim + contradiction -> becomes contested or retracted until resolved
```

## Source-derived doctrine interaction

Fuller/Synergetics concepts should be treated as follows:

| Source material | Default status | Required before standardization |
| --- | --- | --- |
| exact verified quotation | reviewed source | source ref and quote boundary |
| OCR-derived quotation | candidate | manual review |
| diagram-derived insight | candidate visual doctrine | diagram anchor and interpretation notes |
| user extraction summary | candidate operational translation | source-card anchor and review state |
| estate design translation | proposal | owning repo, example, and validation path |

## Repository implications

### ProCybernetica

Defines source-confidence and projection-loss law.

### Ontogenesis

Should encode source confidence, concept promotion, vocabulary drift, and projection-loss refs in concept/claim ontology.

### Sherlock

Should expose confidence, source, projection, usefulness, and trust signals in catalog results.

### GAIA

Should expose projection, frequency, source, uncertainty, and valid-time metadata for world-pattern layers.

### AgentPlane

Should preserve context-pack, policy, evidence, and replay projection boundaries in execution artifacts.

### SourceOS

Should distinguish raw logs, coalesced events, redacted events, operator narratives, and public-safe evidence as different projection surfaces.

### Delivery Excellence

Should count projection loss, stale context, vocabulary drift, and manual-review debt as entropy.

## Conformance questions

A reviewer should ask:

1. What is the source surface?
2. What is the target representation?
3. What changed during projection?
4. What was preserved?
5. What was lost?
6. What confidence level remains?
7. What claim level is allowed?
8. Is manual review required?
9. Is the result public-safe?
10. What downstream action depends on it?

## Current conclusion

Source confidence and projection loss are not documentation niceties. They are constitutional controls. Without them, a cybernetic knowledge system will convert weak signals into false authority.
