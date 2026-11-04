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

## Scope and requested outcome

If the user asks only to summarize, hand off, or stop at the current state, report unfinished work without continuing implementation.
If the user asks to finish the task, complete necessary work within the already authorized objective before closing out.
Anything outside that objective becomes a **follow-up** in the summary, not an edit.

Decide separately what to report to the user and what to persist in documents or other records.
Information needed in the closeout response does not automatically need to be recorded.
Follow applicable guidance provided when making recording decisions.

Close out the whole task, or for an orchestrator the integrated result.
A worker in a larger task closes only its own slice and leaves other workers' files, repo-wide cleanup, and the "done" call to the orchestrator.

## Requested emphasis

Accept natural-language emphasis in the invocation, such as focusing on instruction adherence, validation gaps, or making the handoff easy to resume.
Treat it as a priority for additional review depth and explanation, without requiring a named mode or fixed vocabulary.
Preserve all applicable closeout steps and completion criteria; emphasis does not expand the task's scope or authorization.

Keep review coverage distinct from reporting length: areas outside the emphasis still receive the necessary checks and may be reported briefly when uneventful.
Address material findings and unfinished work regardless of the requested emphasis.
Keep emphasis separate from the [requested outcome](#scope-and-requested-outcome): a focus on handoff quality alone does not mean stopping implementation or switching to a summary-only handoff.
When no emphasis is given, use the task's evidence and risks to allocate attention across the normal flow.

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
Include material changes, validation and its limits, and remaining decisions or work as relevant to understanding the result or continuing the task.
Choose the structure and level of detail for the task and the user's request; this skill prescribes no fixed headings, order, table, or template.
Keep adherence findings and workflow feedback distinguishable from task completion without requiring separate sections or unsupported blanket compliance claims.

For material improvement findings, preserve enough evidence and source context for a later guidance review without requiring a separate record or repeating the conversation.
For a material open question with a plausible observation opportunity, retain what would help resolve it and where that evidence could arise.
A resolved incident does not require a future lesson or observation commitment; follow the selection criteria in the retrospective and case-recording references.

When a handoff document exists, link it and include enough context for the final response to stand on its own without repeating the document.
For work that will continue, preserve consequential decisions and a clear starting point for the next session or colleague.
