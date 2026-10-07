---
name: wrap-up
description: >
  Closes out the current task: reconciles it with the actual project state,
  cleans up, verifies results, and captures useful observations about guidance
  and workflow for later improvement, resuming, or handing off.
  Use when the user explicitly asks to close out the task or session, either by completing it or by handing off its current state.
---

# Wrap Up

Close out the task according to the user's requested outcome.
Leave a verified result or a resumable handoff, along with material observations that can inform the next task's guidance.
These observations can feed a guidance improvement and later follow-up, whose findings can be captured in another closeout; the same closeout procedure also serves ordinary sessions.
Review instruction adherence and workflow feedback as evidence for later improvement; closeout does not itself apply guidance changes or require case recording or Tune Up to be installed.
If the user asks only to summarize, hand off, or stop at the current state, report unfinished work without continuing implementation.
If the user asks to finish the task, complete necessary work within the already authorized objective before closing out.
Anything outside that objective becomes a **follow-up** in the summary, not an edit.

**Scope**: the whole task, or for an orchestrator the integrated result. A
worker in a larger task closes only its own slice and leaves other workers'
files, repo-wide cleanup, and the "done" call to the orchestrator.

## Requested emphasis

Accept natural-language emphasis in the invocation, such as focusing on instruction adherence, validation gaps, or making the handoff easy to resume.
Treat it as a priority for additional review depth and explanation, without requiring a named mode or fixed vocabulary.
Preserve all applicable closeout steps and completion criteria; emphasis does not expand the task's scope or authorization.
Keep review coverage distinct from reporting length: areas outside the emphasis still receive the necessary checks and may be reported briefly when uneventful.
Address material findings and unfinished work regardless of the requested emphasis.
Keep emphasis separate from the requested outcome above: a focus on handoff quality alone does not mean stopping implementation or switching to a summary-only handoff.
When no emphasis is given, use the task's evidence and risks to allocate attention across the normal flow.

## Flow

1. **Inspect** — in every repository or location the task touched (not only
   the working directory): `git status`, `git diff` staged and unstaged,
   untracked files, outputs outside git, and external state changed (links,
   task trackers, services). Earlier "done"/"tested" claims are context; this
   state is evidence. Done when every change is accounted for.

1. **Reconcile** — objective vs. evidence: met, missing, and unrequested
   changes. Handle missing work according to the requested outcome above; list unrequested
   changes for the user to keep or revert.

1. **Clean** — only in the area the task worked in; classify each leftover:
   - **SAFE**: created during this task *and* disposable (scratch scripts,
     debug prints, temp or regenerable output that is not needed as evidence). Remove it.
   - **REVIEW**: probably unneeded but not provably yours or disposable
     (older results, duplicates, pre-existing untracked files). Check
     references and provenance; recommend, let the user decide.
   - **PROTECTED**: raw or measurement data, hand-written or received files,
     unclear origin, anything another worker may use, or the minimum reproduction code, inputs, and logs supporting a conclusion. Keep it.
   For example, when synthetic inputs and temporary reproduction code support an investigation's conclusion, preserve them with the relevant logs as investigation evidence; remove disposable, regenerable binaries and caches.
   Being temporary or regenerable does not by itself make supporting evidence disposable.
   Keeping evidence in `/tmp` only means leaving it in place during cleanup; it is not durable storage and may be cleared later.
   Report that limitation and the retained paths in the closeout summary; when durable retention is needed, use an established authorized location or identify the unresolved storage choice.
   When unsure, pick the safer class.

1. **Update** — when completing the task, update or create documentation needed to use or maintain this task's changes, including changed behavior, setup, and configuration.
   Follow the project's document conventions; unrelated pre-existing inaccuracies are follow-ups.
   For a summary-only handoff, report missing documentation as unfinished work.

1. **Validate** — use the project's relevant checks and available results to establish the final state, then inspect `git status` when applicable.
   Reuse passing results when subsequent changes cannot affect them; rerun affected checks after cleanup or further edits.
   For a new regression test, verify failure on the pre-fix code and success on the fix when feasible and meaningful.
   Distinguish passing checks from unverified regression coverage and report material validation limits.

1. **Review** — read and apply [Retrospective](references/retrospective.md) against the task and final state.
   Distinguish completion evidence from adherence findings and observations about what helped or hindered the workflow.
   Capture material recommendations and, when relevant evidence is available, observations about earlier guidance changes for later assessment.

1. **Handoff** — write the summary below.
   Create a separate handoff file only when later work or transfer benefits from it, following the project's convention.
   Use an established authorized location when durable retention is needed; if none is known, report the unresolved storage choice.
   An OS temp file may serve as a temporary handoff, but report its path and lack of durable retention.
   Reference specs, commits, and diffs by path instead of copying them, name any relevant skills for the next session, and redact secrets.
   Look up related open tasks only in a tracker used for this task or in items the user designated, when relevant to closeout.
   Before updating them, check whether existing authorization covers the concrete change; request approval only when it does not.
   Apply **Optional case recording** below independently of whether a handoff file is needed; link any records written or state any material limitation.

Commit only when asked or by repository convention. Push, merge, release,
and remote branch deletion need explicit go-ahead in this session.

## Optional case recording

Use `agent-loop` under the current execution environment's user home as the neutral default store location.
A user request, applicable guidance, or local configuration may override the location and recording mode.
Read [Case accumulation](references/case-accumulation.md) to resolve those choices, inspect the actual store structure, and record or propose material cases.
A default path does not by itself authorize writing or creating a store.
Reuse established recording authorization within its scope; otherwise leave candidate findings in the summary without blocking closeout.

## Closeout summary

Make the final response self-contained and lead with the outcome most relevant to the user.
Include material changes, validation and its limits, and remaining decisions or work as relevant to understanding the result or continuing the task.
Choose the structure and level of detail for the task and the user's request; this skill prescribes no fixed headings, order, table, or template.
Keep adherence findings and workflow feedback distinguishable from task completion without requiring separate sections or unsupported blanket compliance claims.
For material improvement findings, preserve enough evidence and source context for a later guidance review without requiring a separate record or repeating the conversation.
When a question remains open, retain what would be useful to observe next and the situation in which that observation could be made, so later follow-up has a concrete starting point.
When a handoff document exists, link it and include enough context for the final response to stand on its own without repeating the document.
For work that will continue, preserve consequential decisions and a clear starting point for the next session or colleague.
