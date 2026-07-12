# StegGuardian Wiki Mirror Handoff

## Status

This file is the current handoff and task source of truth for `StegVerse-002/stegguardian-wiki`.

## Current Priority

StegGuardian Wiki is live at `https://stegverse-002.github.io/stegguardian-wiki/` and the Pages repair issue is resolved by user-observed live-site confirmation.

Current integration goal: cross-wiki discovery, machine-readable relationship binding, and health verification.

Standing-Proof-Engine v0.5.0 guardian-boundary propagation has been recorded.

LLM free-tier trust-chain downstream propagation has been recorded as awareness-only documentation.

Media-pipeline Guardian awareness is now installed, indexed, relationship-bound, aggregate-validated, and wired into the existing Pages workflow.

## Current Media-Pipeline Integration

Installed:

```text
pages/media-pipeline-guardian-boundary.md
scripts/check_media_pipeline_guardian_boundary.py
data/page-index.json entry: Media Pipeline Guardian Boundary
data/page-relationship-graph.json node: media-pipeline-guardian-boundary
.github/workflows/pages.yml validation and public index link
scripts/check_guardian_local_state.py aggregate invocation
```

Relationship graph bindings:

```text
media-pipeline-guardian-boundary
  -> stegguardian-verification-status
  relationship: verified_by

stegguardian-verification-status
  -> media-pipeline-guardian-boundary
  relationship: summarizes_verification_for
```

The page and graph remain awareness-only. They do not create live camera authority, microphone authority, broadcast authority, provider authority, Guardian enforcement authority, or execution authority.

Latest graph enforcement commits:

```text
de1da189161ab519e1f2227116b141089f6fbe11
91baf0e8a082c93945ff083297004fd05a562606
```

Latest Pages workflow wiring commit:

```text
df961d7a303c81f7a2481511e0b7a4de7c8de047
```

Published workflow status remains connector-unconfirmed because GitHub has not exposed a commit status record for the latest heads.

## Existing Discovery and Health Infrastructure

Machine-readable record exposure is tracked by:

```text
docs/MACHINE_RECORD_PUBLICATION_STATUS.md
data/public-records-manifest.json
```

Session coordination is recorded in `data/session-coordination-status.json`, checked by `python scripts/check_session_coordination_status.py`, and published by the Pages workflow.

Cross-wiki health is recorded in `data/cross-wiki-health-status.json`, checked by `python scripts/check_cross_wiki_health_status.py`, and published by the Pages workflow. Its state remains `pending_live_peer_checks` until peer URLs and peer machine-record manifests are externally verified.

Live public record URL verification is recorded in `data/live-public-record-url-verification.json`, checked by `python scripts/check_live_public_record_url_verification.py`, and published by the Pages workflow. It records user-observed homepage liveness while keeping individual machine-record URL fetch confirmation pending.

Live public record fetch tooling is installed in `scripts/fetch_live_public_record_urls.py`, documented in `docs/LIVE_PUBLIC_RECORD_URL_FETCH_RUNBOOK.md`, checked by `python scripts/check_live_public_record_fetch_tooling.py`, and published by the Pages workflow.

The page relationship graph is recorded in `data/page-relationship-graph.json`, published by the Pages workflow, and checked by `python scripts/check_page_relationship_graph.py`.

The cross-wiki metadata graph is recorded in `data/cross-wiki-metadata-graph.json`, published by the Pages workflow, listed in the public records manifest, and checked by `python scripts/check_cross_wiki_metadata_graph.py`.

The public records manifest is recorded in `data/public-records-manifest.json`, published by the Pages workflow, and checked by `python scripts/check_public_records_manifest.py`.

All local Guardian propagation and graph checks can be run with:

```text
python scripts/check_guardian_local_state.py
```

## Public URL

- `https://stegverse-002.github.io/stegguardian-wiki/`

## Session Coordination

Parallel sessions must not restart the Pages repair path.

