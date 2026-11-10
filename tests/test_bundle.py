import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from install import install_bundle
from validate import SKILLS, validate_bundle, validate_links, validate_skills


class BundleTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "source"
        shutil.copytree(ROOT / "skills", self.source)
        self.destination = self.root / "project" / ".agents" / "skills"

    def test_repository_validates(self):
        self.assertEqual(validate_bundle(ROOT), [])

    def test_clean_install_has_identical_contents(self):
        targets = install_bundle(self.source, self.destination)
        self.assertEqual(len(targets), 8)
        for name in SKILLS:
            self.assertEqual(
                (self.source / name / "SKILL.md").read_bytes(),
                (self.destination / name / "SKILL.md").read_bytes(),
            )

    def test_dry_run_does_not_create_destination(self):
        self.assertEqual(len(install_bundle(self.source, self.destination, dry_run=True)), 8)
        self.assertFalse(self.destination.parent.exists())

    def test_collision_checks_all_targets_before_copying(self):
        existing = self.destination / SKILLS[-1]
        existing.mkdir(parents=True)
        sentinel = existing / "keep.txt"
        sentinel.write_text("user data", encoding="utf-8")
        for dry_run in (True, False):
            with self.assertRaises(FileExistsError):
                install_bundle(self.source, self.destination, dry_run=dry_run)
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "user data")
        self.assertEqual(list(self.destination.iterdir()), [existing])

    def test_existing_file_is_a_skill_collision(self):
        self.destination.mkdir(parents=True)
        (self.destination / SKILLS[0]).write_text("keep", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            install_bundle(self.source, self.destination)

    def test_destination_file_rejected(self):
        target = self.root / "file"
        target.write_text("keep", encoding="utf-8")
        with self.assertRaises(ValueError):
            install_bundle(self.source, target)

    def test_source_overlap_rejected(self):
        for destination in (self.source, self.source / "nested", self.root):
            with self.subTest(destination=destination), self.assertRaises(ValueError):
                install_bundle(self.source, destination)

    def test_incomplete_source_does_not_write(self):
        (self.source / SKILLS[-1] / "SKILL.md").unlink()
        with self.assertRaises(ValueError):
            install_bundle(self.source, self.destination)
        self.assertFalse(self.destination.exists())

    def test_invalid_front_matter(self):
        path = self.source / SKILLS[0] / "SKILL.md"
        path.write_text("---\nname: wrong\n---\n", encoding="utf-8")
        self.assertTrue(any("front matter" in error for error in validate_skills(self.source)))

    def test_unknown_reference(self):
        path = self.source / SKILLS[0] / "SKILL.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n$unknown-skill\n", encoding="utf-8")
        self.assertTrue(any("Unknown skill" in error for error in validate_skills(self.source)))

    def test_missing_handoff(self):
        path = self.source / SKILLS[0] / "SKILL.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("$engineering-deliver", "delivery"),
            encoding="utf-8",
        )
        self.assertTrue(any("missing handoff" in error for error in validate_skills(self.source)))

    def test_missing_source(self):
        self.assertTrue(validate_skills(self.root / "absent"))

    def test_short_description(self):
        path = self.source / SKILLS[0] / "SKILL.md"
        content = path.read_text(encoding="utf-8")
        lines = content.splitlines()
        lines[2] = "description: Short"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        self.assertTrue(any("not informative" in error for error in validate_skills(self.source)))

    def test_missing_title(self):
        path = self.source / SKILLS[0] / "SKILL.md"
        content = path.read_text(encoding="utf-8").replace("# Engineering Workflow", "Workflow")
        path.write_text(content, encoding="utf-8")
        self.assertTrue(any("Missing title" in error for error in validate_skills(self.source)))

    def test_unexpected_skill(self):
        (self.source / "extra").mkdir()
        self.assertTrue(any("inventory" in error for error in validate_skills(self.source)))

    def test_local_links_and_external_links(self):
        (self.root / "target.md").write_text("# Target", encoding="utf-8")
        (self.root / "links.md").write_text(
            "[local](target.md#section) [external](https://example.com) [anchor](#local)",
            encoding="utf-8",
        )
        self.assertEqual(validate_links(self.root), [])

    def test_broken_and_escaping_links(self):
        (self.root / "links.md").write_text(
            "[missing](absent.md) [escape](../outside.md) [private](file:///C:/private)",
            encoding="utf-8",
        )
        self.assertEqual(len(validate_links(self.root)), 3)

    def test_copy_failure_is_not_success(self):
        with patch("install.shutil.copytree", side_effect=OSError("disk full")):
            with self.assertRaisesRegex(OSError, "disk full"):
                install_bundle(self.source, self.destination)

    def test_cli_dry_run(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "install.py"),
             "--dest", str(self.destination), "--dry-run"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count("Would install:"), 8)
        self.assertFalse(self.destination.exists())

    def test_cli_clean_install(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "install.py"), "--dest", str(self.destination)],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count("Installed:"), 8)
        self.assertEqual(validate_skills(self.destination), [])

    def test_cli_collision_fails(self):
        self.destination.mkdir(parents=True)
        (self.destination / SKILLS[0]).mkdir()
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "install.py"), "--dest", str(self.destination)],
            capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("No files copied", result.stderr)
        self.assertEqual(len(list(self.destination.iterdir())), 1)

    def test_cli_requires_explicit_destination(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "install.py")],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("--dest", result.stderr)


if __name__ == "__main__":
    unittest.main()
