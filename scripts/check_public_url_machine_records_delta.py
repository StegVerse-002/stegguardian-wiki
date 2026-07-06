from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DELTA = ROOT / "docs" / "PUBLIC_URL_MACHINE_RECORDS_DELTA.md"
REQUIRED_LOCAL_RECORDS = [
    ROOT / "data" / "page-index.json",
    ROOT / "data" / "page-metadata.schema.json",
    ROOT / "data" / "page-relationship-graph.json",
    ROOT / "data" / "public-records-manifest.json",
    ROOT / "docs" / "STEGGUARDIAN_VERIFICATION_STATUS.md",
]

REQUIRED_TEXT = [
    "Public URL Machine Records Delta",
    "Machine-record publication is wired and user-observed successful",
    "/pages/llm-free-tier-trust-chain.md",
    "/data/page-index.json",
    "/data/page-metadata.schema.json",
    "/data/page-relationship-graph.json",
    "/data/public-records-manifest.json",
    "/docs/STEGGUARDIAN_VERIFICATION_STATUS.md",
    "user_observed_workflow_success: true",
    "user_observed_machine_record_publication_success: true",
    "connector_confirmed_workflow_metadata: false",
    "independent_public_url_confirmation: pending",
    "does not claim connector-confirmed public deployment",
]


def main() -> int:
    errors = []
    if not DELTA.exists():
        errors.append("missing_public_url_machine_records_delta")
        text = ""
    else:
        text = DELTA.read_text(encoding="utf-8")

    for record in REQUIRED_LOCAL_RECORDS:
        if not record.exists():
            errors.append("missing_local_record:" + str(record.relative_to(ROOT)))

    for item in REQUIRED_TEXT:
        if item not in text:
            errors.append("delta_missing:" + item)

    if errors:
        print("PUBLIC URL MACHINE RECORDS DELTA: FAIL - " + ", ".join(errors))
        return 1
    print("PUBLIC URL MACHINE RECORDS DELTA: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
