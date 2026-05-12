# Digital Control Atlas reconciliation draft

Status: reconciliation draft v0.1, not final schema and not runtime code.

Owner: ProCybernetica reconciliation track.

Adopters: SocioProphet/gaia-world-model, SocioProphet/human-digital-twin, SocioProphet/superconscious, future SourceOS/AgentPlane/Policy Fabric integrations.

Related:

- `docs/reconciliation/DIGITAL_CONTROL_ATLAS_CAPTURE_LEDGER.md`
- `docs/reconciliation/REPO_OWNERSHIP_MAP.md`
- `docs/reconciliation/HUMAN_PROTECTION_LAYER.md`
- `docs/reconciliation/HPL_COVERAGE_MATRIX.md`
- `docs/reconciliation/FCBCP_SOURCE_COVERAGE_MATRIX.md`

## 0. Purpose

The Digital Control Atlas is the shared formal substrate for lawful boundary-calculus programs across world models, human digital twins, recursive agent planning, and cybernetic control nodes.

It is not a simulator by itself. It is a profile-governed representation of charts, transitions, control primitives, solver calls, evidence, and audits.

The purpose of this reconciliation draft is to preserve the useful mathematical architecture while adding authority boundaries, human-protection gates, evidence tiers, and status semantics so that Atlas validity never becomes unchecked permission.

## 1. Core principle

Atlas validity is not operational permission.

A chart may be mathematically coherent and still blocked. A transition may satisfy geometry and still fail policy. A solver may converge and still be unsafe. A program may be valid in simulation and forbidden in the world. A research hypothesis may be useful and still non-exportable as a validated claim.

Every Atlas output must carry both:

1. technical status; and
2. policy/protection status.

## 2. Formal object

Seed formalism:

```text
Atlas A = (
  charts,
  transitions,
  control_primitives,
  solvers,
  audits,
  profiles,
  evidence,
  policy_status
)
```

A chart is a local representation of a domain with geometry, operators, controls, and invariants.

A transition is a typed interface between charts with coordinate, physical, semantic, and policy compatibility data.

A control primitive is an abstract action form. Its meaning is profile-specific; a primitive valid in an information chart is not automatically valid in a human-boundary chart.

A solver call is a request to compute, estimate, optimize, simulate, or verify something. Solver calls are not permissions.

An audit is a technical and policy check that can return `valid`, `invalid`, `speculative`, `unsafe`, `underidentified`, `policy_blocked`, or a more specific Human Protection Layer status.

## 3. Chart datum

Draft chart tuple:

```yaml
chart:
  chart_id: string
  profile_id: string
  owner_repo: string
  domain_kind: euclidean | hyperbolic | spherical | flrw | near_horizon | phase_space | discrete_hyperbolic | human_boundary | world_model | cognition_loop | cybernetic_node | other
  metric:
    representation: symbolic | numeric | mesh | graph | ontology | state_space
    convention: string
    omega_field: optional
    curvature: optional
  operators:
    - laplace_beltrami
    - eikonal
    - continuity
    - wave
    - geodesic
    - state_space
    - policy_eval
    - ontology_validation
  controls:
    admissible_controls: [string]
    blocked_controls: [string]
    cost_functional: optional
  invariants:
    technical: [string]
    protection: [string]
  evidence_tier: E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | unknown
  status: string
```

## 4. Transition datum

The draft transition morphism is not only a coordinate map. It is a typed bundle:

```yaml
transition:
  transition_id: string
  from_chart: string
  to_chart: string
  owner_repo: string
  coordinate_map: optional
  refraction_law: optional
  flux_rule: optional
  code_match_rule: optional
  semantic_match_rule: optional
  policy_match_rule: optional
  residuals:
    coordinate_residual: optional
    refraction_residual: optional
    flux_residual: optional
    code_match_residual: optional
    semantic_match_residual: optional
    policy_residual: optional
    cocycle_residual: optional
  status: valid | invalid | speculative | unsafe | underidentified | policy_blocked | unknown
```

Coordinate agreement is only one slot. Physical, semantic, and policy gluing must be checked separately.

## 5. Mathematical convention corrections

The source draft contains useful formal content, but several conventions must be fixed before schema or solver implementation.

### 5.1 Eikonal Omega convention

If the metric is already conformal:

```text
g = Omega^2 delta
```

