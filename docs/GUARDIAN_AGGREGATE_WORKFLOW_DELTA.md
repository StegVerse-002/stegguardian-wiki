# Guardian Aggregate Workflow Delta

## Purpose

This record preserves the intended Pages workflow simplification without directly modifying deployment authority paths in this pass.

## Installed aggregate checker

```text
python scripts/check_guardian_local_state.py
```

This command runs:

```text
python scripts/check_llm_free_tier_trust_chain_page.py
python scripts/check_page_index.py
python scripts/check_pages_workflow_validation.py
python scripts/check_workflow_verification_status.py
```

## Current workflow state

The current Pages workflow still runs the direct page and page-index checks before deployment:

```text
python scripts/check_llm_free_tier_trust_chain_page.py
python scripts/check_page_index.py
```

## Proposed workflow delta

Replace the two direct validation steps with the aggregate check:

```text
- name: Validate Guardian local state
  run: python scripts/check_guardian_local_state.py
```

## Reason

This reduces future manual drift because the same command validates local page content, page index metadata, workflow configuration, and pending workflow-status evidence.

## Boundary

This document does not modify workflow permissions, publish the site, claim workflow success, claim public deployment success, grant guardian enforcement authority, grant execution authority, or change any free-tier trust-chain non-claim.
