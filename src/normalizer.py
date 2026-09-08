from .models import Finding

SEVERITY_ALIASES = {
    "crit": "critical", "critical": "critical",
    "high": "high", "medium": "medium", "moderate": "medium",
    "low": "low", "info": "informational", "informational": "informational",
}


def normalize_record(record: dict) -> Finding:
    severity_raw = str(record.get("severity", "informational")).strip().lower()
    severity = SEVERITY_ALIASES.get(severity_raw, "informational")
    criticality = max(1, min(5, int(record.get("asset_criticality", 1))))
    return Finding(
        finding_id=str(record["finding_id"]),
        asset_id=str(record["asset_id"]),
        title=str(record.get("title", "Untitled finding")),
        severity=severity,
        asset_criticality=criticality,
        internet_exposed=bool(record.get("internet_exposed", False)),
        known_exploited=bool(record.get("known_exploited", False)),
        days_open=max(0, int(record.get("days_open", 0))),
        sla_days=max(1, int(record.get("sla_days", 30))),
        owner=str(record.get("owner", "unassigned")),
        evidence=list(record.get("evidence", [])),
    )
