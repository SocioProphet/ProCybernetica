# Source Capture: ProCybernetica Prelude B — Linear Algebra, Operators, and State

Source title: `ProCybernetica_Prelude_B_Linear_Algebra_Operators_and_State`

Drive source: https://docs.google.com/document/d/1OSXgi-gXTJf0SE9TMrhkToJCB0qJ5aJADeVzozk42go

Capture purpose: preserve the linear-algebraic runway for the ProCybernetica course and blueprint so later control, mediation, replay, stabilization, and consciousness claims remain mathematically grounded.

## Document identity

Prelude B is titled `Linear Algebra, Operators, and State`.

Subtitle: `A textbook-scale runway for world models, control, observability, mediation, and lawful transformation`.

## Abstract capture

Prelude B teaches the linear-algebraic grammar needed by the rest of the course.

It treats:

- vectors as structured states;
- matrices as operators;
- composition as process law;
- basis changes as representation changes;
- projections as structured approximation;
- eigenstructure as modal memory;
- covariance as geometry of uncertainty;
- state-space form as bridge into feedback, observation, and control.

The goal is not detached algebra. The goal is to make later books on hierarchical control, semantic mediation, lawful learning, mesh stabilization, and cybernetic consciousness mathematically legible.

## Why the prelude exists

Probability gives later books a language for belief under uncertainty.

Linear algebra gives them a language for state, structure, and transformation.

Without that language, talk of world models, feedback, coordination, embeddings, covariance, observability, and node state becomes verbally plausible but mathematically thin.

The student should learn to see:

- vectors as states;
- matrices as lawful transformations;
- subspaces as structural constraints;
- eigenstructure as dynamic memory.

## State, coordinate, and representation

A system state is not the same thing as a coordinate column.

State is the abstract quantity that summarizes what matters for future evolution.

Coordinates are its expression in a chosen basis.

This distinction is essential for claims, node descriptors, belief vectors, embeddings, and basis-dependent projections. A robust architecture must preserve meaning across representation changes.

Basis changes become the mathematical ancestor of schema translation, ontology mapping, and mediated interoperability.

## Vectors as structured states

A vector is an organized bundle of degrees of freedom.

In different systems those degrees may be:

- positions and velocities;
- amplitudes;
- counts;
- beliefs;
- latent dimensions.

Control and observation act on structured state rather than isolated scalars. Treating state as vector is the beginning of lawful compositionality.

## Matrices as operators

A matrix is not merely a table of coefficients. It is an operator that stretches, rotates, shears, projects, mixes, or filters state.

Matrix multiplication is composition of processes.

This later supports stacked preprocessing, state prediction, policy weighting, semantic projection, and control updates.

Linearity is valuable not because the world is linear, but because linear models are tractable, compositional, and locally useful.

## Span, subspace, rank, and nullspace

The first structural questions about an operator are:

- What can it reach?
- What does it erase?
- What constraints does it impose?

Rank gives effective dimensionality of what an operator preserves or can generate.

Nullspace identifies directions that vanish.

In sensing, nullspace corresponds to hidden directions.

In actuation, rank deficiency corresponds to unreachable directions.

In semantics, low-rank projections may intentionally compress but also erase distinctions.

## Four fundamental subspaces

Column space, nullspace, row space, and left nullspace become a map of what a system can represent, sense, control, and where residual inconsistencies remain.

Later control and diagnostics use these spaces as interpretations of:

- actuation;
- sensing;
- residual generation;
- explanation failure.

## Orthogonality, projection, and approximation

Projection formalizes keeping the component of a state relevant to a chosen subspace while discarding the rest.

Orthogonality makes decomposition stable and interpretable.

Least squares is the canonical response to noisy, redundant, inconsistent data.

Approximation is lawful only when residuals remain visible and interpretable.

This becomes a critique-layer principle: a system that reports fitted state but hides residual loses a key channel of self-critique.

## Eigenstructure and mode memory

Eigenvectors are directions preserved up to scale by a transformation.

Eigenvalues say whether motion along those directions grows, shrinks, or oscillates.

In dynamical systems, eigenstructure becomes modal memory:

- some directions decay quickly;
- some persist;
- some dominate the future trajectory.

Cybernetically, eigenstructure is the first disciplined answer to: what kinds of memory does this system have?

## Singular values and anisotropic amplification

Singular values show how an operator stretches or contracts energy along orthogonal directions.

They reveal:

- dominant directions;
- effective rank;
- sensitivity;
- information bottlenecks;
- robustness under perturbation.

