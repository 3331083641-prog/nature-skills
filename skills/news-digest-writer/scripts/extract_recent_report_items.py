#!/usr/bin/env python3
"""Extract titles and URLs from recent Word monitoring reports."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from docx import Document


URL_RE = re.compile(r"https?://\S+")


def extract_items(path: Path) -> list[dict[str, str]]:
    doc = Document(str(path))
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    items: list[dict[str, str]] = []

    for index, text in enumerate(paragraphs):
        if not URL_RE.match(text):
            continue
        title = ""
        for previous in range(index - 1, -1, -1):
            candidate = paragraphs[previous].strip()
            if candidate and not candidate.startswith("近日，") and not URL_RE.match(candidate):
                if candidate not in {
                    "印度、东盟农业政策跟踪",
                    "【本期导读】",
                } and not candidate.startswith("总第") and "农业政策动态" not in candidate:
                    title = candidate
                    break
        items.append({"title": title, "url": text, "file": str(path)})

    return items


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract recent report item titles and URLs.")
    parser.add_argument("paths", nargs="+", help="Docx files or directories to scan")
    args = parser.parse_args()

    files: list[Path] = []
    for raw in args.paths:
        path = Path(raw)
        if path.is_dir():
            files.extend(file for file in path.rglob("*.docx") if not file.name.startswith("~$"))
        elif path.suffix.lower() == ".docx" and path.exists():
            if not path.name.startswith("~$"):
                files.append(path)

    results: list[dict[str, str]] = []
    for file in sorted(set(files)):
        try:
            results.extend(extract_items(file))
        except Exception as exc:
            results.append({"title": "", "url": "", "file": str(file), "error": str(exc)})

    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
