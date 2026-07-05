from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "PUBLIC_URL_VERIFICATION_STATUS.md"

REQUIRED_TEXT = [
    "Public URL Verification Status",
    "https://stegverse-002.github.io/stegguardian-wiki/",
    "user_observed_workflow_success: true",
    "connector_confirmed_workflow_metadata: false",
    "public_url_connector_verified: false",
    ".github/workflows/pages.yml",
    "pages/llm-free-tier-trust-chain.md",
    "data/page-index.json",
    "does not claim connector-confirmed public deployment",
]


def main() -> int:
    errors = []
    if not STATUS.exists():
        errors.append("missing_public_url_verification_status")
        text = ""
    else:
        text = STATUS.read_text(encoding="utf-8")

    for item in REQUIRED_TEXT:
        if item not in text:
            errors.append("status_missing:" + item)

    if errors:
        print("PUBLIC URL VERIFICATION STATUS: FAIL - " + ", ".join(errors))
        return 1
    print("PUBLIC URL VERIFICATION STATUS: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
