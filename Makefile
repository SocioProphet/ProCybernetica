.PHONY: test governance-fabric-tier1-ci governance-fabric-tier2-ci governance-fabric-ci triune-ci

test:
	python -m pytest -q

governance-fabric-tier1-ci:
	python -m pytest -q tests/test_governance_fabric_tier1.py

governance-fabric-tier2-ci:
	python -m pytest -q tests/test_governance_fabric_tier2.py

governance-fabric-ci: governance-fabric-tier1-ci governance-fabric-tier2-ci

triune-ci:
	python -m pytest -q tests/test_triune_admission.py
