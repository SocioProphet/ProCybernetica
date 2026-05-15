# ProCybernetica Notation Standard v0.1

Status: Draft standard.

This standard reserves notation for ProCybernetica governance, proof, replay, evidence, and categorical diagrams. A reserved symbol is a build-contract symbol: incompatible reuse is a standards violation.

## Reserved symbols

| Symbol | Canonical meaning | Forbidden collision |
|---|---|---|
| `\mathfrak W` | Full operational substrate | Governance-only slice, evidence object, or policy lattice |
| `\mathfrak W_{\mathrm{gov}}` | Governance-attestation substrate slice embedded in `\mathfrak W` | Full substrate |
| `\mathcal E` | Evidence layer: events, replay objects, benchmark records, attestations | Total category of a fibration |
| `\mathbf{Gov}` | Total governance category | Evidence layer |
| `\mathbf{Pol}` | Base policy lattice/category | Raw policy file collection without categorical structure |
| `\pi_{\mathrm{gov}}` | Governance fibration projection `\mathbf{Gov} -> \mathbf{Pol}` | Substrate projection family |
| `\Pi` | Substrate observation/projection family | Fibration projection |
| `\rho` | Reversibility distance | Hawkes scaling, density operator, spectral radius |
| `\eta_s` | Per-speaker Hawkes scaling | Reversibility distance |
| `\ell_i` | Log-evidence contribution, `\ell_i = \log \Lambda_i` | Likelihood ratio product itself |
| `\mathcal L` | Lagrangian | Evidence log or cumulative likelihood |

## Canonical substrate notation

The full substrate is:

```math
\mathfrak W=(\mathcal S_{\mathrm{dur}},\mathcal S_{\mathrm{act}},\Theta,\mathcal T,\mathcal C,\Pi,\mathcal E).
```

The governance-attestation slice is:

```math
\mathfrak W_{\mathrm{gov}}=(\mathcal S_{\mathrm{spheres}},\mathcal T_{\mathrm{tokens}},\mathcal P_{\mathrm{policy}},\mathcal A_{\mathrm{attest}},\mathcal R_{\mathrm{retain}})\hookrightarrow\mathfrak W.
```

## Enforcement rule

New standards, diagrams, schemas, theorem-audit records, and consuming-repository conformance files should use this table. If a symbol must be overloaded for historical compatibility, the document must include a local notation warning and migration note.
