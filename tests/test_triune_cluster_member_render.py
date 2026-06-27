"""Tests for the cluster-member record renderer."""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
from pathlib import Path

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "triune" / "cluster-member.v1.json"
INVENTORY = ROOT / "examples" / "triune" / "lab" / "triune-lab.synthetic.yaml"

_renderer_path = ROOT / "tools" / "triune" / "render-cluster-member.py"
_spec = importlib.util.spec_from_file_location("render_cluster_member", _renderer_path)
assert _spec and _spec.loader
_renderer_mod = importlib.util.module_from_spec(_spec)
sys.modules["render_cluster_member"] = _renderer_mod
_spec.loader.exec_module(_renderer_mod)

load_inventory = _renderer_mod.load_inventory
resolve_member = _renderer_mod.resolve_member
render = _renderer_mod.render
validate_output = _renderer_mod.validate_output


def _load_schema():
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _render(member_name: str, live: bool = False) -> dict:
    inventory = load_inventory(INVENTORY)
    entry = resolve_member(inventory, member_name)
    return render(entry, inventory, live=live, operator="test-operator")


# ── Synthetic record rendering ────────────────────────────────────────────────

def test_genesys_record_renders():
    record = _render("genesys")
    assert record["cluster_member_id"] is not None
    assert record["member_role"] == "operator_workstation"
    assert record["execution_status"] == "synthetic_fixture"


def test_k3a_record_renders():
    record = _render("k3-a")
    assert record["member_role"] == "bastion"
    assert record["execution_status"] == "synthetic_fixture"


def test_inception_i1_record_renders():
    record = _render("inception-i1")
    assert record["member_role"] == "inception_control_plane"
    assert record["cluster_member_id"] == "synthetic-i1"
    assert record["control_plane"]["engine"] == "k3s"


def test_inception_i2_record_renders():
    record = _render("inception-i2")
    assert record["cluster_member_id"] == "synthetic-i2"


def test_inception_i3_record_renders():
    record = _render("inception-i3")
    assert record["cluster_member_id"] == "synthetic-i3"


def test_invalid_member_name_raises():
    inventory = load_inventory(INVENTORY)
    with pytest.raises(ValueError, match="not found"):
        resolve_member(inventory, "nonexistent-host")


# ── Schema validation ─────────────────────────────────────────────────────────

def test_genesys_record_validates_against_schema():
    schema = _load_schema()
    record = _render("genesys")
    validate_output(record, schema)  # raises on failure


def test_k3a_record_validates_against_schema():
    schema = _load_schema()
    record = _render("k3-a")
    validate_output(record, schema)


def test_inception_i1_record_validates_against_schema():
    schema = _load_schema()
    record = _render("inception-i1")
    validate_output(record, schema)


# ── Safety invariants ─────────────────────────────────────────────────────────

def test_no_kubeconfig_contents_in_record():
    record = _render("inception-i1")
    record_str = json.dumps(record)
    assert "apiVersion: v1" not in record_str
    assert "clusters:" not in record_str
    assert "certificate-authority-data" not in record_str


def test_synthetic_record_has_non_claims():
    record = _render("inception-i1")
    assert len(record["non_claims"]) > 0


def test_synthetic_flag_in_non_claims():
    record = _render("inception-i1")
    combined = " ".join(record["non_claims"]).lower()
    assert "synthetic" in combined or "live" in combined


def test_production_attachment_not_allowed():
    record = _render("inception-i1")
    assert record["safety_status"]["production_attachment_allowed"] is False


def test_customer_network_not_allowed():
    record = _render("inception-i1")
    assert record["safety_status"]["customer_network_allowed"] is False


def test_no_secrets_written_to_repo_paths(tmp_path):
    """Rendering to a tmp path must not write any kubeconfig content."""
    import subprocess, sys
    out = tmp_path / "test-member.json"
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "triune" / "render-cluster-member.py"),
         "--input", str(INVENTORY), "--member", "inception-i1", "--output", str(out)],
        capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr
    content = out.read_text()
    assert "certificate-authority-data" not in content
    assert "apiVersion: v1" not in content
