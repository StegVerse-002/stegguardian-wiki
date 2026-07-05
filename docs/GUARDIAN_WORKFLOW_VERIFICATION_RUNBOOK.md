# Guardian Workflow Verification Runbook

## Purpose

This runbook reduces manual ambiguity when verifying the StegGuardian wiki Pages workflow after LLM free-tier trust-chain propagation.

## Current installed checks

```text
python scripts/check_llm_free_tier_trust_chain_page.py
python scripts/check_page_index.py
```

These checks are wired into:

```text
.github/workflows/pages.yml
```

## Commits already checked for workflow association

```text
3e933dd638444d6972369fb5ad9431c481711b38
8c42831aad9bc95fd5f1ec6abfe3250bba9a45a5
0cb1f41d784bf62e5238e1909d6b8b5449a2fa4e
```

At the time of this runbook creation, no workflow runs were returned for those checked commits.

## Verification sequence

1. Check the latest commit on the default branch.
2. Query workflow runs associated with that commit.
3. If a run exists, inspect jobs and record:
   - run id;
   - workflow name;
   - conclusion;
   - checker steps;
   - deployment status if present.
4. If no run exists, keep `WORKFLOW_VERIFICATION_STATUS.md` in pending state.
5. Do not claim public deployment success until a workflow run or public URL verification is observed.

## Required result wording

```text
workflow_runs_for_checked_commits: none found at check time
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
