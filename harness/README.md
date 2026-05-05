# nature-skills harness

This harness is a small standard-library Python engine for local skill operations:

- discover every `nature-*` skill folder
- read `SKILL.md` frontmatter without external YAML dependencies
- validate required files, internal Markdown links, reference discoverability, and generated artifacts
- rank skills for a user request using README trigger keywords and frontmatter text
- assemble a launch prompt for a selected skill

## README source of truth

The harness is intentionally anchored to the author's existing README structure. It reads
the root `README.md` Skill index for each skill's status, purpose, and trigger keywords,
and it also uses each skill's own `README.md` as matching context.

This means the harness should not replace or override the human-authored documentation.
When a skill is added or substantially changed, update the README entries first, then use
the harness to validate that the machine-readable launch surface still matches the
author-facing documentation.

## Commands

```bash
python harness/skill_engine.py list
python harness/skill_engine.py validate
python harness/skill_engine.py match "数据可用性声明怎么写"
python harness/skill_engine.py launch nature-paper2ppt --request "把这篇论文做成文献汇报PPT"
```

Include selected references in a launch prompt:

```bash
python harness/skill_engine.py launch nature-polishing \
  --request "Polish this abstract" \
  --reference writing-strategy.md \
  --reference style-guardrails.md
```

The harness does not call an LLM by itself. It creates the deterministic project layer
around the skills so a model host, CLI wrapper, or future API service can select and load
the right skill consistently.
