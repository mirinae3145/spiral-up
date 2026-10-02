# Spiral Up Your Agent

> Wrap up the workflow.
> Tune up the guidance.

Spiral Up brings together two agent skills for task closeout and guidance improvement.

[Wrap Up](skills/wrap-up/SKILL.md) closes a task by checking the final state, verifying results, and reviewing instruction adherence and workflow friction.
[Tune Up](skills/tune-up/SKILL.md) helps improve agent instructions and skills from accumulated cases or direct requests, and assess earlier changes using later evidence.

Observations from one task can inform guidance for the next, whose results provide evidence for further review.

## Tune up guidance

Tune Up assesses selected evidence or a direct request, finds the authoritative source, designs an improvement, applies authorized changes, and reports validation and the next observation needed to assess its effect.
Case-derived recommendations and direct requests enter the same update procedure while preserving their different evidence and authorization.
Direct requests do not require case collection first; analysis-only requests produce findings and a proposal without applying changes.

Example requests:

- "Review these wrap-up cases and propose instruction improvements without applying them."
- "Update my personal guidance to resolve references relative to the containing document."
- "Create a skill for this recurring review task."
- "Assess whether the earlier guidance change helped in these later cases."

The initial scope includes editing instructions and skills, adding rules or skills, consolidating duplication, and removing obsolete guidance.
New skills may define task procedures; broader workflow systems and automation implementation remain follow-ups.
Ordinary code changes and task closeout alone are outside Tune Up's routing.

When available, Tune Up actively uses the AEM operations skill and `aem` CLI to find managed sources and perform authorized management operations.
AEM is optional; other environments use their established authoritative sources and management arrangements.
A failure to locate a known AEM-managed source is reported rather than bypassed by editing an unverified installation.
Source editing, installation, and publication are separate outcomes; an update request does not automatically authorize all three.

Neither skill requires a particular store's directory layout, case ID format, or document headings.
Tune Up follows the selected store's organization and can handle direct requests without any store.
It links evidence, decisions, changed sources and known versions, checks, and later observations through the store's existing conventions when authorized.
The case-recording configuration below does not by itself authorize separate improvement records or instruction changes.
When a result cannot be durably recorded, it remains in the response with the limitation and next check stated.

An applied source change is distinct from an installed change and from evidence that it improved a later task.
Wrap Up can capture later observations and link them to an earlier improvement; Tune Up can then reassess its effect.
This loop does not automatically modify guidance during closeout or claim effectiveness from a passing structure check.

## What to expect from wrap-up

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

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, design boundaries, validation, and contribution practices.

## AI disclosure

These skills are developed with AI assistance and are intended for use by AI agents.
Their reviews and cause analyses may be incomplete or mistaken; case records preserve evidence for later evaluation rather than certify a diagnosis.
