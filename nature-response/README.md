# `nature-response` skill

A revision-response skill for preparing point-by-point replies to reviewers, editor response notes,
and revision-cover text in a Nature / Springer Nature publication style.

This skill is bilingual-aware. It accepts Chinese author notes such as "回复审稿人",
"逐条回复", "返修说明", "编辑意见", or "补充实验", then converts them into
submission-ready English with Chinese action notes for the author.

## What it does

- drafts ready-to-paste point-by-point responses to reviewers
- separates editor comments from reviewer comments
- maps each response to a concrete manuscript change, new analysis, new experiment, or justified
  non-change
- rewrites vague or defensive rebuttal language into specific revision language
- flags unsupported claims, missing evidence, and missing manuscript-location mapping
- aligns Chinese author intent with Nature-style English response wording
- includes a lightweight script to convert plain-text reviewer comments into a rebuttal template

## Source hierarchy

- target journal revision instructions and submission fields
- Nature Portfolio and Springer Nature author guidance
- transparent peer review files from Nature-family journals
- general peer review guidance only when the journal sources do not settle the issue

## File structure

```text
nature-response/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── scripts/
│   ├── lint_response.py
│   └── response_template.py
└── references/
    ├── chinese-author-alignment.md
    ├── real-world-patterns.md
    ├── response-structure.md
    ├── source-basis.md
    ├── tutorials.md
    └── tone-and-risk.md
```

## When to use

- preparing a response to reviewers for a Nature-family or Springer Nature journal
- restructuring a major or minor revision rebuttal
- drafting an editor response note that summarizes manuscript changes
- revising defensive or vague author replies
- mapping reviewer comments to line numbers, figures, analyses, or experiments
- converting Chinese response notes into precise English submission language

## Design intent

The skill should make every response traceable to a reviewer point and a concrete author action or
reasoned non-action. It should not fabricate experiments, line numbers, or manuscript edits. When
information is missing, it should return a usable draft plus a short list of items the author must
confirm, preferably with Chinese notes when the user is working from a Chinese draft.

## Tooling

`scripts/response_template.py` is a formatting helper, not a writing engine. Use it when the user
already has raw reviewer comments in plain text and needs a clean `Reviewer / Comment / Response`
shell before drafting the actual rebuttal.

`scripts/lint_response.py` is a structural checker. Use it on a draft rebuttal when you want to
catch missing reviewer sections, missing `Response:` blocks, or obviously incomplete formatting
before doing content-level editing.

## Validation basis

The current skill has been exercised on realistic revision scenarios covering:

- clarification-only replies with exact manuscript-location mapping
- partial disagreement cases where the authors narrow claims instead of adding new experiments
- Chinese author notes converted into submission-ready English response blocks
- plain-text reviewer comments converted into a response scaffold with `response_template.py`
- draft rebuttals checked for structural omissions with `lint_response.py`
