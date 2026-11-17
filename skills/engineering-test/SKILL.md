---
name: engineering-test
description: Prepare requirement-based acceptance cases early and independently accept identified main commits after merge, with risk-proportionate evidence and defect retests. Use for test planning or acceptance, not development unit tests or branch acceptance.
---

# Engineering Test

## Prepare Acceptance Early

Read the request, acceptance criteria, repository test instructions, actual
design and affected behavior. Prepare cases, data and automation while development
proceeds, including the real user flow, saved result and stage handoffs. Expected
results come from requirements/design, not merely what the code currently does.
Review the actual patch when available for coverage gaps, not as the specification.
Development owns unit tests and branch self-checks. Do not call case preparation,
branch experiments or development evidence independent acceptance.

## Identify The Main Candidate

For independent acceptance, the owner must not have authored this feature's product
code; writing cases/runners does not disqualify them. Use an identified actual
commit on the project's authoritative main branch after authorized PR merge in a
clean isolated checkout or exact source export. Record the product SHA and case/
runner versions. No feature branch, merge preview or unmerged product overlay.
If the candidate is not on main yet, prepare cases and report acceptance pending.

Use the repository's own commands and environment. Do not hardcode WorkflowProgram
or another unrelated framework. This skill supplies no service/data permission.

## Select Checks

For a local change, run focused tests and appropriate static/build checks.
For shared contracts, schema/runtime/deployment changes, broaden to relevant
integration, compatibility, migration, recovery, and smoke checks. Release-wide
checks belong to a release request or comparable blast radius, not every commit.
UI changes need meaningful interaction and visual checks on relevant viewports
when tools are available. Distinguish automated tests from manual observations.
Start with the real business flow. Mock/unit or package-structure results cannot
replace required real tools, providers, representative targets or user acceptance.
For genuinely non-product prose/policy edits, product acceptance can be not
applicable with static review evidence. A runtime skill, prompt, catalog or fixture
is not exempt merely because it is Markdown.

## Execute And Record

Actually run the selected commands. Record command, environment/context needed
to reproduce, outcome, and relevant counts/errors. Do not store credentials or
raw private logs. Map important acceptance criteria to tests or explicit manual
evidence. Report not-run checks and why, not invented passes.

Investigate failures. Distinguish observed baseline failures from patch-induced
failures only with evidence. Never disable tests or weaken acceptance merely to
get green. Missing dependencies, approvals, or network access are gaps to report
or resolve through host controls, not reasons to bypass them.

Reuse checks only when relevant source, locks, toolchain and configuration are
unchanged and identifiable. Do not relabel branch evidence as a main run. After a
relevant fix, retest the new main SHA and affected behavior; do not repeat every
unrelated suite. Structural validation alone is not behavioral acceptance.

## Exit And Handoff

Report passed, failed and unverified scope against the main candidate. Send clear
bugs directly to `$engineering-implement` with reproduction, expected/actual result
and evidence; involve design for contract ambiguity and the user for new business
decisions. Resolve disagreements on the requirement, not by negotiating a failure
into a pass. Never patch product code on main to pass a case.

Fixes return through a development branch, self-checks, `$engineering-review` and
authorized PR/main merge before independent main retest. Pass the acceptance
result and remaining gaps to `$engineering-deliver`. Materially missing validation
or failures block acceptance unless the user accepts the documented limitation;
they remain missing/failed. Merge, independent acceptance and release are distinct.
