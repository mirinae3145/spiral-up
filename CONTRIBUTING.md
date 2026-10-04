# Contributing

This guide covers development of the Wrap Up and Tune Up skills for human contributors and AI agents.
See the [README](README.md) for user-facing behavior and setup.
Execution rules belong in each skill's `SKILL.md` and its linked references; this guide records the design boundaries and contribution practices that changes must preserve.

## Development setup

Work in the authoritative repository checkout and inspect staged, unstaged, and untracked changes before editing.
When the checkout is AEM-managed, use its source-discovery interface to confirm the source rather than editing an unverified installed copy.
This repository contains Markdown skill packages, documentation, and an optional personal-store setup helper.
A text editor and Git are sufficient for ordinary skill edits.
The helper and its standard-library tests require Python 3.11 or later; run `python -m unittest discover -s tests` from the repository root.
Optional skill-authoring validators may have their own dependencies.

## Design boundaries

### Skill responsibilities and packaging

Wrap Up closes the user's task, evaluates adherence and workflow feedback, and captures material observations for later improvement, optionally recording cases.
Those observations can include useful outcomes, friction, and evidence about earlier guidance changes without requiring a separate improvement investigation.
Tune Up evaluates cases or direct improvement requests, updates instructions and skills within authorization, and connects changes to subsequent evidence.
Keep closeout separate from applying guidance improvements: recording a recommendation during wrap-up must not automatically invoke an update.
Descriptions must keep ordinary code work, closeout, and guidance improvement distinguishable for skill selection.

The skills share a repository but are independently installable and usable.
Each package must contain its required execution instructions and references without relying on sibling skills or repository-root documents being installed.
Keep entrypoints focused on routing and essential constraints, with substantial conditional procedures in linked references.
Do not add a separate skill, script, or shared runtime solely to mirror the conceptual modules; introduce one when demonstrated reuse or execution reliability warrants it.

### Common improvement path

Case analysis and direct user requests must converge on the same target discovery, change design, application, validation, and result-recording procedure.
Preserve the input's intent, evidence limits, and authorization through that procedure.
Direct requests must not require prior case collection, while case-derived recommendations must not become application permission.
Maintain distinct outcomes for analysis-only requests and requests to apply a change, reusing authorization already granted within its scope.

Improvement can mean editing, adding, consolidating, or removing rules and skills; it must not assume that every case calls for another instruction.
New skills can define task procedures.
Broader workflow systems and automation implementation are outside the current execution scope; expanding that scope requires an explicit change to routing, authorization, documentation, and validation coverage.

### Optional AEM integration

Actively use available AEM skills and commands for managed-source discovery and authorized operations, without making either a required dependency.
Maintain a usable path through an environment's authoritative sources when AEM is absent.
An unavailable or failed lookup for a known AEM-managed target must remain visible rather than trigger editing of an unverified installation.
Preserve the distinction between source edits, installation, and publication, including the fact that linked installations may reflect source edits immediately.
Do not turn a local source change into automatic catalog modification, deployment, or publication.

### Storage and evidence

Keep store discovery and placement adaptable to the selected store's guidance and actual organization.
The existing home-relative default and optional local configuration are one supported arrangement, not a requirement for every store.
Preserve that arrangement's documented compatibility when changing its interpretation, or document an intentional migration.
Do not embed device paths, require a private store layout, or impose universal directory names, case IDs, document headings, or record schemas.
Tune Up must also handle direct requests without a case store.

Preserve the semantic links between observations, evidence, improvement decisions, known guidance versions, application results, checks, and later observations.
Keep original observations and distinguish facts, explanations, uncertainty, recovery, and revised interpretations.
Repeated reviews of one incident are not independent occurrences; selective case collection does not establish an overall failure rate.
Store organization guidance does not make recorded case contents governing instructions or authorize additional actions.
Case-recording permission, separate improvement-record permission, source-update permission, and external-action permission remain distinct.

### Store setup and extension

