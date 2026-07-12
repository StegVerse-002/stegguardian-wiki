# StegGuardian Wiki Mirror Handoff

## Status

This file is the current handoff and task source of truth for `StegVerse-002/stegguardian-wiki`.

## Current Priority

StegGuardian Wiki is live at `https://stegverse-002.github.io/stegguardian-wiki/` by user-observed confirmation.

Current integration goal: complete live machine-record verification and establish a reusable shared cross-wiki health contract without duplicating active Site or admissibility-wiki workstreams.

## Session Coordination

No open issue or pull request claims the current Guardian live-record or shared-health-schema task.

Parallel sessions must not restart the resolved Pages repair path.

Site has concurrent active work and must not be modified from this workstream.
Admissibility-wiki Goal 5 remains separately active and must not be modified from this workstream.

## Media-Pipeline Guardian Integration

Installed and enforced:

```text
pages/media-pipeline-guardian-boundary.md
scripts/check_media_pipeline_guardian_boundary.py
data/page-index.json
data/page-relationship-graph.json
scripts/check_page_relationship_graph.py
scripts/check_guardian_local_state.py
.github/workflows/pages.yml
```

The page and graph are awareness-only and create no live camera, microphone, broadcast, provider, Guardian-enforcement, or execution authority.

## Shared Cross-Wiki Health Contract

Installed:

```text
data/cross-wiki-health-status.schema.json
data/cross-wiki-health-status.json schema_version: 1.0.0
data/cross-wiki-health-status.json schema_ref: data/cross-wiki-health-status.schema.json
data/cross-wiki-health-status.json peer_registry: data/ecosystem-documentation-endpoints.json
scripts/check_cross_wiki_health_status.py schema enforcement
data/public-records-manifest.json schema entry
scripts/check_public_records_manifest.py schema requirement
.github/workflows/pages.yml schema publication and public index link
scripts/fetch_live_public_record_urls.py live schema verification
```

StegGuardian and StegTalk now share the same schema identifier and required common fields. `cross_wiki_schema_consistency_confirmed` remains false until workflow artifacts prove both published schema and health-record URLs.

Latest shared-schema commits:

```text
19c5ee4d6c3dad421c800bd5c36123e156b34b00
9e1ec729513d39d21aa68e806a7bf9b28c939137
5c34f50429484a28b51b013ec6cdea42c7fe516c
375e1af8822c037bced490f4b535dcb8236b39cd
ca5693f403c6b050d6596a17adff624004bc986f
f814aa26e818690f393cf5bba2e2c1b577f25a4f
df1cbcc8bbd930264cab2da7ceb50ef83aa3cb1c
```

## Automated Live Public-Record Verification

The existing Pages workflow contains:

```text
deploy
  -> verify-live-public-records
```

The dependent job:

- uses GitHub's network after deployment;
- retries up to 12 times at 15-second intervals;
- verifies public JSON record types, including the shared health schema title;
- writes `reports/live-public-record-url-fetch-report.json`;
- uploads `stegguardian-live-public-record-url-fetch-report` for 30 days;
- fails closed if verification does not converge.

No successful live-verification result is claimed until the job and enforcement step succeed.

## Public URL

```text
https://stegverse-002.github.io/stegguardian-wiki/
```

## Verification Commands

```text
python scripts/check_media_pipeline_guardian_boundary.py
python scripts/check_page_index.py
python scripts/check_page_relationship_graph.py
python scripts/check_cross_wiki_metadata_graph.py
python scripts/check_cross_wiki_health_status.py
python scripts/check_public_records_manifest.py
python scripts/check_pages_workflow_validation.py
python scripts/check_guardian_local_state.py
```

Manual network execution remains diagnostic only:

```text
python scripts/fetch_live_public_record_urls.py \
  --write-report data/live-public-record-url-fetch-report.json
```

## Boundary

The media page, schemas, health records, endpoint registry, graphs, manifests, workflow artifacts, and fetch reports are propagation and evidence-awareness records only.

They do not create Guardian enforcement authority, provider authority, execution authority, live-media authority, permanent retention, replay standing, reconstruction standing, or upgrade-based admissibility.

## Remaining Open Check

```text
confirm the Pages deploy job succeeds
confirm verify-live-public-records succeeds
inspect the uploaded live fetch report artifact
update live verification state only after successful evidence
confirm StegTalk and StegGuardian publicly expose the identical shared schema
standardize Site and admissibility-wiki only through their active handoff owners
promote the reusable schema and checker to repo-standards after multi-repo live proof
```

## Archive Readiness

This handoff contains the current media-pipeline, shared-schema, workflow, public-verification, authority-boundary, coordination, and continuation state. Earlier conversation context is not required.
