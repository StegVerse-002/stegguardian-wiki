from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "pages.yml"

REQUIRED_TEXT = [
    "name: Publish StegGuardian Wiki",
    "python scripts/check_llm_free_tier_trust_chain_page.py",
    "python scripts/check_media_pipeline_guardian_boundary.py",
    "python scripts/check_page_index.py",
    "python scripts/check_page_relationship_graph.py",
    "python scripts/check_cross_wiki_metadata_graph.py",
    "python scripts/check_cross_wiki_health_status.py",
    "python scripts/check_ecosystem_documentation_endpoints.py",
    "python scripts/check_live_public_record_url_verification.py",
    "python scripts/check_live_public_record_fetch_tooling.py",
    "python scripts/check_deployment_receipt.py",
    "python scripts/check_session_coordination_status.py",
    "python scripts/check_pages_deployment_trigger_status.py",
    "touch _site/.nojekyll",
    "pages/llm-free-tier-trust-chain.md",
    "pages/media-pipeline-guardian-boundary.md",
    "LLM Free Tier Trust Chain",
    "Media Pipeline Guardian Boundary",
    "data/page-index.json",
    "data/cross-wiki-metadata-graph.json",
    "data/cross-wiki-health-status.json",
    "data/ecosystem-documentation-endpoints.json",
    "data/live-public-record-url-verification.json",
    "data/deployment-receipt.json",
    "data/session-coordination-status.json",
    "data/pages-deployment-trigger-status.json",
    "docs/PAGES_DEPLOYMENT_TRIGGER_DIAGNOSIS.md",
    "docs/LIVE_PUBLIC_RECORD_URL_FETCH_RUNBOOK.md",
    "Cross-Wiki Metadata Graph",
    "Cross-Wiki Health Status",
    "Ecosystem Documentation Endpoints",
    "Live Public Record URL Verification",
    "Live Public Record URL Fetch Runbook",
    "Deployment Receipt",
    "Session Coordination Status",
    "Pages Deployment Trigger Status",
    "uses: actions/upload-pages-artifact@v3",
    "uses: actions/deploy-pages@v4",
    "verify-live-public-records:",
    "needs: deploy",
    "python scripts/fetch_live_public_record_urls.py",
    "reports/live-public-record-url-fetch-report.json",
    "uses: actions/upload-artifact@v4",
    "stegguardian-live-public-record-url-fetch-report",
    "Enforce live record verification result",
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
