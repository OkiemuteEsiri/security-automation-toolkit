# Remediation and Validation Playbook

## Purpose
Define the minimum evidence needed to move a security finding from open to verified closed while preserving auditability.

## Workflow

1. **Triage** — confirm asset ownership, business criticality, exposure, and duplicate status.
2. **Prioritize** — review the calculated priority and the factors contributing to it.
3. **Assign** — route the finding to an accountable technical owner.
4. **Remediate** — patch, reconfigure, upgrade, remove, or apply an approved compensating control.
5. **Validate** — obtain independent technical evidence that the vulnerable state no longer exists.
6. **Close** — require owner confirmation and retain evidence references.

## Minimum closure evidence

- `patch_applied`: records the corrective action;
- `rescan_clean`: represents independent technical validation;
- `owner_confirmed`: records accountability for the resulting state.

## Exceptions
Risk acceptance should not be represented as remediation. A real implementation should use a separate exception object containing approver, rationale, compensating controls, review date, expiration, and residual risk.

## Revalidation triggers

- asset is rebuilt or re-imaged;
- application version changes;
- compensating control is removed;
- vulnerability intelligence materially changes;
- the same weakness reappears in a subsequent assessment.

## Quality checks

- evidence belongs to the correct asset and finding;
- validation occurred after the remediation action;
- clean results are not caused by loss of scanner visibility;
- owner/team mappings remain current;
- exception records are not silently treated as fixes.
