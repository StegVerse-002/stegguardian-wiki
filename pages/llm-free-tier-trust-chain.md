# LLM Free Tier Trust Chain

## Status

This page records downstream StegGuardian awareness of the bounded StegVerse governed LLM free-tier trust chain.

## Source chain

```text
StegVerse-org/LLM-adapter
  -> free_tier_trust metadata
  -> adapter.capabilities.json free-tier fields

StegVerse-Labs/Site
  -> ecosystem-chat.html bounded free-tier trust display
  -> scripts/check_site_llm_free_tier_trust.py

StegVerse-org/StegVerse-SDK
  -> validate_free_tier_metadata
  -> scripts/verify_free_tier_metadata_ingestion.py

StegVerse-Labs/admissibility-wiki
  -> docs/governance/llm-free-tier-trust-chain.md
  -> scripts/check_llm_free_tier_trust_chain.py

GCAT-BCAT-Engine/Publisher
  -> docs/LLM_FREE_TIER_TRUST_CHAIN_STATUS.md
  -> tools/check_llm_free_tier_trust_chain_status.py
```

## Guardian boundary

StegGuardian may reference the trust chain as a downstream propagation note. This page does not create guardian enforcement authority, provider authority, execution authority, permanent retention, replay standing, reconstruction standing, or upgrade-based admissibility.

## Required non-claims

```text
quota availability is not admissibility
receipt export is not permanent retention
replay is not commit-time standing
reconstruction is not commit-time standing
upgrade does not change admissibility requirements
```

## Next integration candidate

Create or update machine-readable page index metadata so this page can be checked without relying on manual README inspection.
