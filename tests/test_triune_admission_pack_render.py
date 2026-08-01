"""Tests for the admission pack renderer (admission-pack.v1 vocabulary).

Acceptance: rendered packs must (a) validate against the canonical JSON Schema
and (b) pass tools/triune/validate-admission-pack.py — the admission gate — for
a well-formed proposal, while fail-closed rules refuse to render bad packs.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[1]
DRY_RUN_FIXTURE = ROOT / "examples" / "triune" / "policy-dry-run.synthetic.json"
SCHEMA_PATH = ROOT / "schemas" / "triune" / "admission-pack.v1.json"


def _load_tool(name: str, relpath: str):
    path = ROOT / relpath
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_renderer = _load_tool("render_admission_pack", "tools/triune/render-admission-pack.py")
_validator = _load_tool("validate_admission_pack_tool", "tools/triune/validate-admission-pack.py")

build_pack = _renderer.build_pack
compute_hash = _renderer.compute_hash
validate_admission_pack = _validator.validate_admission_pack


def _load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


class _Args:
    """Minimal stand-in for argparse.Namespace with the renderer's defaults."""

    def __init__(self, **kwargs):
        defaults = dict(
            candidate="synthetic-i4",
            candidate_name="synthetic-inception-i4",
            candidate_status="proposed",
            member_role="faithful_candidate",
            trust_domain="lab_airgapped",
            requested_role="faithful_member",
            event_ir_ref="synthetic://triune/i4/event-ir",
            proof_ref=["synthetic://triune/i4/proofs/policy-dry-run"],
            sbom_ref="synthetic://triune/i4/sbom/spdx",
            signature_ref=["synthetic://triune/i4/signatures/herald-agent"],
            image_ref=["synthetic://triune/i4/images/herald-agent"],
            network_policy_ref="synthetic://triune/policies/default-deny",
            authority_chain_ref="synthetic://triune/authority-chain/i4",
            dry_run_result="pass",
            dry_run_output=str(DRY_RUN_FIXTURE),
            dry_run_evidence_ref="",
            dry_run_id="",
            epsilon_gate="",
            alpha=0.0073,
            approval_kind="host",
            approved_by="",
            approved_at="",
            rollback_action="Remove ClusterMesh peer; revoke credentials; restore deny-all egress.",
            quarantine_action="Quarantine workloads; preserve evidence for replay.",
            max_revoke_seconds=300,
            pack_id="",
            operator="test-operator",
            live=False,
        )
        defaults.update(kwargs)
        for key, value in defaults.items():
            setattr(self, key, value)


def test_good_pack_validates_against_schema_and_admission_gate() -> None:
    pack = build_pack(_Args())
    jsonschema.validate(pack, _load_schema())          # (a) schema
    errors = validate_admission_pack(pack)             # (b) admission gate
    assert errors == [], f"admission validator rejected a good pack: {errors}"


def test_pass_claim_is_hash_bound_to_dry_run_output() -> None:
    pack = build_pack(_Args())
    expected = compute_hash(DRY_RUN_FIXTURE)
    gate = pack["epsilon_gate"]
    assert gate["epsilon_gate_passed"] is True
    assert gate["dry_run_output_hash"] == expected
    assert gate["dry_run_evidence_ref"]


def test_pass_without_dry_run_output_is_refused() -> None:
    with pytest.raises(ValueError, match="requires --dry-run-output"):
        build_pack(_Args(dry_run_output=""))


def test_pass_with_violations_is_refused(tmp_path: Path) -> None:
    dr = json.loads(DRY_RUN_FIXTURE.read_text(encoding="utf-8"))
    dr["violations"] = ["privileged pod detected"]
    bad = tmp_path / "dry-run-violations.json"
    bad.write_text(json.dumps(dr), encoding="utf-8")
    with pytest.raises(ValueError, match="violation"):
        build_pack(_Args(dry_run_output=str(bad)))


