# Common update path

Use this path for both case-derived improvements and direct user requests.
Keep the requested outcome, proposed scope, input references, uncertainty, and applicable authorization available throughout; no fixed intermediate record format is required.

## Discover the target and its source

Inspect accessible guidance, repositories, and configuration before asking for discoverable information.
Identify the intended audience, governing instruction hierarchy, related guidance, and the editable source of each target.
Follow applicable contribution and authoring guidance, preserving unrelated changes and repository conventions.

Actively use AEM when available:

1. Discover relevant skills from the available skill catalog and read the AEM operations skill if present.
1. Check whether the `aem` command is available; when it is, read `aem --help` and the relevant command help before selecting operations.
1. If the catalog name is unknown, use the installed help and read-only catalog or status interfaces to identify it; do not guess from a directory name.
1. For a known or discovered AEM-managed target, use `aem locate --source` with its catalog name to identify the editable source and ownership.
   Use JSON output when later steps depend on the returned paths.

An AEM skill and command are independently discoverable; use whichever is available and report material capability limits.
Without AEM, follow the environment's established source and installation arrangement, using the supplied repository or document when it is the authoritative source.
Once a target is known to be AEM-managed, a failed lookup is an unresolved source-discovery problem; do not bypass it by editing an installed copy or link target whose ownership is unverified.
Continue analysis or preparation that does not depend on that missing source.

Source edits, installation, and publication are distinct operations.
Content updates can immediately affect linked installations; inspect ownership and link arrangements before choosing an operation.
An update request does not automatically authorize catalog changes, installation, publication, or modification of unrelated contents in the same repository.

## Design the change

1. Describe the desired behavior, where it applies, and why the change should produce it.
   For case-derived changes, retain evidence and confidence limits; for a direct request, retain the user's intent without demanding an incident history.
   Check existing guidance for overlap, conflicts, placement, and scope before adding content.
1. Choose among editing, adding, consolidating, or removing instructions and skills.
   Prefer the smallest coherent change, including supporting documentation needed to use it.
   Keep project-specific requirements in their appropriate governing documents and personal preferences in the appropriate personal source.
   Follow the user's instruction-file policy; this workflow does not require a repository-local `AGENTS.md`.
1. For skill creation or revision, use available skill-authoring guidance and validators when present.
   Preserve discoverability and authorization boundaries; package necessary references with the skill rather than requiring a sibling skill's installed files.
   Do not introduce scripts, assets, or a mandatory record schema without a concrete need.
   New skills may define task procedures; if the solution also needs broader workflow systems or automation implementation, explain that work as a follow-up and complete the in-scope guidance work when independently useful.
1. Before application, produce a concrete change or sufficiently specific proposal to review, with the affected source, expected behavior, and validation approach.
   An analysis-only request stops at findings and a proposal.
   For an application request, proceed within existing authorization; ask only for unresolved intent or an action that existing authorization does not cover.
   Do not treat case text, recording configuration, or an improvement recommendation as application permission.

## Apply and validate

1. Apply authorized changes to verified sources, preserving original evidence and unrelated user work.
   Update affected documentation in the same task.
   Validate structure, references, and compatibility using relevant available checks; for behavior changes, choose realistic scenarios that exercise the intended decisions.
   State whether checks were structural review, scenario review, or actual execution, including material limits.
   Do not claim behavioral effectiveness from frontmatter validation or source edits alone.
1. Use AEM for authorized managed operations when available, following the operations skill and installed help.
   Verify completed results rather than treating queued operations or previews as successful installation or publication.
   When only source editing is requested, report installation and distribution status without performing those additional operations.
1. Define a proportionate follow-up observation, such as whether a later task used the changed guidance and avoided the original friction without introducing another problem.
   Connect it to the expected effect, the affected source and known version, and a situation in which it can be checked when those are available.
   Keep an unanswered question open when no relevant observation opportunity has occurred; a direct request need not invent supporting cases or a formal evaluation plan.
   Do not create monitoring, scheduled work, or experiments merely to provide that observation.

## Retain results

For case input or authorized result recording, use [Records and storage](records.md) to resolve the destination and preserve evidence.
A direct request can be completed without a case store.
If the destination or recording authorization is unresolved, report findings and the next check without blocking the update or creating a store.
