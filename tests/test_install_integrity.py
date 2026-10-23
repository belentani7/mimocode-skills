"""Prevent unverified or link-bearing staged skills from becoming installed."""
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'skill_catalog.py'
spec = importlib.util.spec_from_file_location('skill_catalog', SCRIPT)
assert spec and spec.loader
catalog = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = catalog
spec.loader.exec_module(catalog)


class InstallIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.skill_dir = self.root / 'design-test'
        self.skill_dir.mkdir()
        (self.skill_dir / 'SKILL.md').write_text('---\nname: design-test\ndescription: Test\n---\n', encoding='utf-8')
        self.skill = catalog.Skill('design-test', self.skill_dir, 'Test')
        self.destination = self.root / 'installed'

    def tearDown(self):
        self.tmp.cleanup()

    def assert_clean_failure(self):
        self.assertFalse((self.destination / self.skill.name).exists())
        self.assertEqual([], list(self.destination.glob('.mimocode-stage-*')))

    def test_rejects_tampered_copy_before_install(self):
        real_copytree = catalog.shutil.copytree

        def tamper(src, dst, **kwargs):
            result = real_copytree(src, dst, **kwargs)
            (Path(dst) / 'SKILL.md').write_text('tampered after copy', encoding='utf-8')
            return result

        with patch.object(catalog.shutil, 'copytree', side_effect=tamper):
            with self.assertRaisesRegex(catalog.SkillError, 'changed during installation'):
                catalog.install_one(self.skill, self.destination)
        self.assert_clean_failure()

    def test_rejects_symlink_in_staged_copy(self):
        outside = self.root / 'private.txt'
        outside.write_text('secret', encoding='utf-8')
        real_copytree = catalog.shutil.copytree

        def inject_link(src, dst, **kwargs):
            result = real_copytree(src, dst, **kwargs)
            try:
                (Path(dst) / 'private-link').symlink_to(outside)
            except (OSError, NotImplementedError):
                self.skipTest('symlinks unsupported')
            return result

        with patch.object(catalog.shutil, 'copytree', side_effect=inject_link):
            with self.assertRaisesRegex(catalog.SkillError, 'unsafe skill entry'):
                catalog.install_one(self.skill, self.destination)
        self.assert_clean_failure()

    def test_valid_copy_installs_and_verifies(self):
        target = catalog.install_one(self.skill, self.destination)
        self.assertEqual(target, catalog.verify_one(self.skill, self.destination))
        self.assertTrue((target / 'SKILL.md').is_file())


if __name__ == '__main__':
    unittest.main()
