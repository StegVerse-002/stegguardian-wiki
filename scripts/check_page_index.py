import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "data" / "page-index.json"
PAGE = ROOT / "pages" / "llm-free-tier-trust-chain.md"

REQUIRED_CHAIN = {
    "StegVerse-org/LLM-adapter",
    "StegVerse-Labs/Site",
    "StegVerse-org/StegVerse-SDK",
    "StegVerse-Labs/admissibility-wiki",
    "GCAT-BCAT-Engine/Publisher",
}

REQUIRED_NON_CLAIMS = {
    "guardian_enforcement_authority": False,
    "provider_authority": False,
    "execution_authority": False,
    "permanent_retention": False,
    "replay_standing": False,
    "reconstruction_standing": False,
    "upgrade_based_admissibility": False,
}


def main() -> int:
    errors = []
    if not INDEX.exists():
        errors.append("missing_index")
        payload = {}
    else:
        payload = json.loads(INDEX.read_text(encoding="utf-8"))

    if not PAGE.exists():
        errors.append("missing_llm_free_tier_page")

    pages = payload.get("pages", [])
    entry = next((page for page in pages if page.get("path") == "pages/llm-free-tier-trust-chain.md"), None)
    if entry is None:
        errors.append("missing_llm_free_tier_index_entry")
    else:
        if entry.get("title") != "LLM Free Tier Trust Chain":
            errors.append("index_entry_title_mismatch")
        if entry.get("status") != "installed":
            errors.append("index_entry_status_mismatch")
        if entry.get("activation_state") != "downstream_propagation_awareness_only":
            errors.append("index_entry_activation_state_mismatch")
        if set(entry.get("source_chain", [])) != REQUIRED_CHAIN:
            errors.append("index_entry_source_chain_mismatch")
        non_claims = entry.get("non_claims", {})
        for key, value in REQUIRED_NON_CLAIMS.items():
            if non_claims.get(key) is not value:
                errors.append("index_entry_non_claim_mismatch:" + key)

    if payload.get("production_ready") is not False:
        errors.append("production_ready_must_remain_false")

    if errors:
        print("STEGGUARDIAN PAGE INDEX: FAIL - " + ", ".join(errors))
        return 1
    print("STEGGUARDIAN PAGE INDEX: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
