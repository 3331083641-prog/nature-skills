# Response Structure

Use this file when structuring a point-by-point response package.

## Default package order

1. Short opening note to the editor
2. Editor-only requests, if any
3. Reviewer sections in numerical order
4. Closing note summarizing high-level changes, only if useful

Do not hide reviewer-specific replies inside one long narrative letter when the journal expects
point-by-point responses.

## Standard response block

Use one block per reviewer point:

```text
Comment [n]:
[quoted or tightly summarized reviewer point]

Response:
We thank the reviewer for this comment. We [clarified / added / reanalysed / corrected / did not
change] [specific issue]. [One sentence on what was done or why it was not done.] [Exact location:
Methods paragraph, Results section, Fig. 2 legend, Supplementary Note 3, etc.]
```

The opening thanks can be short. The value is in the action and the evidence.

## What a strong response block contains

- an explicit answer to the point
- a concrete author action or a clear reason for not taking the requested action
- enough scientific detail for the editor or reviewer to assess the change
- exact manuscript mapping when available

## Manuscript mapping guidance

Prefer precise document anchors:

- `Results, paragraph 3`
- `Methods, subsection "Model training"`
- `Fig. 2b and accompanying legend`
- `Supplementary Table 4`

Use exact line numbers only when the user supplies the revised manuscript numbering or asks for
line-number formatting specifically. Do not invent them.

## Editor comments versus reviewer comments

- Put editor comments first when they impose global tasks such as reporting standards, figure
  resolution, data deposition, code sharing, or title/format restrictions.
- Do not answer editor instructions as if they were reviewer comments.
- If one edit resolves several reviewer points, say so in each relevant block instead of making the
  reader hunt for the explanation elsewhere.

## Non-change responses

When the authors did not follow a request:

- state the scientific or practical reason directly
- explain the closest alternative analysis or clarification added
- avoid sounding dismissive or evasive

Example pattern:

```text
We appreciate this suggestion. We did not perform [requested task] because [specific constraint or
scope reason]. To address the underlying concern, we [added control / clarified limitation /
expanded discussion] in [location].
```
