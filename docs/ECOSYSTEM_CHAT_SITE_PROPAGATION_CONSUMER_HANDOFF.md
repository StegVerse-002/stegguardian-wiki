# Ecosystem Chat Site Propagation Consumer Handoff

## Installed result

```text
Repository: StegVerse-002/stegguardian-wiki
Result: AUTONOMOUS_FAIL_CLOSED_GUARDIAN_PROPAGATION_CONSUMER_INSTALLED
Manual user action required: false
Canonical workflow: .github/workflows/pages.yml
```

## Installed files

```text
scripts/check_ecosystem_chat_activation_projection.py
data/ecosystem-chat-activation-status.json
```

The existing hourly Pages workflow refreshes and validates the projection before deployment, uploads the projection artifact, and publishes the status through GitHub Pages. No workflow dispatch, browser action, copy, or user intervention is required.

## Acceptance gates

`VERIFIED_INGESTION_READY` requires valid Site state and packet hashes, matching state binding, a declared StegGuardian destination, Site `ACTIVATION_COMPLETE`, packet `READY_FOR_DOWNSTREAM_INGESTION`, destination `ingestion_ready=true`, no manual action, and all authority flags false.

Otherwise the projection remains `ACTIVATION_EVIDENCE_PENDING` and records exact blockers.

## Current source state

```text
Site state: ACTIVATION_PENDING_EVIDENCE
Site propagation: PENDING_ACTIVATION_EVIDENCE
Destination declared: true
Destination ingestion ready: false
Required action: wait_for_verified_activation_state
Blockers: site_activation_not_complete; destination_ingestion_not_ready
```

## Boundary

The projection does not grant Guardian, execution, release, custody, admissibility, or publication authority.

## Continuation

1. The hourly Pages workflow refreshes the projection from Site.
2. Source failures retain and validate the last fail-closed projection.
3. Pending evidence creates no user task.
4. A valid ready packet advances the projection automatically.
5. Pages deployment publishes the refreshed status.
6. Live-public-record verification confirms the deployed machine record.

## Remaining blocker

```text
Upstream: StegVerse-org/LLM-adapter, then StegVerse-Labs/Site
Blocker: live_activation_observation_not_yet_recorded
Manual user action required: false
```

No tag or release is authorized by this consumer.
