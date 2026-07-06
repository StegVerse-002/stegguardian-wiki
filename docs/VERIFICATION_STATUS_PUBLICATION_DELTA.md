# Verification Status Publication Delta

## Purpose

This record preserves the remaining publication-path delta for the StegGuardian verification status page.

## Installed and indexed

```text
docs/STEGGUARDIAN_VERIFICATION_STATUS.md
scripts/check_stegguardian_verification_status.py
data/page-index.json entry: StegGuardian Verification Status
scripts/check_page_index.py validates the entry
scripts/check_guardian_local_state.py runs the checker set
```

## Current static publication state

The Pages workflow currently copies these content classes into `_site`:

```text
README.md -> _site/README.md
data/page-index.json -> _site/data/page-index.json
receipts/*.json -> _site/receipts/
pages/*.md -> _site/pages/
```

The verification status file is under `docs/`, so it is indexed locally but not guaranteed to be copied into `_site` until the workflow copies docs or the page is moved into `pages/`.

## Safe publication options

Option A:

```text
copy docs/STEGGUARDIAN_VERIFICATION_STATUS.md into _site/docs/STEGGUARDIAN_VERIFICATION_STATUS.md
```

Option B:

```text
move or mirror docs/STEGGUARDIAN_VERIFICATION_STATUS.md to pages/stegguardian-verification-status.md
```

## Boundary

This delta does not modify deployment workflow permissions, claim public URL verification, claim connector-confirmed workflow metadata, claim tag verification, grant guardian enforcement authority, grant execution authority, or alter any non-claim in the verification status page.
