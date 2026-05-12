# Human Protection Layer coverage matrix

Status: seed coverage matrix v0.1.

Owner: ProCybernetica reconciliation track.

Purpose: track whether the Human Protection Layer is only documented or actually covered by downstream doctrine, envelopes, fixtures, tests, reports, and issues.

Related source:

- `docs/reconciliation/HUMAN_PROTECTION_LAYER.md`
- `docs/reconciliation/DIGITAL_CONTROL_ATLAS_CAPTURE_LEDGER.md`
- `docs/reconciliation/REPO_OWNERSHIP_MAP.md`

## 1. Coverage states

| State | Meaning |
|---|---|
| missing | Not captured in docs or issues. |
| documented | Captured in doctrine/adoption prose. |
| issue_opened | Tracking issue exists. |
| schema_candidate | Candidate envelope/schema exists. |
| fixture_added | Positive/negative fixture exists. |
| tested | Automated test exists. |
| enforced | Runtime/policy/conformance gate exists. |
| blocked | Construct is explicitly blocked or excluded. |
| deferred | Deferred with reason and owner. |

## 2. Gate coverage dashboard

| Gate | Construct | ProCybernetica | HDT | GAIA | Superconscious | Current gap |
|---|---|---|---|---|---|---|
| G0 | Claim boundary | documented | documented | partial | documented | Need claim-boundary register and negative tests. |
| G1 | Consent/autonomy | documented | documented | partial | partial | Need consent envelope fields and tests. |
| G2 | Privacy/minimization | documented | documented | partial | documented | Need raw-private-evidence export tests. |
| G3 | Physical safety | documented | documented | n/a/partial | documented | Need human-actuation block tests and research-only profile fixtures. |
| G4 | Psychological/cognitive safety | documented | documented | partial | documented | Need hidden-persuasion / high-impact decision tests. |
| G5 | Cyber/misuse safety | documented | partial | partial | documented | Need trust-surface and policy-admission fixtures. |
| G6 | Redress/revocation/appeal | documented | documented | partial | partial | Need redress fields and high-impact appeal tests. |

## 3. Human Protection Layer doctrine coverage

| HPL item | Source section | Required artifact | Owner repo | Current status | Gap |
|---|---|---|---|---|---|
| People protected before models are useful | HPL §0 | doctrine | ProCybernetica | documented | decision record needed |
| Protected person definition | HPL §2 | doctrine + schema enum/field | ProCybernetica | documented | schema candidate needed |
| Human-impacting action definition | HPL §3 | doctrine + action classification | ProCybernetica | documented | classifier fixture needed |
| Validity is not permission | HPL §4 | doctrine + status gate | ProCybernetica | documented | status tests needed |
| Seven protection gates | HPL §5 | doctrine + conformance checklist | ProCybernetica | documented | checklist fixture needed |
| Status vocabulary | HPL §6 | vocabulary doc + enum schema | ProCybernetica | documented | schema candidate needed |
| Evidence tiers | HPL §7 | vocabulary doc + enum schema | ProCybernetica | documented | schema candidate needed |
| Repo adoption matrix | HPL §8 | ownership map | ProCybernetica | documented | keep synced with ownership map |
| Trust-surface requirement | HPL §9 | trust-surface fixture | Superconscious / SourceOS spec | documented | fixture/test needed |
| Minimum envelope shape | HPL §10 | schema candidate | ProCybernetica | documented | schema candidate needed |
| Minimum tests | HPL §11 | issue/test plan | all adopters | issue_opened | implement tests |
| Publication boundary | HPL §12 | publication matrix alignment | ProCybernetica | documented | decision record needed |
| Immediate reconciliation tasks | HPL §13 | tracking issue | ProCybernetica | issue_opened | complete issue #30 |

## 4. HDT coverage

| HPL requirement | HDT artifact | Current status | Required next step |
|---|---|---|---|
| Raw private evidence local by default | `docs/HUMAN_PROTECTION_LAYER_ADOPTION.md` | documented | Add export test. |
| Consent required for human-derived exports | `docs/HUMAN_PROTECTION_LAYER_ADOPTION.md` | documented | Add missing-consent test. |
| Ω promotion cannot authorize export alone | `docs/HUMAN_PROTECTION_LAYER_ADOPTION.md` | documented | Add policy-decision test. |
| Human actuation blocked by default | `docs/HUMAN_PROTECTION_LAYER_ADOPTION.md` | documented | Add blocked-actuation fixture. |
| FCBCP/HSP-Map research-only default | `docs/HUMAN_PROTECTION_LAYER_ADOPTION.md` | documented | Add research-only profile fixture. |
| Unsupported mechanism labels blocked | HPL + adoption doc | documented | Add negative mechanism tests. |
| Redress required for high-impact outputs | adoption doc | documented | Add export envelope field tests. |

