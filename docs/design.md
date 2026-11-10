# Design And Implementation Plan

## Scope

Deliver an open-source, Codex-first bundle connecting HLD, LLD, design/plan
review, implementation, tests, code review, documentation, and a local Git commit.
It must work as plain instructions without a scheduler or workflow runtime.

This repository authors a standalone formulation of the existing local HLD/LLD
and review practices. It does not redistribute plugin code or the local delegated
agent wrappers. No private provider policy, credentials, or machine paths belong
in the package. English skill instructions and bilingual entry documentation are
maintained here as the authoritative sources for this bundle.

## Design

One coordinator loads seven focused skills. A skill owns its instructions; the
target project's code, tests, repository instructions, and approved design remain
the sources of truth for the target system. Existing user changes are not owned
by this workflow.

The user view is a single skill invocation or a focused stage invocation. The
logical view is a coordinator and seven Markdown stages. Deployment means copying
the eight directories into the host's skill search path; Python is only needed
for the optional installer and package checks. There is no runtime service or
new database. Durable state uses existing project documents/issues/PRs, or a small
repository change record. Resume by reading these records and current Git state,
not by assuming the previous stage succeeded.

| Stage | Consumes | Produces / Exit Condition |
| --- | --- | --- |
| Scope | User request, project instructions, code and Git state | Scope, acceptance criteria, proportionality decision |
| HLD | Scope and system baseline | Architecture decisions and verifiable boundaries |
| LLD | Settled HLD | Implementation contracts and requirement/test mapping |
| Closure | Design and separate implementation plan | Fixed findings, explicit decisions, fresh clean review |
| Implement | Agreed contracts and plan | Scoped patch and related tests |
| Test | Acceptance criteria and final patch | Commands, outcomes, gaps; rerun after relevant changes |
| Review | Final patch and test evidence | Severity-ordered findings; accepted findings repaired |
| Deliver | Reviewed patch and current evidence | Updated docs, durable record, scoped commit and final report |

Narrow fixes can replace HLD/LLD documents with a brief design note and plan.
Unresolved architecture decisions stop dependent implementation. Failed tests or
materially missing checks block claiming completion. A user can explicitly accept
a documented residual gap; this does not turn a skipped test into a pass.
Code fixes after review invalidate affected test evidence. Final documentation
edits are also checked before committing. Push and publication are separate,
explicitly authorized operations. Design-only requests stop after design.

## Implementation Plan

1. Author skills with concrete input/output and failure rules, without runtime code.
2. Add bilingual documentation, license, and an illustrative change record.
3. Add a no-overwrite installer, structural/link validator, and focused unit tests.
4. Run package validation, three design review rounds, and final patch review.
5. Commit only package assets, create the authorized public repository, push,
   and verify remote visibility and commit identity.

## Verification

Unit tests exercise clean install, dry run, collisions, invalid destinations,
and malformed bundles. CI checks supported Python versions on Linux and Windows.
The validator checks skill inventory, simple front matter, required lifecycle
handoffs, and local Markdown links. These are structural checks, not a general
Markdown parser or a proof that an agent obeys the workflow. A future real-project
trial should cover both a small fix and a cross-module change; live-agent
compatibility is not part of the initial acceptance claim.

Installation preflights all name collisions before writing. Copy-time I/O failure
is reported as failure and can leave a partial install; there is no automatic
rollback that might delete user files. Documentation explains manual inspection
and reconciliation. This is sufficient for a trusted, small local bundle without
adding an installation transaction engine.
