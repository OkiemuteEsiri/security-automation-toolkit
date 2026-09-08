import json
import sys
from collections import Counter
from pathlib import Path
from .normalizer import normalize_record
from .risk_engine import score_finding


def main(path: str) -> int:
    records = json.loads(Path(path).read_text(encoding="utf-8"))
    findings = [normalize_record(record) for record in records]
    ranked = sorted(((f, score_finding(f)) for f in findings), key=lambda x: x[1].score, reverse=True)
    counts = Counter(result.priority for _, result in ranked)
    print(f"Findings: {len(ranked)} | " + " | ".join(f"{k}: {counts[k]}" for k in ("P1", "P2", "P3", "P4")))
    for finding, result in ranked:
        print(f"{result.priority} | {result.score:3d} | {finding.asset_id} | {finding.finding_id} | {' + '.join(result.reasons)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
