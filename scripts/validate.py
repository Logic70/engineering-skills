"""Check this instruction bundle without third-party dependencies."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


SKILLS = (
    "engineering-workflow",
    "highlevel-design",
    "lowlevel-design",
    "design-plan-closure-review",
    "engineering-implement",
    "engineering-test",
    "engineering-review",
    "engineering-deliver",
)
ROOT = Path(__file__).resolve().parents[1]


def validate_skills(source: Path) -> list[str]:
    errors = []
    if not source.is_dir():
        return [f"Missing skills directory: {source}"]
    actual = {path.name for path in source.iterdir() if path.is_dir()}
    if actual != set(SKILLS):
        errors.append(f"Skill inventory mismatch: {sorted(actual)}")
    for name in SKILLS:
        path = source / name / "SKILL.md"
        if not path.is_file():
            errors.append(f"Missing skill: {name}")
            continue
        content = path.read_text(encoding="utf-8")
        # This package intentionally uses only two plain front-matter fields.
        header = re.match(
            r"\A---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n",
            content,
        )
        if not header or header.group(1) != name:
            errors.append(f"Invalid front matter: {name}")
        elif len(header.group(2).strip()) < 30:
            errors.append(f"Description is not informative: {name}")
        if not re.search(r"^# \S", content, re.MULTILINE):
            errors.append(f"Missing title: {name}")
        for reference in re.findall(r"\$([a-z][a-z0-9-]+)", content):
            if reference not in SKILLS:
                errors.append(f"Unknown skill reference in {name}: {reference}")
    coordinator = source / "engineering-workflow" / "SKILL.md"
    if coordinator.is_file():
        content = coordinator.read_text(encoding="utf-8")
        for name in SKILLS[1:]:
            if f"${name}" not in content:
                errors.append(f"Coordinator missing handoff: {name}")
    return errors


def validate_links(root: Path) -> list[str]:
    errors = []
    for path in root.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        content = path.read_text(encoding="utf-8")
        # Covers the simple inline links used here, not arbitrary Markdown syntax.
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", content):
            parsed = urlsplit(target)
            if parsed.scheme in {"https", "http", "mailto"}:
                continue
            if parsed.scheme or parsed.netloc or target.startswith(("/", "\\")):
                errors.append(f"Nonportable link in {path.relative_to(root)}: {target}")
                continue
            if not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(root.resolve()) or not destination.exists():
                errors.append(f"Broken local link in {path.relative_to(root)}: {target}")
    return errors


def validate_bundle(root: Path) -> list[str]:
    errors = validate_skills(root / "skills")
    for name in (
        "README.md", "README.zh-CN.md", "LICENSE", "CONTRIBUTING.md",
        "SECURITY.md", "docs/design.md", "examples/change-record.md",
    ):
        if not (root / name).is_file():
            errors.append(f"Missing package document: {name}")
    errors.extend(validate_links(root))
    return errors


def main() -> int:
    errors = validate_bundle(ROOT)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(SKILLS)} skills, package documents, and local links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
