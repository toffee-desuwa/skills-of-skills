"""style_lint.py -- minimal lint for skills-of-skills repo.

Checks:
1. README.md contains required headings (Limitations, Validation).
2. Every *.SKILL.md references both masters and has required sections.
3. Banned-terms scan across all checked files.

Exit code 0 = all checks pass.  Non-zero = at least one failure.
"""

import glob
import os
import re
import sys

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_README_HEADINGS = ["Limitations", "Validation"]

REQUIRED_SKILL_SECTIONS = [
    "Context",
    "Instructions",
    "Validation",
    "Constraints",
    "Handoff",
]

MASTER_REFERENCES = ["STYLE_MASTER", "PROJECT_MASTER"]

BANNED_TERMS = [
    "robust",
    "comprehensive",
    "seamless",
    "leverage",
    "state-of-the-art",
    "cutting-edge",
    "paradigm-shifting",
    "game-changing",
    "next-generation",
]

# Files to scan for banned terms (glob patterns relative to repo root).
SCAN_PATTERNS = ["README.md", "*.md", "examples/*.md"]

# Files that are allowed to contain banned terms (they define the list).
BANNED_TERM_ALLOWLIST = [
    os.path.join(REPO_ROOT, "STYLE_MASTER.md"),
    os.path.join(REPO_ROOT, "scripts", "style_lint.py"),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _headings(text):
    """Return a list of Markdown heading titles (any level)."""
    return [m.group(1).strip() for m in re.finditer(r"^#+\s+(.+)$", text, re.M)]


def _norm(path):
    return os.path.normpath(os.path.abspath(path))


# ---------------------------------------------------------------------------
# Check functions (each returns a list of error strings)
# ---------------------------------------------------------------------------

def check_readme():
    errors = []
    readme_path = os.path.join(REPO_ROOT, "README.md")
    if not os.path.isfile(readme_path):
        return ["README.md not found at repo root."]
    headings = _headings(_read(readme_path))
    for req in REQUIRED_README_HEADINGS:
        if not any(req.lower() == h.lower() for h in headings):
            errors.append(f"README.md missing required heading: {req}")
    return errors


def check_skill_files():
    errors = []
    patterns = [
        os.path.join(REPO_ROOT, "*.SKILL.md"),
        os.path.join(REPO_ROOT, "**", "*.SKILL.md"),
    ]
    paths = set()
    for pat in patterns:
        paths.update(glob.glob(pat, recursive=True))
    if not paths:
        # No skill files is not an error (template repo may have none).
        return []
    for path in sorted(paths):
        rel = os.path.relpath(path, REPO_ROOT)
        text = _read(path)
        # Master references
        for master in MASTER_REFERENCES:
            if master not in text:
                errors.append(f"{rel}: missing reference to {master}")
        # Required sections (check headings)
        headings = _headings(text)
        for sec in REQUIRED_SKILL_SECTIONS:
            if not any(sec.lower() == h.lower() for h in headings):
                errors.append(f"{rel}: missing required section: {sec}")
    return errors


def check_banned_terms():
    errors = []
    paths = set()
    for pat in SCAN_PATTERNS:
        paths.update(glob.glob(os.path.join(REPO_ROOT, pat), recursive=True))
    allowlist = {_norm(p) for p in BANNED_TERM_ALLOWLIST}
    for path in sorted(paths):
        if _norm(path) in allowlist:
            continue
        text = _read(path).lower()
        for term in BANNED_TERMS:
            if term in text:
                rel = os.path.relpath(path, REPO_ROOT)
                errors.append(f"{rel}: contains banned term '{term}'")
    return errors


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    all_errors = []
    checks = [
        ("README headings", check_readme),
        ("SKILL.md structure", check_skill_files),
        ("Banned terms", check_banned_terms),
    ]
    for name, fn in checks:
        errs = fn()
        if errs:
            print(f"FAIL  {name}:")
            for e in errs:
                print(f"  - {e}")
            all_errors.extend(errs)
        else:
            print(f"PASS  {name}")
    if all_errors:
        print(f"\n{len(all_errors)} error(s) found.")
        sys.exit(1)
    else:
        print("\nAll checks passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
