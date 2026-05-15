# Certificate and Bridge SHACL Coverage

Status: v0.1 companion-shape coverage record  
Issue: #46  
Runtime claim: none

## Purpose

This document records the SHACL companion-shape coverage for the certificate-family v1.3 surface and bridge-schema surface.

The companion shapes live at:

```text
shacl/certificates/certificate-family-v1.3.shacl.ttl
shacl/bridges/bridge-schemas-v1.shacl.ttl
```

The SHACL files are coverage companions, not a new source of semantics. JSON Schema and repository-local validators remain the executable schema lanes currently used in CI.

## Certificate companion coverage

The certificate companion file covers all certificate kinds named in #46:

| Certificate family | SHACL shape |
| --- | --- |
| M0 training provenance | `pc:M0TrainingProvenanceCertificateShape` |
| M1A source lock | `pc:M1ASourceLockCertificateShape` |
| M1B witness card | `pc:M1BWitnessCardCertificateShape` |
| M1C causal triad | `pc:M1CCausalTriadCertificateShape` |
| M1.5 attribution graph | `pc:M15AttributionGraphCertificateShape` |
| M1D off-target audit | `pc:M1DOffTargetAuditCertificateShape` |
| M1 composite | `pc:M1CompositeCertificateShape` |
| M2 implementability | `pc:M2ImplementabilityCertificateShape` |
| M3 cross-layer robustness | `pc:M3CrossLayerRobustnessCertificateShape` |
| M5 public note | `pc:M5PublicNoteCertificateShape` |
| ProCybernetica safety case | `pc:ProCyberneticaSafetyCaseCertificateShape` |

The shared base shape is:

```text
pc:BaseCertificateV13Shape
```

It maps to:

```text
schemas/certificates/base-certificate.v1.3.json
```

## Bridge companion coverage

The bridge companion file covers all bridge schemas named in #46:

| Bridge schema | SHACL shape |
| --- | --- |
| `schemas/bridges/ops-history-to-pneumachinalis.v1.json` | `pc:OpsHistoryToPneumachinalisBridgeShape` |
| `schemas/bridges/masonmark-to-certificate.v1.json` | `pc:MasonmarkToCertificateBridgeShape` |
| `schemas/bridges/certificate-to-atlas.v1.json` | `pc:CertificateToAtlasBridgeShape` |

## CI invariant coverage

### CI-1 — manifest/full digest distinction

SHACL coverage:

- certificate base shape requires `cert:subject`;
- certificate base shape requires structural certificate identifiers;
- the coverage file records `pc:invariantCoverage` for CI-1.

Non-SHACL follow-up:

- digest-format and digest-semantic distinction remain best enforced by JSON Schema plus repository-local validators because JSON Schema already checks `artifact_content_sha256` format and future Rego can enforce manifest/full-content policy.

### CI-4 — promotion-state inheritance

SHACL coverage:

- certificate base shape requires `cert:promotion_state`;
- certificate-kind shapes inherit the base shape;
- bridge shapes preserve promotion-state fields where applicable.

Non-SHACL follow-up:

- cross-field promotion-state inheritance is already enforced by `tools/cybernetic_governance/validate_certificate_v13.py` and `tools/cybernetic_governance/validate_bridges.py`.
- SHACL alone is not the complete enforcement layer for composite fragment promotion inheritance, candidate-proofpack-to-Steele prevention, or undecided-fail-closed behavior.

### CI-9 — authority concentration limit

SHACL coverage:

- certificate base shape records `pc:invariantCoverage` for CI-9 and requires the structural fields needed to express authority/adjudication.

Non-SHACL follow-up:

- numeric threshold enforcement for authority concentration should remain in repository-local validators or future Rego because thresholding depends on policy context, signer set interpretation, and review scope.

## F2.2 status

After #46, F2.2 moves from partial/deferred to covered by SHACL companions plus non-SHACL fallback.

The coverage model is:

```text
JSON Schema -> structural field validation
SHACL companion -> RDF/ontology-facing shape coverage
Repository-local Python validators -> cross-field invariants
Future Rego/non-SHACL validator -> policy-threshold and runtime-specific rules
```

## Non-claims

This document does not introduce runtime SHACL enforcement, production policy gating, Rego policies, Atlas runtime admission, certificate adjudication, Masonmark proofpack adjudication, OpsHistory ingestion, or Pneumachinalis scoring. It records companion-shape coverage and the validation boundary between SHACL-expressible and non-SHACL rules.
