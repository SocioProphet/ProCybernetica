# Interpretability Harness Release Composition Governance

**Status:** v0.1 doctrine  
**Owner:** ProCybernetica governance-fabric lane  
**Scope:** Governance law for `superconscious` interpretability harness release-bundle compositions  
**Non-scope:** Runtime steering, provider integration, model download, Neuronpedia API integration, public claim promotion, or semantic proof of feature meaning

## Purpose

This document defines how ProCybernetica treats a `superconscious` interpretability harness release bundle as a Tier 2 governed composition.

It consumes the canonical Tier 2 composition invariant family by reference:

```text
docs/governance-fabric/TIER2_COMPOSITION_INVARIANTS.md
```

The release bundle is not a single model experiment and not a single registry citation. It is a flat composition of governed fragments whose authority, evidence, non-claims, monitor posture, and freshness posture must remain explicit.

## Canonical fragment set

A first-tranche interpretability release bundle contains exactly fourteen fragment classes:

1. `ModelArtifact`
2. `SAEArtifact`
3. `FeatureArtifact`
4. `FeatureExplanation`
5. `FeatureActivationSet`
6. `SteeringIntervention`
7. `CausalTriad`
8. `AttributionGraph`
9. `OffTargetAudit`
10. `ManifoldBaseline`
11. `ImplementabilityCurve`
12. `RobustnessCertificate`
13. `BenchmarkResult`
14. `PublicInterpretabilityNote`

The Superconscious repo owns the current repo-local binding and fixtures for this exact fragment boundary. ProCybernetica owns the governance interpretation of that boundary.

## Governance rule

An interpretability release bundle may support a composed interpretability claim only when the composition preserves these Tier 2 obligations:

```text
receipt_integration: hash_bound_reference
authority_scope_analysis: declared_scope_lattice_v1
non_claim_analysis: explicit_propagate_or_resolve_v1
monitor_independence_analysis: declared_monitor_independence_v1
evidence_freshness_analysis: declared_evidence_freshness_v1
```

The v0.1 Superconscious binding is deliberately doctrine-only and hash-bound. It must not be read as runtime verification, provider execution, feature-causality proof, safety proof, or public promotion.

## Fragment governance obligations

### ModelArtifact

Must identify the model family, model source, version or immutable reference, tokenizer relationship where applicable, and replay class.

Required non-claims include no provider-hidden equivalence and no cross-model transfer unless separately evidenced.

### SAEArtifact

Must identify the SAE family, model relationship, layer, width, sparsity or L0 descriptor where used, and source lock.

Required non-claims include no semantic correctness of the SAE feature labels without downstream evidence.

### FeatureArtifact

Must identify the feature, latent, probe, neuron, or registry concept being referenced.

Required non-claims include no causal claim from identity alone.

### FeatureExplanation

Must distinguish human-authored, model-generated, registry-supplied, validated, rejected, or mixed explanation authority.

Required non-claims include no explanation authority upgrade by prose.

### FeatureActivationSet

Must identify the activation examples, selection policy, position class, and replay class.

Required non-claims include no population-level claim from cherry-picked activations.

### SteeringIntervention

Must identify the intervention kind, target, coefficient schedule, position policy, required source locks, policy decision requirement, and off-target audit requirement.

Required non-claims include no execution authority from specification alone.

### CausalTriad

Must bind proposed cause, behavior, and control or comparison condition.

Required non-claims include no causal proof where only correlation or prompt-level behavior has been measured.

### AttributionGraph

Must distinguish manifest-level graph identity from latent or runtime replay evidence.

Required non-claims include no graph-edge truth from visualization alone.

### OffTargetAudit

Must declare forbidden effects, evaluated side effects, and audit coverage limits.

Required non-claims include no global safety claim from finite off-target checks.

### ManifoldBaseline

Must declare baseline dataset, metric, layer/position policy, and replay class.

