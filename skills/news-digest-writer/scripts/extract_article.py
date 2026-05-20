#!/usr/bin/env python3
"""Extract basic article text from a static webpage URL."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser


class ArticleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._skip_depth = 0
        self._capture_title = False
        self.title_parts: list[str] = []
        self.text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript", "svg"}:
            self._skip_depth += 1
        if tag == "title":
            self._capture_title = True
        if tag in {"p", "h1", "h2", "h3", "li", "blockquote"}:
            self.text_parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg"} and self._skip_depth:
            self._skip_depth -= 1
        if tag == "title":
            self._capture_title = False
        if tag in {"p", "h1", "h2", "h3", "li", "blockquote"}:
            self.text_parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth:
            return
        text = data.strip()
        if not text:
            return
        if self._capture_title:
            self.title_parts.append(text)
        self.text_parts.append(text)


def normalize_text(value: str) -> str:
    value = re.sub(r"[ \t\r\f\v]+", " ", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def fetch(url: str, timeout: int) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
            )
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract basic article text from a static URL.")
    parser.add_argument("url", help="Article URL to fetch")
    parser.add_argument("--timeout", type=int, default=20, help="Request timeout in seconds")
    parser.add_argument("--max-chars", type=int, default=12000, help="Maximum text characters to return")
    args = parser.parse_args()

    try:
        html = fetch(args.url, args.timeout)
    except Exception as exc:
        print(json.dumps({"url": args.url, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1

    article_parser = ArticleTextParser()
    article_parser.feed(html)
    title = normalize_text(" ".join(article_parser.title_parts))
    text = normalize_text(" ".join(article_parser.text_parts))

    print(
        json.dumps(
            {
                "url": args.url,
                "title": title,
                "text": text[: args.max_chars],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
