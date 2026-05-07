# Calibrated Lawful Learning

Status: formal specification draft. No live data were used. All numerical examples are illustrative and exist only to demonstrate the computation path.

## Core claim

Lawful learning is constrained optimization with calibrated gates, slack-enforced constraints, tuned hyperparameters, observer-stable evidence, and replayable ledger records.

The model rejects arbitrary thresholds and meaningless gated inequalities. A positive gate multiplying an inequality does not weaken or strengthen that inequality:

```math
w_r C_r\theta \ge 0,\quad w_r>0
```

is equivalent to:

```math
C_r\theta \ge 0.
```

Therefore gates are used only through hard activation, slack penalties, or augmented Lagrangian terms.

## 26-dimensional state

For an observed object `z_n`, construct a symmetric positive semidefinite operator:

```math
K_n=\mathcal K_\omega(z_n),\qquad K_n=Q_n\Lambda_nQ_n^\top.
```

The first 22 coordinates are normalized top eigenvalues:

```math
\lambda_i(n)=\frac{\tilde\lambda_i(n)}{\sum_{j=1}^{22}\tilde\lambda_j(n)+\varepsilon},\qquad i=1,\ldots,22.
```

The 23rd coordinate is the scalarized unitary or orthogonal expansion:

```math
u_n=\frac{1}{22}\operatorname{Re}\operatorname{tr}(U_n),\qquad U_n=Q_0^\top Q_n.
```

For real-valued systems, `U_n` is orthogonal. For complex-valued systems, it is unitary.

The final three coordinates are a learned spatial connection:

```math
s_n=A_\eta[\lambda_1(n),\ldots,\lambda_{22}(n),u_n]^\top\in\mathbb R^3.
```

The Poincare embedding is:

```math
p_n=\phi(s_n)=\frac{s_n}{1+\|s_n\|_2}.
```

## Constraint families

Lawful learning supports monotonicity, dominance, Edgeworth complementarity, trapezoid bounds, and radial unimodality. Each row is expressed with explicit slack when soft enforcement is required:

```math
C_r\theta+\xi_r\ge0,\qquad \xi_r\ge0.
```

Slack is penalized by a gate-calibrated cost:

```math
\mathcal L_{slack}=\sum_r \mu_r(w_r)\xi_r^2,
```

where:

```math
\mu_r(w_r)=\mu_{min}+(\mu_{max}-\mu_{min})w_r.
```

The gate is learned or tuned:

```math
w_r(x)=\sigma\left(\frac{s_r(x)-t_r}{T_r}\right).
```

Here `s_r(x)` is a regime statistic, `t_r` is a learned or tuned threshold, and `T_r` is a learned or tuned temperature.

## Calibrated thresholds

Thresholds are learned or selected by constrained validation. For top-band energy:

```math
s_{top}=\lambda_1+\lambda_2+\lambda_3,
```

```math
w_{top}=\sigma\left(\frac{s_{top}-t_{top}}{T_{top}}\right).
```

Use a learned quantile threshold:

```math
t_{top}=q_\alpha,\qquad \alpha=0.05+0.90\sigma(\omega).
```

This prevents pathological extreme thresholds.

## Prime/even prior

Prime/even structure is a prior, not a command:

```math
R_{arith}(\Theta)=\lambda_P\|\Theta-\Pi_P\Theta\|_1+\lambda_E\|\Theta-\Pi_E\Theta\|_1+\lambda_2|\Theta_2-\bar\Theta_P|.
```

Required negative controls are shuffled prime/even masks. If shuffled masks perform as well as the real masks, the arithmetic hypothesis is unsupported.

## Hyperparameter tuning

Let:

```math
\psi=(m_i,\lambda_{TV},\lambda_P,\lambda_E,\lambda_2,T_r,\mu_{min},\mu_{max},|\mathcal P|,\varepsilon_{max},n_{min}).
```

Select:

```math
\psi^*=\arg\min_\psi ValLoss(\psi)
```

subject to feasibility:

```math
\max_r[-C_r\theta_\psi]_+\le\varepsilon_{max},
```

```math
Support_r\ge n_{min},
```

```math
Instability(\Theta_\psi)\le I_{max},
```

```math
|\mathcal P|\le P_{max}.
```

Use the one-standard-error rule: select the simplest feasible model whose validation loss is statistically indistinguishable from the best feasible model.

## Hyperbolic geometry discipline

The system does not claim that every Euclidean convex cone automatically becomes globally geodesically convex in the Poincare ball. Constraints are enforced in spectral coordinates and, where needed, in tangent space:

```math
v=\log_0(p),\qquad C_vv\ge0,\qquad p=\exp_0(v).
```

A stable local hyperbolic region is:

```math
\mathcal C_H=\exp_0(\mathcal C_T\cap B_R).
```

## Ledger discipline

Use canonical serialization:

```math
H_t=SHA256(serialize(\theta_t,\Theta_t,\xi_t,\eta_t,H_{t-1})).
```

Serialization must use fixed byte order, fixed dtype, fixed rounding, and fixed field order. SHA-256 is not injective. The claim is tamper evidence under standard collision-resistance assumptions for computationally feasible adversaries.

## Observer-stable evidence

An observer is:

```math
\mathcal O:\mathcal S\rightarrow\mathcal E.
```

A statement is observer-stable if:

```math
\mathcal O_g(s)=\mathcal O(s)
```

for all admissible transformations `g` in the observer group `G`.

## Operational truth score

```math
T(x)=L(x)E(x).
```

Lawful admissibility:

```math
L(x)=\exp(-\kappa\|[-C(\Theta)\theta]_+\|_2).
```

Evidence confidence:

```math
E(x)=I_{ledger}I_{signature}I_{replay}(1-\rho_{env}).
```

Thus:

```math
T(x)=\exp(-\kappa\|[-C(\Theta)\theta]_+\|_2)I_{ledger}I_{signature}I_{replay}(1-\rho_{env}).
```

## Failure modes

Required failure analysis includes eigenvalue degeneracy, infeasible constraint intersections, sparse support, dual explosion, Poincare boundary instability, false arithmetic priors, ledger drift, and observer disagreement.

## Required ablations

| Ablation | Description | Purpose |
|---|---|---|
| A0 | unconstrained model | baseline |
| A1 | fixed constraints, no gates | constraint contribution |
| A2 | learned gates, no arithmetic prior | gate contribution |
| A3 | arithmetic prior, no hyperbolic embedding | arithmetic contribution |
| A4 | hyperbolic embedding, no arithmetic prior | geometry contribution |
| A5 | full model | complete system |
| A6 | shuffled prime/even masks | negative control |
| A7 | ledger perturbation | audit sensitivity |

## Analogy discipline

Physical analogies are structural analogies only. Curvature, energy, entropy, and geodesic language are used only where corresponding mathematical structures are explicitly defined. No claim is made that the computational system literally realizes gravitational, quantum, or thermodynamic dynamics.
