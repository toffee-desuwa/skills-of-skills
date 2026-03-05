# STYLE_MASTER -- skills-of-skills voice contract

This file is the primary voice and style authority for all repos that
reference it. Project-specific skills inherit these rules and must not
contradict them.

---

## Voice contract

- Write like a careful builder, not like an AI assistant.
- Research-first, honest, minimal. Admit boundaries.
- Say what the thing does, what it does not do, and stop.
- Prefer examples over grand claims. Never invent evidence;
  if evidence is missing, say "evidence missing".
- No emojis. No motivational fluff. No vague abstractions without evidence.
- All repo content (README, docs, code comments) must be English.
  Chat reports to the human may be in Chinese (or whatever the human
  uses), but every file committed to the repo must be English.
- Keep master files short (target: under 150 lines). If a section
  grows past that, move the excess into a template or example file.

## Canonical samples

Use these as tone anchors. Match this voice when writing README text,
docs, and code comments. Each sample is annotated with its source repo.

### Sample 1 -- Framing + boundaries [stars STYLE_LOCK.md]

- "This project started from a question I kept returning to:"
- "My current conclusion is that stars are not simply a natural byproduct
  of technical difficulty."
- "This is not a claim of superiority, nor an attempt to rank projects
  by taste."

### Sample 2 -- Observation-driven reasoning [stars STYLE_LOCK.md]

- "While collecting examples for this project, one pattern kept showing up:
  a lot of the 'star decision' seems to happen before anyone runs the code."
- "Code quality still matters -- just often later in the funnel."

### Sample 3 -- Sharp but non-hostile counterexample [stars STYLE_LOCK.md]

- "If stars were mainly about technical difficulty, the top of GitHub would
  look like an ICPC problemset leaderboard -- but it doesn't."

### Sample 4 -- Scope note with explicit boundaries [stars README.md]

> Scope note (v0.3): this tool is **README-first** by default. Docs-first repos (thin README, heavy external docs) may score lower unless you pass `--follow-docs`, which follows one docs link and extracts onboarding cues. Even then, it only supplements `execution_quality` — the other three dimensions stay README-only, since they measure first-screen impression.
> For docs-first repos, a low score often just means the evidence isn't visible in the README's first screen — not that the project is poor.

### Sample 5 -- Conditional framing [stars README.md]

- "If my observations hold (even roughly), then 'getting stars' is less
  about writing the most impressive code and more about reducing
  uncertainty for the reader."

### Sample 6 -- Parenthetical honesty [stars README.md]

- "(they're adjustable, not sacred)"
- "(even before they use it)"

### Sample 7 -- Intent + tradeoffs in code comments [stars STYLE_LOCK.md]

- Comments should explain intent and tradeoffs (why this exists, what we
  are not doing), not teach the language.

### Sample 8 -- Honest limitations [qqbot README.md]

- "Polling interval is fixed at 15 minutes; this is not true realtime push."
- "keyword-based (substring match). They may miss events phrased
  differently or fire on unrelated articles."
- "No LLM integration -- items are presented as-is (title + source + link)."

### Sample 9 -- Fail-open philosophy in docstrings [qqbot news_fetcher.py]

- "Fail-open: returns empty list on error, logs one line."

### Sample 10 -- Version history in module docstring [qqbot news_fetcher.py]

- "RSS feed fetcher and formatter (stdlib only: urllib + xml.etree).
  v0.1.1: per-source cap, dedupe by link, fail-open, Chinese output shell."

## Banned terms

Avoid these unless the context genuinely requires them. Suggested
replacements are in parentheses.

| Banned term          | Replacement suggestion                     |
|----------------------|--------------------------------------------|
| robust               | reliable, tested, fail-open                |
| comprehensive        | covers X and Y (be specific)               |
| seamless             | low-friction, simple                       |
| leverage             | use, rely on                               |
| state-of-the-art     | current, recent (or cite the paper)        |
| cutting-edge         | recent, new                                |
| paradigm-shifting    | (drop it; describe what changed instead)   |
| game-changing        | (drop it; show the before/after instead)   |
| next-generation      | v2, updated (be specific)                  |

## Required README sections

Every repo that references this master must include at least these
headings in its README:

1. **Limitations** -- what the project does not do, known gaps, scope
   boundaries.
2. **Validation** -- how to verify that the project works (commands,
   expected output).

These sections enforce honesty and reduce over-promise risk.
