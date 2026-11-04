# Observation follow-up

Use this procedure to revisit questions left for later and assess the effects of earlier changes.
An observation question or relevant later evidence is sufficient input.
No formal handoff, completed improvement, or case store is required.

## Find the question

Scope discovery to the user's question, selected records, or relevant change or topic.
When asked to find open observation questions, inspect the relevant records and their follow-ups.
Distinguish open questions from answered or superseded ones, and preserve their original intent and later revisions.
Do not treat every recorded suggestion as an active task.
Do not audit unrelated stores or create a tracking system to make the input fit this procedure.

## Locate relevant records

Use the location designated by the user or applicable guidance.
As needed, inspect the store's README, contribution guidance, templates, related records, and actual organization.
Use supported connected tools for a designated non-local store without requiring a local mirror.

For the existing personal arrangement, the default store is `agent-loop` under the current environment's user home.
An explicit location or the optional UTF-8 `.config/agent-loop/config.toml` under that home overrides this default.
Follow explicit user instructions over configuration.
Do not expand configured paths or translate them between Windows and WSL.

The supported configuration contains these fields:

| Field | Supported value |
| --- | --- |
| `version` | `1` |
| `case_recording.root` | An absolute path valid in the current environment. |
| `case_recording.mode` | `automatic`, `proposals`, or `disabled`. |
| `case_recording.audience` | `"personal"` |

If relevant configuration is invalid or the selected store is unavailable, report the limitation without choosing or creating another store.
Continue with accessible supplied evidence and explain which questions or conclusions the missing records leave unresolved.

## Recover observation context

Recover what was left to observe, why it matters, and any condition for a useful observation.
For an earlier improvement, connect the original evidence, decision, and expected effect when available.
When available, include the improvement's changed source, known version, and application or installation results.
For a question without an earlier change, identify the situation and evidence that would answer it.

Distinguish a proposed change from an applied one.
Do not invent a version, expected effect, missing original record, or improvement history.

## Compare current evidence

Look for relevant later tasks, observations, counterexamples, and new friction in the accessible material.
Establish whether a relevant observation opportunity occurred.
For a guidance change, also establish whether the changed guidance was actually used.
Installation or source edits alone do not establish use; a recurrence before use does not establish that the change failed.
When version, exposure, or opportunity is unknown, retain that uncertainty rather than assigning an outcome.

Compare expected and observed behavior, impact, recovery, and conditions that could explain differences.
Use earlier checks only within their known revision and environment.
Passing structure checks do not demonstrate behavioral effectiveness.
Consider other changes in tools, task difficulty, user intervention, or circumstances when they could affect the judgment.
Avoid causal claims that the evidence cannot support.

Treat later reviews, copied summaries, and recovery updates about one incident as the same occurrence.
Use existing references to distinguish separate incidents, without inventing counts or merging uncertain matches.
Selective case records can support an assessment but do not establish an overall failure rate.

## Assess and leave a useful next step

Explain whether the evidence supports the expected effect, challenges it, reveals new friction, or remains inconclusive.
Keep confidence proportional to the evidence.
If no relevant observation opportunity occurred, leave the question open rather than declaring success or failure.
Do not force findings into scores or fixed status labels.

When another check would help, identify what to observe and a situation that would allow it.
For example, a comparable task using the changed guidance could provide the next observation.
Do not substitute an arbitrary date for a missing observation opportunity.
Do not create monitoring, schedules, or experiments without an appropriate request.

If another improvement is warranted, identify its source, evidence, uncertainty, and proposed scope so the finding is actionable.
Assessment does not itself authorize applying that improvement.

## Retain findings within recording scope

Follow the selected store's organization rather than imposing directories, headings, IDs, or a universal schema.
Preserve the original account and improvement decision.
Append dated findings or link assessments instead of rewriting earlier evidence to match a new interpretation.
Use existing references to connect the question, any relevant expected effect, current evidence, judgment, and next observation.
Related reviews of the same incident belong with its existing record rather than becoming duplicate cases.

Write only when the user request, applicable guidance, or personal configuration authorizes the destination and recording scope.
An existing store or default path does not authorize recording.
Subject to explicit user instructions, the personal configuration's modes govern case recording as follows:

| Mode | Recording scope |
| --- | --- |
| `automatic` | Record material personal cases and necessary supporting evidence, including case follow-ups within that scope. |
| `proposals` | Present candidate entries without writes. |
| `disabled` | Skip persistent recording. |

These modes do not authorize separate improvement records or guidance changes.
If recording is not authorized or its destination is unavailable, report findings and the next check without creating another destination.
Link appropriately retained evidence and minimize copied private details.
Recording does not authorize commits, publication, tracker updates, or messages to others.
