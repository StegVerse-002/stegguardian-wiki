# Org AI Entity Capability Standards

## Purpose

This page summarizes the Org AI Entity capability standard from StegVerse-Labs repo-standards.

## Source

- Source repository: StegVerse-Labs/repo-standards
- Source state: 0.1.0-rc.1 release-candidate surface prepared
- Relevant standard: ST-012 Org AI Entity Capability

## Source Authority

StegVerse-Labs/repo-standards remains authoritative for the standards definition, schemas, validators, templates, correction tooling, and release readiness.

StegGuardian wiki is explanatory. It does not validate source standards, grant execution authority, or convert a release candidate into a final release.

## Capability Set

The repo-standards capability model includes:

- audit
- validate
- correct
- generate
- document
- publish
- install
- observe
- govern
- replay
- reconstruct
- report

## Authority Classes

Capabilities do not imply authority.

Authority must be separately declared and validated.

Authority classes include:

- advisory
- corrective
- publishing
- execution
- administrative

## Guard Rule

An Org AI Entity may not correct, validate, publish, install, or govern repository state unless the action can be expressed through required transition elements and permitted by the relevant standard.

## Transition Elements

A governed entity action should identify:

- actor
- action
- target
- scope
- authority
- input state
- evidence
- policy reference
- delegation reference
- validation rule
- output state
- receipt
- failure mode
- recoverability
- human-readable result

## Current Status

The repo-standards surface is at 0.1.0-rc.1. It is suitable for explanatory reference and implementation planning. It must not be treated as final validated release until source validation evidence exists.

## Human-Readable Result

StegGuardian wiki now has an explanatory capability standards surface for Org AI Entity role and authority boundaries.