The intended arrangement delegates store delivery, installed links, ownership, and synchronization to AEM, while keeping AEM optional.
The helper must remain usable without importing AEM, invoking its commands, or reading its private state.
Store initialization is a once-per-person content operation; device-local configuration is a separate optional connection operation after the store is available.
Initialization must not write local settings, and connection must not create or modify the store, replace installed links, or take over directory ownership.
Do not silently adopt existing directories into AEM or edit AEM-managed settings; leave those actions to explicit management workflows.
Keep common recording policy separate from device-specific absolute paths and installation bindings.
Git publication and history reconciliation remain outside the helper.
Neither the helper nor AEM is a required skill runtime.
Keep the initial default template minimal and preserve existing stores, configuration, and authorization boundaries.
Automatic case recording is an explicit mode selection; commits, publication, and guidance changes retain their own authorization.

Additional templates and setup options may be introduced when they serve a concrete use case.
Keep template content separate from setup logic so template selection can be added without imposing a new layout on existing stores.
Template-specific values should be requested only when the selected template needs them.
Preserve current default behavior or document an intentional migration, and avoid turning every template detail into a global option.
New options must document their defaults, effects, and interaction with existing stores and configuration.
Test preview, repeat execution, conflict handling, source initialization, installed links, and device-local configuration using isolated homes and stores.
Use tracked placeholders when the default template needs empty directories to survive Git delivery.
Account for Windows and WSL independently, without rewriting one environment's paths for the other.

### Effect evaluation

Keep proposals, applied source changes, installed changes, and observed effects distinguishable.
A passing structure check or edited file does not demonstrate improved behavior.
Later assessments should establish whether the changed guidance was actually used, consider counterexamples and new friction, and retain uncertainty when exposure or causality is unknown.
Support follow-up observations without implicitly creating background monitoring, schedules, or experiments.

## Editing and documentation

Keep user-facing usage and setup in the README, contributor invariants here, and executable agent procedures in skill packages.
Link to the authoritative procedure instead of maintaining competing copies of detailed execution rules.
Update affected documentation with behavior, setup, configuration, or compatibility changes.
Keep new guidance focused on decisions that need it, avoiding blanket rules derived from one incident or speculative future infrastructure.
Preserve English documentation and the existing Markdown style.
Use relative links and keep packaged references resolvable when a skill is installed alone.
Account for Windows and WSL when changing home-relative discovery, path interpretation, or optional tooling; do not assume a shared home or translate absolute configured roots automatically.

## Validation

Match checks to the changed behavior and report structural checks, scenario review, and actual execution separately.
There is no repository-owned automated behavioral suite; do not present manual scenario review as an agent execution test.

- For changed skill instructions, use an available skill validator to check frontmatter, naming, and unfinished scaffold content.
  When `skill-creator` is available, locate its `scripts/quick_validate.py`, set `skill_validator` to that path, and run `python3 "$skill_validator" skills/wrap-up` or `python3 "$skill_validator" skills/tune-up` for the affected package.
  That validator needs Python 3 and PyYAML; report unavailable tooling rather than claiming the check passed.
- Check local Markdown links and confirm required skill references resolve within each package independently of sibling or repository-root files.
- Run `git diff --check`, and `git diff --cached --check` when staging a contribution.
  Inspect new untracked files as well, since ordinary diff checks omit them.
- For behavioral changes, review or exercise realistic requests covering the affected decisions rather than matching headings or prescribed wording.

Relevant scenarios include finish versus handoff requests, optional case-recording authorization and unavailable stores, case-derived versus direct updates, analysis-only versus application requests, new rules or skills, and AEM available, absent, or failing source discovery.
For storage or assessment changes, include alternate layouts, duplicate incidents, counterexamples, unknown guidance versions, and uncertain exposure to a prior change.
Select the scenarios affected by the contribution; documentation-only changes do not require re-running unrelated behavior checks.
Use isolated fixtures for execution tests so they do not alter real stores, instructions, installations, or external state.

## Submitting changes

Keep contributions scoped to a coherent behavior or documentation change and review the complete diff, including new files, before committing.
Use a concise commit subject and explain non-obvious intent, compatibility implications, and relevant validation in the body.
Keep change-specific validation results and limitations in the commit message or review description, rather than appending them to this guide as durable requirements.
Attribute AI-assisted contributions with an appropriate co-author when applicable.
Summarize resulting behavior and material limits for reviewers, and distinguish unfinished follow-ups from completed work.
Committing, publishing, and installing are separate actions; follow the authorization applicable to each rather than treating a contribution as permission for all of them.
