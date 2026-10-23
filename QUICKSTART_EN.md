# Quick Start - MiMoCode Skills

## Safe offline catalog and selective installation

This repository stores 35 `SKILL.md` directories at its **root**, not in a nested `skills/` folder. Use the bundled Python 3.10+ tool to inspect/search and copy exactly the skills you need without overwriting an existing installation:

```bash
python scripts/skill_catalog.py --list
python scripts/skill_catalog.py --search design --json
python scripts/skill_catalog.py --install design-engineering code-review --dest ~/.codex/skills --dry-run
python scripts/skill_catalog.py --install design-engineering code-review --dest ~/.codex/skills
```

The install tool runs **offline**, never executes downloaded skills, rejects symlinks and special files, prechecks collisions, and stages each folder before placing it in the chosen directory. It does not resolve concurrent installers or automatically update existing skills. Review third-party instructions before granting an AI agent filesystem, terminal, or network permissions. Replace `~/.codex/skills` with the path supported by your agent; install paths are not universal.

For the repository itself:

```bash
python -m pip install 'PyYAML>=6,<7'
python -m unittest discover -s tests -p 'test_*.py' -v
```

## Legacy manual installation examples

### Option 1: Clone entirely (recommended)

```bash
git clone https://github.com/Samuraiprm/mimocode-skills.git ~/.mimocode/skills/
```

### Option 2: Copy individual skills

```bash
# Frontend design skills
cp -r taste-engineering ~/.mimocode/skills/
cp -r design-engineering ~/.mimocode/skills/
cp -r impeccable ~/.mimocode/skills/
cp -r review-animations ~/.mimocode/skills/
cp -r animation-vocabulary ~/.mimocode/skills/
cp -r premium-visual-design ~/.mimocode/skills/
cp -r minimalist-ui ~/.mimocode/skills/
cp -r industrial-brutalist-ui ~/.mimocode/skills/
cp -r redesign-existing ~/.mimocode/skills/
cp -r full-output-enforcement ~/.mimocode/skills/

# Security
cp -r code-audit ~/.mimocode/skills/
cp -r code-review ~/.mimocode/skills/
cp -r pentest ~/.mimocode/skills/

# IoT skills
cp -r iot-* ~/.mimocode/skills/
```

### Option 3: Clone into project folder

```bash
cd your-project
git clone https://github.com/Samuraiprm/mimocode-skills.git .mimocode/
```

## Getting Started

### Frontend Design

```
Create a landing page using taste-engineering
```

```
Review animations in this component using review-animations
```

```
Audit an existing project using redesign-existing
```

### Security

```
Review this PR for security issues
```

```
Audit this endpoint for vulnerabilities
```

### IoT

```
Analyze this device firmware using iot-apktool
```

```
Scan the network for IoT devices using iot-nmap
```

## Full Skill List

See [README_EN.md](README_EN.md) for the complete catalog.
