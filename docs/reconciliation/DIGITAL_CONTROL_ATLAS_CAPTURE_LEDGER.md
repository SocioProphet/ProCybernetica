# Digital Control Atlas capture ledger

Status: seed ledger v0.1.

Owner: ProCybernetica reconciliation track.

Purpose: capture the Digital Control Atlas, FCBCP/HSP-Map, Trueman Mesh, Human Protection Layer, GAIA action-safety, and Superconscious planning-safety material into a traceable cross-repo program.

This ledger is not the final schema. It is the intake control surface. Every source construct should eventually resolve to one of: doctrine, schema, test, issue, exclusion, research-only fixture, speculative-only note, or blocked claim.

## 1. Capture rule

No source construct is considered captured until it has:

1. an owner repo;
2. a target artifact;
3. an evidence tier;
4. a protection/risk class;
5. a status;
6. at least one verification path: review, schema, test, issue, report, or explicit block.

## 2. Capture row shape

```yaml
source_id: string
source_section: string
claim_or_construct: string
type: doctrine | schema | equation | safety_gate | exclusion | solver | profile | test | issue | report | fixture
evidence_tier: E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | unknown
risk_class: none | low | medium | high | critical | unknown
owner_repo: string
target_artifact: string
capture_status: uncaptured | partially_captured | captured | tested | blocked | deferred
verification_path: [string]
notes: string
```

## 3. Evidence tiers

- E0 — metaphor, analogy, or conceptual note.
- E1 — mathematical formalism or typed specification.
- E2 — simulation fixture or toy model.
- E3 — calibrated synthetic or phantom benchmark.
- E4 — ex vivo or lab-controlled evidence.
- E5 — observational real-world evidence.
- E6 — controlled intervention evidence under approved protocol.
- E7 — operationally validated with replay, monitoring, and postmortem evidence.

## 4. Capture domains

| Domain | Name | Primary owner | Secondary repos | Status |
|---|---|---|---|---|
| D0 | Human Protection Layer | ProCybernetica | HDT, GAIA, Superconscious | partially_captured |
| D1 | Digital Control Atlas | ProCybernetica | GAIA, HDT, Superconscious | uncaptured |
| D2 | FCBCP v1.0 | human-digital-twin | ProCybernetica | uncaptured |
| D3 | HSP-Map | human-digital-twin | GAIA, ProCybernetica | uncaptured |
| D4 | Trueman Mesh | human-digital-twin | Superconscious, ProCybernetica | uncaptured |
| D5 | Validated precursor science | human-digital-twin | ProCybernetica | uncaptured |
| D6 | Negative claim boundary / wave-genetics firewall | ProCybernetica | HDT, Superconscious | partially_captured |
| D7 | Materials and instrumentation stack | human-digital-twin | ProCybernetica | uncaptured |
| D8 | Biological mechanism spine | human-digital-twin | ProCybernetica | uncaptured |
| D9 | GAIA world-action safety | gaia-world-model | ProCybernetica | partially_captured |
| D10 | Superconscious planning safety | superconscious | ProCybernetica | partially_captured |
| D11 | ProCybernetica control-node law | ProCybernetica | SourceOS spec, AgentPlane | partially_captured |
| D12 | Evidence, replay, provenance, publication boundary | ProCybernetica | all adopters | partially_captured |

## 5. Initial source inventory

### D0 — Human Protection Layer

