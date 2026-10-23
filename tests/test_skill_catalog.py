"""Offline regression tests for MiMoCode's searchable skill catalog."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "skill_catalog.py"
spec = importlib.util.spec_from_file_location("skill_catalog", SCRIPT)
assert spec and spec.loader
catalog = importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name] = catalog
spec.loader.exec_module(catalog)


class TestSkillCatalog(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.sources = self.root / "sources"
        self.sources.mkdir()
        self.skill = self.sources / "design-example"
        self.skill.mkdir()
        (self.skill / "SKILL.md").write_text(
            "---\nname: design-example\ndescription: Accessible UI review\n---\n# How to review\n",
            encoding="utf-8",
        )
        self.target = self.root / "installed"

    def tearDown(self):
        self.temp.cleanup()

    def test_inventory_finds_only_direct_valid_skill_folders(self):
        (self.sources / "empty").mkdir()
        (self.sources / "not a skill").mkdir()
        actual = catalog.inventory(self.sources)
        self.assertEqual([s.name for s in actual], ["design-example"])
        self.assertEqual(actual[0].description, "Accessible UI review")

    def test_dry_run_is_read_only(self):
        item = catalog.inventory(self.sources)[0]
        result = catalog.install_one(item, self.target, dry_run=True)
        self.assertEqual(result, self.target / item.name)
        self.assertFalse(self.target.exists())

    def test_install_preserves_nested_files_and_rejects_overwrite(self):
        (self.skill / "references").mkdir()
        (self.skill / "references" / "guide.txt").write_text("original", encoding="utf-8")
        item = catalog.inventory(self.sources)[0]
        out = catalog.install_one(item, self.target)
        self.assertEqual((out / "references" / "guide.txt").read_text(), "original")
        (out / "SKILL.md").write_text("personal edit", encoding="utf-8")
        with self.assertRaisesRegex(catalog.SkillError, "already contains"):
            catalog.install_one(item, self.target)
        self.assertEqual((out / "SKILL.md").read_text(), "personal edit")

    def test_rejects_symlinks_in_skill_without_creating_target(self):
        outside = self.root / "secret.txt"
        outside.write_text("secret", encoding="utf-8")
        try:
            (self.skill / "leak.txt").symlink_to(outside)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable")
        item = catalog.inventory(self.sources)[0]
        with self.assertRaisesRegex(catalog.SkillError, "unsafe skill"):
            catalog.install_one(item, self.target)
        self.assertFalse(self.target.exists())

    def test_main_rejects_unknown_selection_before_writing(self):
        result = catalog.main(["--install", "not-a-skill", "--dest", str(self.target)])
        self.assertEqual(result, 1)
        self.assertFalse(self.target.exists())

    def test_main_lists_existing_catalog_without_side_effects(self):
        from contextlib import redirect_stdout
        from io import StringIO
        output = StringIO()
        with redirect_stdout(output):
            result = catalog.main(["--list", "--json"])
        self.assertEqual(result, 0)
        self.assertIn("design", output.getvalue())
        self.assertFalse(self.target.exists())


    def test_verify_matches_installed_files_and_detects_edits(self):
        item = catalog.inventory(self.sources)[0]
        out = catalog.install_one(item, self.target)
        self.assertEqual(catalog.verify_one(item, self.target), out)
        (out / "SKILL.md").write_text("edited", encoding="utf-8")
        with self.assertRaisesRegex(catalog.SkillError, "integrity mismatch"):
            catalog.verify_one(item, self.target)

    def test_verify_rejects_extra_files_and_missing_install(self):
        item = catalog.inventory(self.sources)[0]
        with self.assertRaisesRegex(catalog.SkillError, "missing or unsafe"):
            catalog.verify_one(item, self.target)
        out = catalog.install_one(item, self.target)
        (out / "extra.txt").write_text("unexpected", encoding="utf-8")
        with self.assertRaisesRegex(catalog.SkillError, "integrity mismatch"):
            catalog.verify_one(item, self.target)

    def test_verify_rejects_installed_symlinks(self):
        item = catalog.inventory(self.sources)[0]
        out = catalog.install_one(item, self.target)
        try:
            (out / "shortcut").symlink_to(out / "SKILL.md")
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable")
        with self.assertRaisesRegex(catalog.SkillError, "unsafe skill entry"):
            catalog.verify_one(item, self.target)

    def test_verify_cli_is_read_only_and_returns_nonzero_on_mismatch(self):
        from contextlib import redirect_stdout
        from io import StringIO
        from unittest.mock import patch
        item = catalog.inventory(self.sources)[0]
        out = catalog.install_one(item, self.target)
        with patch.object(catalog, "inventory", return_value=[item]):
            with redirect_stdout(StringIO()) as output:
                self.assertEqual(catalog.main(["--verify", item.name, "--dest", str(self.target)]), 0)
            self.assertIn("verified ", output.getvalue())
            (out / "SKILL.md").write_text("modified", encoding="utf-8")
            with redirect_stdout(StringIO()):
                self.assertEqual(catalog.main(["--verify", item.name, "--dest", str(self.target)]), 1)
        self.assertEqual((out / "SKILL.md").read_text(encoding="utf-8"), "modified")


if __name__ == "__main__":
    unittest.main()
