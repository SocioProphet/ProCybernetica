.PHONY: test governance-fabric-ci

test:
	python -m pytest -q

governance-fabric-ci:
	python -m pytest -q tests/test_governance_fabric_tier1.py