| source_id | construct | type | evidence | risk | owner | target | status | verification |
|---|---|---|---|---|---|---|---|---|
| D0.001 | People are protected before models are useful | doctrine | E1 | high | ProCybernetica | docs/reconciliation/HUMAN_PROTECTION_LAYER.md | captured | review |
| D0.002 | Protected person definition includes users, non-users, bystanders, modeled/inferred/affected persons | doctrine | E1 | high | ProCybernetica | docs/reconciliation/HUMAN_PROTECTION_LAYER.md | captured | review |
| D0.003 | Human-impacting action definition | doctrine | E1 | high | ProCybernetica | docs/reconciliation/HUMAN_PROTECTION_LAYER.md | captured | review |
| D0.004 | Validity is not permission | doctrine | E1 | high | ProCybernetica | docs/reconciliation/HUMAN_PROTECTION_LAYER.md | captured | review |
| D0.005 | Seven protection gates | safety_gate | E1 | critical | ProCybernetica | docs/reconciliation/HUMAN_PROTECTION_LAYER.md | captured | review |
| D0.006 | Safety status vocabulary | schema | E1 | high | ProCybernetica | docs/reconciliation/HUMAN_PROTECTION_LAYER.md | partially_captured | schema-needed |
| D0.007 | Evidence-tier vocabulary | schema | E1 | high | ProCybernetica | docs/reconciliation/HUMAN_PROTECTION_LAYER.md | partially_captured | schema-needed |
| D0.008 | Minimum HPL envelope | schema | E1 | high | ProCybernetica | docs/reconciliation/HUMAN_PROTECTION_LAYER.md | partially_captured | schema-needed |
| D0.009 | Trust-surface requirement | safety_gate | E1 | critical | ProCybernetica | docs/reconciliation/HUMAN_PROTECTION_LAYER.md | captured | test-needed |
| D0.010 | Publication boundary | doctrine | E1 | high | ProCybernetica | docs/reconciliation/HUMAN_PROTECTION_LAYER.md | captured | review |

### D1 — Digital Control Atlas

| source_id | construct | type | evidence | risk | owner | target | status | verification |
|---|---|---|---|---|---|---|---|---|
| D1.001 | Atlas as sheaf of control data over stratified spacetime | doctrine | E1 | medium | ProCybernetica | docs/reconciliation/DIGITAL_CONTROL_ATLAS_RECONCILIATION.md | uncaptured | review |
| D1.002 | Chart tuple `(U, g, O, C, I)` | schema | E1 | medium | ProCybernetica | schemas/atlas-chart.schema.json after reconciliation | uncaptured | schema/test |
| D1.003 | Transition morphism quadruple `(coordinate, refraction, flux, code-match)` | schema | E1 | high | ProCybernetica | schemas/atlas-transition.schema.json after reconciliation | uncaptured | schema/test |
| D1.004 | Cocycle residual on triple overlaps | safety_gate | E1 | high | ProCybernetica | docs/reconciliation/DIGITAL_CONTROL_ATLAS_RECONCILIATION.md | uncaptured | test |
| D1.005 | Eikonal Omega convention correction | equation | E1 | medium | ProCybernetica | docs/reconciliation/DIGITAL_CONTROL_ATLAS_RECONCILIATION.md | uncaptured | test |
| D1.006 | Poincare Laplacian sign convention | equation | E1 | medium | ProCybernetica | docs/reconciliation/DIGITAL_CONTROL_ATLAS_RECONCILIATION.md | uncaptured | test |
| D1.007 | Flux rule dimension/regime declaration | equation | E1 | high | ProCybernetica | docs/reconciliation/DIGITAL_CONTROL_ATLAS_RECONCILIATION.md | uncaptured | test |
| D1.008 | Six control primitives P1-P6 | doctrine | E1 | high | ProCybernetica | docs/reconciliation/DIGITAL_CONTROL_ATLAS_RECONCILIATION.md | uncaptured | review |
| D1.009 | Solver suite 5.1-5.6 | solver | E1 | medium | ProCybernetica | docs/reconciliation/DIGITAL_CONTROL_ATLAS_RECONCILIATION.md | uncaptured | fixture |
| D1.010 | Audit set `V` with technical and policy status | safety_gate | E1 | critical | ProCybernetica | docs/reconciliation/DIGITAL_CONTROL_ATLAS_RECONCILIATION.md | uncaptured | test |

### D2 — FCBCP v1.0