This matters for embeddings, attention-like weighting, dimensional reduction, and retrieval bottlenecks.

## Covariance and geometry of uncertainty

A positive definite matrix encodes a geometry.

In statistics it becomes covariance or precision.

In optimization it becomes curvature.

In energy-based modeling it measures quadratic cost or distance.

Uncertainty is not one scalar width. It is directional. Some combinations of state variables are tightly known; others are weakly constrained.

Scalar confidence can hide high-dimensional uncertainty geometry.

## State-space bridge

The control bridge appears when writing:

```text
x[k+1] = A x[k] + B u[k]
y[k] = C x[k] + D u[k]
```

The state vector compresses the past into what matters for future evolution.

Input enters through `B`.

Measurement leaves through `C`.

Everything later about observers, feedback, controllability, and mesh-level state summaries depends on this representation.

## Meaning of state

State summarizes everything about the past relevant to future behavior under a model.

Choosing state is a constitutional modeling act.

If the chosen state omits relevant history, the controller or mediator acts with structurally incomplete knowledge.

## Controllability and observability

Controllability asks whether repeated action channels can span the relevant state space.

Observability asks whether repeated measurements can reveal hidden state.

In ProCybernetica, controllability generalizes to agency under structured constraints. Policy, embodiment, communication, and authority constraints can create unreachable subspaces.

Observability generalizes to explanation, provenance, and monitoring. A visibility failure may mean the measurement map must be redesigned, not merely inspected harder.

## Similarity, invariance, and mediation

Similarity transformations show that different coordinate realizations can represent the same input-output dynamics.

This becomes a template for mediation and federation:

- services;
- schemas;
- ontologies;
- nodes;
- local world models.

Different internals may participate in shared behavioral contracts if invariants and provenance are preserved.

## Replay as repeated updates

Discrete systems iterate powers of `A`; continuous systems use `e^{At}`.

Replay is not merely a log viewer. It is repeated application of recorded transitions under known operators.

## Numerical stability and conditioning

Not all lawful operations behave well numerically.

Ill-conditioned systems magnify small errors. Near-dependent columns make estimates fragile. Poor scaling obscures structure.

Numerical conditioning becomes cybernetic humility: a system may be right in theory and unstable in computation.

## Linear algebra and explanation

Linear algebra contributes to explanation:

- projection explains approximation;
- residuals explain mismatch;
- rank explains collapsed distinctions;
- singular directions explain dominant features;
- eigenmodes explain long-lived dynamics.

Without this, explanations risk becoming narratives about model outputs rather than structural accounts of representation, measurement, and motion.

## Worked slices

Belief-state update as operator sequence:

```text
prediction: x^- = A x + B u
observation: y = C x + noise
correction: x^+ = x^- + K (y - C x^-)
```

Capability boundaries as subspaces:

- policy and embodiment restrict reachable action sets;
- sensing restricts visible state distinctions;
- controllability and observability become bounded by physics, architecture, law, and governance.

## Common pitfalls

- mistaking coordinates for state;
- treating matrix as bag of numbers rather than operator;
- invoking eigenvalues without identifying operator/regime;
- forgetting lost distinctions in low-rank projection;
- confusing model observability with practical visibility;
- assuming controllability because some actuation exists;
- treating covariance as scalar confidence;
- ignoring numerical conditioning;
- forgetting linearity is often local approximation;
- letting elegant algebra erase provenance and policy.

## Forward links

Prelude B supports:

- Book III: state-space thinking, hierarchy, controllability/observability;
- Book IV: operator composition in mediation and hybrid reasoning;
- Book VI: graph/hypergraph projection logic;
- Book VIII: lawful learning and evidence geometry;
- Book IX: stabilization, replay, mesh observability;
- Book X: reflexivity, state versus representation, observability versus invisibility.

## Problem sets and capstone

Problem sets:

- classify matrices by rank, nullspace, and geometric action;
- derive controllability/observability matrices and interpret cybernetically;
- construct two state-space realizations of one behavior and explain similarity.

Capstone:

Design a mini state-update pipeline for a lawful node using explicit operators for prediction, observation, correction, and policy projection, then explain what each preserves, erases, or constrains.

## Codification implications

Prelude B should inform:

- state and representation docs;
- observability and controllability language;
- semantic projection doctrine;
- belief-state and replay contracts;
- explanation and residual reporting requirements;
- curriculum sequencing.

## Capture status

Captured into GitHub as structured source-state. This is not a replacement for the Drive document. It records the linear-algebraic runway for the blueprint.
