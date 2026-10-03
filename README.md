# Spiral Up Your Agent

> Wrap up the workflow.
> Tune up the guidance.

Spiral Up brings together two agent skills for task closeout and guidance improvement.

[Wrap Up](skills/wrap-up/SKILL.md) closes a task by checking the final state, verifying results, and capturing useful observations about guidance and workflow.
[Tune Up](skills/tune-up/SKILL.md) helps improve agent instructions and skills from accumulated cases or direct requests, and assess earlier changes using later evidence.

Observations from one task can inform guidance for the next, whose results provide evidence for further review.

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

Wrap Up can capture later observations for Tune Up to reassess an improvement.
An applied change and evidence that it helped are separate outcomes.
AEM is optional and can help Tune Up locate managed sources; installation and publication require their own authorization.

## Resume handed-off work (draft)

[Follow Up](skills/follow-up/SKILL.md) is a draft skill for resuming work from a handoff, closeout summary, or designated prior work record.
It recovers the relevant context, checks what has changed, and chooses a useful restart point before continuing within the requested objective.
You can also ask it to prepare a restart without continuing implementation.

Example requests:

- "Continue the task from this handoff and finish the remaining work."
- "Read this handoff and identify the restart point without making changes."

The draft is not yet registered in the AEM catalog or installed for automatic discovery.
During development, ask the agent to read `skills/follow-up/SKILL.md` directly.

## Record cases (optional)

Useful findings can stay in the closeout summary or be saved for later review.
The default personal store is `agent-loop` under the current environment's user home.
Both skills follow the selected store's existing organization.

Authorize case recording in your request or guidance, or configure `.config/agent-loop/config.toml` under that home:

```toml
version = 1

[case_recording]
root = "/absolute/path/to/personal-store"
mode = "automatic"
audience = "personal"
```

Use `automatic` to record material cases, `proposals` to review candidate entries without writes, or `disabled` to skip recording.
Set `root` to an absolute path valid in your environment; Windows and WSL may use different homes and stores.
On Windows, use a TOML literal string for paths containing backslashes.
Recording cases does not authorize guidance changes or separate improvement records.
If the selected store is unavailable, closeout continues with the findings in the summary.

See [Case accumulation](skills/wrap-up/references/case-accumulation.md) for storage, evidence, and authorization details.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, design boundaries, and validation.

## AI disclosure

These skills are developed with AI assistance and intended for use by AI agents.
Reviews and cause analyses may be incomplete or mistaken; case records retain evidence for later evaluation.