| source_id | construct | type | evidence | risk | owner | target | status | verification |
|---|---|---|---|---|---|---|---|---|
| D2.001 | FCBCP system definition | profile | E1 | high | human-digital-twin | docs/research/fcbcp/FCBCP_SPEC_V1.md | uncaptured | review |
| D2.002 | Five components: tissue model, surface array, state observer, compiler/scheduler, verifier/ledger | doctrine | E1 | high | human-digital-twin | docs/research/fcbcp/FCBCP_SPEC_V1.md | uncaptured | review |
| D2.003 | Unified state-space dynamics | equation | E1 | high | human-digital-twin | docs/research/fcbcp/FCBCP_SPEC_V1.md | uncaptured | review/test |
| D2.004 | Modality kernels: electric, acoustic, optical, thermal, magnetic/MNP | schema | E1 | high | human-digital-twin | docs/research/fcbcp/FCBCP_SPEC_V1.md | uncaptured | schema/test |
| D2.005 | Boundary closure and Poynting dose | safety_gate | E1 | critical | human-digital-twin | docs/research/fcbcp/FCBCP_SPEC_V1.md | uncaptured | test |
| D2.006 | MPC with thermal/Pennes/Arrhenius constraints | solver | E1 | critical | human-digital-twin | docs/research/fcbcp/FCBCP_SPEC_V1.md | uncaptured | fixture |
| D2.007 | H1-H5 falsifiable hypotheses | doctrine | E1 | high | human-digital-twin | docs/research/fcbcp/HYPOTHESES.md | uncaptured | review |
| D2.008 | Phase 0-5 research program | report | E1 | high | human-digital-twin | docs/research/fcbcp/PHASE_PLAN.md | uncaptured | review |
| D2.009 | Statistical analysis and power plan | doctrine | E1 | medium | human-digital-twin | docs/research/fcbcp/STATISTICAL_PLAN.md | uncaptured | review |
| D2.010 | Risk register | report | E1 | high | human-digital-twin | docs/research/fcbcp/RISK_REGISTER.md | uncaptured | review |

### D3 — HSP-Map

| source_id | construct | type | evidence | risk | owner | target | status | verification |
|---|---|---|---|---|---|---|---|---|
| D3.001 | HSP-Map data schema | schema | E1 | high | human-digital-twin | human_digital_twin/api/schemas/fcbcp/hsp-map.schema.json | uncaptured | schema/test |
| D3.002 | 18-region partition | schema | E1 | medium | human-digital-twin | data/hsp_map/regions.yaml | uncaptured | test |
| D3.003 | Composite Bio-Feature Vector | schema | E1 | medium | human-digital-twin | docs/research/fcbcp/HSP_MAP_SPEC.md | uncaptured | schema |
| D3.004 | Age scalars | schema | E1 | medium | human-digital-twin | data/hsp_map/age_scalars.yaml | uncaptured | test |
| D3.005 | Frequency bands and design heuristics | doctrine | E1 | medium | human-digital-twin | docs/research/fcbcp/HSP_MAP_SPEC.md | uncaptured | review |

### D4 — Trueman Mesh

| source_id | construct | type | evidence | risk | owner | target | status | verification |
|---|---|---|---|---|---|---|---|---|
| D4.001 | Intent/compiler/scheduler/estimator/verifier/logger decomposition | doctrine | E1 | high | human-digital-twin | docs/research/fcbcp/TRUEMAN_MESH_PROFILE.md | uncaptured | review |
| D4.002 | EM-ISA program model | schema | E1 | high | human-digital-twin | docs/research/fcbcp/TRUEMAN_MESH_PROFILE.md | uncaptured | schema |
| D4.003 | Simulation-only high-level program fixture | fixture | E2 | high | human-digital-twin | examples/fcbcp/trueman_mesh_simulation_program.yaml | uncaptured | test |
| D4.004 | Forensic telemetry row schema | schema | E1 | high | human-digital-twin | human_digital_twin/api/schemas/fcbcp/actuation-event.schema.json | uncaptured | schema/test |

### D5 — Validated precursor science

| source_id | construct | type | evidence | risk | owner | target | status | verification |
|---|---|---|---|---|---|---|---|---|
| D5.001 | Heller ACE/DEP field-biomolecule coupling as validated precursor | doctrine | E5 | medium | human-digital-twin | docs/research/fcbcp/VALIDATED_PRECURSORS.md | uncaptured | citations/review |
| D5.002 | 3D chromatin architecture as lawful regulatory substrate | doctrine | E5 | medium | human-digital-twin | docs/research/fcbcp/VALIDATED_PRECURSORS.md | uncaptured | citations/review |
| D5.003 | Endogenous bioelectric networks as lawful tissue control layer | doctrine | E5 | medium | human-digital-twin | docs/research/fcbcp/VALIDATED_PRECURSORS.md | uncaptured | citations/review |
| D5.004 | Single-cell vs multicellular distinctions | doctrine | E1 | medium | human-digital-twin | docs/research/fcbcp/SCOPE_UNICELLULAR_MULTICELLULAR.md | uncaptured | review |

