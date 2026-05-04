# Code-Evidence Guardrail for Technical Writing

## Purpose

This specification is a hallucination-prevention and code-evidence guardrail for technical, academic, manuscript, README, documentation, and presentation writing.

It is not a complete writing workflow. It should be used together with other specifications that define style, structure, journal tone, slide layout, audience, or formatting.

Other specifications decide how the writing should sound or be organized. This specification decides which implementation claims may be written.

The core rule is:

> Writing must not outrun implementation evidence.

## Contents

- Purpose
- Relationship to Other Writing Specifications
- Trigger Rule
- Code Inspection Is Evidence Collection, Not the Trigger
- Claim Strengthening
- README and Documentation Editing Boundary
- Summarization Boundary
- Explaining Provided Code Boundary
- User Requests Not to Inspect Code
- Anti-Hallucination Priority
- What Counts as an Implementation Claim
- Inspection Depth Levels
- Large Repository Inspection Priority
- Evidence-Level Use Rules
- Direct-Active Evidence
- Direct-Local Evidence
- Existence vs Usage Rule
- Scope
- Claim Types Requiring Code Evidence
- Evidence Hierarchy
- Notebook Evidence
- Partial or Incomplete Codebases
- Narrow Methods from Partial Code
- Handling Inferred Claims
- Material Inferred Claims
- Handling Weak or Unsupported Claims
- Handling Conflicts
- Default Evidence Handling
- User Requests to Hide Risk
- Mandatory Risk Report Conditions
- Risk-Only Reporting
- High-Risk Terms Requiring Strong Evidence
- Writing Rules
- Attribution Rules When Code Is Not Inspected
- Reviewer Response and Manuscript Use
- README Installation and Usage Claims
- Evaluation Protocol Claims
- Figure and Plotting Claims
- Reproducibility Claims
- Privacy and Security
- Minimal Acceptance Standard
- Reviewer Standard

## Relationship to Other Writing Specifications

When this specification conflicts with another writing specification, this specification takes priority for factual claims about implementation.

This includes claims about:

- implementation details
- code behavior
- software workflow
- model architecture
- data loading or preprocessing
- training, inference, or evaluation
- metrics, baselines, or validation procedure
- command-line usage or reproducibility
- pipeline inputs, outputs, or dependencies
- plotting or figure-generation procedures

Other specifications may shape prose style, section structure, journal tone, slide design, or audience adaptation. This specification controls factual grounding.

## Trigger Rule

Trigger this guardrail when the user asks to create, revise, verify, audit, explain, summarize, or polish text that contains or may introduce implementation claims.

Do not trigger this guardrail merely because a repository, code directory, or code file exists. Code presence alone is not a trigger.

Triggering this guardrail does not always mean inspecting code. In L0 cases, the guardrail only prevents claim strengthening and requires attribution when needed.

Implementation claims include factual statements about what the code, model, package, script, workflow, training process, inference process, evaluation process, plotting process, or data-processing path does.

Examples of implementation claims:

- "The pipeline performs five-fold cross-validation."
- "The model uses a transformer encoder."
- "The package supports batch inference."
- "The script normalizes input features."
- "The evaluation computes AUROC and F1."
- "The workflow generates the figures from raw input files."

If the user only requests language editing, translation, formatting, or style adaptation, do not inspect code unless the edit would add, strengthen, or alter implementation claims.

## Code Inspection Is Evidence Collection, Not the Trigger

Scanning a code directory is not the trigger for this specification. It is one possible evidence-collection step after the guardrail has been triggered.

Once triggered, inspect code proportionally to the specificity, risk, and scope of the implementation claims.

Use the minimum inspection depth needed to avoid unsupported specificity.

Do not perform a full repository audit unless the user's request or the claim scope requires it.

## Claim Strengthening

Claim strengthening means changing wording so that a claim becomes broader, more certain, more global, more active-path-specific, or more publication-facing than the evidence supports.

Without code inspection or author confirmation, do not strengthen claims.

Examples of claim strengthening:

- "includes" -> "uses"
- "can support" -> "supports"
- "appears to" -> "performs"
- "the script defines" -> "the pipeline uses"
- "the README states" -> "the package provides"
- "an optional utility exists" -> "the method relies on"
- "the provided file implements" -> "the full workflow performs"

## README and Documentation Editing Boundary

