#!/usr/bin/env python3
"""
Check a draft response-to-reviewers file for common structural problems.

Usage:
    python lint_response.py response.txt
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REVIEWER_RE = re.compile(r"^\s*Reviewer\s+\d+\s*$", re.IGNORECASE)
COMMENT_RE = re.compile(r"^\s*Comment\s+\d+\s*:", re.IGNORECASE)
RESPONSE_RE = re.compile(r"^\s*Response\s*:\s*(.*)$", re.IGNORECASE)


def lint_response(text: str) -> list[str]:
    issues: list[str] = []
    lines = text.splitlines()

    reviewer_count = sum(1 for line in lines if REVIEWER_RE.match(line))
    comment_count = sum(1 for line in lines if COMMENT_RE.match(line))
    response_lines = [line for line in lines if RESPONSE_RE.match(line)]

    if reviewer_count == 0:
        issues.append("No reviewer sections found.")
    if comment_count == 0:
        issues.append("No comment blocks found.")
    if not response_lines:
        issues.append("No response blocks found.")

    for idx, line in enumerate(lines, start=1):
        if COMMENT_RE.match(line):
            has_response = False
            for follow in lines[idx:]:
                if COMMENT_RE.match(follow) or REVIEWER_RE.match(follow):
                    break
                match = RESPONSE_RE.match(follow)
                if match:
                    has_response = True
                    if not match.group(1).strip():
                        issues.append(f"Empty response placeholder near line {idx}.")
                    break
            if not has_response:
                issues.append(f"Comment block near line {idx} has no Response:.")

    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Lint a response-to-reviewers draft.")
    parser.add_argument("input", help="Path to rebuttal draft")
    args = parser.parse_args()

    text = Path(args.input).read_text(encoding="utf-8")
    issues = lint_response(text)

    if issues:
        for issue in issues:
            print(f"- {issue}")
        sys.exit(1)

    print("No structural issues found.")


if __name__ == "__main__":
    main()
