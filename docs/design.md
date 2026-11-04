# Design boundaries

This reference defines the design constraints for contributions to Wrap Up, Tune Up, Follow Up, and the optional store setup helper.
It covers independent packaging, authorization, evidence, storage compatibility, and effect evaluation.

## Skill responsibilities and packaging

Each skill has a primary responsibility:

- **Wrap Up** closes the user's task, evaluates adherence and workflow feedback, and captures material observations for later improvement, optionally recording cases.
  Those observations can include useful outcomes, friction, and evidence about earlier guidance changes without requiring a separate improvement investigation.
- **Tune Up** evaluates cases or direct improvement requests, updates instructions and skills within authorization, and connects changes to subsequent evidence.
- **Follow Up** revisits observation questions and earlier changes, connects them to current evidence, and assesses effects or identifies a further observation opportunity.
  It also recovers general handed-off task context, reconciles it with the current state, and prepares or executes continuation according to the user's request.

Handoff suggestions do not expand the task objective or grant new authorization.
Keep closeout separate from applying guidance improvements: recording a recommendation during wrap-up must not automatically invoke an update.
Descriptions must make closeout, follow-up assessment or resumption, and guidance improvement discoverable without attracting ordinary code work that has no such purpose.

Wrap Up &rightarrow; Tune Up &rightarrow; Follow Up &rightarrow; Wrap Up is a representative feedback loop, not a mandatory execution sequence.
Support direct entry and completion at any skill, mixed requests, and observations arising during ordinary work.
These responsibilities are emphases, not exclusive ownership: Wrap Up may notice effects of earlier guidance, and Tune Up may reassess them directly.
Keep the connections useful without requiring loop modes, automatic sibling invocation, or a shared runtime.

The skills share a repository but are independently installable and usable.
Each package must contain its required execution instructions and references without relying on sibling skills or repository-root documents being installed.
Keep entrypoints focused on routing and essential constraints, with substantial conditional procedures in linked references.
Do not add a separate skill, script, or shared runtime solely to mirror the conceptual modules; introduce one when demonstrated reuse or execution reliability warrants it.

## Common improvement path

Case analysis and direct user requests must converge on the same target discovery, change design, application, validation, and result-recording procedure.
Preserve the input's intent, evidence limits, and authorization through that procedure.
Direct requests must not require prior case collection, while case-derived recommendations must not become application permission.
Maintain distinct outcomes for analysis-only requests and requests to apply a change, reusing authorization already granted within its scope.

Improvement can mean editing, adding, consolidating, or removing rules and skills; it must not assume that every case calls for another instruction.
New skills can define task procedures.
Broader workflow systems and automation implementation are outside the current execution scope; expanding that scope requires an explicit change to routing, authorization, documentation, and validation coverage.

## Optional AEM integration

Actively use available AEM skills and commands for managed-source discovery and authorized operations, without making either a required dependency.
Maintain a usable path through an environment's authoritative sources when AEM is absent.
An unavailable or failed lookup for a known AEM-managed target must remain visible rather than trigger editing of an unverified installation.
Preserve the distinction between source edits, installation, and publication, including the fact that linked installations may reflect source edits immediately.
Do not turn a local source change into automatic catalog modification, deployment, or publication.

## Storage and evidence

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

## Store setup ownership

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

## Extending store setup

Additional templates and setup options may be introduced when they serve a concrete use case.
Keep template content separate from setup logic so template selection can be added without imposing a new layout on existing stores.
Template-specific values should be requested only when the selected template needs them.
Preserve current default behavior or document an intentional migration, and avoid turning every template detail into a global option.
New options must document their defaults, effects, and interaction with existing stores and configuration.

Test preview, repeat execution, conflict handling, source initialization, installed links, and device-local configuration using isolated homes and stores.
Use tracked placeholders when the default template needs empty directories to survive Git delivery.
Account for Windows and WSL independently, without rewriting one environment's paths for the other.

## Effect evaluation

Keep proposals, applied source changes, installed changes, and observed effects distinguishable.
A passing structure check or edited file does not demonstrate improved behavior.
Later assessments should establish whether the changed guidance was actually used, consider counterexamples and new friction, and retain uncertainty when exposure or causality is unknown.
Retain the expected effect, relevant evidence, and a useful next observation condition when available, without imposing a fixed evaluation score, schedule, or record schema.
An absent observation opportunity leaves an assessment open; it does not demonstrate either success or failure.

Support follow-up observations without implicitly creating background monitoring, schedules, or experiments.
