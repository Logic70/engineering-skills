---
name: engineering-test
description: Select and run risk-proportionate tests and verification for the actual engineering patch, record real outcomes, and identify acceptance gaps. Use after implementation or to verify a focused change.
---

# Engineering Test

## Select Checks

Read the request, acceptance criteria, repository test instructions, actual
staged/unstaged diff, and tests for the affected behavior. Use the repository's
own commands and environment. Do not hardcode WorkflowProgram or other unrelated
framework commands.

For a local change, run focused tests and appropriate static/build checks.
For shared contracts, schema/runtime/deployment changes, broaden to relevant
integration, compatibility, migration, recovery, and smoke checks. Release-wide
checks belong to a release request or comparable blast radius, not every commit.
UI changes need meaningful interaction and visual checks on relevant viewports
when tools are available. Distinguish automated tests from manual observations.

## Execute And Record

Actually run the selected commands. Record command, environment/context needed
to reproduce, outcome, and relevant counts/errors. Do not store credentials or
raw private logs. Map important acceptance criteria to tests or explicit manual
evidence. Report not-run checks and why, not invented passes.

Investigate failures. Distinguish observed baseline failures from patch-induced
failures only with evidence. Never disable tests or weaken acceptance merely to
get green. Missing dependencies, approvals, or network access are gaps to report
or resolve through host controls, not reasons to bypass them.

After a relevant edit, rerun affected checks. Earlier success is not proof about
the new patch. Structural validation alone does not establish behavioral success.

## Exit And Handoff

Pass actual evidence, failures, untested behavior, and residual risk to
`$engineering-review`. Materially missing validation or failures block completion
unless the user explicitly accepts the documented limitation. Review may still
proceed to discover other issues, but must retain the incomplete test status.
