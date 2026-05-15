# Certificate Family Index v1.3

Status: v0.1 index  
Issue: #47  
Runtime claim: none

## Purpose

This index defines the canonical base certificate-family surface for the Turn 4 Cairnmark-to-Stele doctrine and v1.3 field bump.

The shared schema is:

```text
schemas/certificates/base-certificate.v1.3.json
```

The shared additive v1.3 fields are:

- `authority_layer`
- `promotion_state`
- `reasoning_trace_ref`
- `cadence_classification`

## Certificate families

| Family | `certificate_kind` | v1.3 status |
| --- | --- | --- |
| M0 training provenance | `m0-training-provenance` | indexed through shared base schema |
| M1A source lock | `m1a-source-lock` | indexed through shared base schema |
| M1B witness card | `m1b-witness-card` | indexed through shared base schema |
| M1C causal triad | `m1c-causal-triad` | indexed through shared base schema |
| M1.5 attribution graph | `m1-5-attribution-graph` | indexed through shared base schema |
| M1D off-target audit | `m1d-off-target-audit` | indexed through shared base schema |
| M1 composite | `m1-composite` | indexed through shared base schema |
| M2 implementability | `m2-implementability` | indexed through shared base schema and transition fixtures |
| M3 cross-layer robustness | `m3-cross-layer-robustness` | indexed through shared base schema |
| M5 public note | `m5-public-note` | indexed through shared base schema |
| ProCybernetica safety case | `procybernetica-safety-case` | indexed through shared base schema |

## Transition states

The shared transition-state vocabulary is:

```text
candidate -> promoted_stele
candidate -> rejected
candidate -> superseded
promoted_stele -> superseded
```

A `candidate` is a Cairnmark: a structured marker requiring adjudication. A `promoted_stele` is a durable promoted certificate state with reasoning trace and authority evidence. `rejected` and `superseded` are terminal or successor-bound states.

## Backward compatibility

This tranche does not mutate older certificate-family files. Instead, it defines the shared v1.3 base schema and validates existing transition fixtures already written in v1.3 form.

Downstream family-specific schemas may later specialize the shared base schema, but they must preserve the four v1.3 fields and the transition-state discipline.

## Non-claims

This index does not adjudicate live proofpacks, implement runtime certificate promotion, implement Atlas admission, implement capability-tier schemas, or prove correctness of any certificate family. It defines the base structural parity needed by #47 and future SHACL work.
