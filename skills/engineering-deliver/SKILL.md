---
name: engineering-deliver
description: Finish an implemented and reviewed engineering change by updating documentation, persisting verification evidence, and creating a scoped local Git commit. Use for delivery, not implicit push or publication.
---

# Engineering Deliver

## Reconcile The Result

Read the user request, repository instructions, accepted design, final patch,
test evidence, and review findings. Resolve blockers before claiming completion.
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

## Final Report

Summarize changed behavior, documentation/record locations, actual checks and
review outcome, residual limitations, and commit ID. Push or public publication
is a separate step requiring explicit user authorization and normal host approval.
When authorized, verify the remote branch/commit and visibility before claiming
publication succeeded. Local success is not evidence of remote publication.
