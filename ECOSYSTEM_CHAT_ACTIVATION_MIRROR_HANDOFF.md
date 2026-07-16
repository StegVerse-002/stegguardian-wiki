# Ecosystem Chat Guardian Projection Mirror Handoff

## Source of truth

This file is the goal-specific continuation source for the Ecosystem Chat activation projection in `StegVerse-002/stegguardian-wiki`.

## Correct repository map

```text
Source: StegVerse-Labs/Site
Destination: StegVerse-002/stegguardian-wiki
Admissibility peer: StegVerse-Labs/admissibility-wiki
Removed nonexistent target: StegVerse-Labs/Sit
```

`StegVerse-Labs/Site` is the existing Site repository and is not duplicated as `StegVerse-Labs/Sit`.

## Installed consumer

```text
scripts/check_ecosystem_chat_activation_projection.py
data/ecosystem-chat-activation-status.json
.github/workflows/pages.yml
```

The existing Pages workflow refreshes and validates the projection before deployment, uploads the projection as a workflow artifact, and publishes it at:

```text
https://stegverse-002.github.io/stegguardian-wiki/data/ecosystem-chat-activation-status.json
```

No standalone workflow was added.

## States

```text
ACTIVATION_EVIDENCE_PENDING
VERIFIED_ACTIVATION_OBSERVED
```

The verified state requires valid Site state and propagation hashes, exact packet-to-state binding, explicit destination declaration, `ACTIVATION_COMPLETE`, and `READY_FOR_DOWNSTREAM_INGESTION`.

## Authority boundary

This projection grants no Guardian authority, execution authority, release authority, custody, standing, or admissibility.

## Remaining work

```text
1. Observe the existing Pages workflow containing the consumer.
2. Allow the workflow to refresh and publish the projection automatically.
3. Observe VERIFIED_ACTIVATION_OBSERVED only after Site emits verified activation evidence.
4. Include the public projection in live-record verification when the existing handoff permits that bounded extension.
```

Manual user action required: false.

## Archive readiness

This handoff and the repository implementation preserve all continuation state for this projection goal.
