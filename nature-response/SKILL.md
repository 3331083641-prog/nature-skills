---
name: nature-response
description: >-
  Prepare, audit, or rewrite Nature-style point-by-point responses to reviewers and revision cover
  notes for Nature Portfolio or Springer Nature submissions. Use when the user asks for a rebuttal,
  author response, revision letter, reviewer-comment reply, major/minor revision response,
  Chinese-to-English response drafting, or a structured response package that aligns manuscript
  changes with specific reviewer and editor comments.
---

# Nature Response Skill

Use this skill to turn reviewer comments, editorial requests, and manuscript changes into a
structured revision response package that is specific, evidence-linked, and safe for resubmission.

The governing layer is Nature Portfolio / Springer Nature revision and peer review practice. The
implementation layer is point-by-point rebuttal structure, claim discipline, and manuscript-change
mapping derived from real peer review files and editorial guidance.

## Default stance

- Treat the response as part of the scientific record. It should help editors and reviewers verify
  what changed, why it changed, and what the authors did not change.
- Answer each reviewer point explicitly. Do not merge unrelated comments into one vague paragraph.
- Prefer direct acknowledgement, concrete action, and exact manuscript-location mapping over
  rhetorical defence.
- Do not claim an experiment, analysis, citation check, or text revision unless the user confirms
  it exists in the manuscript or revision materials.
- Distinguish `done`, `partly done`, and `not done`. If a request was not followed, explain why and
  offer the closest defensible alternative.
- Keep this skill focused on revision responses. Do not rewrite the full manuscript, perform
  statistical analysis, or invent new data unless the user asks for those tasks separately.

## Chinese-user operating mode

When the user writes in Chinese, provides reviewer comments in Chinese, or asks for "回复审稿人",
"逐条回复", "返修说明", or "中英对照":

- Accept Chinese input naturally, but draft the submission-ready response in English unless the
  user explicitly asks for Chinese only.
- Preserve a short Chinese explanation of unresolved decisions when that helps the author confirm
  what was changed.
- Translate intent, not wording. Phrases such as "我们已认真修改" are not enough on their own;
  convert them into specific action-plus-location statements.
- Use `references/chinese-author-alignment.md` for common Chinese-to-English response problems and
  bilingual intake questions.

## Workflow

1. Identify the submission stage and target journal:
   initial rebuttal, major revision, minor revision, or editor-only revision note.
2. Parse the input into units:
   editor requests, Reviewer 1 comments, Reviewer 2 comments, and author-side manuscript changes.
3. Classify each point:
   `text clarification`, `new analysis`, `new experiment`, `citation`, `limitation`, `scope
   disagreement`, `not feasible`, or `editorial formatting`.
4. Draft one response block per reviewer point with this order:
   brief acknowledgement, action taken, evidence or reasoning, manuscript-location mapping.
5. Normalize tone:
   respectful, specific, non-defensive, and proportionate to the request.
6. Check for unsupported claims:
   no invented experiments, no fake line numbers, no "we have revised accordingly" without saying
   what changed.
7. Return a ready-to-paste response package plus unresolved items the author must confirm.

## Quick-start template tool

Use `scripts/response_template.py` when the user already has raw reviewer comments in plain text
and needs a point-by-point scaffold quickly.

```bash
python scripts/response_template.py comments.txt
python scripts/response_template.py comments.txt --output response-template.txt
```

Use the script for structure only. Do not treat its output as a finished rebuttal. The response
content still needs manuscript-aware drafting and factual verification.

## Draft lint tool

Use `scripts/lint_response.py` when the user already has a rebuttal draft and you want a quick
structural check before deeper editing.

```bash
python scripts/lint_response.py response.txt
```

This linter checks for missing reviewer sections, missing `Comment n:` blocks, and comment blocks
that never receive a `Response:` line. It does not judge scientific adequacy or tone.

## Output format

Unless the user asks for another format, return:

```text
Response to Reviewers

Editor comments
- [point-by-point response or "None"]

Reviewer 1
Comment 1: [quoted or summarized reviewer point]
Response: [ready-to-paste response]

Reviewer 2
Comment 1: [quoted or summarized reviewer point]
Response: [ready-to-paste response]

Revision risks / missing confirmations
- [specific flags or "None"]

中文核对
- [用中文列出作者需要确认的改动、证据或行号，或 "无"]
```

When auditing an existing rebuttal, lead with blocking issues first, then provide a revised
version.

## Related files

| File | Open when |
|---|---|
| [scripts/response_template.py](scripts/response_template.py) | The user has plain-text reviewer comments and needs a rebuttal scaffold or reformatted response shell |
| [scripts/lint_response.py](scripts/lint_response.py) | The user has a rebuttal draft and needs a quick structural check before revision |
| [references/response-structure.md](references/response-structure.md) | You need the standard response block shape, section ordering, or editor-versus-reviewer handling |
| [references/tutorials.md](references/tutorials.md) | You need worked examples of strong response blocks, disagreement handling, or Chinese-to-English conversion |
| [references/real-world-patterns.md](references/real-world-patterns.md) | You need response patterns derived from real Nature-family peer review files |
| [references/tone-and-risk.md](references/tone-and-risk.md) | You need tone calibration, disagreement patterns, or red-flag checks |
| [references/chinese-author-alignment.md](references/chinese-author-alignment.md) | The user writes in Chinese, needs bilingual wording, or provides Chinese draft responses |
| [references/source-basis.md](references/source-basis.md) | You need to justify rules with official sources or check which source supports which rule |

## Source hierarchy

Use sources in this order:

1. Target journal revision instructions and submission system fields.
2. Nature Portfolio / Springer Nature author guidance and transparent peer review practice.
3. Real peer review files from Nature-family journals as response-shape evidence.
4. General scholarly peer review guidance only when Nature-family sources do not settle the point.

If revision or peer review instructions may have changed, verify the current journal page before
giving final submission advice.
