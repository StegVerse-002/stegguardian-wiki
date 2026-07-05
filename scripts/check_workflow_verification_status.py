from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "WORKFLOW_VERIFICATION_STATUS.md"

REQUIRED_TEXT = [
    "Workflow Verification Status",
    "workflow_runs_for_checked_commits: none found at check time",
    "combined_statuses_for_latest_commit: none found at check time",
    "status: connector_unconfirmed",
    "StegGuardian Wiki Readiness #31: success",
    "Publish StegGuardian Wiki #46: success",
    "Publish StegGuardian Wiki #45: success for commit b8d9d97",
    "status: user_observed_success_connector_unconfirmed",
    "python scripts/check_llm_free_tier_trust_chain_page.py",
    "python scripts/check_page_index.py",
    "python scripts/check_pages_workflow_validation.py",
    "python scripts/check_guardian_local_state.py",
    "page: pages/llm-free-tier-trust-chain.md installed",
    "index: data/page-index.json includes LLM Free Tier Trust Chain entry",
    "checker: scripts/check_pages_workflow_validation.py installed",
    "checker: scripts/check_user_observed_workflow_evidence.py installed",
    "does not claim connector-confirmed workflow metadata",
    "public deployment verification",
]

REQUIRED_COMMITS = [
    "3e933dd638444d6972369fb5ad9431c481711b38",
    "8c42831aad9bc95fd5f1ec6abfe3250bba9a45a5",
    "0cb1f41d784bf62e5238e1909d6b8b5449a2fa4e",
    "340f4c29fe9c86c37c48a8832727ead88b7ebadb",
    "28acb477dbc06dbd8cca4dd2951727ba2094fba3",
    "981784b7faa964d68fc4c0411356379f422d9ee7",
    "862278e64a3a615f7e242eeb63a61dc8b996d497",
    "b8d9d9761ed40ec0651739ab8c53dd30e6418c57",
]


def main() -> int:
    errors = []
    if not STATUS.exists():
        errors.append("missing_workflow_verification_status")
        text = ""
    else:
        text = STATUS.read_text(encoding="utf-8")

    for item in REQUIRED_TEXT:
        if item not in text:
            errors.append("status_missing:" + item)

    for commit in REQUIRED_COMMITS:
        if commit not in text:
            errors.append("checked_commit_missing:" + commit)

    if errors:
        print("WORKFLOW VERIFICATION STATUS: FAIL - " + ", ".join(errors))
        return 1
    print("WORKFLOW VERIFICATION STATUS: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
