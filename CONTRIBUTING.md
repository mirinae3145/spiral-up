# Contributing

This guide covers development setup, validation, and contribution practices for Wrap Up, Tune Up, and Follow Up.
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

When mddt is available, run its `scripts/mddt.py . --review --exclude 'templates/store/**'` from the repository root to check the document tree.
Exclude store templates from document-structure checks because they are assets copied into a separate document tree.
Keep those templates in the helper's validation scope.

## Scenario review

Select scenarios affected by the contribution from examples such as these:

| Area | Scenarios |
| --- | --- |
| Closeout | Finish versus handoff requests; case recording with and without authorization; unavailable stores. |
| Guidance updates | Case-derived versus direct updates; analysis-only versus application requests; new rules or skills; AEM available, absent, or failing source discovery. |
| Storage and assessment | Alternate layouts; duplicate incidents; counterexamples; unknown guidance versions; uncertain exposure to a prior change. |
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
