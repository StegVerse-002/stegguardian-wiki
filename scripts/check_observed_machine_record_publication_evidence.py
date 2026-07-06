from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "OBSERVED_MACHINE_RECORD_PUBLICATION_EVIDENCE.md"

REQUIRED_TEXT = [
    "Observed Machine Record Publication Evidence",
    "deploy: success",
    "readiness: success",
    "page_relationship_graph_check: pass",
    "public_records_manifest_check: pass",
    "repo_standards_guardian_summary: pass",
    "pages_deployment: reported_success",
    "data/page-metadata.schema.json",
    "data/page-relationship-graph.json",
    "data/public-records-manifest.json",
    "docs/STEGGUARDIAN_VERIFICATION_STATUS.md",
    "status: user_observed_machine_record_publication_success_connector_unconfirmed",
    "does not claim connector-confirmed workflow metadata",
]


def main() -> int:
    errors = []
    if not EVIDENCE.exists():
        errors.append("missing_observed_machine_record_publication_evidence")
        text = ""
    else:
        text = EVIDENCE.read_text(encoding="utf-8")

    for item in REQUIRED_TEXT:
        if item not in text:
            errors.append("evidence_missing:" + item)

    if errors:
        print("OBSERVED MACHINE RECORD PUBLICATION EVIDENCE: FAIL - " + ", ".join(errors))
        return 1
    print("OBSERVED MACHINE RECORD PUBLICATION EVIDENCE: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
