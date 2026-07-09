from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "pages.yml"

REQUIRED_TEXT = [
    "name: Publish StegGuardian Wiki",
    "python scripts/check_llm_free_tier_trust_chain_page.py",
    "python scripts/check_page_index.py",
    "python scripts/check_page_relationship_graph.py",
    "python scripts/check_cross_wiki_metadata_graph.py",
    "python scripts/check_cross_wiki_health_status.py",
    "python scripts/check_live_public_record_url_verification.py",
    "python scripts/check_deployment_receipt.py",
    "python scripts/check_session_coordination_status.py",
    "python scripts/check_pages_deployment_trigger_status.py",
    "touch _site/.nojekyll",
    "pages/llm-free-tier-trust-chain.md",
    "LLM Free Tier Trust Chain",
    "data/page-index.json",
    "data/cross-wiki-metadata-graph.json",
    "data/cross-wiki-health-status.json",
    "data/live-public-record-url-verification.json",
    "data/deployment-receipt.json",
    "data/session-coordination-status.json",
    "data/pages-deployment-trigger-status.json",
    "docs/PAGES_DEPLOYMENT_TRIGGER_DIAGNOSIS.md",
    "Cross-Wiki Metadata Graph",
    "Cross-Wiki Health Status",
    "Live Public Record URL Verification",
    "Deployment Receipt",
    "Session Coordination Status",
    "Pages Deployment Trigger Status",
    "uses: actions/upload-pages-artifact@v3",
    "uses: actions/deploy-pages@v4",
]


def main() -> int:
    errors = []
    if not WORKFLOW.exists():
        errors.append("missing_pages_workflow")
        text = ""
    else:
        text = WORKFLOW.read_text(encoding="utf-8")

    for item in REQUIRED_TEXT:
        if item not in text:
            errors.append("workflow_missing:" + item)

    if errors:
        print("STEGGUARDIAN PAGES WORKFLOW VALIDATION: FAIL - " + ", ".join(errors))
        return 1
    print("STEGGUARDIAN PAGES WORKFLOW VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