def test_flag_result_contradicting_output_result_is_refused() -> None:
    """Fail closed: the pack is hash-bound to the dry-run artifact, so a CLI
    --dry-run-result that disagrees with the artifact's own recorded `result` must be
    refused — otherwise a pack could claim one verdict while its evidence says another.
    The fixture records result='pass'; claiming 'fail' contradicts it."""
    with pytest.raises(ValueError, match="contradicts the dry-run output"):
        build_pack(_Args(dry_run_result="fail"))


def test_dry_run_without_checked_policies_is_refused(tmp_path: Path) -> None:
    dr = json.loads(DRY_RUN_FIXTURE.read_text(encoding="utf-8"))
    dr["checked_policies"] = []
    bad = tmp_path / "dry-run-nopolicies.json"
    bad.write_text(json.dumps(dr), encoding="utf-8")
    with pytest.raises(ValueError, match="checked policy"):
        build_pack(_Args(dry_run_output=str(bad)))


def test_approved_requires_host_approval() -> None:
    with pytest.raises(ValueError, match="HOST approval"):
        build_pack(_Args(candidate_status="approved"))


def test_delegated_operator_approval_is_not_sufficient_for_admitted() -> None:
    with pytest.raises(ValueError, match="HOST approval"):
        build_pack(_Args(
            candidate_status="admitted",
            approved_by="delegate-1",
            approved_at="2026-07-05T00:00:00Z",
            approval_kind="delegated_operator",
        ))


def test_host_approved_pack_passes_schema_and_gate() -> None:
    pack = build_pack(_Args(
        candidate_status="approved",
        approved_by="host-operator",
        approved_at="2026-07-05T00:00:00Z",
        approval_kind="host",
    ))
    jsonschema.validate(pack, _load_schema())
    assert validate_admission_pack(pack) == []
    approvals = pack["admission_decision"]["approvals"]
    assert any(a["approval_kind"] == "host" for a in approvals)


def test_failed_dry_run_renders_schema_valid_but_gate_rejects(tmp_path: Path) -> None:
    """A fail-pack is a legitimate RECORD (schema-valid) but must never pass
    the admission gate — this is the fail-closed proof."""
    dr = json.loads(DRY_RUN_FIXTURE.read_text(encoding="utf-8"))
    dr["result"] = "fail"
    dr["violations"] = ["default-deny missing"]
    bad = tmp_path / "dry-run-fail.json"
    bad.write_text(json.dumps(dr), encoding="utf-8")

    pack = build_pack(_Args(dry_run_result="fail", dry_run_output=str(bad)))
    jsonschema.validate(pack, _load_schema())           # schema-valid record
    errors = validate_admission_pack(pack)              # gate must reject
    assert errors, "admission validator accepted a failed dry-run pack"
    gate = pack["epsilon_gate"]
    assert gate["decision"]["gate_result"] == "fail"
    assert gate["epsilon_gate_passed"] is False
    assert "dry_run_output_hash" not in gate            # no hash-bound pass claim


def test_synthesized_epsilon_gate_is_internally_consistent() -> None:
    """Measurements must sit inside the alpha scale limits the validator enforces."""
    pack = build_pack(_Args())
    gate = pack["epsilon_gate"]
    alpha = gate["alpha"]
    limits = gate["scale_limits"]
    by_scale: dict[str, list[float]] = {"micro": [], "meso": [], "macro": []}
    for m in gate["measurements"]:
        by_scale[m["scale"]].append(m["epsilon_eff"])
    assert max(by_scale["micro"]) <= alpha * limits["micro_multiplier"]
    assert max(by_scale["meso"]) <= alpha * limits["meso_multiplier"]
    assert max(by_scale["macro"]) <= alpha * limits["macro_p95_multiplier"]


def test_ledger_entry_uses_canonical_shape() -> None:
    pack = build_pack(_Args())
    entry = pack["ledger_entry"]
    assert set(entry) == {"event_id", "event_type", "created_at"}
    assert entry["event_type"] == "admission_pack_rendered"
