# Contributing

This guide covers development of the Wrap Up, Tune Up, and Follow Up skills for human contributors and AI agents.
See the [README](README.md) for user-facing behavior and setup.
Execution rules belong in each skill's `SKILL.md` and its linked references.
This guide covers contribution practices; [Design boundaries](docs/design.md) explains the constraints that changes must preserve.

## Development setup

Work in the authoritative repository checkout and inspect staged, unstaged, and untracked changes before editing.
When the checkout is AEM-managed, use its source-discovery interface to confirm the source rather than editing an unverified installed copy.
This repository contains Markdown skill packages, documentation, and an optional personal-store setup helper.
A text editor and Git are sufficient for ordinary skill edits.

The helper and its standard-library tests require Python 3.11 or later; run `python -m unittest discover -s tests` from the repository root.
Optional skill-authoring validators may have their own dependencies.

## Editing and documentation

Keep user-facing usage in the README and detailed setup in its linked [setup guide](docs/store-setup.md).
Keep contribution practices here, contributor invariants in [Design boundaries](docs/design.md), and executable agent procedures in skill packages.

Link to the authoritative procedure instead of maintaining competing copies of detailed execution rules.
Update affected documentation with behavior, setup, configuration, or compatibility changes.
Keep new guidance focused on decisions that need it, avoiding blanket rules derived from one incident or speculative future infrastructure.
Preserve English documentation and the existing Markdown style.

Use relative links and keep packaged references resolvable when a skill is installed alone.
Account for Windows and WSL when changing home-relative discovery, path interpretation, or optional tooling; do not assume a shared home or translate absolute configured roots automatically.

## Validation

Match checks to the changed behavior and report structural checks, scenario review, and actual execution separately.
There is no repository-owned automated behavioral suite; do not present manual scenario review as an agent execution test.

- **Skill structure**: For changed skill instructions, use an available skill validator to check frontmatter, naming, and unfinished scaffold content.
  When `skill-creator` is available, locate its `scripts/quick_validate.py`, set `skill_validator` to that path, and run `python3 "$skill_validator" skills/wrap-up` or `python3 "$skill_validator" skills/tune-up` for the affected package.
  For Follow Up, use `skills/follow-up` as the package path.
  That validator needs Python 3 and PyYAML; report unavailable tooling rather than claiming the check passed.
- **Package links**: Check local Markdown links and confirm required skill references resolve within each package independently of sibling or repository-root files.
- **Diff hygiene**: Run `git diff --check`, and `git diff --cached --check` when staging a contribution.
  Inspect new untracked files as well, since ordinary diff checks omit them.
- **Behavior**: For behavioral changes, review or exercise realistic requests covering the affected decisions rather than matching headings or prescribed wording.

When mddt is available, run its `scripts/mddt.py . --review --exclude 'templates/store/**'` from the repository root to check the document tree.
Exclude store templates from document-structure checks because they are assets copied into a separate document tree.
Keep those templates in the helper's validation scope.

Relevant scenarios include finish versus handoff requests, optional case-recording authorization and unavailable stores, case-derived versus direct updates, analysis-only versus application requests, new rules or skills, and AEM available, absent, or failing source discovery.
For storage or assessment changes, include alternate layouts, duplicate incidents, counterexamples, unknown guidance versions, and uncertain exposure to a prior change.
For Follow Up, include an observation question with no handoff, no relevant observation opportunity, preparation without execution, and a handoff superseded by current artifacts.
Select the scenarios affected by the contribution; documentation-only changes do not require re-running unrelated behavior checks.
Use isolated fixtures for execution tests so they do not alter real stores, instructions, installations, or external state.

## Submitting changes

Keep contributions scoped to a coherent behavior or documentation change and review the complete diff, including new files, before committing.
Use a concise commit subject and explain non-obvious intent, compatibility implications, and relevant validation in the body.
Keep change-specific validation results and limitations in the commit message or review description, rather than appending them to this guide as durable requirements.

Attribute AI-assisted contributions with an appropriate co-author when applicable.
Summarize resulting behavior and material limits for reviewers, and distinguish unfinished follow-ups from completed work.
Committing, publishing, and installing are separate actions; follow the authorization applicable to each rather than treating a contribution as permission for all of them.
