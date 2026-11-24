# Contributing

This guide covers development setup, document structure, validation, and contribution practices for Wrap Up, Tune Up, and Follow Up.
It serves human contributors and AI agents.
See the [README](README.md) for user-facing behavior and setup, and [Design boundaries](docs/design.md) for the constraints that changes must preserve.

## Development setup

This repository contains Markdown skill packages, documentation, and an optional personal-store setup helper.
A text editor and Git are sufficient for ordinary skill edits.
The helper and its standard-library tests require Python 3.11 or later.
Optional skill-authoring validators may have their own dependencies.

Work in the authoritative repository checkout and inspect staged, unstaged, and untracked changes before editing.
For an AEM-managed checkout, use AEM's source-discovery interface to confirm the source before editing.
Do not edit an unverified installed copy.

## Editing and documentation

Keep user-facing usage in the README and detailed setup in its linked [setup guide](docs/store-setup.md).
Keep contribution practices here, contributor invariants in [Design boundaries](docs/design.md), and executable agent procedures in skill packages.

Link to the authoritative procedure instead of maintaining competing copies of detailed execution rules.
Update affected documentation with behavior, setup, configuration, or compatibility changes.
Keep new guidance focused on decisions that need it, avoiding blanket rules derived from one incident or speculative future infrastructure.
Preserve English documentation and the existing Markdown style.

Use relative links and keep packaged references resolvable when a skill is installed alone.
When changing home-relative discovery, path interpretation, or optional tooling, account for Windows and WSL separately.
Do not assume a shared home or automatically translate configured absolute roots between environments.

## Markdown structure

The repository's Markdown follows the [mddt](https://github.com/mirinae3145/mddt) skill, from an installed copy or a checkout of the mddt repository.
Start from its [entry](https://github.com/mirinae3145/mddt/blob/main/skills/mddt/SKILL.md), which says which reference documents each task needs.

For Markdown changes, follow its [writing procedure](https://github.com/mirinae3145/mddt/blob/main/skills/mddt/references/writing.md).
Place content in the document tree before writing it, and reread each changed topic whole once it settles.
Sentence-only corrections and formatting changes that leave the structure as it was need no placement plan.
To find or verify information in these documents, follow its [reading procedure](https://github.com/mirinae3145/mddt/blob/main/skills/mddt/references/reading.md).

The repository adds these specifics:

- **Document trees**: The README is the collection overview, and each skill's `SKILL.md` is the entry of an independently installed tree.
  [Editing and documentation](#editing-and-documentation) says which content belongs in the README, the guides under `docs/`, this guide, and the skill packages.
- **Store templates**: `templates/store/` is copied into a separate personal store whose document tree and record format differ.
  `.mddtignore` leaves it out of every document check, while the helper's tests still cover it.
- **Role of the checker**: Writers and reviewers judge placement, kinds, and summaries, which the checker does not decide.
  A run without errors is the minimum, not evidence that a document conforms.
  When a change keeps a warning after judgment, say why in the review description.

## Licenses

Every tracked file is covered by an annotation in `REUSE.toml`.
The store helper and its tests are MIT, documentation and skill packages are CC BY 4.0, and the store templates and repository configuration are CC0.
Place a new file under a covered path, or add it to the matching annotation.
Running `uvx reuse@6.3.0 lint` from the [REUSE tool](https://reuse.software/) confirms that every file is covered.

## Validation

Match checks to the changed behavior and report structural checks, scenario review, and actual execution separately.
The repository has helper tests but no automated suite for agent behavior.
Do not present manual scenario review as an agent execution test.

- **Skill structure**: For changed skill instructions, use an available skill validator to check frontmatter, naming, and unfinished scaffold content.
  When `skill-creator` is available, locate its `scripts/quick_validate.py` and set `skill_validator` to that path.
  Run `python3 "$skill_validator" skills/wrap-up`, substituting `skills/tune-up` or `skills/follow-up` for the affected package.
  The validator needs Python 3 and PyYAML.
  Report unavailable tooling rather than claiming the check passed.
- **Package links**: Check local Markdown links and confirm required skill references resolve within each package independently of sibling or repository-root files.
- **Diff hygiene**: Run `git diff --check`, and `git diff --cached --check` when staging a contribution.
  Inspect new untracked files as well, since ordinary diff checks omit them.
- **Behavior**: For behavioral changes, review or exercise realistic requests covering the affected decisions rather than matching headings or prescribed wording.
- **Store helper**: For changes affecting the helper or its templates, run `python -m unittest discover -s tests` from the repository root.
- **Document structure**: For Markdown changes, run `uv run <mddt-skill-dir>/scripts/mddt.py .` from the repository root after rereading as [Markdown structure](#markdown-structure) describes.
  Replace `<mddt-skill-dir>` with the installed skill directory or a checkout's `skills/mddt`, and add `--review` after adding child documents.

## Scenario review

Select scenarios affected by the contribution from examples such as these:

| Area | Scenarios |
| --- | --- |
| Closeout | Finish versus handoff requests; case recording with and without authorization; unavailable stores. |
| Guidance updates | Case-derived versus direct updates; analysis-only versus application requests; new rules or skills; installation manager available, absent, or failing source discovery. |
| Storage and assessment | Alternate layouts; duplicate incidents; counterexamples; unknown guidance versions or model identity; a severe single incident; uncertain exposure to a prior change. |
| Follow Up | An observation question with no handoff; no relevant observation opportunity; preparation without execution; a handoff superseded by current artifacts. |

Documentation-only changes do not require re-running unrelated behavior checks.
Use isolated fixtures for execution tests so they do not alter real stores, instructions, installations, or external state.

## Submitting changes

Keep contributions scoped to a coherent behavior or documentation change and review the complete diff, including new files, before committing.
Use a concise commit subject and explain non-obvious intent, compatibility implications, and relevant validation in the body.
Keep change-specific validation results and limitations in the commit message or review description, rather than appending them to this guide as durable requirements.

Attribute AI-assisted contributions with an appropriate co-author when applicable.
Summarize resulting behavior and material limits for reviewers, and distinguish unfinished follow-ups from completed work.
Committing, publishing, and installing are separate actions with their own authorization.
Permission to contribute does not authorize all of them.
