from dataclasses import dataclass
from .models import Finding

@dataclass(frozen=True)
class ValidationResult:
    ready_to_close: bool
    missing_evidence: list[str]

REQUIRED_EVIDENCE = {"patch_applied", "rescan_clean", "owner_confirmed"}


def validate_closure(finding: Finding) -> ValidationResult:
    present = {item.strip().lower() for item in finding.evidence}
    missing = sorted(REQUIRED_EVIDENCE - present)
    return ValidationResult(ready_to_close=not missing, missing_evidence=missing)
