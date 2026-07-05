# Guardian Workflow Verification Runbook

## Purpose

This runbook reduces manual ambiguity when verifying the StegGuardian wiki Pages workflow after LLM free-tier trust-chain propagation.

## Current installed checks

```text
python scripts/check_llm_free_tier_trust_chain_page.py
python scripts/check_page_index.py
python scripts/check_pages_workflow_validation.py
```

The first two checks are wired into:

```text
.github/workflows/pages.yml
```

The workflow configuration check verifies that the Pages workflow contains the expected checker steps, page link, page-index publication, upload-pages-artifact action, and deploy-pages action.

## Commits already checked for workflow association

```text
3e933dd638444d6972369fb5ad9431c481711b38
8c42831aad9bc95fd5f1ec6abfe3250bba9a45a5
0cb1f41d784bf62e5238e1909d6b8b5449a2fa4e
340f4c29fe9c86c37c48a8832727ead88b7ebadb
28acb477dbc06dbd8cca4dd2951727ba2094fba3
981784b7faa964d68fc4c0411356379f422d9ee7
```

At the time of this runbook update, no workflow runs or combined commit statuses were returned for the checked commits.

## Verification sequence

1. Check the latest commit on the default branch.
2. Query workflow runs associated with that commit.
3. Query combined commit status for that commit.
4. Run local configuration checks if a local checkout is available:
   - `python scripts/check_llm_free_tier_trust_chain_page.py`
   - `python scripts/check_page_index.py`
   - `python scripts/check_pages_workflow_validation.py`
5. If a run exists, inspect jobs and record:
   - run id;
   - workflow name;
   - conclusion;
   - checker steps;
   - deployment status if present.
6. If no run exists, keep `WORKFLOW_VERIFICATION_STATUS.md` in pending state.
7. Do not claim public deployment success until a workflow run, combined status, or public URL verification is observed.

## Required result wording

```text
workflow_runs_for_checked_commits: none found at check time
combined_statuses_for_latest_commit: none found at check time
status: pending workflow execution evidence
```

or, after evidence exists:

```text
workflow_run_id: <id>
workflow_conclusion: success|failure|cancelled|timed_out|neutral|skipped|action_required
status: workflow execution evidence recorded
```

## Boundary

This runbook does not claim workflow success, public deployment success, tag verification, guardian enforcement authority, execution authority, permanent retention, replay standing, reconstruction standing, or upgrade-based admissibility.