If the user asks to rewrite, polish, professionalize, shorten, translate, or restructure a README or documentation page, do not verify implementation claims by default.

Default behavior:

- preserve the meaning of existing implementation claims
- do not strengthen implementation claims
- do not add new implementation details
- use attribution when needed
- do not inspect code unless the user asks for implementation accuracy

Trigger code inspection when the user asks for any of the following:

- "make it accurate to the repo"
- "based on the code"
- "based on the implementation"
- "verify against the code"
- "check whether the README matches the code"
- "rewrite this README from the repo"
- "make the documentation reflect the implementation"

README installation and usage claims are higher risk than general prose.

Use these default boundaries:

| README task | Default depth |
|---|---|
| Edit tone, structure, headings, or readability only | L0 |
| Summarize README as a document | L0 with attribution when needed |
| Edit installation commands, CLI flags, default behavior, supported inputs, or supported outputs | At least L1 or L2 |
| Rewrite usage based on the repo | L2 or L3 |
| Check README against implementation | L3 or L4, depending on scope |

Examples:

| User request | Guardrail behavior |
|---|---|
| "Make this README more professional." | Do not inspect code by default. Edit style and structure without strengthening implementation claims. |
| "Summarize this README." | Summarize the README as a document. Do not verify code by default. Attribute claims to the README when needed. |
| "Make this README accurate to the repo." | Trigger guardrail. Inspect relevant code before writing implementation claims. |
| "Check whether this README matches the code." | Trigger guardrail. Inspect relevant code and report mismatches. |
| "Rewrite this README based on the implementation." | Trigger guardrail. Inspect code before writing implementation claims. |

## Summarization Boundary

If the user asks to summarize a document as a document, do not verify implementation claims unless explicitly requested.

In that case, preserve attribution to the source document. Use wording such as:

- "The README describes..."
- "The draft states..."
- "The document claims..."
- "According to the provided text..."

Do not present document claims as verified implementation facts unless code has been inspected.

If the user asks to summarize what the code, repository, package, model, or pipeline does, trigger this guardrail and inspect code proportionally.

## Explaining Provided Code Boundary

If the user asks to explain a provided code file or snippet, trigger this guardrail because the response will contain implementation claims.

However, restrict the scope to the provided code unless the user asks for repository-level or pipeline-level interpretation.

Allowed:

- "This file defines..."
- "This function appears to..."
- "Within the provided code..."
- "The snippet implements..."

Not allowed without broader repository inspection:

- "The main pipeline uses..."
- "The full training workflow..."
- "The experiments rely on..."
- "The package supports..."

If only one file or snippet is provided, do not infer repository-wide behavior from it.

## User Requests Not to Inspect Code

If the user explicitly asks not to inspect code, do not inspect code.

In that case:

- do not introduce new implementation details
- do not strengthen implementation claims
- do not convert cautious claims into factual claims
- preserve, soften, generalize, or attribute existing implementation claims
- optionally note that implementation truth was not verified

For example, if the draft says:

> "We used five-fold cross-validation."

and the user asks only for English polishing without code inspection, the claim may be grammatically polished but must not be expanded into a stronger implementation description.

Allowed:

> "We used five-fold cross-validation."

Safer if attribution is needed:

> "The draft states that five-fold cross-validation was used."

Not allowed without code inspection:

> "The evaluation pipeline rigorously performs five-fold cross-validation across all datasets."

## Anti-Hallucination Priority

Prefer omission, cautious wording, generic phrasing, attribution, or author-check notes over unsupported specificity.

Do not add implementation details merely because they are:

- common for similar methods
- expected by academic convention
- implied by project naming
- present in comments only
- present in filenames only
- useful for narrative completeness
- more polished or impressive

A polished but unsupported claim is worse than a less detailed but evidence-grounded sentence.

## What Counts as an Implementation Claim

Implementation claims are factual statements about implemented behavior, active workflow, supported inputs or outputs, model structure, data processing, training, inference, evaluation, plotting, dependencies, or command-line behavior.

The following related claim types require special care and should not be inferred from code structure alone:

