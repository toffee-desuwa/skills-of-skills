# [PROJECT_NAME].SKILL -- skill template

Inherits: **STYLE_MASTER.md**, **PROJECT_MASTER.md**

> Replace bracketed placeholders with project-specific content.
> Delete this instruction block before committing.

---

## Context

[What is this project? One paragraph. Include tech stack, target users,
and current version.]

## Instructions

[Step-by-step workflow for the agent. Include branch name, commit plan,
and any project-specific rules that go beyond the masters.]

## Validation

[List concrete commands the agent must run after each commit. These
supplement the master validation rules, not replace them.]

```bash
# Example:
python -m compileall .
python -m unittest -q
python scripts/style_lint.py
# project-specific checks:
[ADD YOUR COMMANDS HERE]
```

## Constraints

[Hard constraints specific to this project. Examples: stdlib-only,
no new dependencies, specific Python version, platform requirements.]

## Handoff

[What the agent should do when the work is done. Typically: push
the branch, draft a PR description, stop. Reference PROJECT_MASTER
release authority rules.]

- Push `release/vX.Y.Z` to origin (if remote exists).
- Draft PR description for human review.
- Do NOT merge, tag, or release (per PROJECT_MASTER).
