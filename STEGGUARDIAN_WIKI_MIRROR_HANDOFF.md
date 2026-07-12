# StegGuardian Wiki Mirror Handoff

## Status

This file is the current handoff and task source of truth for `StegVerse-002/stegguardian-wiki`.

## Current Priority

StegGuardian Wiki is live at `https://stegverse-002.github.io/stegguardian-wiki/` by user-observed confirmation.

Current integration goal: complete post-deployment machine-record verification and then standardize cross-wiki health records without duplicating active Site or admissibility-wiki workstreams.

## Session Coordination

No open issue or pull request claims the current Guardian live-record verification task.

Recent repository commits are the current media-pipeline and discovery chain. No newer external commit displaced this handoff before continuation.

Parallel sessions must not restart the resolved Pages repair path.

The Site repository has concurrent active work and must not be modified from this workstream unless its current handoff transfers ownership.

The admissibility-wiki Goal 5 external-framework workstream is separately active. Media-pipeline propagation there remains deferred to that handoff owner.

## Media-Pipeline Guardian Integration

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

## Automated Live Public-Record Verification

The existing Pages workflow now contains two ordered jobs:

```text
deploy
verify-live-public-records
```

The verification job:

- runs only after Pages deployment;
- uses GitHub's network rather than requiring a user-operated environment;
- retries public machine-record fetches up to 12 times at 15-second intervals;
- writes `reports/live-public-record-url-fetch-report.json`;
- uploads `stegguardian-live-public-record-url-fetch-report` through `actions/upload-artifact@v4`;
- retains the artifact for 30 days;
- fails closed if URL and record-type verification does not converge.

Installed automation commits:

```text
9526b4b0ed181e58cff0b6f00df58f687e109c29
ac92f48c2007284bac35ac3432f3aa725dcd0c13
9d24932cd5bd9455bf69384c90f94f5f9a559207
```

The workflow validator now requires the dependent job, bounded fetch command, report path, artifact upload, and enforcement step.

The runbook now treats the workflow artifact as the primary evidence path. Manual execution remains diagnostic only.

No successful live-verification result is claimed until the post-deployment job and its enforcement step succeed.

## Existing Discovery and Health Infrastructure

Machine-readable record exposure is tracked by:

```text
docs/MACHINE_RECORD_PUBLICATION_STATUS.md
data/public-records-manifest.json
```

Cross-wiki health is recorded in `data/cross-wiki-health-status.json` and remains `pending_live_peer_checks` until peer URLs and peer machine-record manifests are verified.

Live public record status is recorded in `data/live-public-record-url-verification.json`. It must not be changed to confirmed before successful workflow evidence exists.

The relationship graph, cross-wiki metadata graph, health record, endpoint registry, deployment receipt, session coordination record, trigger-status record, public-records manifest, and verification documents are published through the existing Pages workflow.

All local checks run through:

```text
python scripts/check_guardian_local_state.py
```

## Public URL

```text
https://stegverse-002.github.io/stegguardian-wiki/
```

## Source Artifacts

Publisher source:

```text
GCAT-BCAT-Engine/Publisher/docs/PUBLISHER_MIRROR_HANDOFF.md
GCAT-BCAT-Engine/Publisher/docs/media-pipeline-site-publication-awareness.md
```

Site source:

```text
StegVerse-Labs/Site/docs/SITE_MIRROR_HANDOFF.md
StegVerse-Labs/Site/docs/media/media-pipeline-overview.md
```

Media origin source:

```text
StegVerse-Labs/collective-environment-engine
```

Additional governed sources remain documented in the installed page and existing relationship records.

## Verification Commands

Local structural verification:

```text
python scripts/check_media_pipeline_guardian_boundary.py
python scripts/check_page_index.py
python scripts/check_page_relationship_graph.py
python scripts/check_cross_wiki_metadata_graph.py
python scripts/check_cross_wiki_health_status.py
python scripts/check_pages_workflow_validation.py
python scripts/check_guardian_local_state.py
```

Manual network diagnostic only:

```text
python scripts/fetch_live_public_record_urls.py \
  --write-report data/live-public-record-url-fetch-report.json
```

Primary network verification occurs automatically in the post-deployment Pages job.

## Publishing Automation

The active workflow is `.github/workflows/pages.yml`.

It validates the media-pipeline boundary page, page index, relationship graph, cross-wiki records, deployment evidence, and existing Guardian documentation before publishing.

It then verifies the deployed machine records through the dependent `verify-live-public-records` job and emits a traceable report artifact.

No additional workflow was added.

## Boundary

SPE and downstream documentation records do not themselves authorize enforcement; commit-time standing remains required.

The media-pipeline page, verification records, metadata, graphs, health records, URL-fetch tooling, workflow artifacts, receipts, and manifests are propagation and evidence-awareness records only.

They do not create Guardian enforcement authority, provider authority, execution authority, live media authority, public broadcast capability, permanent retention, replay standing, reconstruction standing, or upgrade-based admissibility.

## Remaining Open Check

```text
confirm the Pages deploy job succeeds
confirm verify-live-public-records succeeds
inspect the uploaded live fetch report artifact
update data/live-public-record-url-verification.json only after successful evidence
observe the public media-pipeline page after deployment
standardize cross-wiki health records across unclaimed peer repositories
promote the reusable checker to repo-standards after local and live proof
```

## Archive Readiness

This handoff contains the current media-pipeline, discovery, relationship-graph, workflow, automated public-verification, authority-boundary, coordination, and continuation state. Earlier conversation context is not required.