### D6 — Negative claim boundary / wave-genetics firewall

| source_id | construct | type | evidence | risk | owner | target | status | verification |
|---|---|---|---|---|---|---|---|---|
| D6.001 | Gariaev/wave-genetics forensic review | exclusion | E1 | high | ProCybernetica | docs/reconciliation/CLAIM_BOUNDARY_REGISTER.md | partially_captured | review |
| D6.002 | Phantom DNA excluded | exclusion | E1 | critical | ProCybernetica | docs/reconciliation/HUMAN_PROTECTION_LAYER.md | captured | test-needed |
| D6.003 | Semantic wave-text excluded | exclusion | E1 | critical | ProCybernetica | docs/reconciliation/HUMAN_PROTECTION_LAYER.md | captured | test-needed |
| D6.004 | DNA inductor/speaker/microphone excluded as mechanism | exclusion | E1 | critical | ProCybernetica | docs/reconciliation/HUMAN_PROTECTION_LAYER.md | captured | test-needed |
| D6.005 | Native DNA biological magnet excluded | exclusion | E1 | critical | ProCybernetica | docs/reconciliation/HUMAN_PROTECTION_LAYER.md | captured | test-needed |
| D6.006 | Metaphor-only allowance | doctrine | E1 | medium | ProCybernetica | docs/reconciliation/CLAIM_BOUNDARY_REGISTER.md | uncaptured | test |

### D7 — Materials and instrumentation stack

| source_id | construct | type | evidence | risk | owner | target | status | verification |
|---|---|---|---|---|---|---|---|---|
| D7.001 | PVDF-PCNT tile stack | fixture | E1 | medium | human-digital-twin | docs/research/fcbcp/MATERIALS_AND_INSTRUMENTATION.md | uncaptured | review |
| D7.002 | MWCNT/PBA functionalization | fixture | E1 | medium | human-digital-twin | docs/research/fcbcp/MATERIALS_AND_INSTRUMENTATION.md | uncaptured | review |
| D7.003 | Mesoporous silica/MSN typology | fixture | E1 | medium | human-digital-twin | docs/research/fcbcp/MATERIALS_AND_INSTRUMENTATION.md | uncaptured | review |
| D7.004 | Fe3C/Fe carbon-shell particles | fixture | E1 | medium | human-digital-twin | docs/research/fcbcp/MATERIALS_AND_INSTRUMENTATION.md | uncaptured | review |
| D7.005 | Native mass spectrometry provenance | fixture | E1 | low | human-digital-twin | docs/research/fcbcp/MATERIALS_AND_INSTRUMENTATION.md | uncaptured | review |

### D8 — Biological mechanism spine

| source_id | construct | type | evidence | risk | owner | target | status | verification |
|---|---|---|---|---|---|---|---|---|
| D8.001 | Delta Vm -> Ca2+ -> second messengers -> TFs -> RNA -> protein -> chromatin cascade | doctrine | E1 | high | human-digital-twin | docs/research/fcbcp/BIOLOGICAL_MECHANISM_SPINE.md | uncaptured | review |
| D8.002 | SNARE/synaptotagmin exocytosis readout path | doctrine | E1 | medium | human-digital-twin | docs/research/fcbcp/BIOLOGICAL_MECHANISM_SPINE.md | uncaptured | review |
| D8.003 | 3D spheroid secretome validation | fixture | E1 | medium | human-digital-twin | docs/research/fcbcp/BIOLOGICAL_MECHANISM_SPINE.md | uncaptured | review |
| D8.004 | Time-scale ladder ms -> s -> min -> hr -> days | doctrine | E1 | medium | human-digital-twin | docs/research/fcbcp/TIME_SCALE_LADDER.md | uncaptured | review |

### D9 — GAIA world-action safety

