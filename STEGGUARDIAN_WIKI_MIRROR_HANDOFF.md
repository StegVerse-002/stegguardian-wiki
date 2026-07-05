# StegGuardian Wiki Mirror Handoff

## Status

This file is the current handoff and task source of truth for `StegVerse-002/stegguardian-wiki`.

## Current Priority

Standing-Proof-Engine v0.5.0 guardian-boundary propagation has been recorded.

LLM free-tier trust-chain downstream propagation has also been recorded as awareness-only documentation.

Machine-readable page index metadata has been updated for the LLM free-tier trust-chain page.

Pages workflow validation now checks the LLM free-tier trust-chain page and page index before deployment.

Workflow configuration can be checked locally with `python scripts/check_pages_workflow_validation.py`.

Workflow verification status can be checked locally with `python scripts/check_workflow_verification_status.py`.

All local Guardian propagation checks can be run with `python scripts/check_guardian_local_state.py`.

Workflow execution evidence is still pending; `WORKFLOW_VERIFICATION_STATUS.md` and `docs/GUARDIAN_WORKFLOW_VERIFICATION_RUNBOOK.md` record the checked commits and re-check process.

## Public URL

- `https://stegverse-002.github.io/stegguardian-wiki/`

## Source Artifacts

Admissibility source: `StegVerse-Labs/admissibility-wiki`

- `ADMISSIBILITY_MIRROR_HANDOFF.md`
- `pages/spe-v0-5-0-standing-boundary.md`
- `docs/governance/llm-free-tier-trust-chain.md`

Publisher source: `GCAT-BCAT-Engine/Publisher`

- `PUBLISHER_MIRROR_HANDOFF.md`
- `data/spe-v0-5-0-status.json`
- `docs/LLM_FREE_TIER_TRUST_CHAIN_STATUS.md`

Site source: `StegVerse-Labs/Site`

- `SITE_MIRROR_HANDOFF.md`
- `data/spe-v0-5-0-status.json`
- `ecosystem-chat.html`
- `docs/LLM_FREE_TIER_TRUST_STATUS.md`

LLM adapter source: `StegVerse-org/LLM-adapter`

- `adapter.capabilities.json`
- `docs/FREE_TIER_TRUST_POLICY.md`
- `examples/free_tier_trust_policy.json`

SDK source: `StegVerse-org/StegVerse-SDK`

- `docs/FREE_TIER_METADATA_INGESTION.md`
- `sdk.capabilities.json`

Origin source: `StegVerse-Labs/Standing-Proof-Engine`

- `SPE_MIRROR_HANDOFF.md`
- `docs/release_snapshot_v0_5_0.md`
- `samples/destination_receipt_chain_001.json`

Master-records source: `master-records/core-lite`

- `records/spe_destination_receipt_chain_001.json`

## Install Complete

Destination: `StegVerse-002/stegguardian-wiki`

- `pages/spe-v0-5-0-guardian-boundary.md`
- `pages/llm-free-tier-trust-chain.md`
- `LLM_FREE_TIER_TRUST_CHAIN_STATUS.md`
- `scripts/check_llm_free_tier_trust_chain_page.py`
- `data/page-index.json` updated with LLM free-tier trust-chain entry
- `scripts/check_page_index.py`
- `scripts/check_pages_workflow_validation.py`
- `scripts/check_workflow_verification_status.py`
- `scripts/check_guardian_local_state.py`
- `.github/workflows/pages.yml` validates both checkers and links the page in the static index
- `WORKFLOW_VERIFICATION_STATUS.md`
- `docs/GUARDIAN_WORKFLOW_VERIFICATION_RUNBOOK.md`

## Verification

```text
python scripts/check_guardian_local_state.py
```

Expanded checks:

```text
python scripts/check_llm_free_tier_trust_chain_page.py
python scripts/check_page_index.py
python scripts/check_pages_workflow_validation.py
python scripts/check_workflow_verification_status.py
```

## Publishing Automation

- `github/workflows/pages.yml` displayed without the leading dot; actual repository path includes the leading dot.

## Linked Wikis

- `https://stegverse-labs.github.io/admissibility-wiki/`
- `https://stegverse-labs.github.io/Site/`

## Build Rule

Before continuing any StegGuardian wiki task, check this file first and treat it as the current handoff and task source of truth.

## Boundary

SPE v0.5.0 records receipt-chain reconstructability and master-records emission. It does not itself authorize enforcement; commit-time standing remains required.

The LLM free-tier trust-chain page is downstream propagation awareness only. It does not create guardian enforcement authority, provider authority, execution authority, permanent retention, replay standing, reconstruction standing, or upgrade-based admissibility.

## Remaining Open Check

Workflow/tag verification remains pending because no workflow runs or combined statuses were found for the checked commits at check time. README linking remains optional because the propagation page, status file, checker, index entry, workflow validation, workflow configuration checker, workflow verification status checker, aggregate local checker, runbook, and handoff now record the installed state.
