# Contributing

Keep the bundle small, project-neutral, and usable without a runtime dependency.
Do not add lifecycle concepts or configuration unless a concrete use case needs
them. Reuse project instructions rather than prescribing a build system.

For a change, explain the problem, update the relevant skills and documentation,
and run:

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```

Include tests when changing installation or validation behavior. Review the
handoffs as well as each individual skill. Report actual evidence and any missing
live-agent checks. Do not commit secrets, user-specific paths, or machine logs.
Use a focused commit and a pull request with scope and verification results.

Skill names are discovery identifiers. Renaming one requires updating the
installer list, coordinator, documentation, and validator expectations together.
