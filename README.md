# Engineering Skills

A small, portable skill bundle for taking a usable functional change through
design, branch implementation, PR review, authorized integration, and independent
acceptance, with traceable documentation and Git records.

Start with `engineering-workflow`. It coordinates the other skills; it does not
install an agent runtime, prescribe a framework, or replace your project's tools.
Small fixes stay small. Cross-module changes get explicit design contracts.
Merge, independent acceptance, and release are separate outcomes.

[中文说明](README.zh-CN.md) | [Design](docs/design.md) | [Example](examples/change-record.md) | [Acceptance](docs/verification.md)

## Skills

| Skill | Responsibility |
| --- | --- |
| `engineering-workflow` | Select functional slices and coordinate roles, dependencies, and handoffs |
| `highlevel-design` | Define architecture, boundaries, and verification contracts |
| `lowlevel-design` | Specify implementation interfaces and HLD traceability |
| `design-plan-closure-review` | Review and repair designs and plans until closure |
| `engineering-implement` | Implement on a development branch, own unit tests/self-checks, and fix bugs |
| `engineering-test` | Prepare requirement/design-based cases early; independently accept actual main |
| `engineering-review` | Review the PR patch for bugs, regressions, and missing tests |
| `engineering-deliver` | Record evidence, commit scoped changes, and report delivery/acceptance state |

## Install For Codex

Requires Git and Python 3.10+. The skills themselves have no Python dependency.
Clone the repository, then install into a project's skill discovery directory:

```sh
git clone https://github.com/Logic70/engineering-skills.git
cd engineering-skills
python scripts/install.py --dest /path/to/project/.agents/skills --dry-run
python scripts/install.py --dest /path/to/project/.agents/skills
```

On Windows, pass a quoted Windows path to `--dest` instead. To install for your
Codex user, explicitly pass your `~/.codex/skills` directory (use its full path on
Windows). Restart your agent session if it does not rediscover skills immediately.

The installer copies only the eight skill directories. It never replaces an
existing skill: any name collision aborts before copying. Existing local versions
of `highlevel-design`, `lowlevel-design`, or `design-plan-closure-review` must be
reviewed and reconciled manually, or use a clean project installation. Project and
user installations can still shadow one another; check which version your agent
loads. There is no automatic updater or destructive uninstall command.

Permission or disk failures during copying return a failure and may leave a
partial installation. Inspect the destination and remove only files you confirm
belong to that failed attempt before retrying; the installer does not roll back
or delete user files.

Other agents can reuse these Markdown instructions if they support skill
discovery or explicit file loading. Automatic discovery outside Codex is not
claimed or tested. Follow the target agent's own installation instructions.

## Use

```text
Use $engineering-workflow to implement <change> in <repository>.
Follow the repository's instructions and keep unrelated changes untouched.
```

Invoke an individual skill for a narrower task, for example
`$engineering-test` or `$highlevel-design`. These are instruction skills, not
terminal commands. A request for design or review only does not authorize code
changes, commits, or publication.

Choose a small usable business flow, its real saved result or stage handoff, and
observable success evidence. Reuse completed foundations and update only affected
HLD/LLD. Functional progress comes first; defer nonblocking performance tuning,
extreme-case hardening, and compatibility work in the existing backlog without
removing agreed final requirements or acceptance scope. Necessary correctness,
authorization, truthful evidence, data integrity, cancellation, and cleanup remain
required.

Responsibilities are separate, not three copies of the same work:

| Role | Owns |
| --- | --- |
| Design | Affected HLD/LLD, interfaces, data handoffs, and design omissions/conflicts |
| Development | Branch implementation, unit tests, applicable self-checks, PRs, and product fixes |
| Testing | Early cases/data/automation from requirements and design; independent main acceptance and retest |
| Coordinator | Priority, dependencies, file ownership, permissions, evidence coverage, and reporting |

The acceptance owner must not author that feature's product code. Preparing its
acceptance cases or runners does not disqualify the testing owner. Assign roles
per feature; keep parallel work prerequisite-ready with explicit file ownership,
not a permanent agent for every role.

The normal delivery flow is:

```text
Functional scope -> affected design/plan closure
                 -> development branch + unit tests/self-checks -> commit/PR
                 -> code review + merge checks + authorization -> main merge
                 -> independent acceptance of identified actual main commit
Testing prepares requirement/design-based cases while development proceeds.
```

Create the PR after development self-checks, then review it before merge; a
completed PR review is not a prerequisite to creating the PR. Use the project's
authoritative integration branch, called main here. Testing runs a fixed actual
main SHA in a clean isolated checkout or exact source export, not a feature
branch, merge preview, or unmerged product overlay. Record that SHA and the
case/runner versions. Unit/mock results do not replace required real business-flow
and stage-handoff acceptance.

Clear implementation failures return directly to development with reproduction
and evidence. Design resolves requirement/contract ambiguity; new business choices
return to the user. Fixes follow branch -> self-checks -> PR/review -> authorized
main merge -> affected main retest. Clarification must not turn a demonstrated
failure into a pass. Pending post-merge acceptance cannot excuse a failing merge
check, and a merge alone does not mean acceptance or release.

Reuse existing project documents, issues/PRs, and test commands. A concise record
can cover a small change; do not invent a document hierarchy or tracking system.
Persist a repository record only when no existing durable place is available.
The [example](examples/change-record.md) separates development evidence, delivery,
and main acceptance; it is not evidence from an actual application run.

## Safety And Limits

- Repository instructions, user intent, and tool permissions take precedence.
  Preserve explicit pauses; a policy/documentation task does not resume paused
  product work or jobs. This bundle grants no merge, deployment, installation,
  service/account, production, or model/data-egress permission.
- Ordinary implementation requests include scoped local commits under this
  workflow, unless the user or repository prohibits them. Never push, publish,
  delegate, change architecture, or perform destructive Git operations implicitly.
- Do not claim verification or review rounds that were not performed. Report
  passed, failed, and unverified scope separately. Reuse supporting checks only
  when relevant source, locks, toolchain, and configuration are unchanged and
  identifiable; never relabel branch results as main acceptance. Missing checks
  remain missing, and a syntax check is not behavioral acceptance.
- Pure prose or collaboration-policy maintenance may mark product acceptance not
  applicable with static diff/link/consistency checks. Runtime prompts, product
  skills, catalog inputs, and fixtures are not exempt just because they use
  Markdown. Broaden regression for shared behavior or final integration, not
  every documentation edit.
- Never stage unrelated work, credentials, machine-specific configuration, or raw
  execution logs. Existing changes must be preserved.
- No provider credentials, scheduler, external coding agent, or workflow engine is
  bundled. This is not a copy of the WorkflowProgram plugin.

## Validate And Contribute

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```

These checks verify package structure, local Markdown links, key handoff rules,
and installer behavior. They do not prove an LLM follows instructions, replace
tests in a target project, or demonstrate a live Codex integration.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).
Released under the [MIT license](LICENSE). Initial release: `0.1.0`.
