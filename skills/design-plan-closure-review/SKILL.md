---
name: design-plan-closure-review
description: Review and repair engineering designs and implementation or migration plans until accepted findings are fixed and a fresh full review finds no new actionable issue. Use when drafting or materially revising design and planning artifacts.
---

# Design And Plan Closure Review

Read the goal, scope, existing system truth, design, and separate implementation
plan. Review the actual artifacts, not an imagined ideal system. Do not require
large documents for small changes.

## Review Loop

Perform at least three actual review rounds by default. Inspect goal fidelity,
lifecycle and handoffs, information flow, compatibility, boundary ownership,
failure behavior, testability, operations, and implementation ordering.
For a full engineering lifecycle, check early requirement-based test preparation,
development branch unit/self-checks, PR review and authorized merge, then independent
acceptance of an identified actual main commit. Check that bugs return through a
fix branch, self-check, review, PR/main merge and main retest, not patches on main.

For each finding record the issue, impact, decision, and repair/evidence:

- `accept`: repair the design or plan now, then check the repair.
- `reject`: explain why it does not apply or is not justified.
- `defer`: identify a bounded out-of-scope follow-up and residual impact.
- `ask_user`: identify the decision needed; block dependent work until resolved.

Repair accepted findings between rounds. Keep reviewing beyond three rounds if
new actionable issues appear. A deferred issue cannot hide a blocking design
contradiction. Independent design-review agents are optional and require
authorization; serial self-review is valid and must not be described as independent
review. This does not waive the full workflow's independent acceptance owner,
who must not have authored that feature's product code.

## Exit

Stop only when accepted findings are fixed, decisions required for subsequent
work are resolved, the design agrees with the plan, and a fresh full review finds
no new actionable issue. Do not claim that a review ran just to satisfy a count.

Persist a concise summary of actual rounds, finding dispositions, design/plan
changes, and residual assumptions in the existing record. If a decision remains
blocked, report an incomplete review rather than manufacturing closure.
