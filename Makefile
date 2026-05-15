.PHONY: test governance-fabric-tier1-ci governance-fabric-tier2-ci governance-fabric-ci triune-ci falsification-static falsification-fixtures falsification-cross-reference falsification-ci cybernetic-governance-fixtures cybernetic-governance-ci

test:
	python -m pytest -q

governance-fabric-tier1-ci:
	python -m pytest -q tests/test_governance_fabric_tier1.py

governance-fabric-tier2-ci:
	python -m pytest -q tests/test_governance_fabric_tier2.py

governance-fabric-ci: governance-fabric-tier1-ci governance-fabric-tier2-ci

triune-ci:
	python -m pytest -q tests/test_triune_admission.py

falsification-static:
	python scripts/validate_falsification_coverage.py

falsification-fixtures:
	python scripts/validate_falsification_fixture.py

falsification-cross-reference:
	python scripts/validate_falsification_coverage.py

falsification-ci: falsification-static falsification-fixtures falsification-cross-reference

cybernetic-governance-fixtures:
	python tools/cybernetic_governance/validate_defensive_fixtures.py

cybernetic-governance-ci: cybernetic-governance-fixtures
