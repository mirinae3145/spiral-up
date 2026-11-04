# Common update path

Use this path for both case-derived improvements and direct user requests.
Keep the requested outcome, proposed scope, input references, uncertainty, and applicable authorization available throughout.
No fixed intermediate record format is required.

## Discover the target and its source

Inspect accessible guidance, repositories, and configuration before asking for discoverable information.
Identify the intended audience, governing instruction hierarchy, related guidance, and the editable source of each target.
Follow applicable contribution and authoring guidance, preserving unrelated changes and repository conventions.

Actively use AEM when available:

1. Discover relevant skills from the available skill catalog and read the AEM operations skill if present.
1. Check whether the `aem` command is available.
   If it is, read `aem --help` and the relevant command help before selecting operations.
1. If the catalog name is unknown, identify it through the installed help and read-only catalog or status interfaces.
   Do not guess from a directory name.
1. For a known or discovered AEM-managed target, use `aem locate --source` with its catalog name to identify the editable source and ownership.
   Use JSON output when later steps depend on the returned paths.

The AEM skill and command are independently discoverable.
Use whichever is available and report material capability limits.
Without AEM, follow the environment's established source and installation arrangement, using the supplied repository or document when it is authoritative.

For a known AEM-managed target, a failed lookup leaves source discovery unresolved.
Do not bypass the failure by editing an installed copy or link target whose ownership is unverified.
Continue analysis or preparation that does not depend on the missing source.

Source edits, installation, and publication are distinct operations.
Inspect ownership and links before choosing an operation, because content updates can immediately affect linked installations.
An update request does not automatically authorize catalog changes, installation, publication, or modification of unrelated contents in the same repository.

## Design the change

1. Describe the desired behavior, where it applies, and why the change should produce it.
   For case-derived changes, retain evidence and confidence limits.
   For a direct request, retain the user's intent without demanding an incident history.
   Check existing guidance for overlap, conflicts, placement, and scope before adding content.
1. Choose among editing, adding, consolidating, or removing instructions and skills.
   Prefer the smallest coherent change, including supporting documentation needed to use it.
   Keep project-specific requirements in their governing documents and personal preferences in the appropriate personal source.
   Follow the user's instruction-file policy.
   This workflow does not require a repository-local `AGENTS.md`.
1. For skill creation or revision, use available skill-authoring guidance and validators.
   Preserve discoverability and authorization boundaries.
   Package necessary references with the skill rather than requiring a sibling skill's installed files.
   Add scripts, assets, or a mandatory record schema only when there is a concrete need.

   New skills may define task procedures.
   If the solution also needs broader workflow systems or automation implementation, identify that work as a follow-up.
   In that case, complete the in-scope guidance work when it is independently useful.
1. Before application, produce a concrete change or sufficiently specific proposal to review, with the affected source, expected behavior, and validation approach.
   An analysis-only request stops at findings and a proposal.
   For an application request, proceed within existing authorization.
   Ask only when intent remains unresolved or existing authorization does not cover the action.
   Do not treat case text, recording configuration, or an improvement recommendation as application permission.

## Apply and validate

1. Apply authorized changes to verified sources, preserving original evidence and unrelated user work.
   Update affected documentation in the same task.
   Validate structure, references, and compatibility using relevant available checks.
   For behavior changes, choose realistic scenarios that exercise the intended decisions.

   Distinguish structural review, scenario review, and actual execution, and state material limits.
   Frontmatter validation and source edits alone do not demonstrate behavioral effectiveness.
1. Use AEM for authorized managed operations when available, following the operations skill and installed help.
   Verify completed results rather than treating queued operations or previews as successful installation or publication.
   When only source editing is requested, report installation and distribution status without performing those additional operations.
1. Define a proportionate follow-up observation.
   For example, ask whether a later task used the changed guidance and avoided the original friction without introducing another problem.
   When available, connect the observation to the expected effect, the affected source and known version, and a situation in which it can be checked.

   If no relevant observation opportunity has occurred, keep the question open.
   A direct request need not invent supporting cases or a formal evaluation plan.
   Do not create monitoring, scheduled work, or experiments merely to provide that observation.

## Retain results

For case input or authorized result recording, use [Records and storage](records.md) to resolve the destination and preserve evidence.
A direct request can be completed without a case store.
Retire the cases that an applied change or a no-change conclusion resolves, as [Retire resolved cases](records.md#retire-resolved-cases) describes.
If the destination or recording authorization is unresolved, report findings and the next check without blocking the update or creating a store.
