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
Use observations about instruction adherence and workflow to inform later improvements.
A later closeout can capture follow-up findings; ordinary sessions use the same procedure.
Closeout does not itself apply guidance changes or require case recording or an installed Tune Up skill.

## Scope and requested outcome

If the user asks only to summarize, hand off, or stop at the current state, report unfinished work without continuing implementation.
If the user asks to finish the task, complete necessary work within the already authorized objective before closing out.
Anything outside that objective becomes a **follow-up** in the summary, not an edit.

Decide separately what to report to the user and what to persist in documents or other records.
A finding may belong in the response without needing a persistent record.
Follow applicable guidance when deciding what to record.

Close out the whole task, or the integrated result when acting as an orchestrator.
A worker in a larger task closes only its own slice.
As a worker, leave other workers' files, repository-wide cleanup, and the final completion decision to the orchestrator.

## Requested emphasis

Accept natural-language emphasis in the invocation, such as focusing on instruction adherence, validation gaps, or making the handoff easy to resume.
Treat it as a priority for additional review depth and explanation, without requiring a named mode or fixed vocabulary.
Preserve all applicable closeout steps and completion criteria; emphasis does not expand the task's scope or authorization.

Check areas outside the requested emphasis too; report them briefly when uneventful.
Address material findings and unfinished work regardless of emphasis.
A focus on handoff quality alone does not change the [requested outcome](#scope-and-requested-outcome) to stopping implementation or providing only a summary.
When no emphasis is given, allocate attention according to the task's evidence and risks.

## Closeout procedure

Read and apply [Closeout procedure](references/closeout.md) to inspect, reconcile, clean, document, validate, and hand off the final state.
Its cleanup and handoff sections distinguish disposable leftovers from supporting evidence and durable records.

As part of that procedure, read [Retrospective](references/retrospective.md) to assess instruction adherence and workflow feedback using the task's evidence.
If missing history could affect a material finding, read [Session recovery](references/session-recovery.md) for bounded, read-only recovery of relevant local records.

## Optional case recording

Use `agent-loop` under the current execution environment's user home as the neutral default store location.
A user request, applicable guidance, or local configuration may override the location and recording mode.
Read [Case accumulation](references/case-accumulation.md) to resolve those choices, inspect the actual store structure, and record or propose material cases.
A default path does not by itself authorize writing or creating a store.
Reuse established recording authorization within its scope; otherwise leave candidate findings in the summary without blocking closeout.

## Closeout summary

Make the final response self-contained and lead with the outcome most relevant to the user.
Include the material changes, validation results and limits, and remaining decisions or work needed to understand the result or continue the task.
Choose the structure and detail for the task and the user's request; no fixed headings, order, table, or template are required.
Distinguish adherence findings and workflow feedback from task completion.
Separate sections are optional; do not make unsupported claims of complete compliance.

For material improvement findings, retain enough evidence and source context for a later guidance review.
No separate record is required, and there is no need to repeat the conversation.
For a material open question with a plausible observation opportunity, retain what could resolve it and where that evidence could arise.
A resolved incident requires no future lesson or observation commitment; follow the selection criteria in the retrospective and case-recording references.

When a handoff document exists, link it.
Give enough context for the response to stand on its own without repeating the document.
For work that will continue, preserve consequential decisions and a clear starting point for the next session or colleague.
