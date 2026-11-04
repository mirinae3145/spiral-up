# Spiral Up Your Agent

Spiral Up brings together three independently usable agent skills that connect task experience, guidance improvements, and later evidence.

> Wrap up the workflow.
> Tune up the guidance.
> Follow up the handoff.

Choose a skill for the work at hand:

- [Wrap Up](skills/wrap-up/SKILL.md) closes a task by checking the final state, verifying results, and capturing useful observations about guidance and workflow.
- [Tune Up](skills/tune-up/SKILL.md) improves agent instructions and skills from accumulated cases or direct requests.
- [Follow Up](skills/follow-up/SKILL.md) picks up work left for later, including tracking observation questions, assessing earlier changes, and resuming a general handoff.

A typical loop is **Wrap Up &rightarrow; Tune Up &rightarrow; Follow Up &rightarrow; Wrap Up**: retain observations, improve guidance, follow up on the expected effects, and capture what the follow-up work taught us.
Enter wherever the task needs it; each skill accepts other inputs and can finish without invoking the next skill or requiring the whole loop.
Their roles overlap naturally: closeout can reveal evidence about an earlier change, and a guidance review can assess that evidence directly.

To use a package that is not installed, ask the agent to read its `SKILL.md` directly; catalog registration and installation are separate operations.

## Wrap up the workflow

Ask Wrap Up to finish a task or prepare a handoff.
It checks the actual state, handles cleanup and relevant validation, and summarizes the outcome, remaining work, and useful observations about the guidance and workflow.
A handoff-only request leaves unfinished implementation for the next session.

Example requests:

- "Finish this task and wrap up, focusing on validation and remaining work."
- "Prepare a handoff so I can resume this task later."

## Tune up the guidance

Ask Tune Up to improve instructions or skills, review accumulated cases, or assess an earlier change.
It can edit, add, consolidate, or remove guidance; direct requests do not require prior case collection.
You can ask for a proposal before applying changes.

Example requests:

- "Review these cases and propose instruction improvements without applying them."
- "Create a skill for this recurring review task."
- "Assess whether the earlier guidance change helped in these later cases."

Leave the expected effect and a useful next observation with the improvement so later work can assess it.
An applied change and evidence that it helped are separate outcomes.
AEM is optional and can help Tune Up locate managed sources; installation and publication require their own authorization.

## Follow up the handoff

Ask Follow Up to revisit an observation question, assess an earlier improvement, or resume a task from a handoff, closeout summary, or prior work record.
It recovers the relevant context, checks the current evidence, and carries out the requested follow-up.
For an improvement, it checks whether the changed guidance was actually used, what happened, and whether the expected effect is supported, challenged, or still uncertain.
If there has been no relevant observation opportunity, it leaves the question open with a useful condition for checking again.
For a general handoff, it chooses a useful restart point and continues within the requested objective; you can also ask for preparation without execution.

Example requests:

- "Find the observation questions left with this improvement and assess what these later tasks show."
- "Check whether the revised guidance reduced repeated confirmations, including any new friction."
- "Continue the task from this handoff and finish the remaining work."
- "Read this handoff and identify the restart point without making changes."

Follow-up findings can inform another guidance review and be retained during closeout.
Evaluating a change does not automatically apply another one, schedule monitoring, or invoke the other skills.
No fixed record format, evaluation score, or observation schedule is required.

## Record cases (optional)

Useful findings can stay in the closeout summary or be saved for later review.
Select cases for their evidence value, such as consequential incidents or informative patterns, rather than recording every corrected retry.
A case can preserve observations and recovery without prescribing a future lesson or promising a repeat-task check; later guidance review can compare the accumulated evidence.

The default personal store is `agent-loop` under the current environment's user home.
All three skills follow the selected store's existing organization.
Authorize recording through your request, guidance, or local configuration.

[Personal case store setup](docs/store-setup.md) explains recording modes, source initialization, and connecting each device to an existing store.
See [Case accumulation](skills/wrap-up/references/case-accumulation.md) for the agent's storage, evidence, and authorization procedure.

## Documentation and contributing

[Documentation](docs/README.md) introduces the setup guide and the design constraints for contributors.
See [Contributing](CONTRIBUTING.md) for development setup, validation, and submitting changes.

## AI disclosure

These skills are developed with AI assistance and intended for use by AI agents.
Reviews and cause analyses may be incomplete or mistaken; case records retain evidence for later evaluation.
