# Example Change Record

Illustrative template only. Replace placeholders with observed facts; do not
report the commands below as having run. Prefer an existing project record over
creating another parallel source of truth.

## Functional Scope

- Request: <small usable business flow and user-visible outcome>
- Saved result / stage handoff: <real artifact or downstream result>
- Baseline: <integration branch, base SHA, current behavior, pre-existing changes>
- Acceptance: <requirement/design-based observable success criteria>
- Out of scope: <explicit exclusions>
- Deferred nonblocking work: <existing backlog references; agreed final scope preserved>
- Design size: <small note, or HLD/LLD locations and reason>

## Ownership, Design And Plan

- Design owner: <affected design, interfaces, data handoffs, omissions/conflicts>
- Development owner: <product files, unit tests/self-checks, branch, PR, fixes>
- Independent testing owner: <cases/runners; not a product-code author for this feature>
- Coordination: <priority, dependencies, base, allowed files, permissions, evidence coverage>
- Decisions: <boundaries and behavior; link existing design if present>
- Plan: <design/test preparation, branch implementation/self-checks, PR/review, authorized main merge, main acceptance>
- Review rounds: <actual findings, decisions, repairs, fresh final review>
- Open decisions: <none, or blocked decision and owner>
- Authorization / pauses: <explicit limits; this record grants no permission or resumption>

## Early Acceptance Preparation

- Requirement/design references: <authoritative sources; not expectations copied from code>
- Cases/data/automation: <versions and expected results prepared during development>
- Required real environment: <tools/providers/targets/user flow and stage handoffs>
- Prerequisites / unverified scope: <dependencies, access, decisions, owner>
- Status: preparation only, not acceptance of development-branch code.

## Development Evidence

- Development branch / candidate SHA: <identified branch and commit>
- Requirement-to-artifact mapping: <changed product behavior, files, unit tests>

| Criterion / Contract | Changed Artifact | Unit Test / Self-Check | Observed Result |
| --- | --- | --- | --- |
| <criterion> | <file/interface> | <command or manual procedure> | <pass/fail/not run and reason> |

- Supporting-result reuse: <original candidate/scope and unchanged source, locks, toolchain/configuration; or none>
- Limitation: development self-checks do not establish independent main acceptance.

## PR Review And Delivery

- Scope reviewed: <diff against baseline and staged/unstaged coverage>
- Findings: <severity, file/line, impact, resolution>
- Rechecks after repairs: <actual commands and outcomes>
- Residual risk: <explicit limitations or user-accepted gaps>

- Documentation: <updated behavior/configuration/operational instructions>
- Final checks: <checks after final doc/code edits>
- Commit scope: <files included; unrelated work excluded>
- Commit: reported after commit creation, not embedded into that same commit.
- Push / PR: <not authorized, or observed remote branch/commit and PR URL>
- Review / merge checks: <actual checks, failures, missing checks, review status>
- Merge authorization / result: <pending, or actual authorization and resulting main SHA>
- Main acceptance handoff: <test owner, actual main identity, cases/runners, prerequisites>
- Status: <local only / PR open / merged; neither PR creation nor merge proves acceptance or release>

## Independent Main Acceptance

- Source: <authoritative integration branch and fixed actual main SHA>
- Isolation: <clean checkout or exact source export; no feature branch, merge preview, or unmerged product overlay>
- Test owner / case and runner versions: <identity and traceable versions>

| Acceptance Criterion | Real Flow / Handoff Check | Observed Result | Evidence Reference |
| --- | --- | --- | --- |
| <criterion> | <actual command or manual procedure> | <pass/fail/unverified and reason> | <durable record; no raw private logs> |

- Passed scope: <observed outcomes and necessary safety/regression checks>
- Failed / unverified scope: <failures, unavailable checks, residual gaps and owners>
- Pure policy/prose only: <product acceptance N/A reason and actual static checks, if applicable; Markdown alone does not exempt runtime prompts/skills/fixtures>
- Acceptance / release: <independent acceptance state; release/deployment authorization is separate>

## Defect Feedback And Retest

- Defect: <reproduction, requirement/design expectation, actual behavior, evidence>
- Route: <clear bug to development; contract ambiguity to design; new business choice to user>
- Fix delivery: <fix branch/candidate, self-checks, PR/review, checks, merge authorization and main SHA>
- Retest: <actual fixed main SHA, case/runner versions, defect and affected-behavior results>
- Remaining scope: <failures/unverified behavior; no expectation change merely to turn failure green>
