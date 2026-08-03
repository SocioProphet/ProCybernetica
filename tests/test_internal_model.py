"""Tests for the share/withhold equilibrium — both ways, rule by rule.

The invariant that matters most is negative: **an admit signal must never authorise a
share on its own.** Most of this file exists to attack that from different angles,
because a share/withhold organ whose withhold arm can be bypassed is worse than none
— it launders a disclosure as a governed decision.
"""

from __future__ import annotations

import pytest

from procyber.semantic.internal_model import (
    ADMIT_RULES,
    NO_CEILING,
    SHARE_THRESHOLD,
    WITHHOLD_RULES,
    InternalModelState,
    RuleVerdict,
    ShareRequest,
    admit_capability_offer,
    admit_contextualized_specialization,
    admit_counter_example,
    admit_generalization,
    admit_precedent,
    evaluate,
    withhold_contradiction_with_law,
    withhold_linkability_risk,
    withhold_out_of_mandate,
    withhold_provenance_insufficient,
    withhold_staleness,
)
from procyber.semantic.semantic_algebra import (
    ACT,
    BOTTOM,
    FST,
    POT,
    SND,
    SemanticAddress,
    mul,
    prim,
)

MANDATE = frozenset({"telemetry"})


def _addr(layer: int = 2, **kw) -> SemanticAddress:
    term = mul(prim(POT), prim(FST))
    for _ in range(layer - 1):
        term = mul(term, term)
    return SemanticAddress(term=term, **kw)


def _req(**overrides) -> ShareRequest:
    defaults = dict(
        address=_addr(inference="deduced", evidence_ref="ev://1"),
        counterparty="peer:a",
        our_mandate=MANDATE,
        counterparty_mandate=MANDATE,
        topic="telemetry",
        as_of="2026-08-03",
        counterparty_trusted=True,
    )
    defaults.update(overrides)
    return ShareRequest(**defaults)  # type: ignore[arg-type]


# --------------------------------------------------------------------------- #
# The central invariant
# --------------------------------------------------------------------------- #


def test_admit_alone_never_authorises_a_share():
    """An arm that was never evaluated is BOTTOM, and BOTTOM never clears."""
    state = InternalModelState(admit=(RuleVerdict("x", "sealed", "strongest possible"),), withhold=())
    assert state.admit_arm == "sealed"
    assert state.withhold_arm is BOTTOM
    assert state.equilibrium is BOTTOM
    assert state.may_share() is False


def test_withhold_alone_never_authorises_a_share():
    state = InternalModelState(admit=(), withhold=(RuleVerdict("y", NO_CEILING, "clean"),))
    assert state.admit_arm is BOTTOM
    assert state.equilibrium is BOTTOM
    assert state.may_share() is False


def test_equilibrium_never_exceeds_the_withhold_arm():
    """The property that makes withhold rules ceilings rather than weights."""
    from procyber.semantic.semantic_algebra import VERDICT_ORDER

    for withhold in VERDICT_ORDER:
        state = InternalModelState(
            admit=(RuleVerdict("a", "sealed", "max case"),),
            withhold=(RuleVerdict("w", withhold, "ceiling"),),
        )
        assert state.equilibrium == withhold


def test_a_single_refusal_governs_however_strong_the_admit_case():
    state = InternalModelState(
        admit=tuple(RuleVerdict(f"a{i}", "sealed", "strong") for i in range(5)),
        withhold=(
            RuleVerdict("w1", NO_CEILING, "clean"),
            RuleVerdict("w2", "refuse", "veto"),
            RuleVerdict("w3", NO_CEILING, "clean"),
        ),
    )
    assert state.equilibrium == "refuse"
    assert state.may_share() is False


def test_nothing_objected_is_not_nothing_asked():
    """NO_CEILING and BOTTOM must stay distinct or unexamined shares slip through."""
    assert NO_CEILING is not BOTTOM
    asked = InternalModelState(
        admit=(RuleVerdict("a", "probable", "case"),),
        withhold=(RuleVerdict("w", NO_CEILING, "clean"),),
    )
    not_asked = InternalModelState(admit=(RuleVerdict("a", "probable", "case"),), withhold=())
    assert asked.may_share() is True
    assert not_asked.may_share() is False


