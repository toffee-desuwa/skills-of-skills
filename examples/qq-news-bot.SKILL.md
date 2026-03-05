# qq-news-bot.SKILL -- QQ news bot agent skill

Inherits: **STYLE_MASTER.md**, **PROJECT_MASTER.md**

---

## Context

QQ group chat bot that fetches news from RSS feeds and pushes daily
digests. Built on OneBot v11 protocol via NapCat, using a WebSocket
client. Python 3.10+ stdlib only. Current version: v0.2.0.

Key features: daily digest, keyword-based breaking-news alerts,
per-group mute, persona skill packs (neutral / maid_cat).

## Instructions

1. Branch from `main` to `release/vX.Y.Z`.
2. Follow the commit plan (one coherent unit per commit).
3. After each commit: run validations, show `git diff --stat`,
   show short pass/fail summary.
4. Reply to the human in Chinese. Write all repo content in English.
5. Hard gates (stop and wait for human review):
   - After Commit 1 (scaffold).
   - After all commits + final validation pass (before push).

## Validation

Run after every commit:

```bash
python -m compileall .
python -m unittest -q
python -m bot --dry-run --news
```

From Commit 4 onward, also run:

```bash
python -m bot --connect
# Verify startup, then Ctrl-C.
```

## Constraints

- Python 3.10+ stdlib only. No third-party packages.
- SQLite for local storage.
- Config via environment variables only (no config files beyond
  `.env.example`).
- All repo text in English. No emojis.
- Fail-open error handling: network errors log one line and return
  empty results. Never crash the bot on a single feed failure.
- Persona is a pure data layer (JSON key-value mapping). No
  conditional logic in persona files.

## Handoff

- Push `release/vX.Y.Z` to origin (if remote exists).
- Draft PR description for human review.
- Do NOT merge, tag, or release (per PROJECT_MASTER).