then the physical travel-time functional

```text
T = integral Omega/c d l_E
```

corresponds to the Euclidean eikonal:

```text
|grad_E T| = Omega / c
```

Equivalently, in the metric `g`:

```text
|grad_g T|_g = 1 / c
```

The expression `|grad_g T|_g = Omega/c` double-counts Omega and must not be used unless a different convention is explicitly declared.

### 5.2 Poincare ball Laplacian sign convention

For the Poincare ball with

```text
Omega = 2 / (1 - |x|^2)
```

and the standard positive Laplace-Beltrami convention, the drift term has positive sign:

```text
Delta_H u = ((1 - |x|^2)^2 / 4) Delta_E u
            + ((n - 2)(1 - |x|^2) / 2) x dot grad_E u
```

If a negative-Laplacian convention is chosen, the whole document must declare it and use it consistently.

### 5.3 Flux rule dimensional convention

The full conformal n-dimensional rule, using Euclidean normal derivative, is:

```text
[sigma Omega^(n-2) partial_n^E phi]_Sigma = 0
```

A reduced paraxial or dimensionless engineering rule may use another Omega power, such as Omega^2, but that must be explicitly labeled as a reduction, not a universal transition law.

### 5.4 Code-matching semantics

The code-matching rule must not be treated as a universal physical law without dimensional definition.

Safer draft:

```text
C_phys(A) >= R_logical * chi_cut(gamma*, A, noise_model)
```

where `chi_cut` is a declared redundancy/cut inflation factor derived from the chosen information chart and noise model.

## 6. Control primitives

The Atlas preserves six primitive families, but each is profile-scoped.

| Primitive | Name | General meaning | Profile caution |
|---|---|---|---|
| P1 | Geodesic surf | Follow or approximate a natural path under a chart metric | Validity does not imply safety. |
| P2 | Bang-coast-bang | Switch between bounded intervention and passive/coast phases | Human/world use requires separate policy review. |
| P3 | Manifold capture | Enter a stable/controlled manifold and coast | Must not imply hidden authority. |
| P4 | Conformal grading | Shape the environment/material/representation so desired path is natural | In HDT, no human-contact material actuation by default. |
| P5 | Beamed phase array | External field/resource alignment | High-risk in physical profiles; simulation-only unless reviewed. |
| P6 | Code injection/extraction | Information redundancy, export, import, or code-distance control | In HDT, this means evidence/code export structure, not DNA/RNA code injection. |

P6 is especially overloaded and must be profile-qualified. It must not be interpreted as biological code injection in FCBCP/HDT profiles.

## 7. Solver suite

Draft solver families:

| Solver | Purpose | Status |
|---|---|---|
| eikonal | travel-time/geodesic fields | specification only |
| laplace_beltrami | metric-aware boundary-value problems | specification only |
| manifold_continuation | invariant manifold/tube extraction | speculative unless validated in profile |
| optimal_control | bounded control program synthesis | planning only unless policy-admitted |
| tensor_network_code | code-matching/min-cut estimation | simulation/specification |
| inverse_phase_screen | learns/estimates metric or field screens from observations | estimation only; carries posterior uncertainty |
| policy_eval | evaluates authority, consent, privacy, affected-population risk, redress | required before export/action |
| report_generator | converts runs into public-safe evidence reports | required for GAIA-style action outputs |

No solver output is executable authority.

## 8. Audit set

Each Atlas run should produce a typed audit vector.

Minimum audits:

```yaml
audits:
  technical:
    - convention_check
    - chart_validity
    - transition_residual
    - cocycle_residual
    - causality_or_rate_limit
    - invariant_drift
    - solver_convergence
    - uncertainty_or_underidentification
  protection:
    - claim_boundary
    - evidence_tier
    - consent
    - privacy_minimization
    - physical_safety
    - cognitive_safety
    - misuse_review
    - redress
    - trust_surface
    - affected_population_review
  publication:
    - public_safe
    - redaction_required
    - private_local_only
```

Audits must return specific status labels rather than a single boolean.

## 9. Atlas profiles

The Atlas must be profile-governed. A profile declares which charts, primitives, solvers, and export paths are allowed.

Seed profiles:

