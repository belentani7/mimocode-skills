# MIMOCODE-SKILLS — PROJECT MASTER PROMPT

## Product identity
A curated 35-skill repository of structured SKILL.md guides for engineering, design, security, verification and IoT work. The actual root skill directories and their original source attributions are authoritative. This is an **agent instruction library**, not an automated pentest platform, hardware exploit tool, or fully autonomous agent. Keep original license files and source credits; do not merge this with the independently maintained Claude Skills Pack.

## Maximum useful product
Make 35 skills discoverable, searchable, safely installable and verifiable. Users must be able to find relevant skills by language/topic, choose only desired skills, preview changes, and install them into their own supported agent runtime without destroying custom content. Add transparent compatibility metadata, references/provenance inventory, explicit tool-dependency requirements, reliable test gates, and accessible documentation in the existing Russian/English languages.

## Construction roadmap
1. **Real inventory:** validate every root SKILL.md folder and YAML frontmatter, emit machine-readable JSON of actual contents, detect malformed docs, invalid names and missing references.
2. **Safe selection:** implement free-text search, exact-name selection, dry-run, explicit target directory, no automatic execution, no hidden network access, symlink/special-file rejection, collision preflight and copy staging.
3. **Compatibility and supply-chain:** test each skill against known assistants, attach source attribution, flag tool assumptions and side-effectful instructions, never imply that a skill automatically grants access to external services.
4. **Lifecycle:** explicit revision and provenance registry, opt-in updates with diff and backup of customized installations, stable aliases, migration notes and measurable quality rather than marketing ratings.
5. **Verification:** Python 3.10+ tests, frontmatter schema validation, broken reference scans, CLI integration scenarios (including Windows), reproducible offline packaging, CI that actually runs and only truthful release claims.

## Operating instruction to implementation agents
Work in this existing repository, read its current code and open PRs and preserve existing upstream-derived content/credits. Implement code and regression tests rather than repeating documentation-only audits. Do not run security/IoT commands against networks or devices, copy user files, perform paid API calls, or install anything into a user's machine without their explicit selection. No renames/visibility changes without verifying references. Keep changes in reviewable PRs, do not claim tests passed when GitHub Actions cannot allocate a runner, and record the next useful feature before moving to a different historical active repository.
