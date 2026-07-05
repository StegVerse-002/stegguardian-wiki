from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "pages" / "llm-free-tier-trust-chain.md"

REQUIRED_TEXT = [
    "LLM Free Tier Trust Chain",
    "StegVerse-org/LLM-adapter",
    "free_tier_trust metadata",
    "StegVerse-Labs/Site",
    "ecosystem-chat.html bounded free-tier trust display",
    "StegVerse-org/StegVerse-SDK",
    "validate_free_tier_metadata",
    "StegVerse-Labs/admissibility-wiki",
    "docs/governance/llm-free-tier-trust-chain.md",
    "GCAT-BCAT-Engine/Publisher",
    "docs/LLM_FREE_TIER_TRUST_CHAIN_STATUS.md",
    "quota availability is not admissibility",
    "receipt export is not permanent retention",
    "replay is not commit-time standing",
    "reconstruction is not commit-time standing",
    "upgrade does not change admissibility requirements",
]


def main() -> int:
    errors = []
    if not PAGE.exists():
        errors.append("missing_page")
        text = ""
    else:
        text = PAGE.read_text(encoding="utf-8")

    for item in REQUIRED_TEXT:
        if item not in text:
            errors.append("page_missing:" + item)

    if errors:
        print("LLM FREE TIER TRUST CHAIN PAGE: FAIL - " + ", ".join(errors))
        return 1
    print("LLM FREE TIER TRUST CHAIN PAGE: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
