# StegGuardian Wiki Mirror Handoff

## Status

This file is the current handoff and task source of truth for `StegVerse-002/stegguardian-wiki`.

## Current Priority

StegGuardian Wiki is live at `https://stegverse-002.github.io/stegguardian-wiki/` and the Pages repair issue is resolved by user-observed live-site confirmation.

Current integration goal: cross-wiki discovery and health verification.

Standing-Proof-Engine v0.5.0 guardian-boundary propagation has been recorded.

LLM free-tier trust-chain downstream propagation has also been recorded as awareness-only documentation.

Machine-readable page index metadata has been updated for the LLM free-tier trust-chain page and the StegGuardian verification status page.

Shared page metadata schema, the StegGuardian relationship graph, the cross-wiki metadata graph, the cross-wiki health status record, the live public record URL verification record, and the live public record URL fetch verifier are installed.

Machine-readable record exposure is tracked by `docs/MACHINE_RECORD_PUBLICATION_STATUS.md` and `data/public-records-manifest.json`.

Session coordination is recorded in `data/session-coordination-status.json`, checked by `python scripts/check_session_coordination_status.py`, and published by the Pages workflow.

Cross-wiki health is recorded in `data/cross-wiki-health-status.json`, checked by `python scripts/check_cross_wiki_health_status.py`, and published by the Pages workflow. Its state remains `pending_live_peer_checks` until peer URLs and peer machine-record manifests are externally verified.

Live public record URL verification is recorded in `data/live-public-record-url-verification.json`, checked by `python scripts/check_live_public_record_url_verification.py`, and published by the Pages workflow. It records user-observed homepage liveness while keeping individual machine-record URL fetch confirmation pending.

Live public record fetch tooling is installed in `scripts/fetch_live_public_record_urls.py`, documented in `docs/LIVE_PUBLIC_RECORD_URL_FETCH_RUNBOOK.md`, checked by `python scripts/check_live_public_record_fetch_tooling.py`, and published by the Pages workflow.

Pages workflow now publishes the page index, metadata schema, relationship graph, cross-wiki metadata graph, cross-wiki health status, live public record URL verification, live public record fetch runbook, deployment receipt, session coordination status, Pages deployment trigger status, public-records manifest, Pages deployment diagnosis document, and verification status document.

Workflow configuration can be checked locally with `python scripts/check_pages_workflow_validation.py`.

Workflow verification status can be checked locally with `python scripts/check_workflow_verification_status.py`.

Pages deployment trigger diagnosis is recorded in `data/pages-deployment-trigger-status.json` and `docs/PAGES_DEPLOYMENT_TRIGGER_DIAGNOSIS.md`, and checked by `python scripts/check_pages_deployment_trigger_status.py`.

Pages deployment receipt continuity is recorded in `data/deployment-receipt.json` and checked by `python scripts/check_deployment_receipt.py`.

The blocked aggregate workflow rewrite is recorded in `docs/GUARDIAN_AGGREGATE_WORKFLOW_DELTA.md` and checked by `python scripts/check_aggregate_workflow_delta.py`.

User-observed workflow success is recorded in `USER_OBSERVED_WORKFLOW_EVIDENCE.md` and checked by `python scripts/check_user_observed_workflow_evidence.py`.

Public URL verification state is recorded in `PUBLIC_URL_VERIFICATION_STATUS.md` and checked by `python scripts/check_public_url_verification_status.py`.

StegGuardian verification status is recorded in `docs/STEGGUARDIAN_VERIFICATION_STATUS.md`, indexed in `data/page-index.json`, published by the Pages workflow, and checked by `python scripts/check_stegguardian_verification_status.py`.

The page relationship graph is recorded in `data/page-relationship-graph.json`, published by the Pages workflow, and checked by `python scripts/check_page_relationship_graph.py`.

The cross-wiki metadata graph is recorded in `data/cross-wiki-metadata-graph.json`, published by the Pages workflow, listed in the public records manifest, and checked by `python scripts/check_cross_wiki_metadata_graph.py`.

The public records manifest is recorded in `data/public-records-manifest.json`, published by the Pages workflow, and checked by `python scripts/check_public_records_manifest.py`.

All local Guardian propagation and graph checks can be run with `python scripts/check_guardian_local_state.py`.

## Public URL

- `https://stegverse-002.github.io/stegguardian-wiki/`

## Session Coordination

No open issue, open pull request, or existing repository coordination record was found indicating another active session is working the same StegGuardian Pages repair issue.

Parallel sessions must not restart the Pages repair path. If another session is working on Pages repair, route it to public-record verification or cross-wiki health tasks.

Active current-session task ownership: cross-wiki discovery and health verification.

## Org Boundary Rationale

