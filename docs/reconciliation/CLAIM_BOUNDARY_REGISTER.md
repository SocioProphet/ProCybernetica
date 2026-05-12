# Claim Boundary Register

Status: reconciliation draft v0.1.

Owner: ProCybernetica reconciliation track.

Adopters: Human Digital Twin, GAIA World Model, Superconscious, Digital Control Atlas profiles, FCBCP/HSP-Map research profile.

Purpose: prevent metaphor, speculation, unsupported mechanisms, or overbroad claims from becoming validated mechanisms, exportable claims, planning assumptions, or action templates.

This register is not an index of forbidden ideas. It is a classification and routing layer: claims may be valid, research hypotheses, metaphor-only, speculative-only, excluded mechanisms, or blocked from operational use.

## 1. Boundary rule

A claim must declare:

```yaml
claim_id: string
claim_text: string
claim_status: validated | research_hypothesis | metaphor_only | speculative_only | excluded_mechanism | blocked_unsafe | unknown
evidence_tier: E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | unknown
allowed_contexts: [string]
blocked_contexts: [string]
required_label: string
owner_repo: string
review_path: string
```

No downstream repo may promote `metaphor_only`, `speculative_only`, `excluded_mechanism`, `blocked_unsafe`, or `unknown` claims to validated operational status without explicit review, updated evidence tier, and policy admission.

## 2. Status definitions

| Status | Meaning | Export/action rule |
|---|---|---|
| validated | Supported by sufficient evidence for the declared scope. | May be used within scope after policy gates. |
| research_hypothesis | Falsifiable but not validated. | May be used in research protocols, simulation, or preregistration; not operational truth. |
| metaphor_only | Useful language or imagery, not a mechanism. | May appear in explanation with label; cannot drive solver/action logic. |
| speculative_only | Conceptual or mathematical speculation lacking validation. | May appear in research notes; not operational. |
| excluded_mechanism | Mechanism rejected for current framework due to lack of reproducible support or category error. | Blocked from validated claims, action templates, and planning assumptions. |
| blocked_unsafe | Claim/use is unsafe or too easily misused in this context. | Blocked unless separate policy process overrides with explicit rationale. |
| unknown | Not yet classified. | Treat as blocked for high-impact use until classified. |

## 3. Global blocked mechanism labels

These labels are blocked as validated mechanisms across ProCybernetica, HDT, FCBCP/HSP-Map, Superconscious planning, and Atlas profiles unless a future independent review explicitly changes their status.

| claim_id | Label | Status | Allowed contexts | Blocked contexts | Required label |
|---|---|---|---|---|---|
| CBR-0001 | `phantom_dna_field` | excluded_mechanism | historical review, excluded-claim discussion | validated biology, FCBCP mechanism, HDT export, Superconscious planning assumption, GAIA action | Unsupported wave-genetics claim; excluded mechanism. |
| CBR-0002 | `semantic_wave_text` | excluded_mechanism | historical review, metaphor critique | validated biology, cognitive/biological control mechanism, planning assumption | Semantic wave-text claim; excluded mechanism. |
| CBR-0003 | `dna_inductor` | excluded_mechanism | metaphor-only diagram annotation | FCBCP mechanism, materials model, biological actuator claim | DNA is not treated as a lumped inductor in vivo. |
| CBR-0004 | `dna_speaker_microphone` | excluded_mechanism | metaphor critique | acoustic transduction mechanism, biological actuator claim | DNA speaker/microphone claim excluded. |
| CBR-0005 | `holographic_gene_laser` | excluded_mechanism | historical review, claim boundary | validated mechanism, optical control claim | Holographic gene-laser claim excluded. |
| CBR-0006 | `native_dna_biological_magnet` | excluded_mechanism | metaphor critique | magnetothermal/magnetomechanical mechanism | Native DNA biological magnet claim excluded. |
| CBR-0007 | `geometry_implies_circuit_element` | excluded_mechanism | design metaphor discussion | mechanism inference | Shape resemblance alone is not mechanism. |
| CBR-0008 | `unreplicated_field_genetics_mechanism` | excluded_mechanism | research-history review | validated FCBCP/HDT/Atlas claim | Requires independent replication before reclassification. |

## 4. Metaphor-only allowed claims

These claims may be used as disciplined metaphors or taxonomic vocabulary when the non-literal boundary is explicit.

| claim_id | Label | Status | Allowed contexts | Blocked contexts | Required label |
|---|---|---|---|---|---|
| CBR-0101 | `dna_as_storage` | metaphor_only | storage/code/computer doctrine, educational framing | literal random-access machine claim, direct field-coupling proof | Layer metaphor: DNA as persistent biological state, not computer storage device. |
| CBR-0102 | `rna_as_code` | metaphor_only | RNA/protein dynamics framing | Turing/von-Neumann executable claim | Layer metaphor: RNA as transient/regulatory biological instruction substrate. |
| CBR-0103 | `human_as_computer` | metaphor_only | distributed-system analogy | reduction of person to machine, identity claim, autonomy replacement | Layer metaphor only; human is never replaced by a twin. |
| CBR-0104 | `software_of_life` | metaphor_only | industry terminology comparison | evidence for field-coupling mechanism | Taxonomic language, not proof. |
| CBR-0105 | `surface_as_io_boundary` | research_hypothesis | boundary-calculus model with Maxwell/Poynting accounting | mystical surface equivalence | Physical boundary/accounting model only. |

## 5. Validated or lawful precursor claims

These claims are allowed as scientific precursors within their scoped limits. They do not validate excluded mechanisms.

