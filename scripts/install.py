"""Copy the complete skill bundle to an explicitly chosen discovery directory."""

import argparse
import shutil
import sys
from pathlib import Path

from validate import ROOT, SKILLS, validate_skills


def install_bundle(source: Path, destination: Path, *, dry_run: bool = False) -> list[Path]:
    source = source.expanduser().resolve()
    destination = destination.expanduser().resolve()
    errors = validate_skills(source)
    if errors:
        raise ValueError("Invalid source bundle:\n" + "\n".join(errors))
    if destination.is_relative_to(source) or source.is_relative_to(destination):
        raise ValueError("Destination must not overlap the source skills directory.")
    if destination.exists() and not destination.is_dir():
        raise ValueError("Destination must be a directory.")
    targets = [destination / name for name in SKILLS]
    collisions = [path.name for path in targets if path.exists() or path.is_symlink()]
    if collisions:
        raise FileExistsError("No files copied; existing skills: " + ", ".join(collisions))
    if not dry_run:
        destination.mkdir(parents=True, exist_ok=True)
        for name, target in zip(SKILLS, targets):
            shutil.copytree(source / name, target)
    return targets


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", required=True, type=Path, help="Explicit skill discovery directory")
    parser.add_argument("--dry-run", action="store_true", help="Check and print without writing")
    args = parser.parse_args()
    try:
        targets = install_bundle(ROOT / "skills", args.dest, dry_run=args.dry_run)
    except (OSError, ValueError) as error:
        print(f"Install failed: {error}", file=sys.stderr)
        print("A copy failure may leave a partial installation; inspect before retrying.", file=sys.stderr)
        return 1
    action = "Would install" if args.dry_run else "Installed"
    for target in targets:
        print(f"{action}: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
