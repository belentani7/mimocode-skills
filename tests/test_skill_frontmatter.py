"""Every skill must ship a SKILL.md whose YAML frontmatter actually parses.

Contract: README.md ("Вклад") says each skill must have
"SKILL.md с YAML frontmatter (name, description)".  An agent harness
loads the skill by YAML-parsing the frontmatter, so a frontmatter that
a YAML parser rejects means the skill cannot be loaded at all.
"""

import pathlib
import unittest

import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL_DIRS = sorted(
    p for p in REPO_ROOT.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()
)


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("no frontmatter delimiter at start of file")
    end = text.find("\n---", 3)
    if end == -1:
        raise ValueError("unterminated frontmatter block")
    return yaml.safe_load(text[3:end])


class TestSkillFrontmatter(unittest.TestCase):
    def test_skill_count(self):
        self.assertEqual(len(SKILL_DIRS), 35, "README promises 35 skills")

    def test_frontmatter_is_valid_yaml(self):
        errors = []
        for skill_dir in SKILL_DIRS:
            try:
                data = parse_frontmatter(skill_dir / "SKILL.md")
            except Exception as exc:  # noqa: BLE001 - collect every failure
                errors.append(f"{skill_dir.name}: {type(exc).__name__}: {exc}")
                continue
            if not isinstance(data, dict):
                errors.append(f"{skill_dir.name}: frontmatter is not a mapping")
        self.assertEqual(errors, [], "\n" + "\n".join(errors))

    def test_frontmatter_declares_name_and_description(self):
        errors = []
        for skill_dir in SKILL_DIRS:
            try:
                data = parse_frontmatter(skill_dir / "SKILL.md")
            except Exception:  # reported by test_frontmatter_is_valid_yaml
                continue
            for key in ("name", "description"):
                value = data.get(key)
                if not isinstance(value, str) or not value.strip():
                    errors.append(f"{skill_dir.name}: missing/empty '{key}'")
        self.assertEqual(errors, [], "\n" + "\n".join(errors))


if __name__ == "__main__":
    unittest.main()
