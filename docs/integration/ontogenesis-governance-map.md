# Ontogenesis Governance Map

Status: initial integration map

Turn: 4 / 20

## Purpose

This document maps ProCybernetica claim, provenance, ontology, and promotion doctrine to `SocioProphet/ontogenesis`.

The goal is to prevent ProCybernetica from duplicating ontology release discipline, SHACL promotion gates, ledger generation, signatures, SBOMs, namespace ownership, module layout, or SHIR authority.

ProCybernetica owns public constitutional semantics and conformance expectations for cybernetic systems. Ontogenesis owns ontology-governed semantic authority, module lifecycle, validation, and release mechanics.

## Source basis

Primary ontogenesis sources checked:

- `SocioProphet/ontogenesis/README.md`
- `SocioProphet/ontogenesis/docs/README.md`
- `SocioProphet/ontogenesis/docs/specs/audit_policy.md`
- `SocioProphet/ontogenesis/docs/specs/shir-v0.1.md`

Primary ProCybernetica sources:

- `docs/source-captures/PRELUDE_F_ONTOLOGY_CORPUS_SEMANTIC_CONTRACTS_CAPTURE.md`
- `docs/integration/semantic-serdes-shir-map.md`
- `schemas/claim.schema.json`
- `schemas/provenance_record.schema.json`
- `schemas/artifact_envelope.schema.json`
- `schemas/promotion_decision.schema.json`

## Ownership boundary

| Surface | Ontogenesis owns | ProCybernetica owns |
| --- | --- | --- |
| Ontology modules | Upper, Middle, Lower, Domains, Platform, prophet, epi modules | Cybernetic use of ontology modules inside node/world-model/promotion law |
| SHACL gates | Shape bundles and module-local validation gates | Requirement that hard-lane claims pass validation before promotion |
| Module registry | `catalog/registry.ttl` and module metadata | References to ontology/module versions in claims, policies, and provenance |
| Build distribution | `dist/` deterministic generated outputs | Referencing released ontology artifacts as evidence inputs |
| Audit outputs | `audit/` manifests and reports | Public evidence and replay interpretation of those reports |
| Ledger and signatures | `ledger/`, signature pointers, deterministic release evidence | ProvenanceRecord / ArtifactEnvelope references to those receipts |
| SPDX/SBOM | SBOM emission for ontology release artifacts | Public conformance requirement to preserve artifact identity and release evidence |
| SHIR spec | Ontogenesis-owned semantic hyperknowledge contract | ProCybernetica semantic governance and promotion interpretation |
| Claim hard lane | Ontology validation and curation surface | Proposal-versus-promotion law and cybernetic truth boundary |

## Direct mapping

| ProCybernetica contract | Ontogenesis surface | Mapping note |
| --- | --- | --- |
| `Claim` | ontology modules, SHACL gates, SHIR Assertion / CandidateAssertion | Claims should carry ontology/schema refs and not become hard-lane truth unless the relevant ontology/shape gates pass. |
| `ProvenanceRecord` | audit manifests, ledger entries, signatures, SBOM outputs | ProvenanceRecord should reference ontogenesis-generated audit/ledger/signature artifacts instead of recreating them. |
| `ArtifactEnvelope` | generated ontology dist, audit reports, SHACL reports, SBOMs | Ontogenesis outputs can be wrapped or referenced as ArtifactEnvelope evidence. |
| `PolicyEnvelope` | SHACL gate policy, module policy, promotion constraints | PolicyEnvelope records governance interpretation; ontogenesis owns shape enforcement. |
| `PromotionDecision` | module promotion, curation, release gate outcomes | ProCybernetica interprets promotion constitutionally; ontogenesis performs ontology validation/release discipline. |
| `ReplayEnvelope` | deterministic build, ledger verify, JSON-LD roundtrip, SHACL run | ReplayEnvelope can point to ontogenesis validation and build evidence. |
| `EvaluationResult` | SHACL reports, JSON-LD roundtrip results, ledger verification results | EvaluationResult can summarize ontology validation outcomes. |
| `EventEnvelope` / `TraceEvent` | ontology build/release events, curation events | ProCybernetica tracks cybernetic control significance; ontogenesis owns event specifics if/when defined. |

## Claim promotion mapping

A ProCybernetica claim is not canonical merely because it exists.

Recommended claim lifecycle with ontogenesis:

```text
candidate claim
  -> ontology/schema refs assigned
  -> evidence/provenance refs attached
  -> SHACL gate evaluated by ontogenesis
  -> curation / validation result recorded
  -> ProCybernetica PromotionDecision issued
  -> claim may become hard-lane evidence
```

Mapping to `Claim.status`:

| Claim status | Ontogenesis/SHIR relation | Rule |
| --- | --- | --- |
| `candidate` | CandidateAssertion / proposed semantic object | Cannot be canonical truth. |
| `hypothesis` | inferred/provisional semantic object | Requires validation and curation. |
| `validated` | SHIR Assertion or shape-passing governed claim | May support promotion if policy and replay pass. |
| `derived` | derived semantic object | Preserve derivation and source module refs. |
| `stale` | superseded/deprecated module or invalidated evidence | Preserve history and avoid silent deletion. |
| `retracted` | curation/repair decision | Preserve reason and ledger/provenance references. |

