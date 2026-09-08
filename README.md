# Security Automation Toolkit

A defensive security engineering toolkit for normalizing findings, prioritizing risk, generating remediation queues, and validating closure using synthetic data. The project demonstrates how repetitive security operations can be converted into transparent, testable automation without relying on production credentials or client data.

## Why this project exists
Security teams often receive findings from multiple scanners and telemetry sources with inconsistent schemas. This project provides a small but extensible Python pipeline that:

1. normalizes heterogeneous findings into a canonical model;
2. calculates an explainable risk score using severity, asset criticality, exploit context, and exposure;
3. creates remediation queues by owner and SLA status;
4. validates whether remediation evidence is sufficient to close a finding;
5. produces analyst-friendly summary metrics.

## Architecture

```text
Synthetic inputs
     |
     v
Normalizer ---> Canonical Finding Model
     |                    |
     v                    v
Risk Engine --------> Prioritized Queue
     |                    |
     v                    v
Metrics             Remediation Validator
```

## Repository structure

```text
src/
  models.py
  normalizer.py
  risk_engine.py
  remediation.py
  cli.py
data/
  synthetic_findings.json
tests/
  test_pipeline.py
docs/
  architecture.md
  validation-playbook.md
.github/workflows/
  tests.yml
```

## Risk model
The score is intentionally explainable rather than opaque. It combines:

- normalized severity;
- business/asset criticality;
- known-exploited context;
- internet exposure;
- remediation age/SLA pressure.

The output is a 0-100 score with a priority band (`P1`-`P4`) and human-readable reasons.

## Safe lab methodology
All included records are synthetic. Hostnames, owners, CVE-like identifiers, and evidence values are fictional. The project does not scan external systems, exploit vulnerabilities, or require privileged credentials.

## Usage

```bash
python -m src.cli data/synthetic_findings.json
python -m unittest discover -s tests -v
```

## Example output

```text
P1 | 92 | WEB-001 | synthetic-CVE-0001 | Internet-facing + KEV-like context + Critical asset
P2 | 73 | APP-014 | synthetic-CVE-0002 | High severity + SLA overdue
```

## Security engineering concepts demonstrated

- vulnerability normalization and data quality
- risk-based prioritization
- SLA and remediation workflow automation
- defensive security data engineering
- validation evidence and closure governance
- unit-tested Python automation
- CI quality gates

## Limitations
This is a portfolio lab, not a commercial vulnerability management platform. The scoring weights are examples and should be calibrated to an organization's risk appetite, threat model, asset taxonomy, and policy.

## Roadmap

- add CSV adapter and schema validation
- export JSON/CSV remediation queues
- add ATT&CK-aware detection-finding adapter
- add trend calculations and aging metrics
- add typed configuration for scoring weights

## Ethics
Use this project only with data and systems you are authorized to handle. No production targeting, credential collection, or exploit automation is included.
