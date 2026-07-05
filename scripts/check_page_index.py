import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "data" / "page-index.json"
LLM_PAGE = ROOT / "pages" / "llm-free-tier-trust-chain.md"
VERIFY_PAGE = ROOT / "docs" / "STEGGUARDIAN_VERIFICATION_STATUS.md"

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

REQUIRED_VERIFY_NON_CLAIMS = {
    "connector_confirmed_workflow_metadata": False,
    "public_deployment_verification": False,
    "tag_verification": False,
    "guardian_enforcement_authority": False,
    "execution_authority": False,
}


def main() -> int:
    errors = []
    if not INDEX.exists():
        errors.append("missing_index")
        payload = {}
    else:
        payload = json.loads(INDEX.read_text(encoding="utf-8"))

    if not LLM_PAGE.exists():
        errors.append("missing_llm_free_tier_page")
    if not VERIFY_PAGE.exists():
        errors.append("missing_verification_status_page")

    pages = payload.get("pages", [])
    llm_entry = next((page for page in pages if page.get("path") == "pages/llm-free-tier-trust-chain.md"), None)
    if llm_entry is None:
        errors.append("missing_llm_free_tier_index_entry")
    else:
        if llm_entry.get("title") != "LLM Free Tier Trust Chain":
            errors.append("llm_index_entry_title_mismatch")
        if llm_entry.get("status") != "installed":
            errors.append("llm_index_entry_status_mismatch")
        if llm_entry.get("activation_state") != "downstream_propagation_awareness_only":
            errors.append("llm_index_entry_activation_state_mismatch")
        if set(llm_entry.get("source_chain", [])) != REQUIRED_CHAIN:
            errors.append("llm_index_entry_source_chain_mismatch")
        non_claims = llm_entry.get("non_claims", {})
        for key, value in REQUIRED_NON_CLAIMS.items():
            if non_claims.get(key) is not value:
                errors.append("llm_index_entry_non_claim_mismatch:" + key)

    verify_entry = next((page for page in pages if page.get("path") == "docs/STEGGUARDIAN_VERIFICATION_STATUS.md"), None)
    if verify_entry is None:
        errors.append("missing_verification_status_index_entry")
    else:
        if verify_entry.get("title") != "StegGuardian Verification Status":
            errors.append("verification_index_entry_title_mismatch")
        if verify_entry.get("status") != "installed":
            errors.append("verification_index_entry_status_mismatch")
        if verify_entry.get("activation_state") != "local_validation_pass_user_observed_workflow_success_connector_unconfirmed":
            errors.append("verification_index_entry_activation_state_mismatch")
        checks = set(verify_entry.get("checks", []))
        if "python scripts/check_guardian_local_state.py" not in checks:
            errors.append("verification_index_entry_missing_aggregate_check")
        if "python scripts/check_stegguardian_verification_status.py" not in checks:
            errors.append("verification_index_entry_missing_page_check")
        non_claims = verify_entry.get("non_claims", {})
        for key, value in REQUIRED_VERIFY_NON_CLAIMS.items():
            if non_claims.get(key) is not value:
                errors.append("verification_index_entry_non_claim_mismatch:" + key)

    if payload.get("production_ready") is not False:
        errors.append("production_ready_must_remain_false")

    if errors:
        print("STEGGUARDIAN PAGE INDEX: FAIL - " + ", ".join(errors))
        return 1
    print("STEGGUARDIAN PAGE INDEX: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
