"""Tests for the outbound chokepoint — both ways.

Two things must hold: emission is unreachable without a cleared share decision, and
there is exactly ONE way out. The second is checked against the real tree, not a
fixture, because a chokepoint that is only true of a test double is not one.
"""

from __future__ import annotations

import json

import pytest

from procyber.semantic.internal_model import (
    NO_CEILING,
    InternalModelState,
    RuleVerdict,
    ShareRequest,
    evaluate,
)
from procyber.semantic.semantic_algebra import BOTTOM, SemanticAddress, mul, prim, POT, FST
from procyber.semantic.serialization_channel import (
    ChannelRefusal,
    WireEnvelope,
    emit,
    single_channel_violations,
)

MANDATE = frozenset({"telemetry"})


def _addr(**kw) -> SemanticAddress:
    return SemanticAddress(term=mul(mul(prim(POT), prim(FST)), mul(prim(POT), prim(FST))), **kw)


def _cleared() -> InternalModelState:
    return evaluate(
        ShareRequest(
            address=_addr(inference="deduced", evidence_ref="ev://1"),
            counterparty="peer:a",
            our_mandate=MANDATE,
            counterparty_mandate=MANDATE,
            topic="telemetry",
            as_of="2026-08-03",
            counterparty_trusted=True,
        )
    )


def _refused() -> InternalModelState:
    return evaluate(
        ShareRequest(
            address=_addr(inference="deduced"),  # no evidence_ref -> provenance refuses
            counterparty="peer:a",
            our_mandate=MANDATE,
            counterparty_mandate=MANDATE,
            topic="telemetry",
            as_of="2026-08-03",
            counterparty_trusted=True,
        )
    )


# --------------------------------------------------------------------------- #
# Emission requires a cleared decision
# --------------------------------------------------------------------------- #


def test_a_cleared_decision_emits():
    env = emit({"k": "v"}, channel="peer:a", decision=_cleared())
    assert isinstance(env, WireEnvelope)
    assert env.verify()


def test_a_refused_decision_cannot_emit():
    with pytest.raises(ChannelRefusal) as excinfo:
        emit({"k": "v"}, channel="peer:a", decision=_refused())
    assert "provenance" in str(excinfo.value)


def test_an_abstained_decision_cannot_emit():
    """BOTTOM is not a weak yes."""
    abstained = InternalModelState(admit=(RuleVerdict("a", "sealed", "s"),), withhold=())
    assert abstained.equilibrium is BOTTOM
    with pytest.raises(ChannelRefusal) as excinfo:
        emit({"k": "v"}, channel="peer:a", decision=abstained)
    assert "abstained" in str(excinfo.value)


def test_refusal_raises_rather_than_returning_falsy():
    """A refusal a caller can ignore by not checking the result is not a refusal."""
    with pytest.raises(ChannelRefusal):
        emit({"k": "v"}, channel="peer:a", decision=_refused())


def test_decision_is_required_and_keyword_only():
    with pytest.raises(TypeError):
        emit({"k": "v"}, channel="peer:a")  # type: ignore[call-arg]


def test_non_mapping_payload_refused():
    with pytest.raises(TypeError):
        emit(["not", "a", "mapping"], channel="peer:a", decision=_cleared())  # type: ignore[arg-type]


# --------------------------------------------------------------------------- #
# What travels
# --------------------------------------------------------------------------- #


def test_the_warrant_travels_with_the_payload():
    """A receiver that cannot see why something was sent cannot evaluate it."""
    env = emit({"k": "v"}, channel="peer:a", decision=_cleared())
    body = json.loads(env.body)
    assert body["warrant"]["verdict"]
    assert body["warrant"]["bindingReason"]


def test_an_address_travels_as_a_skeleton_not_in_full():
    """Structure travels; the referent and evidence pointer stay behind."""
    env = emit(
        {"k": "v"},
        channel="peer:a",
        decision=_cleared(),
        address=_addr(iri="kko:Sensitive", evidence_ref="ev://secret"),
    )
    assert "kko:Sensitive" not in env.body
    assert "ev://secret" not in env.body
    assert json.loads(env.body)["address"]["code"]


def test_the_body_is_canonical_and_reproducible():
    a = emit({"b": 1, "a": 2}, channel="c", decision=_cleared())
    b = emit({"a": 2, "b": 1}, channel="c", decision=_cleared())
    assert a.body == b.body
    assert a.digest == b.digest


def test_tampering_is_detectable():
    env = emit({"k": "v"}, channel="peer:a", decision=_cleared())
    tampered = WireEnvelope(channel=env.channel, body=env.body.replace('"v"', '"w"'), digest=env.digest)
    assert env.verify()
    assert not tampered.verify()


# --------------------------------------------------------------------------- #
# Exactly one way out — checked against the real tree
# --------------------------------------------------------------------------- #


def test_the_shipped_kernel_has_exactly_one_outbound_path():
    violations = single_channel_violations()
    assert violations == [], f"second outbound path: {violations}"


def test_the_detector_bites_on_json_encoded_elsewhere(tmp_path):
    leak = tmp_path / "sneaky.py"
    leak.write_text("import json\ndef out(x):\n    return json.dumps(x)\n", encoding="utf-8")
    findings = single_channel_violations([str(leak)])
    assert any("JSON encoded outside" in f[2] for f in findings)


def test_the_detector_bites_on_an_envelope_built_elsewhere(tmp_path):
    leak = tmp_path / "forger.py"
    leak.write_text("def out():\n    return WireEnvelope(channel='x', body='{}', digest='d')\n", encoding="utf-8")
    findings = single_channel_violations([str(leak)])
    assert any("WireEnvelope constructed outside" in f[2] for f in findings)


def test_the_detector_excludes_the_channel_itself():
    """The channel necessarily does both things it forbids elsewhere."""
    from procyber.semantic import serialization_channel

    assert single_channel_violations([serialization_channel.__file__]) == []


def test_the_encoding_primitive_is_permitted():
    from procyber.semantic import semantic_algebra

    assert single_channel_violations([semantic_algebra.__file__]) == []
