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

## Preserved Upstream Readiness Surface

The active Guardian summary remains bound to `Standing-Proof-Engine v0.5.0` and status `READY_FOR_UPSTREAM_GATE_EVENTS`. ST-017 adoption does not supersede that upstream readiness contract.

## ST-017 Sandbox-First Adoption

Installed on validation branch `validation/st017-sandbox-adoption`:

```text
templates/sandbox-first/stegguardian-wiki.sandbox-profile.json
scripts/run_sandbox_validation.py
scripts/check_st017_sandbox_adoption.py
reports/sandbox-first-validation.report.json
.github/workflows/pages.yml PR validation job
```

Required sequence:

```text
change installed
-> isolated temporary repository copy
-> compile and Guardian validators
-> SANDBOX PASS
-> GitHub Actions observation
-> merge
-> main-only Pages deployment
-> live public-output verification
```

The existing Pages workflow is preserved. Pull requests execute validation and upload `stegguardian-st017-sandbox-report`; deployment and live-record verification remain restricted to non-PR execution after validation succeeds.

Current branch status after the first observed execution:

```text
SANDBOX: FAIL — canonical live-fetch command marker missing
GITHUB_ACTIONS: FAIL
PUBLIC_OUTPUT: NOT_VERIFIED
```

The marker defect has been repaired and the next PR run must be inspected before merge.

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

## Automated Live Public-Record Verification

The existing Pages workflow contains:

```text
deploy
  -> verify-live-public-records
```

The dependent job uses GitHub's network after deployment, retries up to 12 times at 15-second intervals, writes `reports/live-public-record-url-fetch-report.json`, uploads `stegguardian-live-public-record-url-fetch-report`, and fails closed if verification does not converge.

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
python scripts/check_st017_sandbox_adoption.py --structural-only
python scripts/run_sandbox_validation.py
```

## Boundary

The media page, schemas, health records, endpoint registry, graphs, manifests, workflow artifacts, sandbox reports, and fetch reports are propagation and evidence-awareness records only.

They do not create Guardian enforcement authority, provider authority, execution authority, live-media authority, permanent retention, replay standing, reconstruction standing, release authority, tag authority, deployment authority beyond the existing workflow, or upgrade-based admissibility.

## Remaining Open Check

```text
rerun and inspect the repaired ST-017 pull-request sandbox
merge only after SANDBOX PASS and both PR workflows PASS
confirm the resulting main Pages deploy job succeeds
confirm verify-live-public-records succeeds
inspect the uploaded live fetch report artifact
update live verification state only after successful evidence
confirm StegTalk and StegGuardian publicly expose the identical shared schema
standardize Site and admissibility-wiki only through their active handoff owners
```

## Archive Readiness

This handoff contains the current ST-017 adoption, media-pipeline, shared-schema, workflow, public-verification, authority-boundary, coordination, and continuation state. Earlier conversation context is not required.
