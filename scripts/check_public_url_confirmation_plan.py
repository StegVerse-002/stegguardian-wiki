from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DELTA = ROOT / "docs" / "PUBLIC_URL_MACHINE_RECORDS_DELTA.md"
STATUS = ROOT / "PUBLIC_URL_VERIFICATION_STATUS.md"
MANIFEST = ROOT / "data" / "public-records-manifest.json"

REQUIRED_PUBLIC_PATHS = [
    "/",
    "/pages/llm-free-tier-trust-chain.md",
    "/data/page-index.json",
    "/data/page-metadata.schema.json",
    "/data/page-relationship-graph.json",
    "/data/public-records-manifest.json",
    "/docs/STEGGUARDIAN_VERIFICATION_STATUS.md",
]


def main() -> int:
    errors = []
    if not DELTA.exists():
        errors.append("missing_public_url_machine_records_delta")
        delta_text = ""
    else:
        delta_text = DELTA.read_text(encoding="utf-8")

    if not STATUS.exists():
        errors.append("missing_public_url_verification_status")
    if not MANIFEST.exists():
        errors.append("missing_public_records_manifest")

    for path in REQUIRED_PUBLIC_PATHS:
        if path not in delta_text:
            errors.append("missing_required_public_path:" + path)

    required_phrases = [
        "user_observed_machine_record_publication_success: true",
        "connector_confirmed_workflow_metadata: false",
        "independent_public_url_confirmation: pending",
        "does not claim connector-confirmed public deployment",
    ]
    for phrase in required_phrases:
        if phrase not in delta_text:
            errors.append("missing_public_url_delta_phrase:" + phrase)

    if errors:
        print("PUBLIC URL CONFIRMATION PLAN: FAIL - " + ", ".join(errors))
        return 1
    print("PUBLIC URL CONFIRMATION PLAN: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
