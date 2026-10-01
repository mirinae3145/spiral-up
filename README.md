# Wrap Up

Wrap Up is an agent skill for closing a task with an evidence-based account of what changed, what was verified, and what remains.
Invoke it with `wrap up`, `마무리해`, or another explicit request to finish the work.
The execution rules live in [SKILL.md](skills/wrap-up/SKILL.md).

## What to expect

The skill checks the actual project state, reconciles it with the task, removes disposable leftovers, updates documentation made inaccurate by the task, and runs relevant checks.
A request to finish includes necessary work within the authorized objective; a request only to summarize, hand off, or stop reports unfinished work without continuing implementation.
Required documentation may be updated or created as part of completion.
Passing checks are reused unless later changes could affect them; validation limits remain explicit.
Instruction adherence and workflow feedback are assessed separately from whether the task succeeded.
The final response adapts to the task and your request, covering relevant outcomes, evidence, and remaining work without a fixed response template.

Cleanup preserves the minimum reproduction code, inputs, and logs supporting a conclusion, including synthetic inputs and temporary scripts, while removing disposable, regenerable binaries and caches.
Evidence left in `/tmp` is retained only for the current cleanup, not durably archived; the summary identifies its paths and this limitation, with an authorized durable location used when needed or the storage choice left explicit.

A useful retrospective describes observable behavior, its impact, and a concrete improvement or further check.
It should not end with self-blame or assume that one failure proves a defect in the user, environment, guidance, or model.
Recovered mistakes can still contain useful evidence.

When missing history could affect a material review conclusion, the skill loads the [session recovery procedure](skills/wrap-up/references/session-recovery.md) and attempts to recover the relevant local records.
This read-only review is independent of optional case recording and does not modify session logs.
If records are missing or incomplete, the summary states the remaining review limitations.

A separate handoff file is created when later work or transfer benefits from it.
Durable handoffs use an established authorized location; temporary handoff files are identified as temporary.
Related tracker items are consulted only when the tracker was used for the task or the user designated the items, and updates require applicable existing authorization or new approval.

## Set up case accumulation

Persistent recording is optional.
The default personal store is `agent-loop` under the current environment's user home.
The skill inspects the actual store's README, templates, and existing organization to choose suitable locations for cases and evidence.
It uses `cases/` and `evidence/` only when the store has no established organization.

Override the location or recording mode in your request, applicable guidance, or an optional UTF-8 `.config/agent-loop/config.toml` under that home:

```toml
version = 1

[case_recording]
root = "/absolute/path/to/personal-store"
mode = "automatic"
audience = "personal"
```

Use an absolute path valid in the current environment.
On native Windows, use a TOML literal string for paths containing backslashes.
Windows and WSL resolve their own home directories and can select different stores.
No configuration file is required to inspect the default location.
The default path or an existing directory alone does not authorize persistent writes.
Authorize recording in your request or applicable guidance, or enable `automatic` mode in the local configuration.
Use `proposals` for candidate entries without writes, or `disabled` to turn off recording.
An invalid enabled configuration or an unavailable selected store is reported without preventing closeout or silently selecting another store.

Recording approval is reused within its store, audience, and scope.
It does not authorize task-tracker updates, external feedback, changes to governing instructions, or Git commits and pushes.
The [case accumulation procedure](skills/wrap-up/references/case-accumulation.md) describes discovery, placement, and evidence preservation.
Without a resolved recording arrangement, useful findings remain in the closeout summary.
A conversation summary alone does not guarantee that a future session will retrieve it.

## Best practices

- Record material incidents and useful outcomes, not every tool call or routine success.
- Keep observations distinct from explanations; include model identity or version only when known and relevant.
- Search related records before adding a case, and update the same incident instead of counting a later review as another occurrence.
- Connect proposed mitigations to their subsequently observed results, including successful cases and counterexamples.
- Revisit hypotheses when evidence changes; preserve the original observation and explain the revised interpretation.
- Use stable case identifiers and durable evidence references, minimizing copied conversation text and private information.
- Treat repeated observations as grounds for comparison, not an automatic instruction change or proof of a model-wide tendency.

Recording happens during closeout, without background monitoring or a separate experiment workflow.
Selective records can support learning but cannot establish an overall failure rate.

## Optional Git exclusion

For personal records inside repositories, you can choose a common directory convention and exclude it through your global Git ignore configuration.
This avoids requiring a `.gitignore` edit in every repository.
If paths vary by project, a single global pattern may not be suitable; team-owned records may instead belong in Git.

Ask explicitly if you want the agent to configure exclusions.
It should inspect the existing configuration, preserve its contents, derive a pattern from your chosen record location, and check what the pattern excludes.
No global Git settings are changed merely by invoking this skill.
Ignore rules do not affect already tracked files and are not a privacy or access-control mechanism.

## AI disclosure

This skill is developed with AI assistance and is intended for use by AI agents.
Its reviews and cause analyses may be incomplete or mistaken; case records preserve evidence for later evaluation rather than certify a diagnosis.
