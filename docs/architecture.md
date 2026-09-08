# Architecture

## Objective
Provide a transparent defensive automation pipeline that converts heterogeneous security findings into prioritized, owner-aware remediation work without hiding risk logic behind a black box.

## Components

### Normalization layer
Maps source-specific severity labels and optional fields into the canonical `Finding` model. Input validation intentionally constrains criticality and SLA values to safe ranges.

### Risk engine
Calculates a deterministic 0-100 score. The current model uses:

- severity: up to 40 points;
- asset criticality: up to 25 points;
- internet exposure: 15 points;
- known-exploited context: 20 points;
- overdue SLA: 10 points.

Scores are capped at 100 and translated into P1-P4 priority bands.

### Remediation validator
Separates technical remediation from governance closure. A finding is not marked ready to close unless evidence confirms patch/application action, clean validation, and accountable owner confirmation.

### CLI/reporting layer
Produces a sorted analyst queue and basic priority distribution without requiring external services.

## Trust boundaries
No network calls are required. The included lab consumes local synthetic JSON only. Real integrations should isolate API credentials in a secrets manager and add schema validation, retry handling, audit logging, and least-privilege service identities.

## Failure modes

- incorrect source mappings can distort severity;
- stale asset criticality can create false prioritization;
- known-exploited flags require trusted enrichment sources;
- closure evidence can be present but semantically invalid;
- risk weights require periodic governance review.

## Extension pattern
Adapters should transform source records into the canonical model rather than embedding vendor-specific fields into scoring logic. This keeps policy, ingestion, and reporting independently testable.
