---
name: code-evidence-guardrail
description: >-
  Overlay-only guardrail for grounding implementation claims in code evidence. Use primarily
  with a primary writing, manuscript, README, presentation, figure, or explanation skill when
  code-grounded accuracy is requested. Use directly only when the user explicitly asks for
  code-faithfulness auditing, implementation verification, hallucination checking against code,
  or code/text consistency review. Do not use as the primary writing or polishing skill.
---

# Code-Evidence Guardrail

Use primarily as an overlay guardrail, not as a primary writing skill.

Use directly only when the user explicitly asks for code-faithfulness auditing,
implementation verification, hallucination checking against code, or code/text consistency
review.

Do not use this skill as the primary manuscript, README, PPT, polishing, figure, data, or
reviewer-response workflow. A primary task-specific skill should control style, structure,
audience, and output format.

This guardrail controls whether factual implementation claims are supported, cautious,
attributed, flagged, or omitted.

For explicit user invocation, load `references/spec.md` before evaluating implementation
claims.

When used as an overlay, load `references/spec.md` only if the task requires full
code-grounding or verification. For language-only polishing, translation, formatting, or
document summarization, do not inspect code by default; only avoid adding or strengthening
implementation claims.
