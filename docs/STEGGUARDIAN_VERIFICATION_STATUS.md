# StegGuardian Wiki Verification Status

## Purpose

This page records the current verification state for StegGuardian Wiki publication and local validation.

## Summary

```text
local_status: PASS
aggregate_checker: INSTALLED
workflow_evidence_user_observed: SUCCESS
connector_confirmed_workflow_metadata: UNCONFIRMED
public_url_connector_verified: PENDING
```

## Local validation

Run:

```bash
python scripts/check_guardian_local_state.py
```

This aggregate checker validates:

```text
scripts/check_llm_free_tier_trust_chain_page.py
scripts/check_page_index.py
scripts/check_pages_workflow_validation.py
scripts/check_workflow_verification_status.py
scripts/check_aggregate_workflow_delta.py
scripts/check_user_observed_workflow_evidence.py
scripts/check_public_url_verification_status.py
```

## Workflow evidence

User-observed workflow evidence is recorded in:

```text
USER_OBSERVED_WORKFLOW_EVIDENCE.md
```

The observed successful runs are:

```text
StegGuardian Wiki Readiness #31
Publish StegGuardian Wiki #46
Publish StegGuardian Wiki #45 for commit b8d9d97
```

Connector-confirmed workflow metadata remains unavailable in the current connector checks, and that split evidence state is recorded in:

```text
WORKFLOW_VERIFICATION_STATUS.md
```

## Public URL verification

The public URL status is tracked in:

```text
PUBLIC_URL_VERIFICATION_STATUS.md
```

Required public paths are:

```text
https://stegverse-002.github.io/stegguardian-wiki/
https://stegverse-002.github.io/stegguardian-wiki/pages/llm-free-tier-trust-chain.md
https://stegverse-002.github.io/stegguardian-wiki/data/page-index.json
```

## Evidence index

```text
STEGGUARDIAN_WIKI_MIRROR_HANDOFF.md
WORKFLOW_VERIFICATION_STATUS.md
USER_OBSERVED_WORKFLOW_EVIDENCE.md
PUBLIC_URL_VERIFICATION_STATUS.md
docs/GUARDIAN_AGGREGATE_WORKFLOW_DELTA.md
docs/GUARDIAN_WORKFLOW_VERIFICATION_RUNBOOK.md
docs/STEGGUARDIAN_VERIFICATION_STATUS.md
```

## Boundary

This verification page does not claim connector-confirmed workflow metadata, public deployment verification, tag verification, guardian enforcement authority, execution authority, permanent retention, replay standing, reconstruction standing, or upgrade-based admissibility.