| source_id | construct | type | evidence | risk | owner | target | status | verification |
|---|---|---|---|---|---|---|---|---|
| D9.001 | HPL adoption for GAIA actions | doctrine | E1 | high | gaia-world-model | docs/HUMAN_PROTECTION_LAYER_ADOPTION.md | captured | issue #27 |
| D9.002 | Affected-population review template | schema | E1 | high | gaia-world-model | gaia/actions/templates/affected-population-review.yaml | uncaptured | test |
| D9.003 | GAIA action report policy status | report | E1 | medium | gaia-world-model | gaia/reports/templates/atlas-action-report.md | uncaptured | test |

### D10 — Superconscious planning safety

| source_id | construct | type | evidence | risk | owner | target | status | verification |
|---|---|---|---|---|---|---|---|---|
| D10.001 | HPL adoption for Superconscious planning | doctrine | E1 | high | superconscious | docs/human-protection-layer-adoption.md | captured | issue #7 |
| D10.002 | HPLScope assessed event | schema | E1 | high | superconscious | examples/hpl-scope.protected-person.json | uncaptured | test |
| D10.003 | Planning does not authorize execution | safety_gate | E1 | critical | superconscious | tests/test_planning_does_not_authorize_execution.py | uncaptured | test |

### D11 — ProCybernetica control-node law

| source_id | construct | type | evidence | risk | owner | target | status | verification |
|---|---|---|---|---|---|---|---|---|
| D11.001 | Atlas objects mapped to Fractal Control Nodes | doctrine | E1 | high | ProCybernetica | docs/reconciliation/FRACTAL_CONTROL_NODE_MAPPING.md | uncaptured | review |
| D11.002 | Policy-status vocabulary as conformance law | doctrine | E1 | high | ProCybernetica | docs/reconciliation/CONTROL_PROGRAM_STATUS_VOCABULARY.md | uncaptured | review |
| D11.003 | HPL v0 reconciliation issue | issue | E1 | medium | ProCybernetica | issue #30 | captured | issue |

### D12 — Evidence, replay, provenance, publication boundary

| source_id | construct | type | evidence | risk | owner | target | status | verification |
|---|---|---|---|---|---|---|---|---|
| D12.001 | Public-by-default, sanitize narrowly | doctrine | E1 | high | ProCybernetica | docs/reconciliation/HUMAN_PROTECTION_LAYER.md | captured | review |
| D12.002 | Raw human evidence local/private by default | safety_gate | E1 | critical | human-digital-twin | docs/HUMAN_PROTECTION_LAYER_ADOPTION.md | captured | test-needed |
| D12.003 | Safe operational traces, not raw chain-of-thought/private evidence | safety_gate | E1 | high | superconscious | docs/human-protection-layer-adoption.md | captured | test-needed |
| D12.004 | GAIA reports include evidence tier, uncertainty, limitations, policy status | report | E1 | medium | gaia-world-model | docs/HUMAN_PROTECTION_LAYER_ADOPTION.md | captured | test-needed |

## 6. Capture status dashboard

| Status | Count at seed |
|---|---:|
| captured | 20 |
| partially_captured | 9 |
| uncaptured | 43 |
| tested | 0 |
| blocked | 0 |
| deferred | 0 |

The seed count is approximate and should be recalculated as rows are added or split.

## 7. Next capture actions

1. Create `docs/reconciliation/REPO_OWNERSHIP_MAP.md`.
2. Create `docs/reconciliation/FCBCP_SOURCE_COVERAGE_MATRIX.md`.
3. Create `docs/reconciliation/HPL_COVERAGE_MATRIX.md`.
4. Create `docs/reconciliation/DIGITAL_CONTROL_ATLAS_RECONCILIATION.md`.
5. Create `docs/reconciliation/CLAIM_BOUNDARY_REGISTER.md`.
6. Add repo issues that point to exact ledger rows.
7. Add tests only after reconciliation decides canonical field names.

## 8. Definition of complete capture

A source construct is complete only when it is one of:

- captured_as_doctrine;
- captured_as_schema;
- captured_as_test;
- captured_as_issue;
- captured_as_exclusion;
- captured_as_research_only;
- captured_as_speculative_only;
- blocked_as_unsafe_or_unsupported;
- deferred_with_reason.

No source row should remain `uncaptured` at the end of the capture program.
