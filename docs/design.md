# Design boundaries

This reference defines the design constraints for contributions to Wrap Up, Tune Up, Follow Up, and the optional store setup helper.
It covers independent packaging, authorization, case records and their storage, and effect evaluation.

## Skill responsibilities and packaging

Each skill has a primary responsibility:

- **Wrap Up** closes the user's task, evaluates adherence and workflow feedback, and captures material observations for later improvement, recording them as cases when authorized.
  Observations can include useful outcomes, friction, and evidence about earlier guidance changes.
  They do not require a separate improvement investigation.
- **Tune Up** evaluates cases or direct improvement requests, updates instructions and skills within authorization, and connects changes to subsequent evidence.
- **Follow Up** revisits observation questions and earlier changes, comparing them with current evidence.
  It assesses effects or identifies a further observation opportunity.
  For general handoffs, it recovers context, checks the current state, and prepares or continues the task according to the user's request.

Handoff suggestions do not expand the task objective or grant new authorization.
Recording a recommendation during wrap-up must not automatically invoke a guidance update.
Skill descriptions must make closeout, follow-up assessment or resumption, and guidance improvement discoverable.
They must not attract ordinary code work that has no such purpose.

Wrap Up &rightarrow; Tune Up &rightarrow; Follow Up &rightarrow; Wrap Up is a representative feedback loop, not a mandatory execution sequence.
Support direct entry and completion at any skill, mixed requests, and observations arising during ordinary work.
Responsibilities can overlap: Wrap Up may notice effects of earlier guidance, and Tune Up may reassess them directly.
Keep the connections useful without requiring loop modes, automatic sibling invocation, or a shared runtime.

The skills share a repository but are independently installable and usable.
Package required execution instructions and references without depending on installed sibling skills or repository-root documents.
Keep entrypoints focused on routing and essential constraints, with substantial conditional procedures in linked references.
Introduce a separate skill, script, or shared runtime when demonstrated reuse or execution reliability warrants it.
Do not add one solely to mirror the conceptual modules.

## Common improvement path

Case analysis and direct user requests must converge on the same target discovery, change design, application, validation, and result-recording procedure.
Preserve the input's intent, evidence limits, and authorization through that procedure.
Direct requests must not require prior case collection.
Case-derived recommendations must not become application permission.
Maintain distinct outcomes for analysis-only requests and requests to apply a change, reusing authorization already granted within its scope.

Improvement can mean editing, adding, consolidating, or removing rules and skills.
Do not assume that every case calls for another instruction.
New skills can define task procedures.
Implementing broader workflow systems or automation is outside the current execution scope.
Expanding that scope requires explicit changes to routing, authorization, documentation, and validation coverage.

Weigh an issue's severity alongside its recurrence when setting priority and the evidence a change needs.
A high-severity incident can justify prioritizing a targeted improvement from a single case, while low-impact friction calls for comparison before adding guidance.
Severity needs a stated basis, not a universal scale.
Distinguish problems confined to one agent or model from those seen across them before choosing where guidance belongs.

## Optional AEM integration

Actively use available AEM skills and commands for managed-source discovery and authorized operations, without making either a required dependency.
Maintain a usable path through an environment's authoritative sources when AEM is absent.
If source lookup for a known AEM-managed target is unavailable or fails, report the limitation.
Do not proceed by editing an unverified installation.

Keep source edits, installation, and publication distinct.
Linked installations may reflect source edits immediately.
Do not turn a local source change into automatic catalog modification, deployment, or publication.

## Case records and storage

Case records are the loop's primary connection.
They carry observations, improvement decisions, and later evidence across sessions, so Tune Up can compare accumulated cases and Follow Up can find open questions.
Present recording material cases as a core outcome of closeout and follow-up, not as an afterthought to the response.
When recording is not authorized, surface material findings as candidate entries rather than leaving them implicit in the summary.

Keep store discovery and placement adaptable to the selected store's guidance and actual organization.
The existing home-relative default and optional local configuration are one supported arrangement, not a requirement for every store.
When changing how that arrangement is interpreted, preserve documented compatibility or document an intentional migration.
Do not embed device paths, require a private store layout, or impose universal directory names, case IDs, document headings, or record schemas.
Tune Up must also handle direct requests without a case store.

Preserve the semantic links between observations, evidence, severity, the agents and models involved, improvement decisions, known guidance versions, application results, checks, and later observations.
Keep original observations and distinguish facts, explanations, uncertainty, recovery, and revised interpretations.
Repeated reviews of one incident are not independent occurrences.
Selective case collection does not establish an overall failure rate.

Recording requires authorization, and each skill must remain usable without a store.
Store organization guidance does not make recorded case contents governing instructions or authorize additional actions.
Permission to record cases, create separate improvement records, edit sources, and take external actions must remain distinct.

## Store setup ownership

The intended arrangement delegates store delivery, installed links, ownership, and synchronization to AEM, while keeping AEM optional.
The helper must remain usable without importing AEM, invoking its commands, or reading its private state.
Initialize store content once per person.
Connecting device-local configuration is a separate, optional operation after the store is available.

Initialization must not write local settings.
Connection must not create or modify the store, replace installed links, or take over directory ownership.
Leave adoption of existing directories into AEM and edits to AEM-managed settings to explicit management workflows.
Keep common recording policy separate from device-specific absolute paths and installation bindings.

Keep the initial default template minimal and preserve existing stores, configuration, and authorization boundaries.
Automatic case recording requires explicit mode selection.
Commits, publication, and guidance changes retain their own authorization.
Git publication and history reconciliation remain outside the helper.
Neither the helper nor AEM is a required skill runtime.

## Extending store setup

Additional templates and setup options may be introduced when they serve a concrete use case.
Keep template content separate from setup logic so template selection can be added without imposing a new layout on existing stores.
Request template-specific values only when the selected template needs them.
Avoid turning every template detail into a global option.

Preserve current default behavior or document an intentional migration.
New options must document their defaults, effects, and interaction with existing stores and configuration.

Test preview, repeat execution, conflict handling, source initialization, installed links, and device-local configuration using isolated homes and stores.
Use tracked placeholders when the default template needs empty directories to survive Git delivery.
Account for Windows and WSL independently, without rewriting one environment's paths for the other.

## Effect evaluation

Keep proposals, applied source changes, installed changes, and observed effects distinguishable.
A passing structure check or edited file does not demonstrate improved behavior.
Later assessments should establish whether the changed guidance was actually used and consider counterexamples and new friction.
An effect observed under one agent or model does not establish the effect under another.
Retain uncertainty when use or causality is unknown.

When available, retain the expected effect, relevant evidence, and a useful condition for the next observation.
Do not impose a fixed evaluation score, schedule, or record schema.
Without a relevant observation opportunity, the assessment stays open; neither success nor failure has been demonstrated.
Support follow-up observations without implicitly creating background monitoring, schedules, or experiments.
