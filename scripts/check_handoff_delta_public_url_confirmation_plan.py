from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DELTA = ROOT / "docs" / "HANDOFF_DELTA_PUBLIC_URL_CONFIRMATION_PLAN.md"

REQUIRED_TEXT = [
    "Handoff Delta: Public URL Confirmation Plan",
    "scripts/check_observed_machine_record_publication_evidence.py",
    "scripts/check_handoff_delta_observed_publication_success.py",
    "scripts/check_public_url_machine_records_delta.py",
    "scripts/check_public_url_confirmation_plan.py",
    "python scripts/check_guardian_local_state.py",
    "/pages/llm-free-tier-trust-chain.md",
    "/data/page-index.json",
    "/data/page-metadata.schema.json",
    "/data/page-relationship-graph.json",
    "/data/public-records-manifest.json",
    "/docs/STEGGUARDIAN_VERIFICATION_STATUS.md",
    "connector_confirmed_run_ids: pending",
    "independent_public_url_confirmation: pending",
    "does not claim connector-confirmed workflow metadata",
]


def main() -> int:
    errors = []
    if not DELTA.exists():
        errors.append("missing_handoff_delta_public_url_confirmation_plan")
        text = ""
    else:
        text = DELTA.read_text(encoding="utf-8")

    for item in REQUIRED_TEXT:
        if item not in text:
            errors.append("delta_missing:" + item)

    if errors:
        print("HANDOFF DELTA PUBLIC URL CONFIRMATION PLAN: FAIL - " + ", ".join(errors))
        return 1
    print("HANDOFF DELTA PUBLIC URL CONFIRMATION PLAN: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
