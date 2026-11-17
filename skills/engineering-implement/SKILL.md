---
name: engineering-implement
description: Implement an agreed engineering change using existing code patterns, preserving unrelated work and mapping requirements to focused tests. Use after scope and necessary design decisions are settled.
---

# Engineering Implement

## Inputs

Read repository instructions, current Git status/diff, agreed scope, acceptance
criteria, design contracts, and the separate plan. Inspect affected code and
tests before editing. For a small change, a concise design note is sufficient.
Do not treat a design-only request as permission to implement.

## Work

Use a development/fix branch from the intended baseline, not main as a staging
area. Name explicit PR dependencies instead of copying unmerged code into main.
Keep one coherent business flow and its review fixes on the same branch. Do not
create another worktree unless isolation or concurrency actually requires it.

Implement the smallest coherent change following existing frameworks, helpers,
and conventions. Preserve unrelated staged and unstaged work. Do not reset,
reformat broadly, add dependencies, or create abstractions without current need.

Validate unknown input at the responsible boundary; preserve required security,
data integrity, cleanup, and error propagation. Catch errors only where recovery,
translation, or useful boundary context is possible. Write or update tests for
changed behavior, including relevant failure cases, in proportion to blast radius.
Development owns these unit tests and applicable build/type/static self-checks;
they are not independent acceptance. Share the requirement-to-test mapping and
design contracts with testing early so its cases need not wait for the code.

Prioritize usable functionality. Do not defer blocking correctness, authorization,
truthful evidence, data integrity or necessary cleanup; schedule nonblocking DFX
separately without deleting agreed final requirements. Do not infer a test's
expected result merely from current implementation.

If the implementation contradicts the settled design or reveals a product
decision, update the design through its owner and review before continuing the
dependent work. Do not quietly expand scope. Use existing test/build tooling;
do not substitute a generic package command for the target project's tools.

External-agent delegation is optional and requires explicit user authorization.
Never bundle provider settings or use delegation to bypass host permissions.
The accepting agent remains responsible for inspecting the diff and test evidence.

## Handoff

Pass changed files/behavior, requirement-to-test mapping, actual checks already
run, and known gaps to `$engineering-deliver` for the scoped commit and authorized
PR, then `$engineering-review`. Give `$engineering-test` the same context for case
preparation, not branch acceptance. After an authorized merge, transfer the actual
main SHA to an independent acceptance owner who did not author this product code.
Resolve clear acceptance bugs on a fix branch through self-checks, review, PR/main
merge and independent main retest. Do not patch main to make a case pass or change
the expectation to conceal failure. Implementation alone is not completion.
