---
name: lowlevel-design
description: Translate a settled HLD into implementation-ready files, interfaces, schemas, runtime behavior, error handling, and requirement-to-test traceability. Use for substantial changes after architecture boundaries are decided.
---

# Low-Level Design

## Inputs

Read the authoritative HLD, actual code/tests/configuration, and existing detailed
design. Identify settled decisions and unresolved constraints. If implementing
would change an HLD boundary, return that decision to the design owner rather
than silently introducing architecture. A small fix can use a brief design note
instead of this full stage.

## Specify The Implementation

Define only the surfaces needed by the change:

- Files/modules to add or change, their responsibility and dependency direction.
- Public and internal interfaces, inputs, outputs, validation ownership.
- Data/schema changes, invariants, state transitions, and compatibility.
- Ordered runtime steps, preconditions, errors, and resource cleanup.
- Retry, concurrency, idempotency, recovery, and rollback only where applicable.
- Configuration, deployment, observability, and security boundaries where relevant.

Validate unknown input at its owning boundary. Preserve established internal
contracts without redundant checks. Avoid single-use abstractions, hypothetical
fallbacks, and speculative concurrency machinery. Obtain a user decision before
expanding scope for optional robustness without a concrete failure case.

Create a concise mapping:

| Requirement / HLD Decision | File Or Module | Interface / Invariant | Test Or Evidence |
| --- | --- | --- | --- |
| Actual requirement | Actual artifact | Verifiable contract | Concrete check |

Keep task order, rollout phases, temporary bridges, and removal sequencing in a
separate implementation/migration plan, not in the steady-state design.

## Output And Handoff

Deliver implementation contracts, HLD traceability, open decisions, and the
separate plan. Run `$design-plan-closure-review`. Hand settled artifacts and
acceptance criteria to `$engineering-implement`; unresolved blocking decisions
stop implementation. A request only for the LLD stops after the design output.
