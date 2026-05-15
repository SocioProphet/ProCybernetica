# Calibrated Lawful Learning Conformance

Status: v0.1 conformance smoke  
Issue: #24  
Runtime claim: none

## Purpose

This note records the repository-native conformance smoke for calibrated lawful learning.

The conformance lane validates:

- JSON Schema parseability for `schemas/lawful-learning/*.schema.json`;
- YAML parseability and semantic section checks for `examples/lawful-learning/*.yaml`;
- deterministic toy worked examples in `tests/test_lawful_learning_toy.py`.

## Commands

Run the lightweight schema/example validator:

```bash
make lawful-learning-fixtures
```

Run the local conformance lane:

```bash
make lawful-learning-ci
```

Run the deterministic toy examples directly:

```bash
PYTHONPATH=. python -m pytest -q tests/test_lawful_learning_toy.py
```

Run the conformance smoke tests directly:

```bash
PYTHONPATH=. python -m pytest -q tests/test_lawful_learning_conformance.py
```

## Coverage

Schema files:

```text
schemas/lawful-learning/model.schema.json
schemas/lawful-learning/constraint.schema.json
schemas/lawful-learning/ledger.schema.json
```

Example files:

```text
examples/lawful-learning/model.yaml
examples/lawful-learning/tuning.yaml
examples/lawful-learning/ledger.yaml
```

Toy worked examples:

```text
procyber/lawful_learning/toy.py
tests/test_lawful_learning_toy.py
```

## Non-claims

No live data are used. The YAML examples are deterministic formal configuration examples only. The toy examples are deterministic calculations, not empirical results, production evidence, or model-performance claims.
