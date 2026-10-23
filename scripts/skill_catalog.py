#!/usr/bin/env python3
"""Discover, search, validate and selectively install MiMoCode skills offline.

This repository stores skill folders at its root (not under skills/).
No code from a skill is ever executed. Existing destinations are preserved.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import stat
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
NAME = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


@dataclass(frozen=True)
class Skill:
    name: str
    path: Path
    description: str

    def to_dict(self) -> dict[str, str]:
        return {"name": self.name, "description": self.description}


class SkillError(ValueError):
    pass


def summary(path: Path) -> str:
    """Return a one-line summary without importing/performing skill instructions."""
    text = path.read_text(encoding="utf-8-sig")
    if not text.startswith("---\n"):
        raise SkillError(f"{path}: missing YAML frontmatter")
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        raise SkillError(f"{path}: missing closing frontmatter delimiter")
    # Full YAML validation remains covered by the existing PyYAML test suite.
    # For search we do not need to parse any embedded YAML code or tags.
    match = re.search(r"^description:\s*(.*)$", parts[0], re.MULTILINE)
    if not match:
        raise SkillError(f"{path}: no description field")
    value = match.group(1).strip().strip("\"'")
    if not value or value in {">", "|", ">-", "|-"}:
        return parts[1].lstrip().splitlines()[0][:160] or "(no summary)"
    return value[:160]


def inventory(root: Path = REPO) -> list[Skill]:
    """Find only immediate skill directories; never follow symlinks."""
    found = []
    for folder in sorted(root.iterdir(), key=lambda x: x.name):
        if folder.is_symlink() or not folder.is_dir() or not NAME.fullmatch(folder.name):
            continue
        entry = folder / "SKILL.md"
        if entry.is_symlink() or not entry.is_file():
            continue
        found.append(Skill(folder.name, folder, summary(entry)))
    return found


def validate_contents(folder: Path) -> None:
    """Reject symlinks and special files so copying cannot read outside a skill."""
    for parent, dirs, files in os.walk(folder, followlinks=False):
        for name in [*dirs, *files]:
            entry = Path(parent) / name
            mode = entry.lstat().st_mode
            if stat.S_ISLNK(mode) or not (stat.S_ISDIR(mode) or stat.S_ISREG(mode)):
                raise SkillError(f"unsafe skill entry: {entry}")


def install_one(skill: Skill, destination: Path, dry_run: bool = False) -> Path:
    target = destination / skill.name
    if target.exists() or target.is_symlink():
        raise SkillError(f"destination already contains {skill.name}: {target}")
    validate_contents(skill.path)
    if dry_run:
        return target
    destination.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".mimocode-stage-", dir=destination))
    try:
        staging = temporary / skill.name
        shutil.copytree(skill.path, staging, symlinks=False)
        if target.exists() or target.is_symlink():
            raise SkillError(f"destination appeared during install: {target}")
        staging.rename(target)
    finally:
        shutil.rmtree(temporary, ignore_errors=True)
    return target


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Inspect and install MiMoCode skills offline.")
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument("--list", action="store_true", help="List the skills actually present")
    actions.add_argument("--search", metavar="WORDS", help="Search skill names and descriptions")
    actions.add_argument("--install", nargs="+", metavar="SKILL", help="Install selected skills by folder name")
    parser.add_argument("--dest", type=Path, help="Target skills directory for --install")
    parser.add_argument("--dry-run", action="store_true", help="Validate installation without writing")
    parser.add_argument("--json", action="store_true", help="JSON results for --list or --search")
    args = parser.parse_args(argv)
    try:
        skills = inventory()
        if args.install is None:
            selected = skills if args.list else [
                skill for skill in skills
                if args.search.casefold() in (skill.name + " " + skill.description).casefold()
            ]
            if args.json:
                print(json.dumps([s.to_dict() for s in selected], ensure_ascii=False, indent=2))
            else:
                for skill in selected:
                    print(f"{skill.name:30} {skill.description}")
            return 0

        if args.dest is None:
            raise SkillError("--install requires an explicit --dest folder")
        if len(set(args.install)) != len(args.install):
            raise SkillError("duplicate skill names in request")
        catalog = {s.name: s for s in skills}
        unknown = [name for name in args.install if name not in catalog]
        if unknown:
            raise SkillError("unknown skill(s): " + ", ".join(unknown))
        destination = args.dest.expanduser().resolve()
        if destination.exists() and not destination.is_dir():
            raise SkillError(f"not a directory: {destination}")
        # Validate the entire request BEFORE installing any part of it.
        for name in args.install:
            skill = catalog[name]
            validate_contents(skill.path)
            target = destination / name
            if target.exists() or target.is_symlink():
                raise SkillError(f"destination already contains {name}: {target}")
        for name in args.install:
            target = install_one(catalog[name], destination, args.dry_run)
            print(("would install " if args.dry_run else "installed ") + str(target))
        return 0
    except (OSError, UnicodeError, SkillError) as exc:
        print(f"mimocode: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