Tracking issue: `SocioProphet/human-digital-twin#7`.

## 5. GAIA coverage

| HPL requirement | GAIA artifact | Current status | Required next step |
|---|---|---|---|
| Affected-population review | `docs/HUMAN_PROTECTION_LAYER_ADOPTION.md` | documented | Add action template. |
| CV/provenance before action | GAIA architecture + adoption doc | documented | Add validation check. |
| Evidence tier in reports | adoption doc | documented | Add report template. |
| Speculative world-control claim block | adoption doc | documented | Add blocked fixture. |
| Reversibility/rollback | adoption doc | documented | Add action template field. |
| Policy status in action outputs | adoption doc | documented | Add validation fixture. |

Tracking issue: `SocioProphet/gaia-world-model#27`.

## 6. Superconscious coverage

| HPL requirement | Superconscious artifact | Current status | Required next step |
|---|---|---|---|
| HPL scope assessment | `docs/human-protection-layer-adoption.md` | documented | Add `HPLScope.assessed` fixture. |
| Planning does not authorize execution | adoption doc | documented | Add test. |
| Policy admission before side effects | adoption doc | documented | Add test fixture. |
| Private evidence excluded from safe trace | adoption doc | documented | Add trace fixture/test. |
| Unsupported mechanisms cannot become assumptions | adoption doc | documented | Add blocked-plan fixture. |
| Memory write requires memory decision | adoption doc | documented | Add test. |
| HPL status in replay/benchmark | adoption doc | documented | Add artifact fixture. |

Tracking issue: `SocioProphet/superconscious#7`.

## 7. ProCybernetica coverage

| HPL requirement | ProCybernetica artifact | Current status | Required next step |
|---|---|---|---|
| Reconciliation draft | `docs/reconciliation/HUMAN_PROTECTION_LAYER.md` | documented | Complete issue #30. |
| Capture ledger | `docs/reconciliation/DIGITAL_CONTROL_ATLAS_CAPTURE_LEDGER.md` | documented | Expand rows. |
| Ownership map | `docs/reconciliation/REPO_OWNERSHIP_MAP.md` | documented | Keep synced. |
| Claim-boundary register | planned | missing | Create register. |
| Evidence-tier register | planned | missing | Create register. |
| Status vocabulary | planned | missing | Create vocabulary doc. |
| Fractal Control Node mapping | planned | missing | Create mapping doc. |
| HPL decision record | planned | missing | Draft after reconciliation. |
| Schema candidates | planned | missing | Defer until terms reconciled. |

Tracking issue: `SocioProphet/ProCybernetica#30`.

## 8. Minimum test inventory

The following tests must exist before HPL is considered executable rather than merely documented.

| Test | Owner | Current status |
|---|---|---|
| Unsupported mechanism labels are blocked. | HDT / ProCybernetica | missing |
| Speculative claims cannot export as validated. | HDT / ProCybernetica | missing |
| Human actuation blocked by default. | HDT | missing |
| Raw private evidence cannot export by default. | HDT | missing |
| Missing consent blocks consent-required human-derived export. | HDT | missing |
| Missing trust-surface authority blocks side-effectful tool path. | Superconscious / SourceOS spec | missing |
| High-impact outputs require redress/appeal path. | HDT / Superconscious | missing |
| GAIA action requires affected-population review when people may be affected. | GAIA | missing |
| Superconscious planning trace cannot authorize execution. | Superconscious | missing |
| GAIA report includes provenance and policy decision. | GAIA | missing |
| HDT Ω export includes evidence tier and minimization basis. | HDT | missing |

## 9. HPL completion criteria

HPL capture is complete when:

1. ProCybernetica reconciliation terms are stable.
2. Each adopter has an adoption document linked from its docs index.
3. Each adopter has at least one positive fixture, one blocked fixture, and one needs-review fixture.
4. HPL envelope schema candidates exist.
5. Minimum tests pass in downstream repos.
6. Public-safe reports or summaries exist.
7. No high-risk item remains only in prose.
