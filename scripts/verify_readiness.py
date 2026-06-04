#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SENSITIVE_PATTERNS = [
    ("private key block", re.compile(r"-{5}BEGIN [A-Z ]*PRIVATE KEY-{5}")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    (
        "AWS secret assignment",
        re.compile(r"aws_secret_access_key\s*[:=]\s*['\"]?[A-Za-z0-9/+=]{20,}", re.I),
    ),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    (
        "literal password assignment",
        re.compile(
            r"\b(pass(word)?|pwd)\s*=\s*(?!\{PASSWORD\}|<password>|example|changeme|redacted|placeholder)[^\s'\"]{8,}",
            re.I,
        ),
    ),
    ("local user file URL", re.compile(r"file:///Users/[^\s\"')<]+")),
    ("local private path", re.compile(r"/Users/[A-Za-z0-9._-]+/[^\s\"')<]+")),
    ("meeting join link language", re.compile(r"\bjoin (zoom|teams|webex)\b", re.I)),
    ("meeting id", re.compile(r"\bmeeting id[: ]+[0-9 -]{6,}\b", re.I)),
    ("raw conversation dump reference", re.compile(r"\braw " + r"trans" + r"cript\b", re.I)),
]
SKIP_DIRS = {".git", "dist", "node_modules", "coverage", "tmp"}
TEXT_SUFFIXES = {".html", ".md", ".json", ".css", ".js", ".txt", ".py"}


def iter_files():
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def main():
    failures = []
    checked = 0
    for path in iter_files():
        checked += 1
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in SENSITIVE_PATTERNS:
            if path == Path(__file__).resolve():
                continue
            if pattern.search(text):
                failures.append(f"{path.relative_to(ROOT)} contains sensitive pattern: {label}")
    if failures:
        print("Readiness check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"Readiness check passed: {checked} public files inspected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
