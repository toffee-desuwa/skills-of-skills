# skills-of-skills

A minimal "skills' skill" mother repo that manages project-specific AI agent
skills through progressive disclosure: master rules at the top, a reusable
template in the middle, and concrete project skills at the bottom.

Status: **v0.1.0** (two masters, one template, one example skill, one lint script).

---

## Problem

Agent skill files tend to grow until they hit context limits. Copy-pasting
style rules and workflow gates into every project skill creates drift and bloat.

This repo solves that with a three-layer structure:

1. **STYLE_MASTER.md** -- voice and style rules, canonical samples, banned terms.
2. **PROJECT_MASTER.md** -- branching model, commit discipline, release authority,
   validation gates.
3. **Project skills** (`*.SKILL.md`) -- inherit from both masters, add only
   project-specific context.

A project skill references the masters instead of inlining their content.
The agent loads the master it needs, when it needs it -- progressive disclosure
instead of context dumping.

## File layout

```
README.md
STYLE_MASTER.md
PROJECT_MASTER.md
SKILL_TEMPLATE.md
examples/
  qq-news-bot.SKILL.md
scripts/
  style_lint.py
.github/
  workflows/
    skill_check.yml
```

## Quickstart

### Lint all skill files

```bash
python scripts/style_lint.py
```

The lint script checks:
- Required sections exist in every `*.SKILL.md` (Context, Instructions,
  Validation, Constraints, Handoff).
- Masters are referenced.
- Banned terms are absent.
- This README contains Limitations and Validation headings.

## Validation

After every commit, run:

```bash
python -m compileall .
python scripts/style_lint.py
```

Both must pass before pushing.

## Limitations

- v0.1 is deliberately minimal: one example skill, simple substring lint.
- The lint script does not parse Markdown structure -- it uses line-level
  pattern matching. False positives are possible on unusual formatting.
- Masters encode the author's current style preferences. They are not
  universal standards.
- This repo does not enforce skill loading order at runtime. That is the
  responsibility of the agent framework consuming these files.
- No automated tests beyond the lint script in v0.1.

## License

MIT
