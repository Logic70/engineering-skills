# Engineering Skills

A small, portable skill bundle for taking an engineering change from design to
implementation, verification, documentation, and a traceable Git commit.

Start with `engineering-workflow`. It coordinates the other skills; it does not
install an agent runtime, prescribe a framework, or replace your project's tools.
Small fixes stay small. Cross-module changes get explicit design contracts.

[中文说明](README.zh-CN.md) | [Design](docs/design.md) | [Example](examples/change-record.md) | [Acceptance](docs/verification.md)

## Skills

| Skill | Responsibility |
| --- | --- |
| `engineering-workflow` | Scope the change and coordinate the lifecycle |
| `highlevel-design` | Define architecture, boundaries, and verification contracts |
| `lowlevel-design` | Specify implementation interfaces and HLD traceability |
| `design-plan-closure-review` | Review and repair designs and plans until closure |
| `engineering-implement` | Implement the agreed change using existing patterns |
| `engineering-test` | Select and run risk-proportionate verification |
| `engineering-review` | Review the final patch for bugs, regressions, and missing tests |
| `engineering-deliver` | Update documentation, capture evidence, and commit scoped changes |

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

The normal sequence is:

```text
Scope -> HLD when warranted -> LLD when warranted -> design/plan closure
      -> implementation -> tests -> patch review -> docs/evidence -> Git commit
```

Each stage consumes the preceding stage's actual outputs. Reuse existing project
documents and test commands. For small changes, a concise change record can cover
scope, plan, evidence, and delivery; do not invent a full document hierarchy.
Evidence can use an existing issue/PR or repository document. Persist a repository
record when there is no existing durable place. The example is a template, not
test evidence from an actual application run.

## Safety And Limits

- Repository instructions, user intent, and tool permissions take precedence.
- Ordinary implementation requests include scoped local commits under this
  workflow, unless the user or repository prohibits them. Never push, publish,
  delegate, change architecture, or perform destructive Git operations implicitly.
- Do not claim verification or review rounds that were not performed. Skipped or
  unavailable checks must remain visible. Materially missing validation blocks a
  completion claim; passing a syntax check is not behavioral acceptance.
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
