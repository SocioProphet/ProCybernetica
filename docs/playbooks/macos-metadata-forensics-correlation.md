# MFEL Playbook — macOS Metadata Forensics Correlation

Status: v0.1 public-safe playbook  
Standard: SP-STD-MFEL-0001  
Runtime claim: none

## Purpose

This playbook defines how ProCybernetica reviews macOS metadata artifacts under SP-STD-MFEL-0001 without overclaiming from local indexing, cache churn, diagnostic summaries, or service activity.

The playbook is designed for sanitized/public-safe case records. It does not authorize collection, surveillance, endpoint monitoring, actor attribution, or raw-log publication.

## Inputs

Permitted public-safe inputs include:

- sanitized Core Spotlight plist summaries;
- sanitized Notes/Spotlight indexing summaries;
- sanitized FileProvider, iCloud, or CloudKit churn summaries;
- sanitized CoreSuggestions adjacency notes;
- sanitized SpotlightKnowledge journal/keyphrase/NLP processing summaries;
- sanitized boot/reset or kernel-panic seam summaries;
- sanitized microstackshot/resource-pressure summaries;
- synthetic fixtures representing the above.

Raw private logs, account identifiers, device identifiers, local absolute paths, note body text, credentials, private message content, and customer/user data must not be committed to the public repository.

## Case format

Every case should validate against:

```text
schemas/mfel/observation.schema.json
```

The public case must include:

- `redaction_boundary`;
- `observed_facts`;
- `derived_facts`;
- `interpretations`;
- `hypotheses`;
- `prohibited_conclusions`;
- `negative_evidence`;
- `missing_evidence`;
- `non_claims`.

## Workflow

### 1. Declare the redaction boundary

State what is withheld and why. Common withheld fields:

- account identifiers;
- device identifiers;
- absolute local paths;
- private note content;
- raw plist values;
- raw log lines containing private data;
- local usernames;
- private bundle state.

Do not hide missing evidence behind redaction language. If evidence is necessary but withheld, say so explicitly.

### 2. Record observed facts only

Observed facts are direct or sanitized observations, such as:

- a plist key exists;
- a sanitized metadata record indicates indexing;
- a service emitted a resource-pressure summary;
- a boot/reset seam occurred;
- a FileProvider or CloudKit state transition is present in a sanitized summary.

Observed facts do not establish compromise, intent, actor identity, remote access, or exfiltration.

### 3. Derive bounded facts

Derived facts may connect observations through deterministic or bounded transforms:

- grouping by service family;
- comparing timestamps within a declared window;
- classifying records as local indexing or service churn;
- identifying that a case lacks network evidence;
- identifying that a case lacks actor attribution basis.

Every derived fact must name its derivation and input references.

### 4. Interpret with alternatives

Interpretations must include plausible alternatives. Common alternatives:

- normal Spotlight indexing;
- cache rebuild;
- Notes metadata refresh;
- FileProvider sync;
- iCloud or CloudKit state churn;
- OS service maintenance;
- diagnostic collection;
- local configuration drift;
- unexplained artifact requiring private-evidence review.

An interpretation remains defeasible.

### 5. State hypotheses with negative and missing evidence

Suspicious or high-risk hypotheses require negative evidence and missing evidence.

Examples of missing evidence:

- endpoint forensic trace;
- packet or connection telemetry;
- authenticated access-control evidence;
- independent corroboration from an unrelated evidence source;
- signed external actor indicator;
- chain of custody for raw artifacts.

Examples of negative evidence:

- local indexing is a plausible explanation;
- no network-flow artifact is included;
- no actor attribution evidence is included;
- artifact source is a single dependent pipeline;
- private data is withheld from public review.

### 6. Record prohibited conclusions

Prohibited conclusions are not optional. A metadata-forensics case should explicitly say what it does not license.

Common prohibited conclusions:

- remote exfiltration from local indexing evidence alone;
- coordinated compromise from plist churn alone;
- actor attribution from metadata clustering alone;
- surveillance claims from local diagnostic summaries alone;
- production incident status from sanitized examples.

## Review checklist

A macOS metadata case is not standard-conforming unless:

- [ ] redaction boundary is explicit;
- [ ] raw private logs are absent from the public artifact;
- [ ] every observation is in `observed_facts`;
- [ ] every inference is outside `observed_facts`;
- [ ] every suspicious/high-risk hypothesis has `negative_evidence` and `missing_evidence`;
- [ ] prohibited conclusions are present;
- [ ] actor attribution is absent or evidence-bound;
- [ ] non-claims are explicit.

## Anti-patterns

Do not write:

- "Spotlight indexed a note, therefore it was exfiltrated.";
- "plist churn means compromise.";
- "microstackshots prove surveillance.";
- "absence of a benign explanation proves an adversary.";
- "multiple records from one pipeline are independent corroboration.";
- "sanitized evidence implies private evidence must exist."

## Public-safe examples

Reference examples:

- `examples/mfel/notes-spotlight-indexing.sanitized.yaml`;
- `examples/mfel/corespotlight-plist.sanitized.yaml`.

These examples are method fixtures. They do not describe live incidents and do not claim compromise, actor attribution, remote access, or exfiltration.
