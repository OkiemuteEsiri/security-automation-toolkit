import unittest
from src.normalizer import normalize_record
from src.risk_engine import score_finding
from src.remediation import validate_closure


class SecurityAutomationTests(unittest.TestCase):
    def test_normalizer_maps_alias_and_bounds_criticality(self):
        finding = normalize_record({"finding_id":"F1","asset_id":"A1","severity":"crit","asset_criticality":9})
        self.assertEqual(finding.severity, "critical")
        self.assertEqual(finding.asset_criticality, 5)

    def test_known_exploited_internet_facing_is_high_priority(self):
        finding = normalize_record({"finding_id":"F2","asset_id":"A2","severity":"critical","asset_criticality":5,"internet_exposed":True,"known_exploited":True})
        result = score_finding(finding)
        self.assertEqual(result.priority, "P1")
        self.assertGreaterEqual(result.score, 85)

    def test_overdue_adds_context(self):
        finding = normalize_record({"finding_id":"F3","asset_id":"A3","severity":"high","asset_criticality":3,"days_open":45,"sla_days":30})
        result = score_finding(finding)
        self.assertIn("Remediation SLA overdue", result.reasons)

    def test_closure_requires_all_evidence(self):
        finding = normalize_record({"finding_id":"F4","asset_id":"A4","severity":"medium","asset_criticality":2,"evidence":["patch_applied"]})
        validation = validate_closure(finding)
        self.assertFalse(validation.ready_to_close)
        self.assertIn("rescan_clean", validation.missing_evidence)

    def test_complete_evidence_closes(self):
        finding = normalize_record({"finding_id":"F5","asset_id":"A5","severity":"low","asset_criticality":1,"evidence":["patch_applied","rescan_clean","owner_confirmed"]})
        self.assertTrue(validate_closure(finding).ready_to_close)


if __name__ == "__main__":
    unittest.main()