| Claim type | Examples | Evidence requirement |
|---|---|---|
| Design-intent claims | "designed for large-scale analysis" | Documentation, architecture, or author confirmation |
| Usability claims | "easy to use", "simple", "flexible" | User-facing interface, examples, or user evidence |
| Performance claims | "fast", "robust", "scalable" | Benchmarks, experiments, or measurement evidence |
| Adoption claims | "widely used", "production-ready" | Usage data, deployment evidence, or external support |
| Scientific claims | "novel", "validated", "clinically relevant" | Manuscript-level or external scientific evidence |
| Result claims | "improves accuracy", "outperforms baselines" | Result tables, metrics, evaluation scripts, or manuscript evidence |

Code evidence may support implementation. Code alone does not establish scientific novelty, clinical validity, biological mechanism, physical causality, or performance superiority.

## Inspection Depth Levels

Use the shallowest inspection level sufficient for the requested claim.

Inspection depth should be determined by claim scope, not by document type alone.

For example, a Methods-related task does not automatically require repository-level inspection. A single Methods sentence may require only L1 or L2. A full Methods section spanning data processing, model architecture, training, inference, and evaluation may require L3.

| Level | Use when | Required inspection |
|---|---|---|
| `L0: No code inspection` | Pure language editing, translation, formatting, document summarization, README/documentation polishing without implementation verification, or user explicitly asks not to verify code. | Do not add or strengthen implementation claims. Attribute claims to the source when needed. |
| `L1: Targeted inspection` | Revising, explaining, or verifying one narrow implementation claim, file, function, class, config, or snippet. | Inspect the directly relevant file, function, class, config, test, snippet, or documented command. |
| `L2: Path inspection` | Writing or revising a paragraph about one workflow area, such as model, dataset, training, inference, plotting, or evaluation. | Inspect the entry point, relevant module, config, and call path for that workflow area. |
| `L3: Repository-level inspection` | Writing or revising multiple claims spanning more than one major workflow area, such as data processing plus model architecture plus training plus evaluation. | Inspect repo structure, main entry points, configs, core modules, relevant scripts, tests, and examples. |
| `L4: Audit mode` | User asks for verification, hallucination check, evidence ledger, risk review, or line-by-line review. | Build an explicit claim-evidence map and report risks. |

## Large Repository Inspection Priority

For large repositories, do not attempt exhaustive inspection unless explicitly requested and feasible.

Prioritize inspection in this order:

1. user-mentioned files, modules, functions, commands, or claims
2. documented commands or entry points
3. configuration consumed by those entry points
4. imported modules on the relevant call path
5. tests or examples exercising the claimed behavior
6. notebooks or scripts tied to result generation
7. documentation and comments as supporting evidence only

If the repository is too large for complete inspection, avoid repository-wide claims unless the relevant active paths have been inspected.

## Evidence-Level Use Rules

| Evidence level | Meaning | Use in final prose |
|---|---|---|
| `direct-active` | Explicit evidence on the active execution path, or a documented execution path that is consistent with inspected executable code. | May be written as a factual implementation claim. |
| `direct-local` | Code exists locally, but use in the active workflow is not established. | May support claims that the repository defines or includes the feature, but not that the main pipeline uses it. |
| `author-confirmed` | The user or author has confirmed the implementation claim, but code verification is absent or incomplete. | May be written if appropriate, but must not be represented as code-verified evidence. |
| `inferred` | Reasonably inferred from call flow, imports, module interaction, naming plus partial path evidence, or incomplete execution path. | May be written only with cautious wording, unless confirmed by the user or authors. |
| `weak` | Suggested by comments, filenames, README text, docstrings, naming, or incomplete code paths. | Should not be written as a factual claim. May be surfaced as an author-check question. |
| `unsupported` | No reliable implementation evidence was found. | Must not be written as a factual claim. Remove, generalize, attribute to source text, or flag for confirmation. |

A claim that the workflow uses a behavior requires evidence that the behavior is on the active or documented execution path and is consistent with inspected code.

Merely finding an implemented function, class, module, or file is not enough to claim that the main workflow uses it.

Author confirmation may permit a claim to be written, but it should be distinguished from code-verified evidence when reporting verification status.

## Direct-Active Evidence

Direct-active evidence may include:

- source code on the active call path
- configuration consumed by an entry script
- command-line arguments used by the relevant workflow
- workflow files that execute the relevant step
- tests or examples that exercise the relevant supported behavior
- notebooks that clearly reproduce the relevant workflow
- documented commands that are consistent with inspected code

A documented execution path counts as direct-active evidence only when it is consistent with inspected executable code.

