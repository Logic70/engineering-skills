---
name: engineering-workflow
description: Coordinate an engineering implementation from proportionate HLD and LLD through review, tests, documentation, and a scoped Git commit. Use for an end-to-end engineering change, not a design-only or review-only request.
---

# Engineering Workflow

## Establish Scope

Read repository instructions, relevant code and tests, and Git status before
editing. Record the requested outcome, acceptance criteria, exclusions, and
pre-existing changes. User intent and host permissions override this workflow.
Never turn a design-only, question, or review-only request into implementation.

Use existing project artifacts as the durable record. If none exists, create a
concise change record in the project's documentation convention. Record decisions,
verification outcomes, review findings, and remaining gaps; do not save raw logs
or private configuration. Inspect the current record and Git state when resuming.

## Choose The Necessary Design

For a narrow, understood change, keep a short design note and implementation
plan in the record. Skip full HLD/LLD and record why. For cross-module behavior,
architecture, deployment, or data ownership changes, use `$highlevel-design`,
then `$lowlevel-design` after architecture decisions are settled. Reuse existing
approved designs rather than generating duplicates.

Use `$design-plan-closure-review` for design and implementation-plan changes.
Keep design behavior separate from implementation sequencing. Unresolved
architecture decisions block dependent implementation. A design-only request
ends at the requested design output.

## Implement And Verify

1. Load `$engineering-implement` with the agreed scope, design, and plan.
2. Load `$engineering-test` for the actual patch and acceptance criteria.
3. Load `$engineering-review` for the final patch and test evidence.
4. Repair accepted findings and rerun affected tests and review. Never carry
   stale test results forward after a relevant edit.
5. Load `$engineering-deliver` to update docs, persist evidence, check the final
   patch, and create a scoped local Git commit.

Load the named installed skill files; a reference here is not evidence that a
stage ran. All eight skills must be available for the complete workflow. If a
required skill is missing, report the installation gap instead of inventing its
contents. Narrow stage invocations do not require running unrelated stages.

## Completion Contract

Report changed behavior, checks actually run, findings and residual gaps, durable
record location, and commit ID. Do not claim completion with unresolved blocking
findings or materially missing validation unless the user explicitly accepts the
documented limitation. A skipped check remains skipped, never passed.

If Git is unavailable, identity is missing, or the target is not a repository,
report the delivery gap. Do not silently initialize Git or configure identity in
someone else's project. This workflow authorizes only a scoped local commit for
an implementation request unless higher-priority instructions say otherwise.
Push, publication, external-agent delegation, and destructive operations require
explicit authorization and normal host approval controls.
