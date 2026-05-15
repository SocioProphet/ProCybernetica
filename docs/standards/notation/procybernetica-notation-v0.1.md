# ProCybernetica Notation Standard v0.1

Status: Draft standard.  
Scope: ProCybernetica standards, governance schemas, theorem-audit records, categorical diagrams, replay specifications, and consuming-repository conformance documents.

## 1. Purpose

This standard reserves notation for ProCybernetica's categorical governance layer. The goal is to prevent symbol collision across manuscripts, schemas, validators, audit logs, and consuming repositories.

A reserved symbol is a build-contract symbol. Reusing it for an incompatible concept is a standards violation.

## 2. Reserved symbols

| Symbol | Canonical meaning | Scope | Forbidden collisions |
|---|---|---|---|
| `\mathfrak W` | Full operational / consciousness substrate | Whole architecture | Do not use for governance-only slice, evidence object, or policy lattice |
| `\mathfrak W_{\mathrm{gov}}` | Governance-attestation substrate slice embedded in `\mathfrak W` | ProCybernetica governance layer | Do not use for the full substrate |
| `\mathcal E` | Evidence layer: event logs, replay objects, benchmark records, attestations | Evidence and replay standards | Do not use as total space of a fibration |
| `\mathbf{Gov}` | Total category of governed objects/actions/tokens/attestations | Governance fibration | Do not use `\mathcal E` for this role |
| `\mathbf{Pol}` | Base policy lattice/category | Governance fibration | Do not use for policy documents as raw files without categorical structure |
| `\pi_{\mathrm{gov}}` | Governance fibration projection `\mathbf{Gov} -> \mathbf{Pol}` | Governance fibration | Do not confuse with substrate projection family `\Pi` |
| `\Pi` | Substrate observation/projection family | World-model substrate | Do not use for fibration projection |
| `\rho` | Reversibility distance | Reversibility / counter-evidence layer | Do not use for Hawkes scaling, density operators, or spectral radius |
| `\eta_s` | Per-speaker Hawkes scaling or speaker-specific excitation parameter | Temporal/event intensity layer | Do not use `\rho_s` for this role |
| `\ell_i` | Log-evidence contribution, `\ell_i = \log \Lambda_i` | Evidence accumulation | Do not conflate likelihood ratio `\Lambda_i` with log-likelihood contribution |
| `\mathcal L` | Lagrangian | Optimization / dual-update layer | Do not abbreviate cumulative evidence as `\mathcal L` |

## 3. Canonical substrate notation

The full operational substrate is:

```math
\mathfrak W =
(\mathcal S_{\mathrm{dur}},
 \mathcal S_{\mathrm{act}},
 \Theta,
 \mathcal T,
 \mathcal C,
 \Pi,
 \mathcal E).
```

The governance-attestation slice is:

```math
\mathfrak W_{\mathrm{gov}} =
(\mathcal S_{\mathrm{spheres}},
 \mathcal T_{\mathrm{tokens}},
 \mathcal P_{\mathrm{policy}},
 \mathcal A_{\mathrm{attest}},
 \mathcal R_{\mathrm{retain}})
\hookrightarrow
\mathfrak W.
```

The governance fibration is:

```math
\pi_{\mathrm{gov}}:\mathbf{Gov}\to\mathbf{Pol}.
```

The evidence cocone is:

```math
\lambda:D\Rightarrow\Delta L_{\mathrm{agg}}.
```

The evidence aggregate may be called a colimit only after a witness proves:

```math
\operatorname{Cocone}(D,-)
\cong
\operatorname{Hom}_{\mathcal C_{\mathrm{ev}}}(L_{\mathrm{agg}},-)
```

naturally in the target object.

## 4. Reserved-symbol enforcement

New standards must not introduce a conflicting use of a reserved symbol.

If a historical document uses a conflicting symbol, the new standard must include a local notation warning and migration note.

## 5. Diagram convention

The canonical diagram set is:

1. Governance-attestation substrate slice: `W_gov -> W`.
2. Governance fibration: `pi_gov: Gov -> Pol`.
3. Projection / fibration factorization: `h = m o e`.
4. Evidence cocone: `lambda: D => Delta L_agg`.

All diagrams must use reserved symbols consistently.
