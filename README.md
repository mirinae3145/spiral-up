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
Both skills remain independently usable without the helper or AEM.

See [Case accumulation](skills/wrap-up/references/case-accumulation.md) for storage, evidence, and authorization details.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, design boundaries, and validation.

## AI disclosure

These skills are developed with AI assistance and intended for use by AI agents.
Reviews and cause analyses may be incomplete or mistaken; case records retain evidence for later evaluation.
