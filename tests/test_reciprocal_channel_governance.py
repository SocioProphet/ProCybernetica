from tools.cybernetic_governance.validate_reciprocal_channel_governance import validate


def test_reciprocal_channel_governance_fixtures_pass() -> None:
    result = validate()
    assert result["passed"], result