Documentation alone cannot establish active workflow behavior.

Tests and examples can prove supported behavior, but not necessarily main experimental usage unless tied to the relevant documented workflow, active entry point, or result path.

CI jobs can support runnable or tested behavior, but not manuscript experiment usage unless the CI job is explicitly the result-generation workflow.

## Direct-Local Evidence

Direct-local evidence means the codebase contains a feature, but active use has not been established.

Direct-local evidence can support claims such as:

- "The repository includes..."
- "The codebase defines..."
- "The provided module implements..."
- "An optional utility is present for..."

Direct-local evidence cannot support claims about:

- default behavior
- main workflow behavior
- experimental usage
- method design
- training behavior
- evaluation behavior
- result generation

Example:

If the repository contains `cross_validation.py`, but the main training or evaluation path does not call it, then this is allowed:

> "The repository includes a cross-validation utility."

This is not allowed:

> "The evaluation pipeline performs cross-validation."

## Existence vs Usage Rule

Distinguish code existence from active use.

| Claim type | Required evidence |
|---|---|
| "The repository includes X." | File, function, class, or module existence may be enough. |
| "The package supports X." | CLI, API, config option, tests, examples, or documentation showing X is usable. |
| "The main pipeline uses X." | Active entry point, config, or call-path evidence. |
| "The experiments used X." | Experiment script, config, log, notebook, or result-generation path evidence. |
| "The method relies on X." | Core active-path evidence showing X is necessary, not merely optional. |
| "The results demonstrate X." | Manuscript-level result evidence; code alone is insufficient. |

Do not claim that a method, pipeline, or experiment used a component merely because the repository contains a file with a relevant name.

## Scope

Apply this guardrail when writing or revising:

- manuscript Methods or Supplementary Methods
- model, algorithm, or pipeline descriptions
- software, tool, package, or repository descriptions
- README or documentation prose when implementation accuracy is requested
- PPT method or workflow slides
- reviewer-response explanations about implementation
- figure captions or result descriptions that depend on implementation details
- implementation-related responses to peer reviewers
- technical summaries that claim what code does
- explanations of provided code, limited to the inspected/provided code scope

Do not use this guardrail to infer scientific novelty, biological mechanism, clinical relevance, physical causality, or performance superiority from code alone.

## Claim Types Requiring Code Evidence

Require code evidence before writing factual claims about:

- model type, architecture, layers, modules, loss functions, or optimization strategy
- data formats, filtering, normalization, feature extraction, augmentation, batching, or splits
- training configuration, epochs, batch size, learning rate, scheduler, seeds, or checkpoints
- inference behavior, prediction outputs, thresholds, post-processing, or supported modes
- evaluation metrics, baselines, validation protocols, cross-validation, or benchmarks
- pipeline stages, command-line workflow, dependencies, inputs, outputs, or reproducibility steps
- plotting or figure-generation procedures when prose describes how a figure was produced
- API behavior, CLI behavior, package modes, or supported input/output formats

## Evidence Hierarchy

Prefer evidence in this order:

1. Executable source code on the active path
2. Configuration consumed by entry scripts
3. Workflow files such as `Snakefile`, `nextflow.config`, shell scripts, launch scripts, or CI jobs
4. Tests or examples that exercise the behavior
5. Notebooks that clearly reproduce the workflow
6. Documentation that matches inspected implementation
7. Comments, names, and docstrings

Documentation alone should not override code.

Comments, filenames, and naming are weak evidence unless supported by executable behavior.

If source code, documentation, manuscript text, and comments conflict, prioritize inspected executable behavior.

## Notebook Evidence

A notebook may count as direct evidence only when it clearly forms part of the relevant workflow and contains an executable path for the claim.

Treat a notebook as stronger evidence when:

- it is referenced by documentation, scripts, or manuscript materials
- it runs the relevant preprocessing, training, inference, evaluation, or plotting steps
- it uses the same inputs, configs, or modules as the claimed workflow
- it appears tied to result generation

Treat a notebook as weak or inferred evidence when:

- it is exploratory
- it is incomplete
- it is disconnected from the main workflow
- it uses toy data
- it is not tied to the manuscript or result path
- it contains outputs without reproducible execution context

## Partial or Incomplete Codebases

If the available codebase is partial, treat repository-wide claims as unsupported unless the relevant active path is present.

