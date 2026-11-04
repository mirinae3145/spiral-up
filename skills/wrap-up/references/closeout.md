# Closeout procedure

Reconcile the requested outcome with the actual final state, complete the applicable closeout work, and leave a verified result or resumable handoff.
This procedure covers inspection, cleanup, documentation, validation, retrospective review, and handoff records.

## Complete the closeout

Apply these steps within the requested outcome and authorized scope:

1. **Inspect** &mdash; in every repository or location the task touched (not only the working directory): `git status`, `git diff` staged and unstaged, untracked files, outputs outside git, and external state changed (links, task trackers, services).
   Earlier "done"/"tested" claims are context; this state is evidence.
   Done when every change is accounted for.
1. **Reconcile** &mdash; objective vs. evidence: met, missing, and unrequested changes.
   Handle missing work according to the [requested outcome](../SKILL.md#scope-and-requested-outcome); list unrequested changes for the user to keep or revert.
1. **Clean** &mdash; only in the area the task worked in, using [Cleanup decisions](#cleanup-decisions) to classify each leftover.
1. **Update** &mdash; when completing the task, update or create documentation needed to use or maintain this task's changes, including changed behavior, setup, and configuration.
   Follow the project's document conventions; unrelated pre-existing inaccuracies are follow-ups.
   For a summary-only handoff, report missing documentation as unfinished work.
1. **Validate** &mdash; use the project's relevant checks and available results to establish the final state, then inspect `git status` when applicable.
   Reuse passing results when subsequent changes cannot affect them; rerun affected checks after cleanup or further edits.
   For a new regression test, verify failure on the pre-fix code and success on the fix when feasible and meaningful.
   Distinguish passing checks from unverified regression coverage and report material validation limits.
1. **Review** &mdash; read and apply [Retrospective](retrospective.md) against the task and final state.
   Distinguish completion evidence from adherence findings and observations about what helped or hindered the workflow.
   Capture material recommendations and, when relevant evidence is available, observations about earlier guidance changes for later assessment.
1. **Handoff** &mdash; write the [Closeout summary](../SKILL.md#closeout-summary) and follow [Handoff records](#handoff-records) when a separate record is useful.
   Apply [Optional case recording](../SKILL.md#optional-case-recording) independently of whether a handoff file is needed; link any records written or state any material limitation.

Commit only when asked or by repository convention.
Push, merge, release, and remote branch deletion need explicit go-ahead in this session.

## Cleanup decisions

Classify leftovers by provenance and retention value; when unsure, pick the safer class.

| Class | Conditions | Action |
| --- | --- | --- |
| SAFE | Created during this task and disposable: scratch scripts, debug prints, or temporary or regenerable output that is not needed as evidence. | Remove it. |
| REVIEW | Probably unneeded but not provably yours or disposable: older results, duplicates, or pre-existing untracked files. | Check references and provenance; recommend, let the user decide. |
| PROTECTED | Raw or measurement data, hand-written or received files, unclear origin, anything another worker may use, or the minimum reproduction code, inputs, and logs supporting a conclusion. | Keep it. |

For example, when synthetic inputs and temporary reproduction code support an investigation's conclusion, preserve them with the relevant logs as investigation evidence; remove disposable, regenerable binaries and caches.
Being temporary or regenerable does not by itself make supporting evidence disposable.

Keeping evidence in `/tmp` only means leaving it in place during cleanup; it is not durable storage and may be cleared later.
Report that limitation and the retained paths in the closeout summary; when durable retention is needed, use an established authorized location or identify the unresolved storage choice.

## Handoff records

Create a separate handoff file only when later work or transfer benefits from it, following the project's convention.
Use an established authorized location when durable retention is needed; if none is known, report the unresolved storage choice.
An OS temp file may serve as a temporary handoff, but report its path and lack of durable retention.
Reference specs, commits, and diffs by path instead of copying them, name any relevant skills for the next session, and redact secrets.

Look up related open tasks only in a tracker used for this task or in items the user designated, when relevant to closeout.
Before updating them, check whether existing authorization covers the concrete change; request approval only when it does not.
