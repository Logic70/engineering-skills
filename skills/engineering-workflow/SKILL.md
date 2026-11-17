---
name: engineering-workflow
description: Coordinate feature-first engineering with requirement-aligned design, branch development and unit tests, and independent main-only acceptance. Use for an engineering iteration or lifecycle handoff, not a standalone design or review request.
---

# Engineering Workflow

## Establish Scope

Read repository instructions, relevant code and tests, and Git status before
editing. Record the requested outcome, acceptance criteria, exclusions, and
pre-existing changes. User intent and host permissions override this workflow.
Never turn a design-only, question, or review-only request into implementation.
Preserve pauses: separate workflow maintenance does not resume product work.

Keep this reusable policy in this skill bundle, not copied into a target project's
AGENTS.md or contribution guide unless the user requests that destination. Follow
project rules and surface conflicts rather than silently rewriting or bypassing
them. The workflow grants no push, merge, deployment or external-service permission.

Use existing project artifacts as the durable record. If none exists, create a
concise change record in the project's documentation convention. Record decisions,
verification outcomes, review findings, and remaining gaps; do not save raw logs
or private configuration. Inspect the current record and Git state when resuming.

## Organize A Functional Iteration

Choose a small usable business flow and its observable result or stage handoff,
not a list of helpers, schemas or test counts. Prioritize functional delivery.
Blocking correctness, authorization, truthful evidence, data integrity and necessary
stop/cleanup remain required; put nonblocking DFX in the existing backlog without
deleting agreed final scope. Do not keep extending unrelated foundations.

Assign responsibility per feature, not permanent agents for every stage:

- Design owns requirement-aligned HLD/LLD and ambiguous contracts.
- Development owns branch implementation, unit tests, self-checks and fixes.
- Testing prepares independent cases, data and automation from requirements and
  design early, then accepts actual main code after merge. Its acceptance owner
  must not author that feature's product code; authoring cases/runners is allowed.
- The coordinator owns scope, dependencies, permissions, file ownership and
  evidence coverage, without routinely duplicating the three roles' work.

Parallelize prerequisite-ready work with explicit ownership when delegation is
authorized. Name scope, base, allowed files and expected output. Do not add agents,
tracking systems or repeated checks merely to fill roles or demonstrate activity.

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

## Develop, Deliver And Accept

Use the project's authoritative integration branch, called main here; do not
invent a differently named branch to match this wording.

1. Load `$engineering-test` early to prepare requirement/design-based acceptance
   cases while `$engineering-implement` develops on its development branch.
   Development owns unit tests and applicable build/type/static self-checks.
2. Load `$engineering-deliver` to record self-checks, update affected docs, commit
   the coherent change, and, when authorized, push and open its PR. PR creation
   does not require a review to have already finished.
3. Load `$engineering-review` for the actual candidate and development evidence.
   Repair accepted findings on the same branch, rerun affected self-checks, and
   update the reviewed candidate. Reuse valid unaffected evidence, not stale runs.
4. After review, applicable merge checks and actual authorization, deliver through
   the normal PR process into main. Never call missing/failing checks passed or
   push product changes directly to main. Pending post-merge acceptance is not a
   failed pre-merge check; known failures cannot be relabeled to bypass a gate.
5. Transfer the fixed actual main commit and case versions to the independent
   acceptance owner using `$engineering-test`. No feature-branch code, unmerged
   overlays or PR merge previews count as main acceptance.
6. Clear implementation bugs return directly to development with reproduction,
   expected/actual results and evidence. Involve design for ambiguous contracts,
   the user for new business choices. Fix on a development branch, self-check,
   review and PR/main merge, then independently retest the defect and affected flow.

Load the named installed skill files; a reference here is not evidence that a
stage ran. All eight skills must be available for the complete workflow. If a
required skill is missing, report the installation gap instead of inventing its
contents. Narrow stage invocations do not require running unrelated stages.

## Completion Contract

Report the business outcome, development/self-check/PR/merge status, independent
main acceptance, residual gaps, record location and commit IDs separately. Merge,
acceptance and release are different outcomes; one feature is not whole-project
completion. Do not claim completion with unresolved blockers or materially missing
validation unless the user explicitly accepts the documented limitation. A failed
or skipped check stays failed or skipped. An archive is evidence housekeeping,
not proof of business correctness or a new product workflow stage.

If Git is unavailable, identity is missing, or the target is not a repository,
report the delivery gap. Do not silently initialize Git or configure identity in
someone else's project. This workflow authorizes only a scoped local commit for
an implementation request unless higher-priority instructions say otherwise.
Push, publication, external-agent delegation, and destructive operations require
explicit authorization and normal host approval controls.
