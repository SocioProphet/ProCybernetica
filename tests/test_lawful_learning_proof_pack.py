"""Ledger-convergence: a lawful-learning lifecycle record maps to the CANONICAL estate ProofPack,
validated against the vendored proof-pack schema (prophet-core-contracts, commit 6e8a1647)."""
from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from procyber.lawful_learning.loop import run_lifecycle
from procyber.lawful_learning.proof_pack import to_canonical_proof_pack

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "tests" / "fixtures" / "proof-pack.schema.json").read_text())
VALIDATOR = Draft202012Validator(SCHEMA)


def _pack(**over):
    record = run_lifecycle([0.1, 0.2, 0.3, 0.4, 0.5])
    kw = dict(subject_id="ll-run-1", signatures=["did:key:z6Mk"], created_at="2026-08-03T00:00:00Z")
    kw.update(over)
    return to_canonical_proof_pack(record, **kw)


def test_lawful_learning_record_maps_to_canonical_pack():
    pack = _pack()
    errors = sorted(VALIDATOR.iter_errors(pack), key=lambda e: list(e.path))
    assert errors == [], [e.message for e in errors]


def test_pack_carries_ledger_head_epistemic_and_checks():
    pack = _pack()
    assert pack["ledger"]["algo"] == "sha256"
    assert pack["epistemic_level"] in ("bounded", "synthetic")
    assert pack["proof_pack_id"].startswith("proofpack_")
    names = {c["name"] for c in pack["checks"]}
    assert {"constraint_violation", "truth_score"} <= names


def test_unsigned_pack_is_unrepresentable():
    with pytest.raises(ValueError):
        _pack(signatures=[])


def test_epistemic_override_still_schema_valid():
    pack = _pack(epistemic_level="empirical")
    assert pack["epistemic_level"] == "empirical"
    assert list(VALIDATOR.iter_errors(pack)) == []
