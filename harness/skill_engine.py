#!/usr/bin/env python3
"""Discover, validate, match, and launch local nature-skills.

The harness deliberately uses only the Python standard library so it can run in a
fresh checkout before any plotting, PPTX, or YAML dependencies are installed.
It treats the root README Skill index and each skill README as the human-authored
source of truth for status, purpose, trigger terms, and matching context.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)|<img\s+[^>]*src=\"([^\"]+)\"")
GENERATED_SUFFIXES = {".pptx", ".pdf", ".svg", ".tiff", ".tif"}


@dataclass
class Skill:
    name: str
    path: Path
    metadata: dict[str, str]
    status: str = ""
    purpose: str = ""
    triggers: tuple[str, ...] = ()

    @property
    def skill_md(self) -> Path:
        return self.path / "SKILL.md"

    @property
    def readme(self) -> Path:
        return self.path / "README.md"

    @property
    def references(self) -> list[Path]:
        ref_dir = self.path / "references"
        return sorted(ref_dir.glob("*.md")) if ref_dir.exists() else []


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_frontmatter(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return text
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "\n".join(lines[index + 1 :]).lstrip()
    return text


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    raw: list[str] = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        raw.append(line)

    metadata: dict[str, str] = {}
    index = 0
    while index < len(raw):
        line = raw[index]
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            index += 1
            continue

        key, value = match.group(1), match.group(2).strip()
        index += 1
        if value in {">", ">-", "|", "|-"}:
            block: list[str] = []
            while index < len(raw):
                next_line = raw[index]
                if re.match(r"^[A-Za-z0-9_-]+:\s*", next_line):
                    break
                block.append(next_line.strip())
                index += 1
            metadata[key] = " ".join(part for part in block if part)
        else:
            metadata[key] = value.strip("\"'")
    return metadata


def parse_index(readme: Path) -> dict[str, dict[str, object]]:
    if not readme.exists():
        return {}

    index: dict[str, dict[str, object]] = {}
    for line in read_text(readme).splitlines():
        if not line.startswith("| [`nature-"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) < 4:
            continue
        name_match = re.search(r"`([^`]+)`", parts[0])
        if not name_match:
            continue
        index[name_match.group(1)] = {
            "status": parts[1],
            "purpose": parts[2],
            "triggers": tuple(re.findall(r'"([^"]+)"', parts[3])),
        }
    return index


def discover(root: Path = ROOT) -> list[Skill]:
    index = parse_index(root / "README.md")
    skills: list[Skill] = []
    for path in sorted(root.glob("nature-*")):
        if not path.is_dir() or not (path / "SKILL.md").exists():
            continue
        metadata = parse_frontmatter(read_text(path / "SKILL.md"))
        row = index.get(path.name, {})
        skills.append(
            Skill(
                name=metadata.get("name", path.name),
                path=path,
                metadata=metadata,
                status=str(row.get("status", "")),
                purpose=str(row.get("purpose", "")),
                triggers=tuple(row.get("triggers", ())),
            )
        )
    return skills


def check_markdown_links(root: Path) -> list[str]:
    issues: list[str] = []
    for markdown in sorted(root.rglob("*.md")):
        rel = markdown.relative_to(root)
        in_fence = False
        for number, line in enumerate(read_text(markdown).splitlines(), start=1):
            if line.startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for match in LINK_RE.finditer(line):
                target = match.group(1) or match.group(2)
                if re.match(r"^(https?:|mailto:|#)", target):
                    continue
                target_path = target.split("#", 1)[0]
                if not target_path:
                    continue
                full = (markdown.parent / target_path).resolve()
                try:
                    full.relative_to(root.resolve())
                except ValueError:
                    issues.append(f"{rel}:{number}: link escapes repository: {target}")
                    continue
                if not full.exists():
                    issues.append(f"{rel}:{number}: missing link target: {target}")
    return issues


def validate(root: Path = ROOT) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    root_index = parse_index(root / "README.md")

    def add(level: str, subject: str, message: str) -> None:
        results.append({"level": level, "subject": subject, "message": message})

    for skill in discover(root):
        subject = skill.path.name
        metadata = skill.metadata
        if not metadata.get("name"):
            add("error", subject, "SKILL.md frontmatter is missing name")
        if skill.name != skill.path.name:
            add("error", subject, f"frontmatter name {skill.name!r} does not match folder")
        if not metadata.get("description"):
            add("error", subject, "SKILL.md frontmatter is missing description")
        if not skill.readme.exists():
            add("warn", subject, "README.md is missing")
        if skill.path.name not in root_index:
            add("warn", subject, "root README skill index is missing this skill")

        skill_lines = len(read_text(skill.skill_md).splitlines())
        if skill_lines > 500:
            add("warn", subject, f"SKILL.md has {skill_lines} lines; consider splitting references")

        launch_text = read_text(skill.skill_md)
        if skill.readme.exists():
            launch_text += "\n" + read_text(skill.readme)
        for ref in skill.references:
            if ref.name not in launch_text and f"references/{ref.name}" not in launch_text:
                add("warn", subject, f"reference is not discoverable from SKILL.md or README.md: {ref.name}")

    for issue in check_markdown_links(root):
        add("error", "markdown", issue)

    for generated in sorted(root.rglob("*")):
        if not generated.is_file() or generated.suffix.lower() not in GENERATED_SUFFIXES:
            continue
        if ".git" in generated.parts or "assets" in generated.parts:
            continue
        add("warn", "generated-artifact", str(generated.relative_to(root)))

    return results


def normalize_words(text: str) -> set[str]:
    return {word for word in re.findall(r"[A-Za-z0-9][A-Za-z0-9_-]{1,}", text.lower())}


def score(skill: Skill, query: str) -> int:
    query_lower = query.lower()
    query_words = normalize_words(query)
    corpus = " ".join(
        [
            skill.name,
            skill.metadata.get("description", ""),
            skill.purpose,
            " ".join(skill.triggers),
            read_text(skill.readme)[:4000] if skill.readme.exists() else "",
        ]
    ).lower()

    total = 0
    for trigger in skill.triggers:
        trigger_lower = trigger.lower()
        if trigger_lower in query_lower or query_lower in trigger_lower:
            total += 20
    total += 2 * len(query_words & normalize_words(corpus))
    if skill.name.replace("nature-", "") in query_lower:
        total += 10
    return total


def cmd_list(args: argparse.Namespace) -> int:
    rows = []
    for skill in discover(args.root):
        rows.append(
            {
                "skill": skill.path.name,
                "status": skill.status or "-",
                "references": len(skill.references),
                "purpose": skill.purpose or skill.metadata.get("description", "")[:80],
            }
        )
    print_table(rows, ["skill", "status", "references", "purpose"])
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    issues = validate(args.root)
    if args.json:
        print(json.dumps(issues, ensure_ascii=False, indent=2))
    elif issues:
        for issue in issues:
            print(f"[{issue['level']}] {issue['subject']}: {issue['message']}")
    else:
        print("OK: all skill checks passed.")
    return 1 if any(issue["level"] == "error" for issue in issues) else 0


def cmd_match(args: argparse.Namespace) -> int:
    rows = []
    for skill in discover(args.root):
        rows.append(
            {
                "score": score(skill, args.query),
                "skill": skill.path.name,
                "triggers": ", ".join(skill.triggers[:4]),
            }
        )
    rows.sort(key=lambda row: (-int(row["score"]), row["skill"]))
    print_table(rows[: args.limit], ["score", "skill", "triggers"])
    return 0


def cmd_launch(args: argparse.Namespace) -> int:
    skills = {skill.path.name: skill for skill in discover(args.root)}
    skill = skills.get(args.skill)
    if skill is None:
        print(f"Unknown skill: {args.skill}", file=sys.stderr)
        return 2

    sections = [
        f"# Launch {skill.path.name}",
        "## Metadata",
        f"- status: {skill.status or 'unlisted'}",
        f"- purpose: {skill.purpose or 'not listed'}",
        f"- triggers: {', '.join(skill.triggers) or 'not listed'}",
        "## Skill Instructions",
        strip_frontmatter(read_text(skill.skill_md)),
    ]

    references = list(args.reference or [])
    if args.include_references:
        references.extend(ref.name for ref in skill.references)
    if references:
        ref_by_name = {ref.name: ref for ref in skill.references}
        sections.append("## Loaded References")
        for name in references:
            ref = ref_by_name.get(name) or ref_by_name.get(Path(name).name)
            if ref is None:
                sections.append(f"### Missing Reference: {name}")
                continue
            sections.extend([f"### {ref.relative_to(skill.path)}", read_text(ref)])

    if args.request:
        sections.extend(["## User Request", args.request])

    output = "\n\n".join(sections).rstrip() + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


def print_table(rows: list[dict[str, object]], columns: list[str]) -> None:
    if not rows:
        print("(none)")
        return
    widths = {
        column: max(len(column), *(len(str(row.get(column, ""))) for row in rows))
        for column in columns
    }
    print("  ".join(column.ljust(widths[column]) for column in columns))
    print("  ".join("-" * widths[column] for column in columns))
    for row in rows:
        print("  ".join(str(row.get(column, "")).ljust(widths[column]) for column in columns))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Local harness for nature-skills.")
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root.")
    subparsers = parser.add_subparsers(required=True)

    list_parser = subparsers.add_parser("list", help="List discovered skills.")
    list_parser.set_defaults(func=cmd_list)

    validate_parser = subparsers.add_parser("validate", help="Validate skill metadata and links.")
    validate_parser.add_argument("--json", action="store_true", help="Emit JSON results.")
    validate_parser.set_defaults(func=cmd_validate)

    match_parser = subparsers.add_parser("match", help="Rank skills for a user request.")
    match_parser.add_argument("query", help="User request to match.")
    match_parser.add_argument("--limit", type=int, default=4, help="Number of matches to show.")
    match_parser.set_defaults(func=cmd_match)

    launch_parser = subparsers.add_parser("launch", help="Assemble a launch prompt for a skill.")
    launch_parser.add_argument("skill", help="Skill folder name, for example nature-polishing.")
    launch_parser.add_argument("--request", default="", help="User request to append.")
    launch_parser.add_argument("--reference", action="append", help="Reference file to include.")
    launch_parser.add_argument("--include-references", action="store_true", help="Include all references.")
    launch_parser.add_argument("--output", type=Path, help="Write launch prompt to a file.")
    launch_parser.set_defaults(func=cmd_launch)

    return parser


def main(argv: Optional[Iterable[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
