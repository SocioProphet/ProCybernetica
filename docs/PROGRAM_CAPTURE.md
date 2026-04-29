# ProCybernetica Program Capture

This document captures the program architecture being codified from the ProCybernetica Drive corpus into the public `SocioProphet/ProCybernetica` GitHub repository.

## Program thesis

ProCybernetica is the operational cybernetic framework for the Prophet ecosystem. Its role is to turn control, cognition, governance, replay, lawful learning, and platform assurance into explicit contracts and executable machinery.

EpiCybernetica is the companion epistemic layer: the critique, evidence, replay, contradiction-handling, calibration, and governance loop that keeps the operational fabric accountable.

Together they define an engineering target: systems that maintain self-models and world-models, allocate attention, store memory across time scales, evaluate value and risk, plan and act under policy constraints, explain themselves, and revise their models only through lawful evidence-bearing transitions.

## Foundational pattern

The core architectural pattern is the repeated control node. Every meaningful component is treated as a node with a stable outer contract. The embodiment changes; the constitutional surface does not.

A repository is a node whose actuators include writes, commits, merges, retractions, replications, index updates, and quarantine actions.

An agent is a node whose actuators include tool invocations, messages, patches, proposals, delegations, and explanations.

A process runner is a node whose actuators include job starts, checkpoints, retries, compensations, aborts, and handoffs.

A robot, sensor, operator console, or embodied subsystem follows the same pattern with physical or human-interface sensors and actuators.

## Fractal Node Contract

Each node should expose at least these constitutional surfaces:

- identity;
- lifecycle;
- interfaces;
- memory;
- world model;
- value judgment;
- behavior generation;
- executor;
- learning;
- coordination;
- observability.

The node shape is deliberately close to the 4D/RCS lineage but updated for modern software: managed lifecycle, typed envelopes, policy constraints, provenance, replay, learning hooks, and integration with contemporary planners, retrieval systems, foundation models, and runtime services.

## Authority plane and information plane

The program must preserve a hard distinction between authority and information.

The authority plane carries command, priority, budget, permission, promotion, and actuation rights.

The information plane carries observations, queries, evidence, telemetry, explanations, peer exchange, memory references, and shared state.

Information may be graph-like and lateral. Authority must remain typed, bounded, and auditable.

## Genesis and Inception

Genesis is compile-time formation. It produces signed or versioned seeds that define role archetype, ontology slice, goal schema, allowed organs, retrieval profile, memory profile, policy profile, provider profile, federation profile, and approval profile.

Inception is runtime binding. It binds a seed to an actor, project, trust domain, runtime, region, mission context, memory cursors, provider handles, policy bundles, and workload identity.

The K3 bridge is the bootstrap and promotion protocol between seed formation and world-authorized operation.

Canonical lifecycle states include:

- `INIT_SESSION`;
- `PROBE_ACCEPT`;
- `INJECT_SEED`;
- `SEED_PUBLISH`;
- `VERIFY_TWIN`;
- `TWIN_READY`;
- `GATED_HOST_UPDATE`;
- `QUARANTINE`;
- `REVOKE`;
- `ROLLBACK`.

## Memory and state separation

The Drive corpus repeatedly warns against collapsing conversation state, memory, workflow history, execution scratch, and artifact storage into one undifferentiated context store.

The codified architecture should distinguish at least:

- session/thread state;
- project state;
- semantic memory fabric;
- workflow and event history;
- ephemeral tool sandbox;
- persistent artifact library;
- provenance and evidence memory.

Each plane may share physical infrastructure in early prototypes, but the logical distinction must remain stable.

## Lawful learning and promotion

A proposal is not a promotion.

The system may propose new prompts, models, policies, extractors, schemas, plans, or rankings. Promotion is the constitutional act that admits a proposal into operational use or canonical truth.

Promotion must require evidence, replay, policy compatibility, calibration, provenance, and an operator-visible trace.

Soft-lane outputs may assist, propose, rank, summarize, and critique. They do not directly become hard-lane truth or irreversible actuation without validation and policy pass.

## Replay and evidence

Replay is not optional debugging. It is constitutional memory.

Every consequential node transition, command, delegation, artifact, evaluation, promotion, incident, and quarantine decision should produce evidence that can be reconstructed later.

The first implementation kit should therefore include:

- replay envelopes;
- event logs;
- trace events;
- evaluation results;
- promotion decisions;
- incident reports;
- artifact envelopes.

## Repository role

This public GitHub repository should become the canonical public surface for:

- doctrine;
- schemas;
- profiles;
- reference implementation;
- examples;
- conformance tests;
- curriculum index;
- platform integration contracts.

It should not become the production data store, customer operations repo, secret store, or live telemetry archive.

## First executable milestone

Milestone `v0.1.0` should implement the smallest useful constitutional loop:

1. validate a typed node descriptor;
2. register the node;
3. transition the node through legal lifecycle states;
4. record transition evidence;
5. replay an event log;
6. emit an evaluation result;
7. issue a promotion decision;
8. quarantine when thresholds fail.

This turns the program from doctrine into runnable machinery while preserving the public/private boundary.
