from dataclasses import dataclass
from .models import Finding

SEVERITY_POINTS = {"critical": 40, "high": 30, "medium": 20, "low": 10, "informational": 0}

@dataclass(frozen=True)
class RiskResult:
    score: int
    priority: str
    reasons: list[str]


def score_finding(finding: Finding) -> RiskResult:
    score = SEVERITY_POINTS[finding.severity]
    reasons = [f"{finding.severity.title()} severity"]
    score += finding.asset_criticality * 5
    if finding.asset_criticality >= 4:
        reasons.append("Business-critical asset")
    if finding.internet_exposed:
        score += 15
        reasons.append("Internet-facing")
    if finding.known_exploited:
        score += 20
        reasons.append("Known-exploited context")
    if finding.overdue:
        score += 10
        reasons.append("Remediation SLA overdue")
    score = min(100, score)
    priority = "P1" if score >= 85 else "P2" if score >= 65 else "P3" if score >= 40 else "P4"
    return RiskResult(score, priority, reasons)
