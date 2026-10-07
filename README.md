# Spiral Up Your Agent

> Wrap up the workflow.
> Tune up the guidance.
> Follow up on what changed.

Spiral Up brings together three independently usable agent skills that connect task experience, guidance improvements, and later evidence.

[Wrap Up](skills/wrap-up/SKILL.md) closes a task by checking the final state, verifying results, and capturing useful observations about guidance and workflow.
[Tune Up](skills/tune-up/SKILL.md) improves agent instructions and skills from accumulated cases or direct requests.
[Follow Up](skills/follow-up/SKILL.md) picks up work left for later, including tracking observation questions and assessing the effects of earlier changes, or resuming a general handoff.

A typical loop is **Wrap Up &rightarrow; Tune Up &rightarrow; Follow Up &rightarrow; Wrap Up**: retain observations, improve guidance, follow up on the expected effects, and capture what the follow-up work taught us.
Enter wherever the task needs it; each skill accepts other inputs and can finish without invoking the next skill or requiring the whole loop.
Their roles overlap naturally: closeout can reveal evidence about an earlier change, and a guidance review can assess that evidence directly.

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

## Follow up on earlier work

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
To use a package that is not installed, ask the agent to read its `SKILL.md` directly; catalog registration and installation are separate operations.

## Record cases (optional)

Useful findings can stay in the closeout summary or be saved for later review.
The default personal store is `agent-loop` under the current environment's user home.
All three skills follow the selected store's existing organization.

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
If the selected store is unavailable, retain available findings in the response and report any gaps that limit the requested review.
Follow-up evidence can be appended to an existing case within its recording authorization; preserve the original account and link the earlier change when available.

### Initialize once, connect each device

The intended arrangement uses AEM to deliver the personal store and manage its installed directory link across devices.
The helper initializes store content and optionally connects local recording settings; it does not own directory delivery, AEM state, or synchronization.
AEM is not a runtime dependency: independently prepared or synchronized stores work with the same commands.
The helper needs a checkout of this repository and Python 3.11 or later; use `python3` if that is your Python command.

Initialize the source store once per person, before distributing it:

```bash
python scripts/setup_store.py init --root /absolute/source-store --dry-run
python scripts/setup_store.py init --root /absolute/source-store
```

`init` creates only a basic README, case template, and `cases/` and `evidence/` directories with Git-trackable placeholders.
An absent or empty directory, including a checkout containing only `.git`, receives this template.
Other nonempty stores retain their existing organization.
No device-local configuration is read or written.
Choose the source store path explicitly rather than creating content at a path AEM will later install as a link.
Commit and distribute the initialized source through your chosen management workflow.

On each device, first install/connect the existing store through AEM or your independent workflow.
For stores receiving local records through AEM directory management, use a link; edits to installed copies are not collected into the source.
Then, if local recording configuration is needed, preview and connect it:

```bash
python scripts/setup_store.py configure --root /absolute/installed-store --mode automatic --dry-run
python scripts/setup_store.py configure --root /absolute/installed-store --mode automatic
python scripts/setup_store.py configure --check
```

`configure` requires an existing store, accepts installed directory links, and never changes store contents or creates the store.
It writes `.config/agent-loop/config.toml` under the current environment's home.
Without `--root`, it uses the existing configured path or `~/agent-loop`; without `--mode`, it keeps the existing mode or uses `proposals` for a new configuration.
Selecting `automatic` authorizes material personal case records and necessary evidence across tasks, subject to explicit user instructions.
Existing configuration is validated and preserved; conflicting requested values require an explicit edit through its governing owner.
If AEM settings already manage that file, use the AEM settings workflow for changes rather than this helper.

Store delivery does not deliver this separate local configuration.
Common recording policy can come from personal guidance or selected AEM-managed settings; absolute store paths and target bindings remain device-specific.
If applicable guidance already authorizes recording at the default store, local configuration may be unnecessary.
Git transport still requires authorized publication; concurrent histories require explicit reconciliation rather than automatic merging by this helper.

Both commands support `--dry-run` without writes.
`configure --check` validates the existing configuration and store directory; it does not guarantee later write access or evaluate record content.
An interrupted setup may leave files already created; inspect that partial state before retrying.
The helper does not initialize Git, authorize commits, install skills, modify catalogs, or publish anything.
All three skills remain independently usable without the helper or AEM.

See [Case accumulation](skills/wrap-up/references/case-accumulation.md) for storage, evidence, and authorization details.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, design boundaries, and validation.

## AI disclosure

These skills are developed with AI assistance and intended for use by AI agents.
Reviews and cause analyses may be incomplete or mistaken; case records retain evidence for later evaluation.
