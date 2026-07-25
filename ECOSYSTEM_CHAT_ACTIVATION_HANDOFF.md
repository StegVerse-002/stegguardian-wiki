# Ecosystem Chat Activation Handoff

## Scope

This record preserves the bounded downstream Ecosystem Chat activation projection for `StegVerse-002/stegguardian-wiki`.

## Authoritative source chain

```text
StegVerse-Labs/Site exact-SHA orchestration
-> Site terminal orchestration receipt
-> master-records/orchestration custody RECORDED
-> reconstruction PASS
-> GCAT-BCAT-Engine/Publisher custody-bound activation status
-> StegGuardian Wiki importer
-> data/ecosystem-chat-publisher-activation.json
-> data/ecosystem-chat-activation-status.json
-> Guardian validation and Pages deployment chain
```

## Installed files

```text
scripts/import_publisher_ecosystem_chat_activation.py
scripts/check_guardian_activation_orchestration_contract.py
scripts/check_guardian_local_state.py
.github/workflows/pages.yml
data/ecosystem-chat-publisher-activation.json (generated)
data/ecosystem-chat-activation-status.json (generated public mirror)
```

## Acceptance boundary

The Guardian importer records a verified projection only when Publisher provides:

```text
schema = stegverse.publisher.ecosystem_chat_activation_status.v2
status_sha256 = valid canonical digest
status = VERIFIED_ACTIVATION_IMPORTED
activation_complete = true
terminal_custody_verified = true
terminal_custody_sha256 = valid SHA-256 digest
custody_repository = master-records/orchestration
manual_user_action_required = false
publication_authorized = false
release_authorized = false
execution_authorized = false
```

Missing upstream evidence remains `PENDING_PUBLISHER_ACTIVATION`. Invalid schema, digest, custody, or authority fields become `REJECTED_PUBLISHER_ACTIVATION` and fail closed.

## Orchestration repair

The Pages workflow no longer owns an hourly schedule. It now uses:

```text
push to main -> validate -> import custody-bound Publisher projection -> deploy -> verify
pull request -> validation only
workflow dispatch -> validation only
cancel-in-progress = true
```

A manual dispatch cannot deploy Pages. Superseded runs are cancelled. The workflow no longer reads Site activation directly for the Guardian activation decision; Publisher is the required bounded downstream source after Master Records custody.

## Authority boundary

```text
Publisher activation != Guardian enforcement authority
terminal custody != Guardian enforcement authority
reconstruction PASS != execution authority
Guardian projection != publication authority
Pages deployment != admissibility determination
URL verification != standing
```

All projection authority flags remain false.

## Current evidence state

```text
terminal-custody-aware importer: INSTALLED
Guardian orchestration contract: INSTALLED
canonical local-state binding: INSTALLED
hourly workflow schedule: REMOVED
superseded-run cancellation: INSTALLED
manual deployment authority: REMOVED
first live custody-bound Guardian projection: NOT YET OBSERVED
first live Pages verification containing custody hash: NOT YET OBSERVED
```

## Next task

```text
1. Observe the first current-main workflow containing commit b5b44cc9b7b38f2540c2fcf95d89786e6308f579 or later.
2. Repair only the first exact validation failure without weakening custody checks.
3. Preserve the first Guardian projection carrying the same terminal_custody_sha256 as Publisher and admissibility-wiki.
4. Preserve the first successful live Pages verification for that projection.
5. Do not infer Guardian authority from projection, custody, reconstruction, deployment, or URL availability.
```

## Archive readiness

Repository history, this handoff, the importer, the orchestration contract, the canonical local-state chain, workflow artifacts, and the eventual live projection preserve continuation. The active cross-repository goal remains open until a real custody hash is observed consistently across Publisher, admissibility-wiki, and StegGuardian Wiki.
