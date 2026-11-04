# Personal case store setup

This guide explains how to authorize case recording, initialize a shared source store, and connect an existing store on each device.
The setup helper requires a checkout of this repository and Python 3.11 or later.
Run its commands from the repository root, using `python3` if that is your Python command.

## Recording settings

Authorize case recording in your request or guidance, or configure `.config/agent-loop/config.toml` under the current environment's user home:

```toml
version = 1

[case_recording]
root = "/absolute/path/to/personal-store"
mode = "automatic"
audience = "personal"
```

Choose the recording mode for the intended level of authorization:

| Mode | Behavior |
| --- | --- |
| `automatic` | Record material cases and retire resolved ones. |
| `proposals` | Review candidate entries and retirement candidates without writes. |
| `disabled` | Skip recording. |

Choose `automatic` to accumulate cases across tasks, which is what lets later guidance reviews and follow-ups build on earlier closeouts.
With `proposals`, candidate entries stay in each response until you record them.

Set `root` to an absolute path valid in your environment.
Windows and WSL may use different homes and stores.
On Windows, use a TOML literal string for paths containing backslashes.

Recording cases does not authorize guidance changes or separate improvement records.
If the selected store is unavailable, retain available findings in the response and report any gaps that limit the requested review.
You can append follow-up evidence within the case's recording authorization.
Preserve the original account.
Link the earlier change when available.

## Store delivery

The intended arrangement uses AEM to deliver the personal store and manage its installed directory link across devices.
The helper initializes store content and optionally connects local recording settings.
It does not own directory delivery, AEM state, or synchronization.
AEM is not a runtime dependency.
Independently prepared or synchronized stores work with the same commands.

## Initialize the source store

Initialize the source store once per person, before distributing it.
Choose the source path explicitly; do not initialize content at a path AEM will later install as a link.
Preview the operation before applying it:

```bash
python scripts/setup_store.py init --root /absolute/source-store --dry-run
python scripts/setup_store.py init --root /absolute/source-store
```

`init` creates only a basic README, case template, and `cases/` and `evidence/` directories with Git-trackable placeholders.
An absent or empty directory, including a checkout containing only `.git`, receives this template.
Other nonempty stores retain their existing organization.
No device-local configuration is read or written.

Commit and distribute the initialized source through your chosen management workflow.

## Connect each device

On each device, first connect the existing store through AEM installation or your independent workflow.
For stores receiving local records through AEM directory management, use a link.
Edits to installed copies are not collected into the source.
If local recording configuration is needed, preview and connect it:

```bash
python scripts/setup_store.py configure --root /absolute/installed-store --mode automatic --dry-run
python scripts/setup_store.py configure --root /absolute/installed-store --mode automatic
python scripts/setup_store.py configure --check
```

`configure` requires an existing store and accepts installed directory links.
It never changes store contents or creates the store.
It writes `.config/agent-loop/config.toml` under the current environment's home.
Selecting `automatic` authorizes material personal case records, necessary evidence, and retirement of resolved cases across tasks, subject to explicit user instructions.

Omitted options use these defaults:

| Option | Existing configuration | New configuration |
| --- | --- | --- |
| `--root` | Keep the configured store path. | Use `~/agent-loop`. |
| `--mode` | Keep the configured recording mode. | Use `proposals`. |

Existing configuration is validated and preserved.
Conflicting requested values require an explicit edit through the configuration's governing owner.
If AEM settings already manage that file, use the AEM settings workflow for changes rather than this helper.

Store delivery does not include this separate local configuration.
If applicable guidance already authorizes recording at the default store, local configuration may be unnecessary.
Common recording policy can come from personal guidance or selected AEM-managed settings.
Absolute store paths and target bindings remain device-specific.

## Check setup and recover interruptions

Both commands support `--dry-run` without writes.
`configure --check` validates the existing configuration and store directory.
It does not guarantee later write access or evaluate record content.
An interrupted setup may leave files already created.
Inspect that partial state before retrying.

The helper does not initialize Git, authorize commits, install skills, modify catalogs, or publish anything.
Git transport requires authorized publication.
Concurrent histories require explicit reconciliation; the helper does not merge them automatically.
All three skills remain independently usable without the helper or AEM.
