# Example Change Record

Illustrative template only. Replace placeholders with observed facts; do not
report the commands below as having run. Prefer an existing project record over
creating another parallel source of truth.

## Scope And Acceptance

- Request: <user-visible change>
- Baseline: <relevant code, current behavior, pre-existing changes>
- Acceptance: <observable success criteria>
- Out of scope: <explicit exclusions>
- Design size: <small note, or HLD/LLD locations and reason>

## Design And Plan

- Decisions: <boundaries and behavior; link existing design if present>
- Plan: <ordered implementation and verification steps>
- Review rounds: <actual findings, decisions, repairs, fresh final review>
- Open decisions: <none, or blocked decision and owner>

## Implementation And Verification

| Acceptance Criterion | Changed Artifact | Check | Observed Result |
| --- | --- | --- | --- |
| <criterion> | <file/interface> | <command or manual procedure> | <pass/fail/not run and reason> |

## Patch Review

- Scope reviewed: <diff against baseline and staged/unstaged coverage>
- Findings: <severity, file/line, impact, resolution>
- Rechecks after repairs: <actual commands and outcomes>
- Residual risk: <explicit limitations or user-accepted gaps>

## Delivery

- Documentation: <updated behavior/configuration/operational instructions>
- Final checks: <checks after final doc/code edits>
- Commit scope: <files included; unrelated work excluded>
- Commit: reported after commit creation, not embedded into that same commit.
- Push/publication: <not requested, or explicit authorization and observed result>