Prefer local claims such as:

- "this module defines..."
- "the provided script implements..."
- "the available code includes..."
- "the inspected files suggest..."

Avoid global claims such as:

- "the pipeline performs..."
- "the experiments used..."
- "the method is trained with..."
- "the repository provides an end-to-end workflow..."

unless the necessary active-path evidence is available.

This applies when:

- only one or a few files are available
- configs are missing
- entry scripts are missing
- code depends on private packages
- training parameters are supplied by an external platform
- README claims exceed the inspected implementation
- notebooks show results without a reproducible execution path
- the repository is too large for complete inspection

Ask for additional code only when the missing evidence is necessary for the requested output. Otherwise, produce a conservative partial answer using the inspected evidence and flag the limitation.

## Narrow Methods from Partial Code

If the user asks for a Methods section but only partial code is available, write only a narrow Methods description supported by the provided or inspected code.

For example, if only `model.py` is available:

- describe the model architecture only if supported by the file
- do not invent data loading, training, inference, or evaluation details
- do not describe the full pipeline
- include a limitation or author-check note that training, evaluation, and data processing could not be verified from the provided files

Allowed:

> "The provided code defines the model architecture..."

Not allowed:

> "The model was trained using..."

> "The evaluation used..."

> "The pipeline processed the data by..."

unless those paths are present and inspected.

## Handling Inferred Claims

Inferred claims must stay cautious unless confirmed by the user or authors.

Allowed wording:

- "The code suggests that..."
- "The workflow appears to..."
- "Based on the inspected call path, the pipeline likely..."
- "This module appears to be responsible for..."
- "The available implementation suggests..."

Do not convert inferred evidence into deterministic wording such as:

- "the pipeline performs..."
- "the model uses..."
- "the method relies on..."
- "the experiments used..."

unless the user or authors confirm the interpretation, or direct-active evidence is found.

## Material Inferred Claims

Only material inferred claims require a risk report.

A material inferred claim is one that affects interpretation of:

- method design
- workflow behavior
- reproducibility
- training procedure
- inference behavior
- evaluation protocol
- metrics or baselines
- scientific interpretation
- result generation
- reviewer-facing or publication-facing claims

The following contexts make inferred claims material by default:

- manuscript Methods
- Supplementary Methods
- reviewer responses
- README installation or usage instructions
- evaluation protocols
- benchmark descriptions
- figure or result-generation descriptions
- reproducibility instructions
- claims about default package or CLI behavior

In manuscript-facing, reviewer-facing, README usage, and reproducibility contexts, treat implementation claims as material by default unless they are clearly local, auxiliary, and unrelated to method behavior or user execution.

Minor inferred claims may remain in prose with cautious wording without a separate risk report.

Example of a minor inferred claim:

> "This helper appears to format intermediate outputs."

Example of a material inferred claim:

> "The workflow appears to perform cross-validation during evaluation."

The second claim affects evaluation interpretation and should trigger a risk note unless direct-active evidence is found or the author confirms it.

## Handling Weak or Unsupported Claims

Weak claims should usually be omitted from final prose.

Unsupported claims must not appear as factual statements.

If the unsupported claim is important to the user's goal, surface it as an author check.

Example:

```text
Author check
- The draft says that the pipeline performs cross-validation, but I found no direct-active evaluation script or configuration evidence. Confirm this before including the claim.
```

Unsupported claims may be replaced with:

- a more generic statement
- attribution to the provided text
- an omission
- a risk note
- an author-check question

## Handling Conflicts

If source code, documentation, manuscript text, README text, comments, or user-provided claims conflict:

1. State the conflict.
2. State what the inspected code directly supports.
3. State what the draft or documentation claims.
4. Recommend a conservative revision.
5. Ask the author to confirm whether the code or text is outdated.

Do not silently resolve conflicts in favor of the more polished, more impressive, or more publication-friendly version.

Example:

```text
Implementation-risk notes
- Claim: The README says the training uses Adam.
  Evidence level: conflicting
  Why it is risky: The inspected training code appears to instantiate AdamW instead.
  Recommended action: Revise the claim to AdamW if the inspected code is current, or confirm whether README or code is outdated.
```

## Default Evidence Handling

Maintain an internal claim-evidence map while drafting or revising. This map does not need to be shown to the user by default.

