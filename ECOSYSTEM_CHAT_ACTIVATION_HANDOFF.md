# Ecosystem Chat Activation Handoff

## Scope

This record preserves the automatic downstream Ecosystem Chat activation projection for `StegVerse-002/stegguardian-wiki`.

## Source chain

```text
StegVerse-Labs/Site activation state
-> GCAT-BCAT-Engine/Publisher hourly importer
-> Publisher data/ecosystem-chat-activation-status.json
-> StegGuardian Wiki importer
-> data/ecosystem-chat-publisher-activation.json
-> existing Guardian local-state and Pages validation chain
```

## Installed files

```text
scripts/import_publisher_ecosystem_chat_activation.py
scripts/check_guardian_local_state.py
data/ecosystem-chat-publisher-activation.json (generated)
.github/workflows/pages.yml (existing workflow owner)
```

`check_guardian_local_state.py` now invokes the Publisher importer before the existing Guardian validators. No new workflow, manual dispatch, artifact download, file movement, merge observation, or user confirmation is required for this projection.

## Acceptance boundary

The importer requires:

- Publisher schema `stegverse.publisher.ecosystem_chat_activation_status.v1`;
- Publisher publication, release, custody, and execution flags to remain `false`;
- `manual_user_action_required=false`;
- `status=VERIFIED_ACTIVATION_IMPORTED` and `activation_complete=true` before recording a verified projection.

Missing Publisher state is recorded as `PENDING_PUBLISHER_ACTIVATION`. Invalid schema or authority fields fail closed as `REJECTED_PUBLISHER_ACTIVATION`.

## Authority boundary

The projection is awareness-only. It does not create Guardian enforcement authority, publication authority, release authority, custody, execution authority, deployment authority, or an admissibility determination.

## Commits

```text
40ff08c4872d9c7b51edf1bf4b980103119075b5  add importer
beb3847e281a650265a436fe057e7beef701b075  integrate importer into Guardian local-state chain
```

GitHub exposed no combined status checks for `beb3847`. Missing status is not treated as validation success; the repository-owned Pages workflow remains responsible for producing evidence.

## Manual-task posture

```text
manual_user_action_required: false
continuation_owner: existing Guardian validation and Pages workflow
source_observation_owner: Publisher hourly importer
```

## Archive readiness

No future continuation requires the conversation that installed this consumer. Remaining activation is determined by upstream machine-generated evidence and the repository-owned workflow.
