---
name: highlevel-design
description: Create or review an HLD for substantial engineering changes, defining architecture boundaries, user and deployment views, runtime and data behavior, and verifiable quality contracts. Avoid a full HLD for a narrow local fix unless requested.
---

# High-Level Design

## Inputs

Read the request, repository instructions, existing architecture, implementation,
tests, configuration, and any prior design. Separate observed facts, assumptions,
proposals, and unresolved user decisions. Assess whether an HLD is proportionate.

## Design

Record the goal, baseline, constraints, in-scope and out-of-scope behavior, and
authoritative artifacts. Describe steady-state architecture, not task sequencing.

Cover these views:

- User: actors, workflows, visible outcomes, and failure experience.
- Logical: components, responsibilities, interfaces, ownership, dependency direction.
- Deployment: processes, hosts/services, configuration, trust and resource boundaries.
- Runtime: important requests/jobs, ordered interactions, state transitions, recovery.
- Data: source of truth, schemas, persistence, ownership, consistency, lifecycle.

Always cover user, logical, and deployment views. Assess runtime and data views;
mark either not applicable with a reason rather than inventing unnecessary state.
For each significant boundary state inputs, outputs, owner, failure behavior,
compatibility obligations, and verification. Do not add concepts just to fill a
template. Reuse the system's patterns and name alternatives only where decisions
have real tradeoffs.

Connect important reliability, security, performance, and operational claims to
a mechanism and check. Distinguish structural checks from integration checks and
observable behavior. Identify which documents/code are authoritative, supporting,
historical, or deprecated when there is potential conflict.

## Output And Handoff

Deliver an HLD in the project's existing documentation layout, explicit open
decisions, and a separate implementation/migration plan when requested. Use
`$design-plan-closure-review` to repair issues before handing off. Do not claim
approval merely because the author self-reviewed the design. Ask the user to
resolve decisions that change product scope or architecture beyond authorization.

Pass the settled HLD and remaining constraints to `$lowlevel-design`. For a
design-only request, stop here; do not edit production code or commit implicitly.
