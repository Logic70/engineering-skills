---
name: engineering-review
description: Review an engineering patch for concrete bugs, regressions, security and performance risks, and missing tests before delivery. Use for final code review or a standalone review-only request.
---

# Engineering Review

Read scope, design contracts, baseline, actual staged and unstaged changes, and
test evidence. Include newly added files that ordinary git diff omits. Inspect
surrounding callers and tests for affected contracts. Do not confuse unrelated
pre-existing work with the patch under review.
For a PR, inspect its actual base/head and complete diff, not only local edits.
Review follows development self-checks and may follow PR creation; it precedes
authorized main merge. Development unit/self-check evidence is distinct from the
independent acceptance that follows the actual main merge.

Prioritize concrete correctness defects, behavioral regressions, trust boundary
failures, data integrity, resource handling, material performance changes, and
missing tests. Avoid speculative hardening and style churn. Broaden security
review only when the requested scope or concrete risk warrants it.

Report findings first, sorted by severity, with file/line, failure scenario,
impact, and evidence. Follow with open questions, assumptions, and a short summary.
If no issues are found, say so and still identify verification gaps. Never imply
that no findings proves absence of bugs.

For the implementation workflow, repair accepted findings within scope, rerun
affected tests, and review the resulting patch again. Block delivery for unresolved
material issues. A standalone review-only request reports findings without editing
or committing unless asked. Independent or parallel agents require authorization;
do not represent self-review as an external approval.

Hand the final reviewed patch, actual review coverage, finding resolutions,
current test evidence, and residual risk to `$engineering-deliver` for authorized
merge and main acceptance handoff. Do not require post-merge acceptance before
the merge, or move a known failing development/required merge check into pending
acceptance to bypass it. Code review alone is not independent acceptance or release.
