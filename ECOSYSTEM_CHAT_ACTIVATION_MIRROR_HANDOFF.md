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

## Execution ownership and collision partition

Standard: `StegVerse-Labs/Continuity/docs/REPOSITORY_HANDOFF_STANDARD.md` / `stegverse.handoff-execution-ownership/v1`.

### MANUAL / SESSION-STARTABLE

```yaml
- task_id: STEGGUARDIAN-ECOSYSTEM-CHAT-HANDOFF-ADOPTION-023
  execution_owner: repo-standards #37 integration lane + StegGuardian repository owner
  claim_state: CLAIMED_FOR_INTEGRATION
  worker_registry_ref: StegVerse-Labs/repo-standards#37 + StegVerse-002/stegguardian-wiki#23
  manual_execution_allowed: true
  manual_allowed_role: integration
  collision_scope: ownership metadata/textual migration in this handoff only; excludes Site activation production, Pages execution, projection state mutation, Guardian product behavior, claims/fences/leases, custody, standing, admissibility, release, and runtime authority
  release_condition: this textual migration is merged and its integration issue is closed or superseded
  next_executable_action: merge only the ownership metadata after repository validation; do not implement the machine-owned activation/projection lane
```

### WORKER-OWNED / DO NOT COMPETE

```yaml
- task_id: STEGGUARDIAN-ECOSYSTEM-CHAT-PROJECTION-ACTIVE
  execution_owner: existing StegGuardian Pages/projection lane plus the upstream Site activation owner
  claim_state: MACHINE_OWNED
  worker_registry_ref: ECOSYSTEM_CHAT_ACTIVATION_HANDOFF.md + STEGGUARDIAN_WIKI_MIRROR_HANDOFF.md + current Site activation handoff/task/receipt state
  manual_execution_allowed: false
  manual_allowed_role: observation
  collision_scope: Site activation evidence production, projection refresh, Pages validation/deployment, live-record verification, and all underlying runtime/custody/evidence transitions
  release_condition: Site emits the required hash-bound activation evidence and the existing StegGuardian machine lane independently observes/publishes the valid projection according to its canonical gates
  next_executable_action: allow the existing machine-owned Pages/projection path to continue; observe resulting evidence without substituting manual completion
```

### ESCALATED / AUTHORITY-OWNED

```yaml
- task_id: STEGGUARDIAN-ECOSYSTEM-CHAT-AUTHORITY
  execution_owner: applicable component authority -> ecosystem governance -> human authority when explicitly required
  claim_state: ESCALATED
  worker_registry_ref: current upstream/downstream handoffs plus StegVerse-Labs/Continuity/docs/REPOSITORY_HANDOFF_STANDARD.md
  manual_execution_allowed: false
  manual_allowed_role: reconciliation
  collision_scope: Guardian authority, execution authority, release authority, custody, standing, admissibility, or any attempt to promote projection/transport evidence into authority
  release_condition: the applicable canonical authority explicitly grants or reassigns the bounded authority scope
  next_executable_action: fail closed and escalate; projection evidence alone may not satisfy or create authority
```

### COMPLETED / SUPERSEDED

- The standalone-workflow approach is superseded; this projection remains integrated into the existing Pages workflow.
- The nonexistent `StegVerse-Labs/Sit` target is superseded by the canonical `StegVerse-Labs/Site` repository map.
- Any inference that projection observation grants Guardian, execution, release, custody, standing, or admissibility authority is superseded/prohibited.
