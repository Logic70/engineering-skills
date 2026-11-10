---
name: engineering-review
description: Review an engineering patch for concrete bugs, regressions, security and performance risks, and missing tests before delivery. Use for final code review or a standalone review-only request.
---

# Engineering Review

Read scope, design contracts, baseline, actual staged and unstaged changes, and
test evidence. Include newly added files that ordinary git diff omits. Inspect
surrounding callers and tests for affected contracts. Do not confuse unrelated
pre-existing work with the patch under review.

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
current test evidence, and residual risk to `$engineering-deliver`.
