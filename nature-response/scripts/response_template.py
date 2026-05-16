#!/usr/bin/env python3
"""
Build a point-by-point response template from plain-text reviewer comments.

Usage:
    python response_template.py comments.txt
    python response_template.py comments.txt --output template.txt
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REVIEWER_HEADER_RE = re.compile(r"^\s*(reviewer|referee)\s*#?\s*(\d+)\s*:?\s*$", re.IGNORECASE)
COMMENT_HEADER_RE = re.compile(r"^\s*(comment|point)\s*#?\s*(\d+)\s*:?\s*$", re.IGNORECASE)
NUMBERED_POINT_RE = re.compile(r"^\s*(\d+)[\.\)]\s+(.+)$")


def parse_comments(text: str) -> list[tuple[str, list[str]]]:
    reviewers: list[tuple[str, list[str]]] = []
    current_reviewer = "Reviewer 1"
    current_comments: list[str] = []
    current_block: list[str] = []

    def flush_block() -> None:
        nonlocal current_block, current_comments
        block = "\n".join(line.rstrip() for line in current_block).strip()
        if block:
            current_comments.append(block)
        current_block = []

    def flush_reviewer() -> None:
        nonlocal current_reviewer, current_comments
        flush_block()
        if current_comments:
            reviewers.append((current_reviewer, current_comments))
        current_comments = []

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if REVIEWER_HEADER_RE.match(line):
            flush_reviewer()
            reviewer_num = REVIEWER_HEADER_RE.match(line).group(2)
            current_reviewer = f"Reviewer {reviewer_num}"
            continue
        if COMMENT_HEADER_RE.match(line):
            flush_block()
            continue
        numbered = NUMBERED_POINT_RE.match(line)
        if numbered:
            flush_block()
            current_block.append(numbered.group(2))
            continue
        if not line.strip():
            flush_block()
            continue
        current_block.append(line)

    flush_reviewer()
    return reviewers or [("Reviewer 1", [text.strip()] if text.strip() else [])]


def render_template(reviewers: list[tuple[str, list[str]]]) -> str:
    parts = ["Response to Reviewers", "", "Editor comments", "- None", ""]
    for reviewer_name, comments in reviewers:
        parts.append(reviewer_name)
        if not comments:
            parts.append("Comment 1: [insert reviewer comment]")
            parts.append("Response: [insert response]")
            parts.append("")
            continue
        for idx, comment in enumerate(comments, start=1):
            compact = " ".join(segment.strip() for segment in comment.splitlines()).strip()
            parts.append(f"Comment {idx}: {compact}")
            parts.append("Response: [insert response]")
            parts.append("")
    parts.extend(
        [
            "Revision risks / missing confirmations",
            "- [insert missing evidence, line numbers, or unresolved points]",
            "",
            "中文核对",
            "- [插入需要作者确认的内容]",
        ]
    )
    return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a Nature-style response template.")
    parser.add_argument("input", help="Plain-text reviewer comments file")
    parser.add_argument("--output", help="Optional output path")
    args = parser.parse_args()

    source = Path(args.input)
    text = source.read_text(encoding="utf-8")
    rendered = render_template(parse_comments(text))

    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