def test_no_admit_rule_applying_abstains():
    state = InternalModelState(
        admit=(RuleVerdict("a", BOTTOM, "n/a"),),
        withhold=(RuleVerdict("w", NO_CEILING, "clean"),),
    )
    assert state.admit_arm is BOTTOM
    assert state.equilibrium is BOTTOM


# --------------------------------------------------------------------------- #
# Admit rules — each fires and each abstains
# --------------------------------------------------------------------------- #


def test_generalization_fires_on_a_derived_general_claim():
    v = admit_generalization(_req(address=_addr(layer=2, inference="induced")))
    assert v.verdict == "sealed"


def test_generalization_is_weaker_when_merely_asserted():
    v = admit_generalization(_req(address=_addr(layer=2, inference="asserted")))
    assert v.verdict == "probable"


def test_generalization_abstains_on_a_specific_claim():
    assert admit_generalization(_req(address=_addr(layer=1))).verdict is BOTTOM


def test_specialization_requires_a_context_envelope():
    with_env = admit_contextualized_specialization(_req(address=_addr(valid_until="2027-01-01")))
    without = admit_contextualized_specialization(_req(address=_addr()))
    assert with_env.verdict == "probable"
    assert without.verdict is BOTTOM


def test_precedent_requires_an_evidence_pointer():
    assert admit_precedent(_req(address=_addr(evidence_ref="ev://7"))).verdict == "probable"
    assert admit_precedent(_req(address=_addr())).verdict is BOTTOM


def test_counter_example_is_the_strongest_admit_case():
    assert admit_counter_example(_req(address=_addr(mood="negate"))).verdict == "sealed"
    assert admit_counter_example(_req(address=_addr(mood="assert"))).verdict is BOTTOM


def test_capability_offer_requires_the_topic_in_our_mandate():
    assert admit_capability_offer(_req(topic="telemetry")).verdict == "probable"
    assert admit_capability_offer(_req(topic="payroll")).verdict is BOTTOM


def test_there_are_exactly_five_admit_rules():
    assert len(ADMIT_RULES) == 5


# --------------------------------------------------------------------------- #
# Withhold rules — each imposes its ceiling and each clears
# --------------------------------------------------------------------------- #


def test_provenance_refuses_without_an_evidence_chain():
    assert withhold_provenance_insufficient(_req(address=_addr())).verdict == "refuse"
    assert withhold_provenance_insufficient(_req(address=_addr(evidence_ref="ev://1"))).verdict == NO_CEILING


def test_linkability_quarantines_a_grounded_address_to_an_untrusted_peer():
    v = withhold_linkability_risk(
        _req(address=_addr(iri="kko:Subject", evidence_ref="ev://1"), counterparty_trusted=False)
    )
    assert v.verdict == "quarantine"


def test_linkability_clears_for_a_trusted_peer():
    v = withhold_linkability_risk(
        _req(address=_addr(iri="kko:Subject", evidence_ref="ev://1"), counterparty_trusted=True)
    )
    assert v.verdict == NO_CEILING


def test_skeleton_only_clears_linkability_even_when_untrusted():
    """Structure may travel where the referent may not."""
    v = withhold_linkability_risk(
        _req(
            address=_addr(iri="kko:Subject", evidence_ref="ev://1"),
            counterparty_trusted=False,
            skeleton_only=True,
        )
    )
    assert v.verdict == NO_CEILING


def test_staleness_caps_an_expired_claim_without_refusing_it():
    """A lapsed claim may still be shared — never as a current one."""
    v = withhold_staleness(_req(address=_addr(valid_until="2023-12-31"), as_of="2026-08-03"))
    assert v.verdict == "weak"
    assert v.verdict != "refuse"


