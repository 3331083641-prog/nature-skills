# Chinese Author Alignment

Use this file when the user writes in Chinese, provides Chinese reviewer comments, or asks for
bilingual wording. The goal is to convert Chinese revision intent into Nature-ready English
response language.

## Core terminology

| 中文 | Preferred English | Notes |
|---|---|---|
| 回复审稿人 | Response to Reviewers | Use as the main heading when the journal expects a rebuttal file. |
| 逐条回复 | point-by-point response | Preserve the one-comment-one-response structure. |
| 编辑意见 | editor comments | Keep separate from reviewer comments. |
| 补充实验 | additional experiment | Use only when the experiment was actually done. |
| 补充分析 | additional analysis | Prefer this when existing data were re-analysed. |
| 修改正文 | revised the manuscript | Follow with what changed and where. |
| 讨论中补充说明 | added discussion / clarified in the Discussion | Name the location more precisely when possible. |
| 我们认为 | we interpret / we consider | Often better than a blunt disagreement formula. |
| 超出本文范围 | beyond the scope of the current study | Explain why and what was done instead. |
| 感谢审稿人的建议 | we thank the reviewer for this suggestion | Keep short; do not let gratitude replace content. |

## Chinese-to-English conversion rules

- Convert `我们已认真修改` into a specific revision statement:
  say what changed, where it changed, and whether the change was textual, analytical, or
  experimental.
- Convert `我们同意这个问题很重要` into action:
  add whether the issue was clarified, tested, or acknowledged as a limitation.
- Convert `因时间限制未补实验` carefully:
  avoid making convenience sound like a scientific reason. Explain scope, feasibility, or data
  constraints, then add the best indirect fix.
- Convert `已在文中标红` into manuscript-neutral wording:
  name the section, figure, or supplementary file instead of relying on colour markup.
- Convert `见回复1` only when necessary:
  most points should still get a self-contained answer.

## Bilingual intake questions

Ask only what is needed for the response.

```text
请确认这些字段：
1. 每条审稿意见对应的实际改动是什么？是补实验、补分析、补引用，还是只改文字？
2. 是否有修订稿中的具体位置，例如章节、小节、图号、补充说明或行号？
3. 哪些意见没有完全采纳？原因是范围、数据限制、时间、还是实验不可行？
4. 是否需要同时回复编辑意见？
5. 是否需要中英对照，还是只输出英文提交版本？
```

## Recommended bilingual output

When useful, provide English first and Chinese second:

```text
Response:
[English submission-ready response]

中文核对
- 这条回复对应的实际改动：[brief Chinese explanation]
- 需要作者确认：[location / evidence / whether experiment was really done]
```
