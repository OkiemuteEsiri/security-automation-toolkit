from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Finding:
    finding_id: str
    asset_id: str
    title: str
    severity: str
    asset_criticality: int
    internet_exposed: bool = False
    known_exploited: bool = False
    days_open: int = 0
    sla_days: int = 30
    owner: str = "unassigned"
    evidence: List[str] = field(default_factory=list)

    @property
    def overdue(self) -> bool:
        return self.days_open > self.sla_days