## Ontology module mapping

Ontogenesis module layers map to ProCybernetica roles as follows:

| Ontogenesis layer | ProCybernetica role |
| --- | --- |
| Upper | abstract categories for node, event, artifact, policy, role, relation, and value semantics |
| Middle | reusable operational concepts across domains |
| Lower | implementation-specific semantic detail |
| Domains | domain-specific scoring, platform, office, model, economic, or workstation concepts |
| Platform | platform/runtime vocabularies for Prophet Platform, SourceOS, SociOS, AgentPlane, and related systems |
| prophet | product-specific ontology for Prophet surfaces |
| epi | EpiCybernetica/governance, evidence, contradiction, and lawful-learning concepts |

ProCybernetica should reference these layers by ontology/module ID and version, not import their source definitions into this repo.

## Release and evidence mapping

Ontogenesis release discipline includes:

- parse validation;
- SHACL validation;
- JSON-LD roundtrip checks;
- deterministic dist builds;
- ledger build and verification;
- detached signature pointer generation;
- SPDX SBOM emission.

ProCybernetica evidence interpretation:

| Ontogenesis artifact | ProCybernetica wrapper/ref |
| --- | --- |
| SHACL report | `EvaluationResult.evidence_refs` or `ArtifactEnvelope` |
| dist manifest | `ArtifactEnvelope` |
| ledger entry | `ProvenanceRecord.evidence_refs` |
| signature pointer | `ProvenanceRecord.attestation_refs` |
| SBOM | `ArtifactEnvelope` / `ProvenanceRecord.source_refs` |
| JSON-LD roundtrip report | `EvaluationResult` evidence |
| module registry entry | `Claim.ontology_ref` or `PolicyEnvelope.scope` |

## SHIR governance mapping

Ontogenesis SHIR defines semantic hyperknowledge objects and rules for preserving context before downstream projections.

ProCybernetica must not duplicate SHIR Node, Anchor, Connector, RoleBinding, Link, Context, Assertion, Evidence, Projection, Receipt, CandidateAssertion, LinkageCandidate, CurationDecision, NoiseAssessment, RepairAction, or ProjectionLossReport schemas.

ProCybernetica should:

- reference SHIR objects as semantic evidence;
- require SHIR receipts/projection-loss reports where semantic lowering affects public claims or dashboards;
- map curation and repair outcomes to `PromotionDecision`, `IncidentReport`, or future adapter records;
- treat SHIR candidate assertions as soft-lane inputs until validated.

## ProCybernetica schema implications

### Keep

- `Claim`
- `ProvenanceRecord`
- `ArtifactEnvelope`
- `EvaluationResult`
- `PromotionDecision`
- `ReplayEnvelope`
- `PolicyEnvelope`

### Do not add in ProCybernetica v0

- ontology module schema;
- SHACL report schema;
- ontology ledger schema;
- signature artifact schema;
- SBOM schema;
- SHIR object schemas.

Those belong upstream or in existing standards surfaces.

### Consider later

- `ExternalEvidenceRef` to reference ontogenesis artifacts uniformly.
- `examples/integrations/ontogenesis/claim_shacl_gate_ref.example.json`.
- `examples/integrations/ontogenesis/ontology_release_evidence_ref.example.json`.

## Required adapter posture

A future ontogenesis adapter should produce references like:

```json
{
  "artifact_ref": "ontogenesis://dist/<module>@<version>",
  "shacl_report_ref": "ontogenesis://audit/shacl/<run-id>",
  "ledger_ref": "ontogenesis://ledger/<entry-id>",
  "signature_ref": "ontogenesis://signatures/<entry-id>",
  "procybernetica_contract": "ProvenanceRecord"
}
```

The adapter should not copy ontogenesis generated artifacts wholesale into ProCybernetica unless a public fixture or example is intentionally created.

## Open questions

1. Should `Claim.ontology_ref` be constrained to ontogenesis namespace/module refs in v0.1?
2. Should ProCybernetica require SHACL report refs for every `Claim.status = validated` fixture?
3. Should scoring/dashboard evidence rows reference ontogenesis curation decisions where available?
4. Should `PromotionDecision.evidence_refs` require at least one ontogenesis validation ref when the subject is a semantic claim?
5. Should ontology release evidence become a canonical example under `examples/integrations/ontogenesis/`?

## Follow-up backlog

- Add ontogenesis adapter fixtures after all estate maps are complete.
- Update `docs/scoring/schema.md` to allow ontology/SHACL refs in evidence rows.
- Revisit `Claim` schema only after SourceOS/SociOS and Prophet Platform maps are complete.
- Add a conformance check later: claims promoted to validated status should include ontology refs and validation evidence.

## Current conclusion

Ontogenesis is the ontology governance and semantic authority release lane. ProCybernetica should not duplicate that machinery. It should require, reference, and interpret ontogenesis validation and release evidence as part of cybernetic promotion, replay, provenance, and public conformance law.
