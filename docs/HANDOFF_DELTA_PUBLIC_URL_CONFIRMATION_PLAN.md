# Handoff Delta: Public URL Confirmation Plan

## Status

This document supplements `STEGGUARDIAN_WIKI_MIRROR_HANDOFF.md` for the newest public URL confirmation work.

## Newly checkable items

```text
scripts/check_observed_machine_record_publication_evidence.py
scripts/check_handoff_delta_observed_publication_success.py
scripts/check_public_url_machine_records_delta.py
scripts/check_public_url_confirmation_plan.py
```

## Aggregate validation

```text
python scripts/check_guardian_local_state.py
```

now includes the observed publication evidence, observed publication handoff delta, public URL machine-record delta, and public URL confirmation plan.

## Required public URL set

```text
/
/pages/llm-free-tier-trust-chain.md
/data/page-index.json
/data/page-metadata.schema.json
/data/page-relationship-graph.json
/data/public-records-manifest.json
/docs/STEGGUARDIAN_VERIFICATION_STATUS.md
```

## Remaining open checks

```text
connector_confirmed_run_ids: pending
independent_public_url_confirmation: pending
```

## Boundary

This delta does not claim connector-confirmed workflow metadata, independent public URL confirmation, tag verification, guardian enforcement authority, execution authority, permanent retention, replay standing, reconstruction standing, or upgrade-based admissibility.