| claim_id | Claim | Status | Evidence tier | Allowed contexts | Boundary |
|---|---|---|---|---|---|
| CBR-0201 | Nucleic acids and extracellular vesicles can be electrically manipulated or measured in certain AC electrokinetic / dielectrophoretic settings. | validated | E5 | validated precursor docs, instrumentation discussion | Does not imply semantic field genetics or phantom DNA. |
| CBR-0202 | 3D chromatin architecture is a lawful regulatory substrate. | validated | E5 | validated precursor docs, biological mechanism spine | Does not imply holographic genome semantics. |
| CBR-0203 | Endogenous bioelectric networks can influence development, physiology, and gene-expression pathways. | validated | E5 | bioelectricity / mechanism spine | Does not imply external field control is safe or validated. |
| CBR-0204 | Membrane potential can couple to second messengers and transcriptional cascades. | validated | E5 | FCBCP research hypotheses, mechanism spine | Dose, timing, cell type, and context remain constrained. |
| CBR-0205 | Light, heat, acoustic, magnetic-particle, and electric modalities can have lawful physical kernels under declared mechanisms. | research_hypothesis | E1-E5 depending on kernel | FCBCP modality tables | Each kernel must be separately validated and safety-gated. |

## 6. FCBCP/HSP-Map claim boundaries

| Claim | Allowed status | Required boundary |
|---|---|---|
| Boundary transfer models estimate surface-to-interior coupling. | research_hypothesis / simulation | Must include uncertainty and not imply human actuation. |
| HSP-Map models layered tissue properties. | research_hypothesis | Must be person-specific, uncertain, and consent-gated for human data. |
| FCBCP can compile modality schedules in simulation. | research_hypothesis | Simulation-only unless external review path exists. |
| Human actuation is safe. | unknown / blocked by default | Requires external review, safety model, consent, and regulatory/ethics path. |
| Iso-Delta-Vm trajectories produce equivalent transcript outcomes. | research_hypothesis | Must be tested under H4; not assumed. |
| Channel blockers establish mechanism. | research_hypothesis | Must be experimentally demonstrated; not inferred. |

## 7. Digital Control Atlas claim boundaries

| Claim | Allowed status | Required boundary |
|---|---|---|
| Atlas chart validity | validated only within declared math convention | Does not imply permission. |
| Solver convergence | technical status only | Does not imply safety or policy permission. |
| Profile allows primitive | profile-local status | Does not imply cross-profile permission. |
| P6 code injection/extraction | information/profile-local metaphor | In HDT, cannot mean biological code injection. |
| Negative-energy or exotic transport claims | speculative_only unless evidence changes | Must abort to speculative status, not operational plan. |
| World-action plan | planning status | Requires GAIA validation, affected-population review, report, and policy decision. |

## 8. Superconscious planning boundaries

Superconscious may reason over these labels but must not convert blocked or speculative labels into operational assumptions.

Blocked in Superconscious planning assumptions:

- excluded mechanisms;
- unknown high-impact mechanisms;
- speculative-only mechanisms when proposing real-world or human-impacting action;
- any claim whose owner profile marks it blocked or research-only.

Allowed in Superconscious safe traces:

- claim label;
- claim status;
- blocked reason;
- required review path;
- evidence pointer.

Not allowed in safe traces:

- raw private evidence;
- raw private chain-of-thought;
- unsupported mechanism treated as valid;
- authorization of execution.

## 9. GAIA action boundaries

GAIA world-action templates must not be generated from:

- speculative world-control claims;
- hidden or unattributable data sources;
- unvalidated high-impact causal mechanisms;
- missing affected-population review;
- missing provenance/license status;
- missing reversibility or rollback statement where action is proposed.

World-model observation and internal planning may reference speculative claims if clearly labeled, but reports and action templates must preserve the label.

## 10. HDT export boundaries

HDT export must block or downgrade claims when:

- evidence tier is below declared export threshold;
- consent is missing where required;
- raw private evidence would be attached by default;
- claim is metaphor-only but represented as identity or mechanism;
- claim is speculative-only but represented as validated;
- unsupported biological mechanism appears as validated;
- human actuation is implied or requested without external review path.

## 11. Required negative tests

Before this register is considered executable, downstream repos must add tests proving:

- `phantom_dna_field` cannot be exported as validated.
- `semantic_wave_text` cannot become a planning assumption.
- `dna_inductor` cannot appear as FCBCP mechanism.
- `dna_speaker_microphone` cannot appear as acoustic modality mechanism.
- `holographic_gene_laser` cannot appear as optical modality mechanism.
- `native_dna_biological_magnet` cannot appear as magnetothermal mechanism.
- `dna_as_storage`, `rna_as_code`, and `human_as_computer` remain metaphor-only unless rewritten in mechanistic terms.
- P6 in HDT cannot mean biological code injection.
- Atlas validity cannot bypass HPL status.
- GAIA action templates preserve speculative labels.
- Superconscious safe traces preserve blocked/speculative status.

## 12. Reclassification process

A blocked or excluded claim may be reconsidered only through explicit review.

Minimum requirements:

1. new evidence source;
2. independent replication or equivalent justification if biological/physical;
3. mechanism statement;
4. limitations and falsification criteria;
5. risk review;
6. downstream impact review;
7. updated evidence tier;
8. policy decision;
9. changelog entry in this register.

Until reclassification is merged, the old status remains binding.

## 13. Immediate downstream actions

- HDT: add negative tests for blocked mechanism labels.
- Superconscious: add blocked-planning fixtures for excluded mechanisms.
- GAIA: add report/action templates that preserve speculative status.
- ProCybernetica: reconcile this register with HPL status vocabulary and future schema candidates.
