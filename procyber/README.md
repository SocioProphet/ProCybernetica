# procyber

Reference implementation package for the public ProCybernetica contracts.

The package is intentionally small at first. Its job is to prove the constitutional loop:

1. load and validate schema-bound envelopes;
2. register and supervise nodes;
3. emit lifecycle transition records;
4. replay event evidence;
5. evaluate replay outputs;
6. issue promotion or quarantine decisions.

This package should remain a reference implementation. Production services should consume the same schemas and profiles but may use different storage, policy, telemetry, and orchestration backends.
