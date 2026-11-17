# Initial Acceptance Record

Date: 2026-11-09. Scope: the standalone `0.1.0` bundle, installer, validator,
documentation, and CI definition. The workspace initially contained no project
files or Git repository. This release does not modify or install over the user's
existing global skills.

## Design And Plan Review

Three serial self-review rounds were performed; no independent agent review is
claimed. Each round considered goal fidelity, stage handoffs, evidence flow,
compatibility, ownership, failures, verification, operations, and ordering.

| Round | Findings / Decision | Repair And Check |
| --- | --- | --- |
| 1 | Accept: copy-time failures needed an explicit partial-install recovery contract, not just collision protection. | Documented failure propagation and manual inspection in both READMEs and the design; tested that copy errors propagate. No automatic deletion/rollback added. |
| 2 | Accept: acceptance coverage needed a real CLI install and explicit-destination failure check, beyond function calls and dry run. | Added CLI installation, missing-destination, short-description and missing-title tests; installed output validates and command failures remain nonzero. |
| 3 | Fresh full review found no new actionable design/plan issue. | Rechecked scope, source ownership, all skill handoffs, stale-test rules, dirty-index safeguards, bilingual installation guidance, code, tests, and CI definition. |

No accepted findings remain open. Design describes the final instruction bundle;
the separate plan in the design document describes implementation/publication
order. Rejected findings: none. Deferred feature additions: none required for the
initial scope.

## Observed Local Verification

Environment: Windows, Python 3.13.5.

| Check | Observed Result |
| --- | --- |
| `python scripts/validate.py` | Passed: eight skills, package documents, local links |
| `python -m unittest discover -s tests -v` | Passed: 22 tests |
| Installation smoke | CLI copied all eight skills into a temporary project discovery directory and the copied skills validated |
| Failure behavior | Collisions, invalid source/destination, overlap, missing arguments and copy failure covered by tests |
| Privacy pattern check | No local account paths, configured personal email, common token patterns or private key headers found in package files |

The privacy pattern check is not a comprehensive security audit. Final staged
content and whitespace are inspected before commit; the resulting commit ID is
reported after creation, not embedded in this same record.

## Limits And Publication

At initial local acceptance, hosted CI had not yet run. On 2026-11-10, the
[first hosted run](https://github.com/Logic70/engineering-skills/actions/runs/42768424919)
passed all four Linux/Windows and Python 3.10/3.13 combinations. That run exposed
deprecated Node runtime warnings from the original action versions. Before
tagging, the workflow was updated to the verified official v7 action lines for
[checkout](https://github.com/actions/checkout) and
[setup-python](https://github.com/actions/setup-python); this follow-up requires
another hosted run. Consult GitHub Actions for its actual result.

No live Codex session discovery or target application end-to-end trial
is claimed. Other-agent automatic discovery and behavioral compliance are also
unverified. The example change record is illustrative, not application evidence.

Public GitHub creation and push are explicitly authorized by the user. Remote
visibility and commit identity must be checked after push. A local commit or this
document alone is not evidence of successful remote publication.

## 2026-11-17 Workflow Revision

Scope: reconcile the existing eight skills with feature-first design, development
and independent testing responsibilities. No ninth skill, installer change,
dependency, runtime, service or target-application change is included. Existing
main baseline: `55c71a07e591d349089e1e1ade71f9759cf7008a`.

The revised handoff is affected HLD/LLD plus early independent test preparation,
development-branch implementation/unit/self-checks, commit and authorized PR,
review and authorized main merge, then independent actual-main acceptance.
Acceptance defects return through a fix branch, self-checks, review, PR/main and
main retest. Merge, acceptance and release are separate outcomes. Functional
delivery takes priority over nonblocking DFX without discarding final scope or
mandatory correctness, authorization, data integrity and truthful evidence.

| Review | Observed Finding And Resolution |
| --- | --- |
| 1: scope and handoffs | Accepted: the old coordinator treated testing as a late branch-verification stage, HLD/LLD did not hand criteria to early independent test planning, and closure did not distinguish optional design-review assistance from acceptance independence. Updated those handoffs and related implementation/review/delivery contracts. |
| 2: eight-skill scenarios | An independent read-only reviewer found no new actionable behavioral issue across small/large changes, PR review fixes, authorization gates, main identity, defect retest, missing evidence and paused/design-only scopes. This was instruction review, not a target-application run. |
| 3: fresh full review | Independent read-only review of all eight skills, bilingual entries, design/plan, example and this record found no new actionable issue. Early planning, role independence, PR/main gates, defect feedback, evidence reuse and historical claims are consistent; no accepted finding remains open. |

Observed development verification on Windows, Python 3.13.5:

- `python -B scripts/validate.py`: passed, eight skills and local package links.
- `python -B -m unittest discover -s tests -v`: all 22 tests passed, including
  no-overwrite installation and validation behavior. Installer, validator and
  test code are unchanged; these checks do not prove instruction compliance.
- After the affected documentation updates, `python -B scripts/validate.py` and
  `git diff --check` passed again. No installer, validator or test-code change.
- A limited pattern scan found no machine-specific account paths, private-key
  headers, common GitHub token prefix or target-project name in the revised
  package documentation/skills; this is not a comprehensive security audit.

Hosted checks, actual merge and independent main verification are pending at
this branch record; their observed state belongs in the PR record, not an
invented pass here. This revision does not
claim a real target-project trial, live agent discovery, or new cross-platform
execution from these local checks. No blanket product-acceptance exemption is
claimed merely because the deliverable uses Markdown.