Show evidence notes, a risk report, or an evidence ledger only when needed.

When all material implementation claims are directly supported and no major ambiguity is found, the final answer may omit the evidence ledger.

Do not expose internal evidence maps unless the user requests verification, audit, evidence, or line-by-line review, or unless risk reporting is required.

When evidence or risk notes are shown, prefer repository-relative paths such as `src/model.py` over absolute local paths.

## User Requests to Hide Risk

The user may request not to show a full evidence ledger.

The user may not request that material risk be hidden.

If an unsupported material claim, material conflict, or material inferred claim affects the final output, include at least a brief author-check note, limitation note, or implementation-risk note.

Do not silently include unsupported material claims as facts.

## Mandatory Risk Report Conditions

Show a concise risk report when any of the following occurs:

- an unsupported material claim appears in the user-provided text and remains relevant to the task
- a material inferred claim is retained in the final prose
- source code and documentation conflict on a material implementation point
- code is incomplete but the user asks for a repository-wide or workflow-wide description
- the user asks for code-grounded writing but no relevant code can be inspected
- a high-risk term is used without strong evidence
- a key active-path, workflow, default-behavior, result-generation, or publication-facing
  implementation detail cannot be traced to direct-active evidence
- the user explicitly requests audit, verification, evidence, or line-by-line review

Do not show a risk report merely because every minor implementation detail lacks exhaustive repository-wide verification.

## Risk-Only Reporting

By default, do not show a full evidence ledger. Show only risks.

Default format:

```text
Implementation-risk notes
- Claim:
  Evidence level:
  Why it is risky:
  Recommended action:
```

The risk report should focus only on claims that are:

- material and inferred
- weak
- unsupported
- conflicting
- dependent on incomplete code inspection
- dependent on high-risk terminology
- likely to affect reproducibility, evaluation, or scientific interpretation

## High-Risk Terms Requiring Strong Evidence

The following terms require strong evidence and should not be used casually:

- "novel"
- "first"
- "state-of-the-art"
- "robust"
- "fully automated"
- "end-to-end"
- "reproducible"
- "clinically validated"
- "mechanistically demonstrates"
- "significantly improves"
- "comprehensive"
- "generalizable"
- "validated across"
- "production-ready"
- "scalable"
- "benchmark-leading"

Code evidence may support implementation-related terms only when the inspected active path demonstrates them.

For example:

- "end-to-end" requires evidence that the inspected workflow covers the claimed process from input to output.
- "fully automated" requires evidence that the claimed workflow does not depend on unmentioned manual intervention.
- "reproducible" requires evidence such as fixed configs, documented commands, environment or dependency files, seeds where relevant, and reproducible scripts.
- "state-of-the-art", "significantly improves", and "validated across" require result-level evidence, not code alone.
- "clinically validated" requires clinical validation evidence, not code alone.

If strong evidence is not available, omit the term or replace it with a narrower factual statement.

## Writing Rules

### Direct-Active Evidence

When evidence is direct-active, factual implementation language is allowed.

Allowed:

- "The pipeline reads..."
- "The model consists of..."
- "The training script optimizes..."
- "The evaluation code computes..."

### Direct-Local Evidence

When evidence is direct-local, use repository-inclusion language.

Allowed:

- "The repository includes..."
- "The codebase defines..."
- "The module implements..."
- "An optional utility is provided for..."

Not allowed:

- "The main pipeline uses..."
- "The experiments used..."
- "The method relies on..."
- "The results were generated with..."

### Author-Confirmed Claims

When a claim is author-confirmed but not code-verified, it may be used if appropriate for the task, but verification status must not be overstated.

Allowed:

- "According to author confirmation, ..."
- "The authors confirmed that ..."
- "This point was not independently verified in the inspected code."

Not allowed:

- presenting author-confirmed information as direct-active code evidence
- claiming the code demonstrates the point when code was not inspected or did not establish it

### Inferred Evidence

When evidence is inferred, use cautious language.

Allowed:

- "The workflow appears to..."
- "The code suggests..."
- "This module is likely used to..."
- "Based on the inspected path..."

### Weak Evidence

When evidence is weak, avoid factual prose and use author-check language.

Allowed:

- "The documentation states..., but implementation evidence was not found."
- "This appears to be intended, but the executable path is unclear."
- "Author confirmation is needed before including this claim."

