# Recovery Authority

## Purpose

Recovery authority defines who or what may restore, rebind, or resume access after loss, compromise, device transition, or operator degradation.

## Boundary

Recovery authority must be explicitly granted. It must not be inferred from account profile readiness, account session readiness, local candidate status, or guardian documentation.

## Required Inputs

A recovery authority claim should identify:

- account or entity being recovered
- requesting actor
- recovery scope
- evidence references
- validity window
- policy or delegation reference
- recoverability profile
- receipt output

## Non-Claims

Recovery authority does not follow automatically from:

- local account profile creation
- local account session activity
- guardian boundary documentation
- public discovery readiness
- prototype candidate status

## Standing Rule

A recovery action is admissible only when current authority, policy, evidence, and context support the action at the time of recovery.