| Profile | Owner repo | Role |
|---|---|---|
| `procybernetica.control-law.v0` | ProCybernetica | Doctrine, conformance, status vocabulary, claim boundary, control-node law. |
| `hdt.human-boundary.v0` | human-digital-twin | Human-boundary claims, Ω readiness, consent, minimization, redress. |
| `hdt.fcbcp-research.v0` | human-digital-twin | FCBCP/HSP-Map simulation and research-only profile. |
| `gaia.world.v0` | gaia-world-model | World-model charts, actions, provenance, affected-population reports. |
| `superconscious.cognition-loop.v0` | superconscious | Planning, policy-admission requests, safe trace, replay-plan emission. |

## 10. Repo alignment

### ProCybernetica

Owns reconciliation, doctrine, profile registry, claim-boundary register, evidence/status vocabulary, and conformance requirements.

Does not own raw human evidence, live runtime execution, or final canonical schemas before promotion.

### Human Digital Twin

Owns human-boundary profiles, Ω claims, FCBCP/HSP-Map research profile, privacy/minimization, and human export envelopes.

Does not own human actuation authority.

### GAIA World Model

Owns world-chart profile, CV/ontology validation, action templates, affected-population review, and generated reports.

Does not bypass provenance or promote speculative world-control claims to actions.

### Superconscious

Owns planning, HPL scope assessment, policy-admission requests, safe traces, and replay-plan emission.

Does not authorize execution, finalize schemas, export HDT claims, or promote GAIA actions.

## 11. Status vocabulary

Atlas profile outputs must use a status vocabulary compatible with HPL.

Recommended labels:

- SAFE_TO_SIMULATE;
- SAFE_TO_PUBLISH_AS_SPEC;
- SAFE_TO_USE_AS_INTERNAL_PLANNING;
- SAFE_TO_EXPORT_AS_CLAIM;
- SAFE_FOR_SYNTHETIC_TEST;
- SAFE_FOR_PHANTOM_TEST;
- SAFE_FOR_EX_VIVO_RESEARCH;
- REQUIRES_ETHICS_REVIEW;
- REQUIRES_REGULATORY_REVIEW;
- BLOCKED_HUMAN_ACTUATION;
- BLOCKED_UNSUPPORTED_CLAIM;
- BLOCKED_PRIVACY_RISK;
- BLOCKED_CONSENT_MISSING;
- BLOCKED_AUTHORITY_MISSING;
- BLOCKED_UNDERIDENTIFIED;
- BLOCKED_AFFECTED_POPULATION_RISK;
- BLOCKED_POLICY;
- SPECULATIVE_ONLY.

## 12. Minimum Atlas envelope

```yaml
atlas_run:
  run_id: string
  profile_id: string
  owner_repo: string
  purpose: string
  evidence_tier: E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | unknown
  charts: [string]
  transitions: [string]
  primitives: [string]
  solver_calls: [string]
  audits:
    technical_status: string
    policy_status: string
    protection_status: string
  trust_surface:
    declared: boolean
    authority_ref: string
  publication:
    public_safe: boolean
    redaction_required: boolean
    private_local_only: boolean
  provenance:
    source_refs: [string]
    evidence_hash: string
    policy_version: string
  result:
    allowed_next_step: plan_only | simulate | publish_spec | request_review | export_claim | block
    reasons: [string]
```

## 13. Conformance tests required before schema promotion

- Eikonal Omega convention test.
- Poincare Laplacian sign convention test.
- Flux-rule dimension/regime guard test.
- Transition residual field presence test.
- Cocycle residual field presence test.
- Profile blocks disallowed primitives test.
- P6 cannot mean biological code injection in HDT test.
- Atlas validity cannot authorize export/action test.
- Missing trust-surface authority blocks side-effectful path test.
- Speculative status cannot export as validated test.
- Human Protection Layer gates present for human-boundary profiles test.
- Affected-population review present for GAIA action profiles test.
- Superconscious planning trace cannot authorize execution test.

## 14. Next reconciliation steps

1. Create `ATLAS_PROFILE_REGISTRY.md`.
2. Create `CONTROL_PROGRAM_STATUS_VOCABULARY.md`.
3. Create `FRACTAL_CONTROL_NODE_MAPPING.md`.
4. Create schema candidates only after terminology review.
5. Open downstream issues pointing to exact capture-ledger rows.
6. Add synthetic conformance fixtures before runtime implementation.