def test_staleness_clears_within_validity():
    v = withhold_staleness(_req(address=_addr(valid_until="2030-01-01"), as_of="2026-08-03"))
    assert v.verdict == NO_CEILING


def test_out_of_mandate_refuses_on_either_side():
    ours = withhold_out_of_mandate(_req(topic="payroll"))
    theirs = withhold_out_of_mandate(
        _req(topic="telemetry", counterparty_mandate=frozenset({"other"}))
    )
    assert ours.verdict == "refuse"
    assert theirs.verdict == "refuse"


def test_in_both_mandates_clears():
    assert withhold_out_of_mandate(_req()).verdict == NO_CEILING


def test_standing_policy_conflict_refuses():
    assert withhold_contradiction_with_law(_req(standing_policy_conflict=True)).verdict == "refuse"


def test_a_revoked_address_refuses():
    v = withhold_contradiction_with_law(_req(address=_addr(revocation_ref="rev://9")))
    assert v.verdict == "refuse"


def test_there_are_exactly_five_withhold_rules():
    assert len(WITHHOLD_RULES) == 5


# --------------------------------------------------------------------------- #
# End to end
# --------------------------------------------------------------------------- #


def test_a_clean_general_claim_may_be_shared():
    state = evaluate(_req(address=_addr(layer=2, inference="deduced", evidence_ref="ev://1")))
    assert state.may_share() is True
    assert state.equilibrium == NO_CEILING


def test_a_claim_without_provenance_is_refused_end_to_end():
    state = evaluate(_req(address=_addr(layer=2, inference="deduced")))
    assert state.equilibrium == "refuse"
    assert state.may_share() is False
    assert "provenance" in state.binding_reason()


def test_a_grounded_claim_to_an_untrusted_peer_is_quarantined_end_to_end():
    state = evaluate(
        _req(
            address=_addr(layer=2, inference="deduced", evidence_ref="ev://1", iri="kko:Subject"),
            counterparty_trusted=False,
        )
    )
    assert state.equilibrium == "quarantine"
    assert state.may_share() is False
    assert "linkability" in state.binding_reason()


def test_evaluate_always_runs_both_arms():
    """There is no code path that produces a decision from one arm."""
    state = evaluate(_req())
    assert len(state.admit) == len(ADMIT_RULES)
    assert len(state.withhold) == len(WITHHOLD_RULES)


def test_binding_reason_names_the_governing_rule():
    state = evaluate(_req(topic="payroll", our_mandate=frozenset({"payroll"})))
    assert "out_of_mandate" in state.binding_reason()


def test_binding_reason_says_when_no_case_was_made():
    state = InternalModelState(
        admit=(RuleVerdict("a", BOTTOM, "n/a"),),
        withhold=(RuleVerdict("w", NO_CEILING, "clean"),),
    )
    assert "no case for sharing" in state.binding_reason()


def test_every_rule_gives_a_reason():
    state = evaluate(_req())
    for verdict in state.admit + state.withhold:
        assert verdict.reason, f"{verdict.rule} returned a verdict with no reason"


def test_serialisation_reports_both_arms_and_the_binding_reason():
    payload = evaluate(_req()).to_json()
    assert payload["mayShare"] is True
    assert payload["admitArm"] and payload["withholdArm"]
    assert len(payload["admit"]) == 5 and len(payload["withhold"]) == 5
    assert payload["bindingReason"]


def test_abstention_serialises_as_null_not_as_a_verdict():
    state = InternalModelState(admit=(RuleVerdict("a", "sealed", "s"),), withhold=())
    payload = state.to_json()
    assert payload["equilibrium"] is None
    assert payload["mayShare"] is False


def test_threshold_is_respected():
    state = InternalModelState(
        admit=(RuleVerdict("a", "sealed", "s"),),
        withhold=(RuleVerdict("w", "weak", "cap"),),
    )
    assert state.may_share(threshold="weak") is True
    assert state.may_share(threshold=SHARE_THRESHOLD) is False
