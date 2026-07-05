from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "pages.yml"

REQUIRED_TEXT = [
    "name: Publish StegGuardian Wiki",
    "python scripts/check_llm_free_tier_trust_chain_page.py",
    "python scripts/check_page_index.py",
    "pages/llm-free-tier-trust-chain.md",
    "LLM Free Tier Trust Chain",
    "data/page-index.json",
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
