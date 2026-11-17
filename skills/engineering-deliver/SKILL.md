---
name: engineering-deliver
description: Record and commit a coherent self-checked change, support authorized PR review and main merge, and hand off independent acceptance with truthful status. Use for scoped delivery, not implicit push, merge or release permission.
---

# Engineering Deliver

## Reconcile The Result

Read the user request, repository instructions, accepted design, final patch,
development evidence, and available review findings. Resolve blockers before
claiming completion. A commit or open PR can precede review; authorized main merge
requires completed review and applicable passing merge checks.
Document a user-accepted limitation accurately; never relabel a failed/skipped
check as passed. Design-only and review-only requests do not authorize a commit.

Update affected user/API/configuration/deployment documentation using existing
locations. Keep the implemented code and design consistent. Persist scope,
decisions, actual commands/outcomes, review resolutions, and residual gaps in an
existing issue/PR or repository record. If none exists, add a concise change
record following project conventions. Avoid redundant status files and raw logs.

Inspect documentation changes and run relevant final checks after all edits.
Code or contract changes require affected tests and review again. Check the diff
for accidental private paths, credentials, generated noise, and unrelated edits.

## Commit Only The Intended Change

A normal implementation request under this workflow includes a local commit
unless the user or repository says otherwise. Inspect Git status, staged diff,
unstaged diff, and newly added files before staging. Never use blanket staging in
a dirty worktree. Stage only intended paths/hunks and inspect the staged diff.
Do not include another person's staged work. If the index already contains
unrelated changes or the same file mixes ownership that cannot be separated
safely, ask how to proceed; do not silently unstage or overwrite their work.

Create a focused commit using the repository's message convention (Conventional
Commits if none exists). Respect hooks; if they modify files, inspect and recheck
before committing. Never bypass hooks, amend earlier work, force-push, or reset
without explicit authorization. If identity or repository setup is missing,
report it rather than silently changing Git configuration or initializing a repo.

After committing, verify the commit contents, capture its ID, and inspect status
to identify remaining unrelated changes. Report the ID in the final response or
existing external record; do not create recursive commits just to embed a commit's
own hash in its contents. If commit creation fails, preserve work and report the
delivery gap. Do not call delivery complete without the requested commit.

## Authorized PR And Main Handoff

Push, merge and release require applicable user authorization and host controls;
this skill does not grant them. For authorized integration, push the development
branch and open a coherent PR with business scope, affected design, acceptance
cases, actual self-checks, limitations and post-merge handoff. Do not push product
changes directly to main. An open PR is not merged; missing CI is not passing CI.

After `$engineering-review` and required checks pass, merge only the reviewed
candidate through the normal authorized PR process. Verify the actual merge and
main SHA. Update only a clean available local main by fast-forward; preserve active
worktrees and consumers. Remote backup is not approval, acceptance or release.

Transfer main SHA, case/runner versions and known gaps to the independent owner
using `$engineering-test`. Pending main acceptance does not prevent describing a
successful merge, but must not be described as passed. Acceptance bugs go back to
development for branch/self-check/review/PR/main/retest, never patches on main.
For genuinely non-product prose/policy changes, record why product acceptance is
not applicable and the static checks used; runtime prompts/skills are not exempt
by extension alone. Follow existing evidence housekeeping without inventing a
new product stage; retain source/failures when archiving fails, never fake a pass.

## Final Report

Summarize the usable outcome, documentation/record locations, actual self-checks
and review, commit/PR/merge state, independent main acceptance and limitations.
Keep merge, acceptance and release separate. Push or public publication
is a separate step requiring explicit user authorization and normal host approval.
When authorized, verify the remote branch/commit and visibility before claiming
publication succeeded. Local success is not evidence of remote publication.
