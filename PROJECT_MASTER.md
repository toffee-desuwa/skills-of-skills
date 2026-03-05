# PROJECT_MASTER -- skills-of-skills workflow contract

This file is the workflow, validation, and release authority for all repos
that reference it. Project-specific skills inherit these rules.

---

## Branching model

- Default branch: `main`.
- All work happens on a `release/*` branch (e.g., `release/v0.1.0`).
- Merge to `main` via pull request only. No direct pushes to `main` after
  the initial scaffold commit.

## Commit discipline

### Slicing rule

Each commit should be a coherent, reviewable unit. Prefer small commits
over large ones. A single commit should not mix unrelated changes (e.g.,
do not combine a new feature with a formatting cleanup).

### Validation after each commit

After every commit, run the project's validation commands and show a short
pass/fail summary. Do not proceed to the next commit if validations fail.
If validations fail and you cannot resolve the issue, stop and ask the
human. Do not attempt workarounds that drift from the original task.

Typical validation pattern:

```bash
python -m compileall .          # syntax check (if Python)
python scripts/style_lint.py    # lint check (if lint script exists)
# project-specific checks go here
```

### Final validation pass

Before pushing to origin, run all validations one final time. This is the
last gate before code leaves the local machine.

## O1 defense (minimum requirements)

Every project skill must include these safeguards against hallucination,
drift, and silent failure:

1. **Explicit validation commands** -- the skill must list concrete
   commands that verify the work (not just "check that it works").
2. **One final validation pass** -- the skill must require a complete
   validation run before any push or handoff.
3. **Clear limitations** -- the skill (and the README) must state what
   the project does not do and where it may fail.

These are non-negotiable. A skill that omits any of them is incomplete.

## Scope freeze

If the task declaration includes scope constraints (e.g., "no new deps",
"no logic changes", "patch only"), treat them as absolute. Do not add
nice-to-have improvements, refactors, or bonus features that fall outside
the declared scope. When in doubt, ask.

## Repository safety baseline (default)

These are the default repo-level guardrails for all projects unless
explicitly overridden.

- **Protected `main`:** `main` should be protected. Direct pushes to
  `main` are avoided.
- **Required checks:** `main` should require at least one CI check
  before merging. Minimal CI is acceptable: `compileall` + `unittest`
  (+ one smoke command if applicable).
- **No approvals requirement for solo maintainers:** do **not** require
  review approvals when the repo is maintained by a single person
  (avoids deadlocks).
- **Agent authority (implementation only):** agents may create branches,
  commit, run validations, and push non-protected branches (e.g.,
  `release/*`, `chore/*`) after final validations pass. Agents may
  draft PR / release text, but do not perform merge/tag/release actions.
- **Human authority (integration & release):** the human maintainer
  opens PRs (if needed), merges to `main`, tags versions, and publishes
  GitHub Releases.

If a repository currently lacks CI, add a minimal workflow, trigger it
once, then enable "required checks" in branch protection.

## Release authority

This policy is fixed and applies to all projects referencing this master:

- Agents may create and push branches after final validations pass.
- Agents must NOT merge pull requests.
- Agents must NOT create tags.
- Agents must NOT publish releases.
- Agents may draft PR descriptions and release notes for the human to
  review and execute.

## Progressive disclosure

The three-layer loading order:

1. **Master** (this file + STYLE_MASTER.md) -- loaded once, rarely
   changes. Contains rules that apply everywhere.
2. **Template** (SKILL_TEMPLATE.md) -- loaded when creating a new
   project skill. Defines the required structure.
3. **Project skill** (`*.SKILL.md`) -- loaded per task. Contains only
   project-specific context, commands, and constraints. References
   masters instead of duplicating their content.

An agent should load the minimum layer needed for the current task.
If the task is project-specific, load the project skill; the skill's
header tells the agent which masters to consult if needed.
