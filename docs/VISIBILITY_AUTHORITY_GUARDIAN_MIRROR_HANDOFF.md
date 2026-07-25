# Visibility Authority Guardian Mirror Handoff

## Source of truth

This file records the visibility-versus-authority Guardian integration. The repository-wide source of truth remains `STEGGUARDIAN_WIKI_MIRROR_HANDOFF.md`.

## Goal

Preserve the rule that visibility, acknowledgement, publication, and reconstruction do not create Guardian or execution authority.

## Installed files

```text
pages/visibility-authority-guardian-boundary.md
data/visibility-authority-guardian-status.json
scripts/check_visibility_authority_guardian_boundary.py
data/page-index.json
templates/sandbox-first/stegguardian-wiki.sandbox-profile.json
```

## Validation

The dedicated validator is bound into the existing ST-017 sandbox profile. No new active workflow is created. Merge requires sandbox and existing Pages workflow validation to pass.

## Boundaries

```text
public visibility != Guardian authority
acknowledgement != endorsement
reference != association
reconstruction != authorization
publication != execution authority
```

The documentation is propagation awareness only. It creates no Guardian enforcement, publication, execution, custody, release, deployment, standing, or admissibility authority.

## Completion condition

The goal is complete when the existing pull-request sandbox passes and the change is merged. Main-only deployment and public verification remain governed by the existing Pages workflow.

No user action is required. The complete thread is ready for archiving once workflow evidence and the merge are durable.