### Unsupported Evidence

Do not write unsupported claims as facts.

Replace them with:

- a more generic statement
- attribution to the provided source
- omission
- a risk note
- an author-check question

## Attribution Rules When Code Is Not Inspected

When code is not inspected and the task is to summarize, polish, translate, or restructure provided text, attribute implementation claims to the provided text when needed.

Allowed:

- "The README describes the package as supporting batch inference."
- "The draft states that the model uses five-fold cross-validation."
- "The provided text describes an end-to-end workflow."

Not allowed without inspection:

- "The package supports batch inference."
- "The model uses five-fold cross-validation."
- "The workflow is end-to-end."

## Reviewer Response and Manuscript Use

For reviewer responses, manuscript Methods, and Supplementary Methods, be especially conservative.

Do not add implementation details to satisfy reviewer expectations unless they are supported by direct-active evidence or confirmed by the authors.

In these contexts, inferred claims are material by default unless clearly minor and unrelated to method behavior, reproducibility, evaluation, or result interpretation.

When a reviewer asks about implementation details and code evidence is incomplete, provide a conservative answer and include an author-check note.

For publication-facing writing, prefer precise but narrow claims over broad claims.

## README Installation and Usage Claims

README installation and usage sections are high-impact because users may rely on them to run the software.

Claims about installation, command-line options, default behavior, supported inputs, supported outputs, environment setup, dependencies, and reproducibility require direct-active or clearly verified evidence.

Inferred claims in README installation or usage instructions are material by default.

If verification is not performed, preserve existing claims without strengthening them and consider attribution or limitation wording where appropriate.

## Evaluation Protocol Claims

Evaluation protocol claims are material by default.

Claims about metrics, baselines, cross-validation, holdout sets, benchmarks, statistical tests, aggregation, thresholds, or result selection require direct-active evidence or manuscript-level result evidence, depending on the claim.

Do not infer evaluation protocol from file names such as `eval.py`, `metrics.py`, or `cross_validation.py` alone.

## Figure and Plotting Claims

When describing how a figure or result was generated, require evidence from:

- plotting scripts
- notebooks tied to result generation
- result aggregation code
- saved configuration
- figure-generation commands
- manuscript result files, when available

Do not infer plotting, smoothing, filtering, normalization, aggregation, or statistical comparison procedures from figure appearance alone.

Figure and result-generation claims are material by default.

## Reproducibility Claims

Claims about reproducibility require more than the presence of code.

Strong reproducibility evidence may include:

- documented commands
- dependency files
- environment files
- fixed configurations
- seeds where relevant
- workflow scripts
- input/output specifications
- tests or examples
- versioned data references, when appropriate

Without such evidence, avoid terms such as "reproducible", "fully reproducible", or "push-button reproducible."

Reproducibility claims are material by default.

## Privacy and Security

Do not include in user-facing prose:

- absolute local paths
- API keys or access tokens
- credentials
- private server names
- unpublished dataset locations
- usernames
- passwords
- patient or participant identifiers
- internal institutional storage paths
- private cloud bucket paths
- private database names or connection strings

Use generic descriptions when needed.

Examples:

- Replace `/home/user/private/project/data/raw_patients` with "a local data directory."
- Replace private bucket paths with "private cloud storage."
- Replace usernames with "the local environment."

Evidence notes may use repository-relative file paths when they do not expose private information.

## Minimal Acceptance Standard

A response satisfies this guardrail when:

- material implementation claims are checked against appropriate evidence when verification is required
- direct-active, direct-local, author-confirmed, inferred, weak, and unsupported claims are treated differently
- unsupported specificity is omitted, generalized, attributed, or flagged
- conflicts between code and text are reported when material
- material risks are not hidden, even if the user does not want a full evidence ledger
- risk notes are shown only when required or requested
- final prose does not claim more than the inspected evidence supports
- code inspection depth matches claim scope rather than document type alone
- explanations of provided code do not expand into unsupported repository-wide or pipeline-wide claims

## Reviewer Standard

The final writing should survive this question:

> Where is this implementation claim supported?

For every material implementation claim, the answer should be one of:

- supported by direct-active evidence
- limited to direct-local repository-inclusion language
- author-confirmed but not independently code-verified
- cautiously worded as inferred
- attributed to the source text
- flagged for author confirmation
- omitted because it is unsupported