Required non-claims include no universal activation manifold coverage.

### ImplementabilityCurve

Must declare the metric, interpolation or perturbation policy, and window of validity.

Required non-claims include no deployability claim from geometric proximity alone.

### RobustnessCertificate

Must declare perturbation family, benchmark family, threshold, and failure modes.

Required non-claims include no adversarial completeness.

### BenchmarkResult

Must declare task set, evaluator, seed or determinism posture, and evidence refs.

Required non-claims include no general behavioral claim outside the benchmark class.

### PublicInterpretabilityNote

Must bind public prose to evidence refs, non-claims, promotion state, and publication boundary.

Required non-claims include no peer-review substitution and no public safety claim unless separately promoted.

## Neuronpedia registry-only rule

Neuronpedia-style registry evidence is admissible as candidate-discovery evidence and public artifact citation evidence.

It is not automatically runtime replay evidence.

It is not automatically feature-steering authority.

It is not automatically proof that a local model, tokenizer, SAE, activation cache, or intervention substrate reproduces the registry artifact.

A registry-only feature may enter the bundle as a `FeatureArtifact`, `FeatureExplanation`, or source-locked registry reference. It may not by itself satisfy the source-lock obligations for `SteeringIntervention`, `CausalTriad`, `ImplementabilityCurve`, or `RobustnessCertificate`.

## Promotion boundary

The v0.1 bundle may be used for:

- candidate discovery;
- fixture-level schema validation;
- negative-boundary enforcement;
- doctrine-bound composition tests;
- public-note draft preparation with explicit non-claims.

The v0.1 bundle may not be used for:

- runtime steering authorization;
- provider API execution;
- model mutation;
- public claim promotion;
- safety certification;
- claim that registry evidence proves local replay;
- claim that finite fixtures prove general interpretability validity.

## Admission failures

A bundle must fail governance admission if:

1. Any required fragment class is missing or duplicated.
2. Any fragment lacks a digest, source lock, provenance reference, or explicit non-claim appropriate to its type.
3. A registry-only artifact is used as a live runtime or steering substrate.
4. A black-box provider binding claims hidden-state, residual-stream, SAE, transcoder, activation-patching, or feature-steering authority.
5. A public note omits non-claims.
6. A steering intervention lacks policy decision and off-target audit obligations.
7. A composition attempts to promote runtime, safety, or public claims from doctrine-only binding evidence.
8. A composition narrows constituent non-claims without explicit resolution evidence.
9. A composition claims independent monitoring without declared monitor distinctness.
10. A composition claims fresh evidence without freshness analysis.

## Cross-repo ownership

`superconscious` owns the repo-local harness schema, fixtures, and semantic checker.

`ProCybernetica` owns this governance doctrine and Tier 2 composition interpretation.

`SocioSphere` should register the governed interpretability harness use case and rollout state.

`Policy Fabric` should own any future policy decision semantics for executing steering interventions.

`AgentPlane` should own future runtime execution evidence and replay artifacts.

`SourceOS/sourceos-spec` or the selected standards repo may receive stable schema vocabulary only after the repo-local v0.1 surface has survived review.

`Ontogenesis` may receive RDF/JSON-LD/SHACL vocabulary only after terms stabilize.

## Non-claims

This document does not claim that the harness proves interpretability correctness.

This document does not claim that Neuronpedia artifacts are unreliable.

This document does not claim runtime execution exists.

This document does not claim a public note is promoted.

This document does not claim recursive composition.

This document does not replace the Tier 2 composition invariant catalog.

## Next work

1. Register the governed interpretability harness use case in `SocioProphet/sociosphere`.
2. Add one cross-repo reference from Superconscious docs to this ProCybernetica doctrine file.
3. Keep provider-boundary hardening in Superconscious until v0.1 review stabilizes.
4. Defer SourceOS/Ontogenesis vocabulary promotion until the v0.1 fixtures stop changing.
