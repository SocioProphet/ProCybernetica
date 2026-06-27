"""Tests for the admission pack renderer."""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
from pathlib import Path

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[1]
DRY_RUN_FIXTURE = ROOT / "examples" / "triune" / "policy-dry-run.synthetic.json"
SCHEMA_PATH = ROOT / "schemas" / "triune" / "admission-pack.v1.json"

_renderer_path = ROOT / "tools" / "triune" / "render-admission-pack.py"
_spec = importlib.util.spec_from_file_location("render_admission_pack", _renderer_path)
assert _spec and _spec.loader
_renderer_mod = importlib.util.module_from_spec(_spec)
sys.modules["render_admission_pack"] = _renderer_mod
_spec.loader.exec_module(_renderer_mod)

build_pack = _renderer_mod.build_pack
compute_hash = _renderer_mod.compute_hash


def _load_schema():
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


class _Args:
    """Minimal stand-in for argparse.Namespace."""
    def __init__(self, **kwargs):
        defaults = dict(
            candidate="synthetic-i4",
            candidate_name="synthetic-inception-i4",
            candidate_status="proposed",
            event_ir_ref="synthetic://triune/i4/event-ir",
            proof_ref="synthetic://triune/i4/proofs/policy-dry-run",
            sbom_ref="",
            signature_ref="",
            image_ref="",
            network_policy_ref="",
            dry_run_result="pass",
            dry_run_output=str(DRY_RUN_FIXTURE),
            dry_run_evidence_ref="synthetic://triune/i4/evidence/policy-dry-run.json",
            revocation_ref="synthetic://triune/i4/evidence/revocation-plan.json",
            host_approval_kind="",
            approved_by="",
            approved_at="",
            pack_id="",
            operator="test-operator",
            live=False,
        )
        defaults.update(kwargs)
        for k, v in defaults.items():
            setattr(self, k, v)


# ── Pass pack validates ───────────────────────────────────────────────────────

def test_synthetic_pass_pack_validates():
    schema = _load_schema()
    pack = build_pack(_Args())
    jsonschema.validate(pack, schema)


def test_synthetic_pass_pack_has_hash():
    pack = build_pack(_Args())
    assert len(pack["policy"]["dry_run_output_hash"]) == 64
    assert pack["policy"]["dry_run_output_hash"].islower()


def test_synthetic_pass_pack_status_is_proposed():
    pack = build_pack(_Args())
    assert pack["candidate_status"] == "proposed"


def test_synthetic_pass_pack_is_synthetic_fixture():
    pack = build_pack(_Args())
    assert pack["execution_status"] == "synthetic_fixture"


# ── Missing dry-run hash fails ────────────────────────────────────────────────

def test_missing_dry_run_output_with_pass_result_raises():
    with pytest.raises(ValueError, match="dry-run-output"):
        build_pack(_Args(dry_run_result="pass", dry_run_output=""))


# ── Missing dry-run evidence ref fails ───────────────────────────────────────

def test_missing_evidence_ref_with_no_output_path_raises():
    with pytest.raises(ValueError, match="dry-run-evidence-ref|dry-run-output"):
        build_pack(_Args(
            dry_run_result="pass",
            dry_run_output="",
            dry_run_evidence_ref="",
        ))


# ── Approved without host approval fails ─────────────────────────────────────

def test_approved_without_host_approval_raises():
    with pytest.raises(ValueError, match="host_approval_kind|approved"):
        build_pack(_Args(candidate_status="approved"))


# ── Admitted without host approval fails ─────────────────────────────────────

def test_admitted_without_host_approval_raises():
    with pytest.raises(ValueError, match="host_approval_kind|approved"):
        build_pack(_Args(candidate_status="admitted"))


# ── Approved WITH host approval succeeds ─────────────────────────────────────

def test_approved_with_host_approval_renders():
    pack = build_pack(_Args(
        candidate_status="approved",
        host_approval_kind="host",
        approved_by="operator-1",
        approved_at="2026-06-11T00:00:00Z",
    ))
    assert pack["candidate_status"] == "approved"
    assert pack["decision"]["host_approval"]["approved_by"] == "operator-1"


# ── Policy violations fail admission ─────────────────────────────────────────

def test_violation_in_dry_run_sets_gate_fail(tmp_path):
    violation_fixture = tmp_path / "dry-run-violation.json"
    violation_fixture.write_text(json.dumps({
        "dry_run_id": "test-violation",
        "result": "pass",
        "checked_policies": ["no-privileged-pods"],
        "violations": ["no-privileged-pods: pod spec allows privileged=true"],
    }), encoding="utf-8")
    pack = build_pack(_Args(
        dry_run_output=str(violation_fixture),
        dry_run_evidence_ref="local://test-violation.json",
    ))
    assert pack["decision"]["gate_result"] == "fail"
    assert pack["policy"]["violations"] != []


# ── Reversal plan required ────────────────────────────────────────────────────

def test_reversal_plan_present_with_steps():
    pack = build_pack(_Args())
    assert len(pack["reversal_plan"]["steps"]) > 0
    assert pack["reversal_plan"]["revocation_evidence_ref"] != ""


# ── Non-claims required ───────────────────────────────────────────────────────

def test_non_claims_present():
    pack = build_pack(_Args())
    assert len(pack["non_claims"]) > 0


# ── No secrets in output ─────────────────────────────────────────────────────

def test_no_secrets_in_rendered_pack(tmp_path):
    import subprocess
    out = tmp_path / "test-pack.json"
    result = subprocess.run(
        [sys.executable,
         str(ROOT / "tools" / "triune" / "render-admission-pack.py"),
         "--candidate", "synthetic-i4",
         "--candidate-name", "synthetic-inception-i4",
         "--event-ir-ref", "synthetic://triune/i4/event-ir",
         "--dry-run-result", "pass",
         "--dry-run-output", str(DRY_RUN_FIXTURE),
         "--dry-run-evidence-ref", "synthetic://triune/i4/evidence/policy-dry-run.json",
         "--output", str(out)],
        capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr
    content = out.read_text()
    assert "apiVersion: v1" not in content
    assert "certificate-authority-data" not in content
    # Verify schema
    pack = json.loads(content)
    schema = _load_schema()
    jsonschema.validate(pack, schema)