Active current-session task ownership: media-pipeline relationship binding and cross-wiki discovery/health verification.

The Site repository has concurrent active work and should not be modified from this workstream unless its current handoff explicitly transfers ownership.

The admissibility-wiki Goal 5 external-framework workstream is separately active. Media-pipeline propagation there remains deferred to that current handoff owner.

## Org Boundary Rationale

StegGuardian wiki is intentionally published from `StegVerse-002/stegguardian-wiki` because Guardian documentation belongs to the governed-entity org boundary. Linked StegVerse-Labs wikis remain part of the same ecosystem documentation mesh. The different GitHub Pages origin is deliberate and should not be interpreted as an orphaned or drifted repo.

## Source Artifacts

Admissibility source: `StegVerse-Labs/admissibility-wiki`

```text
ADMISSIBILITY_MIRROR_HANDOFF.md
pages/spe-v0-5-0-standing-boundary.md
docs/governance/llm-free-tier-trust-chain.md
```

Publisher source: `GCAT-BCAT-Engine/Publisher`

```text
docs/PUBLISHER_MIRROR_HANDOFF.md
data/spe-v0-5-0-status.json
docs/LLM_FREE_TIER_TRUST_CHAIN_STATUS.md
docs/media-pipeline-site-publication-awareness.md
```

Site source: `StegVerse-Labs/Site`

```text
docs/SITE_MIRROR_HANDOFF.md
data/spe-v0-5-0-status.json
ecosystem-chat.html
docs/LLM_FREE_TIER_TRUST_STATUS.md
docs/media/media-pipeline-overview.md
```

Media origin source: `StegVerse-Labs/collective-environment-engine`

LLM adapter source: `StegVerse-org/LLM-adapter`

SDK source: `StegVerse-org/StegVerse-SDK`

Standing proof origin: `StegVerse-Labs/Standing-Proof-Engine`

Master-records source: `master-records/core-lite`

## Verification

```text
python scripts/check_media_pipeline_guardian_boundary.py
python scripts/check_page_index.py
python scripts/check_page_relationship_graph.py
python scripts/check_cross_wiki_metadata_graph.py
python scripts/check_cross_wiki_health_status.py
python scripts/check_guardian_local_state.py
```

Live URL fetch command:

```text
python scripts/fetch_live_public_record_urls.py --write-report data/live-public-record-url-fetch-report.json
```

## Publishing Automation

The active workflow is `.github/workflows/pages.yml`.

It validates the media-pipeline boundary page, page index, relationship graph, cross-wiki records, deployment evidence, and existing Guardian documentation before publishing.

The generated index directly links `pages/media-pipeline-guardian-boundary.md`.

No additional workflow was added.

## Boundary

SPE v0.5.0 records receipt-chain reconstructability and master-records emission. It does not itself authorize enforcement; commit-time standing remains required.

The media-pipeline page, LLM free-tier trust-chain page, verification status page, metadata schema, relationship graph, cross-wiki metadata graph, cross-wiki health status, live public record URL verification, live public record fetch tooling, deployment receipt, session coordination status, Pages deployment trigger status, Pages deployment diagnosis document, and public-records manifest are downstream propagation and evidence-awareness records only.

They do not create Guardian enforcement authority, provider authority, execution authority, live media authority, public broadcast capability, connector-confirmed workflow metadata, all-machine-record URL verification, permanent retention, replay standing, reconstruction standing, or upgrade-based admissibility.

## Remaining Open Check

```text
confirm the latest Pages workflow succeeds with media-pipeline validation
observe the public media-pipeline page after deployment
execute the live URL fetch command from a networked environment
commit data/live-public-record-url-fetch-report.json after verified success
standardize cross-wiki health records across StegTalk Wiki, Admissibility Wiki, and Site
promote the reusable checker to repo-standards after local proof
```

## Archive Readiness

This handoff contains the current media-pipeline, discovery, relationship-graph, workflow, public-verification, authority-boundary, and continuation state. Earlier conversation context is not required.
