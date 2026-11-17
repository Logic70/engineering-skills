# Design And Implementation Plan

## Scope

Maintain an open-source, Codex-first bundle connecting affected HLD/LLD,
design/plan review, branch implementation, PR review, authorized integration,
independent main acceptance, and traceable documentation/Git records. Integrate
the feature-first collaboration policy into the existing eight skills, not a
ninth coordinator, tracking system, scheduler, or workflow runtime.

This repository authors a standalone formulation of HLD/LLD and review practices.
It does not redistribute plugin code or delegated-agent wrappers. No private
provider policy, credentials, or machine paths belong in the package. English
skill instructions and bilingual entry documentation are authoritative here.

## Design

One coordinator loads seven focused skills. The target project's requirements,
code, tests, repository rules, and approved design remain its sources of truth.
Existing user changes are not owned by this workflow. The user view is a single
skill invocation or a focused task invocation; the logical view is eight Markdown
skills, not a mandatory linear sequence of agents.

Deployment copies the eight directories into the host's skill search path.
Python is only needed for the optional installer and package checks; there is no
runtime service or database. Durable state uses existing project documents,
issues/PRs, or a concise repository change record. Resume from these records and
current Git state, not assumptions about prior success. The authoritative
integration branch is called main below; retain its actual project name.

### Functional Scope And Responsibilities

Select a small usable business flow, its real saved result or stage handoff, and
observable completion evidence. Reuse completed foundations and update only
affected HLD/LLD. If the flow cannot run independently under existing contracts,
design identifies the smallest legitimate integration scope instead of bypassing
constraints or indefinitely extending unrelated foundations.

Prioritize functionality. Necessary correctness, authorization, truthful evidence,
data integrity, cancellation, and cleanup remain required. Defer nonblocking
performance tuning, extreme-case hardening, and compatibility work in the existing
backlog without removing agreed final requirements or acceptance scope.

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Design | Affected requirement-aligned HLD/LLD, interfaces, data handoffs, constraints, and omissions/conflicts | No repeated whole-system redesign or front-loaded nonblocking DFX |
| Development | Branch implementation, unit tests, self-checks, PRs, and product fixes | Self-checks are not independent acceptance |
| Testing | Early requirement/design-based cases/data/automation, main acceptance, and fix verification | No product edits to make tests pass or expectations copied merely from code |
| Coordinator | Scope, priority, dependencies, file ownership, permissions, evidence coverage, and reporting | Does not routinely duplicate all roles or rerun unchanged valid checks |

Assign roles per feature. The independent acceptance owner cannot author its
product code; authoring acceptance cases/runners is compatible with testing
ownership. Delegation identifies role, functional slice, base, allowed files, and
expected output. Parallelize prerequisite-ready work with explicit ownership,
not a permanent agent for every role. Narrow fixes can use a brief design note
and plan instead of full HLD/LLD. Unresolved design decisions block dependent work.

### Handoffs And Feedback

| Handoff | Consumes | Produces / Exit Condition |
| --- | --- | --- |
| Scope and design | Request, rules, baseline, requirements | Functional outcome, affected design/plan, verifiable contracts |
| Early test preparation | Requirements, design, real handoffs | Cases/data/automation while development proceeds; no branch acceptance claim |
| Development | Settled contracts and plan | Branch patch, unit tests, self-check evidence, scoped commit and PR |
| PR review and integration | Actual PR patch, evidence, applicable checks | Findings repaired/rechecked, authorized main merge, identified resulting SHA |
| Independent acceptance | Actual fixed main SHA, cases and runner versions | Real-flow/handoff evidence; passed, failed, and unverified scope |
| Defect feedback | Reproduction, expected/actual result, evidence | Clear bugs to development; contract ambiguity to design; new business choice to user |
| Fix and retest | Defect scope and affected behavior | Fix branch/self-checks/PR/review/authorized main merge, then affected main retest |
| Delivery record | Source identities, review, checks, acceptance and authorization state | Updated docs, Git/PR records, distinct merge/acceptance/release status |

Create the PR after development self-checks, then review it before merge;
completed PR review is not a prerequisite for creating the PR. Applicable merge
checks and actual authorization remain required. Pending post-merge acceptance is
not a failed pre-merge check, but cannot be used to bypass a known failing merge
check.

Testing runs an identified actual main commit in a clean isolated checkout or
exact source export, not a feature branch, PR merge preview, or unmerged product
overlay. Record product SHA and case/runner versions. Start with the real user
flow and stage handoffs, then necessary correctness/safety and impact-based
regression. Unit/mock results do not replace required real tools, providers,
targets, or user-flow acceptance.

Clear bugs return directly to development. Design joins requirement/contract
ambiguity; the user resolves new business choices. Clarification identifies the
correct expectation, not a way to negotiate a demonstrated failure into a pass.
Recheck the defect and affected behavior, not every unrelated suite. Prioritize
regressions breaking main without stopping independent work unnecessarily,
resetting history, or assuming a data migration can be reversed.

### Evidence And Permissions

Report failures, skipped checks, unverified behavior, and user-accepted residual
gaps truthfully; none becomes a pass. Reuse supporting results only when relevant
source, locks, toolchain, and configuration are unchanged and identifiable. Never
relabel branch results as main acceptance. Check final documentation edits before
committing. Merge, independent acceptance, and release are distinct; one accepted
feature does not complete the project or authorize deployment.

Preserve repository rules, user intent, host controls, and explicit pauses. A
policy/documentation task does not resume paused product work. These skills grant
no merge, deployment, installation, service/account, production, or model/data-egress
authority. Normal implementation includes a scoped local commit unless prohibited;
push, publication, external delegation, and destructive operations still require
applicable authorization. Design/review-only requests stop at the requested output.

## Implementation Plan

1. Update the existing coordinator, implementation, test, review, and delivery
   handoffs. Preserve the HLD/LLD models, development tests, and focused reviewer.
2. Reconcile bilingual entry documentation, this affected design, and the example
   record. Keep development evidence, delivery, and main acceptance identifiable.
   Do not change inventory, installation, scripts, or introduce a runtime.
3. Perform actual design/plan closure and scoped patch reviews; run the package
   validator and unit tests. Record observed results and limitations in the
   existing verification record, not raw private logs.
4. Commit the intended branch changes. Push/create a PR only under the task's
   authorization, verify the remote identity, and report check/review/merge state
   without claiming unperformed project acceptance.

## Verification

Unit tests exercise clean install, dry run, collisions, invalid destinations, and
malformed bundles. CI checks supported Python versions on Linux and Windows. The
validator checks inventory, front matter, handoffs, and local Markdown links. It
is not a general Markdown parser or proof an agent follows the workflow.

This policy update is not a real-project acceptance run. A future trial should
cover a small fix, a cross-module flow, early independent case preparation,
actual-main source identity, and a defect's PR/main retest cycle. Claim no such
trial or cross-agent/platform compatibility without observed evidence.

Pure prose/collaboration-policy maintenance may mark product acceptance not
applicable with static diff/link/consistency review. Runtime prompts, product
skills, catalog inputs, and fixtures are not exempt merely because they use
Markdown. The bundle's package checks remain applicable here. Broaden target
regression for shared behavior or final integration, not every prose edit.
Evidence archiving follows the target's existing rules: closeout, not a new
product stage or proof of correctness. Preserve source/failure evidence when
archiving fails; uncertain evidence cannot justify a pass.

Installation preflights name collisions before writing. Copy-time I/O failure is
reported and may leave a partial install; automatic rollback could delete user
files, so documentation requires manual inspection/reconciliation. This preserves
the small trusted bundle without adding an installation transaction engine.
