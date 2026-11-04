# Closeout procedure

Check the actual final state against the requested outcome and complete the applicable closeout work.
Leave a verified result or a resumable handoff.
This procedure covers inspection, cleanup, documentation, validation, retrospective review, and handoff records.

## Complete the closeout

Apply these steps within the requested outcome and authorized scope:

1. **Inspect** &mdash; check every repository or location the task touched, not only the working directory.
   Inspect `git status`, staged and unstaged diffs, untracked files, and outputs outside Git.
   Also inspect external state the task changed, such as links, task trackers, and services.
   Earlier "done" or "tested" claims provide context; the actual state provides evidence.
   Finish inspection when every change is accounted for.
1. **Reconcile** &mdash; compare the evidence with the objective to identify completed work, missing work, and unrequested changes.
   Handle missing work according to the [requested outcome](../SKILL.md#scope-and-requested-outcome).
   List unrequested changes for the user to keep or revert.
1. **Clean** &mdash; only in the area the task worked in, using [Cleanup decisions](#cleanup-decisions) to classify each leftover.
1. **Update** &mdash; when completing the task, provide the documentation needed to use or maintain its changes.
   Cover changed behavior, setup, and configuration, following the project's document conventions.
   Leave unrelated pre-existing inaccuracies as follow-ups.
   For a summary-only handoff, report missing documentation as unfinished work.
1. **Validate** &mdash; establish the final state using the project's relevant checks and available results, then inspect `git status` when applicable.
   Reuse passing results when subsequent changes cannot affect them.
   Rerun affected checks after cleanup or further edits.
   For a new regression test, verify failure on the pre-fix code and success on the fix when feasible and meaningful.
   Distinguish passing checks from unverified regression coverage and report material validation limits.
1. **Review** &mdash; read and apply [Retrospective](retrospective.md) against the task and final state.
   Distinguish completion evidence from adherence findings and observations about what helped or hindered the workflow.
   Capture material recommendations and, when relevant evidence is available, observations about earlier guidance changes for later assessment.
1. **Handoff** &mdash; write the [Closeout summary](../SKILL.md#closeout-summary) and follow [Handoff records](#handoff-records) when a separate record is useful.
   Apply [Case recording](../SKILL.md#case-recording) whether or not a handoff file is needed; a handoff file does not replace a case record.
   Link any records written or state any material limitation.

Commit only when asked or by repository convention.
Push, merge, release, and remote branch deletion need explicit go-ahead in this session.

## Cleanup decisions

Classify leftovers by provenance and retention value; when unsure, pick the safer class.

| Class | Conditions | Action |
| --- | --- | --- |
| SAFE | Created during this task and disposable: scratch scripts, debug prints, or temporary or regenerable output that is not needed as evidence. | Remove it. |
| REVIEW | Probably unneeded but not provably yours or disposable: older results, duplicates, or pre-existing untracked files. | Check references and provenance; recommend, let the user decide. |
| PROTECTED | Raw or measurement data; hand-written or received files; unclear origin; anything another worker may use; minimum reproduction code, inputs, and logs supporting a conclusion. | Keep it. |

Preserve synthetic inputs, temporary reproduction code, and relevant logs when they support an investigation's conclusion.
Remove disposable, regenerable binaries and caches.
Temporary or regenerable evidence is not necessarily disposable.

Leaving evidence in `/tmp` preserves it during cleanup, but the directory may be cleared later.
Report the retained paths and lack of durable storage in the closeout summary.
When durable retention is needed, use an established authorized location or identify the unresolved storage choice.

## Handoff records

Create a separate handoff file only when later work or transfer benefits from it, following the project's convention.
Use an established authorized location when durable retention is needed; if none is known, report the unresolved storage choice.
An OS temp file may serve as a temporary handoff, but report its path and lack of durable retention.
Reference specs, commits, and diffs by path instead of copying them.
Name any relevant skills for the next session and redact secrets.

When relevant to closeout, look up related open tasks only in a tracker used for this task or in items the user designated.
Before updating those tasks, check whether existing authorization covers the concrete change.
Request approval only when it does not.