StegGuardian wiki is intentionally published from `StegVerse-002/stegguardian-wiki` because Guardian documentation belongs to the governed-entity org boundary. Linked StegVerse-Labs wikis remain part of the same ecosystem documentation mesh. The different GitHub Pages origin is deliberate and should not be interpreted as an orphaned or drifted repo.

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
- `docs/STEGGUARDIAN_VERIFICATION_STATUS.md`
- `docs/PAGES_DEPLOYMENT_TRIGGER_DIAGNOSIS.md`
- `docs/LIVE_PUBLIC_RECORD_URL_FETCH_RUNBOOK.md`
- `LLM_FREE_TIER_TRUST_CHAIN_STATUS.md`
- `PUBLIC_URL_VERIFICATION_STATUS.md`
- `docs/MACHINE_RECORD_PUBLICATION_STATUS.md`
- `data/page-metadata.schema.json`
- `data/page-relationship-graph.json`
- `data/cross-wiki-metadata-graph.json`
- `data/cross-wiki-health-status.json`
- `data/live-public-record-url-verification.json`
- `data/deployment-receipt.json`
- `data/session-coordination-status.json`
- `data/pages-deployment-trigger-status.json`
- `data/public-records-manifest.json`
- `scripts/check_page_relationship_graph.py`
- `scripts/check_cross_wiki_metadata_graph.py`
- `scripts/check_cross_wiki_health_status.py`
- `scripts/check_live_public_record_url_verification.py`
- `scripts/fetch_live_public_record_urls.py`
- `scripts/check_live_public_record_fetch_tooling.py`
- `scripts/check_deployment_receipt.py`
- `scripts/check_session_coordination_status.py`
- `scripts/check_pages_deployment_trigger_status.py`
- `scripts/check_public_records_manifest.py`
- `scripts/check_machine_record_publication_status.py`
- `scripts/check_llm_free_tier_trust_chain_page.py`
- `data/page-index.json` updated with LLM free-tier trust-chain and verification status entries
- `scripts/check_page_index.py`
- `scripts/check_pages_workflow_validation.py`
- `scripts/check_workflow_verification_status.py`
- `docs/GUARDIAN_AGGREGATE_WORKFLOW_DELTA.md`
- `scripts/check_aggregate_workflow_delta.py`
- `USER_OBSERVED_WORKFLOW_EVIDENCE.md`
- `scripts/check_user_observed_workflow_evidence.py`
- `scripts/check_public_url_verification_status.py`
- `scripts/check_stegguardian_verification_status.py`
- `scripts/check_guardian_local_state.py`
- `.github/workflows/pages.yml` validates and publishes machine-readable records, cross-wiki graph, cross-wiki health status, live public record URL verification, live public record fetch runbook, deployment receipt, session coordination status, Pages trigger diagnosis records, and verification status
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
python scripts/check_page_relationship_graph.py
python scripts/check_cross_wiki_metadata_graph.py
python scripts/check_cross_wiki_health_status.py
python scripts/check_live_public_record_url_verification.py
python scripts/check_live_public_record_fetch_tooling.py
python scripts/check_deployment_receipt.py
python scripts/check_session_coordination_status.py
python scripts/check_pages_deployment_trigger_status.py
python scripts/check_machine_record_publication_status.py
python scripts/check_public_records_manifest.py
python scripts/check_pages_workflow_validation.py
python scripts/check_workflow_verification_status.py
python scripts/check_aggregate_workflow_delta.py
python scripts/check_user_observed_workflow_evidence.py
python scripts/check_public_url_verification_status.py
python scripts/check_stegguardian_verification_status.py
```

Live URL fetch command:

```text
python scripts/fetch_live_public_record_urls.py --write-report data/live-public-record-url-fetch-report.json
```

## Publishing Automation

- `github/workflows/pages.yml` displayed without the leading dot; actual repository path includes the leading dot.
- The workflow publishes `data/page-index.json`, `data/page-metadata.schema.json`, `data/page-relationship-graph.json`, `data/cross-wiki-metadata-graph.json`, `data/cross-wiki-health-status.json`, `data/live-public-record-url-verification.json`, `data/deployment-receipt.json`, `data/session-coordination-status.json`, `data/pages-deployment-trigger-status.json`, `data/public-records-manifest.json`, `docs/LIVE_PUBLIC_RECORD_URL_FETCH_RUNBOOK.md`, `docs/PAGES_DEPLOYMENT_TRIGGER_DIAGNOSIS.md`, and `docs/STEGGUARDIAN_VERIFICATION_STATUS.md` into the static site output.
- The workflow writes `_site/.nojekyll` before upload to avoid Jekyll processing conflicts.

## Linked Wikis

- `https://stegverse-labs.github.io/admissibility-wiki/`
- `https://stegverse-labs.github.io/Site/`
- `https://stegverse-labs.github.io/stegtalk-wiki/`

## Build Rule

Before continuing any StegGuardian wiki task, check this file first and treat it as the current handoff and task source of truth.

## Boundary

SPE v0.5.0 records receipt-chain reconstructability and master-records emission. It does not itself authorize enforcement; commit-time standing remains required.

The LLM free-tier trust-chain page, verification status page, metadata schema, relationship graph, cross-wiki metadata graph, cross-wiki health status, live public record URL verification, live public record fetch tooling, deployment receipt, session coordination status, Pages deployment trigger status, Pages deployment diagnosis document, and public-records manifest are downstream propagation and evidence-awareness records only. They do not create guardian enforcement authority, provider authority, execution authority, connector-confirmed workflow metadata, all-machine-record URL verification, permanent retention, replay standing, reconstruction standing, or upgrade-based admissibility.

## Remaining Open Check

Next unassigned work: execute the live URL fetch command from a networked environment, commit `data/live-public-record-url-fetch-report.json` after success, standardize cross-wiki health records across StegTalk Wiki, Admissibility Wiki, and Site, and promote the reusable checker to repo-standards after local proof.
