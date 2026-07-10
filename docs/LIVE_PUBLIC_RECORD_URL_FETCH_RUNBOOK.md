# Live Public Record URL Fetch Runbook

## Purpose

This runbook verifies that the published StegGuardian Wiki machine-readable records are reachable from GitHub Pages.

The public homepage is user-observed live at:

```text
https://stegverse-002.github.io/stegguardian-wiki/
```

Individual machine-record URL fetch confirmation remains pending until this runbook is executed from an environment that can reach GitHub Pages.

## Command

```text
python scripts/fetch_live_public_record_urls.py --write-report data/live-public-record-url-fetch-report.json
```

## Expected Result

The command should exit with status `0` only when every expected machine-readable URL returns JSON with the expected record type.

Expected records:

```text
data/public-records-manifest.json
data/cross-wiki-metadata-graph.json
data/cross-wiki-health-status.json
data/deployment-receipt.json
data/session-coordination-status.json
data/pages-deployment-trigger-status.json
data/live-public-record-url-verification.json
```

## Completion Step

After the command succeeds:

1. Commit `data/live-public-record-url-fetch-report.json`.
2. Update `data/live-public-record-url-verification.json` so:

```json
{
  "verification_state": {
    "external_fetch_confirmed_by_current_session": true,
    "all_machine_record_urls_confirmed": true
  }
}
```

3. Update the handoff remaining-open-check section.
4. Keep all authority and standing non-claims unless a separate governed transition grants them.

## Boundary

This fetch runbook verifies public URL reachability only. It does not grant cross-repo authority, standing, execution authority, guardian enforcement authority, or peer-machine-record verification.
