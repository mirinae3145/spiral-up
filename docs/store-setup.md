# Personal case store setup

This guide explains how to authorize optional case recording, initialize a shared source store, and connect an existing store on each device.
The setup helper requires a checkout of this repository and Python 3.11 or later.
Run its commands from the repository root; use `python3` if that is your Python command.

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
| `automatic` | Record material cases. |
| `proposals` | Review candidate entries without writes. |
| `disabled` | Skip recording. |

Set `root` to an absolute path valid in your environment; Windows and WSL may use different homes and stores.
On Windows, use a TOML literal string for paths containing backslashes.

Recording cases does not authorize guidance changes or separate improvement records.
If the selected store is unavailable, retain available findings in the response and report any gaps that limit the requested review.
Follow-up evidence can be appended to an existing case within its recording authorization; preserve the original account and link the earlier change when available.

## Store delivery

The intended arrangement uses AEM to deliver the personal store and manage its installed directory link across devices.
The helper initializes store content and optionally connects local recording settings; it does not own directory delivery, AEM state, or synchronization.
AEM is not a runtime dependency: independently prepared or synchronized stores work with the same commands.

## Initialize the source store

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

## Connect each device

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

## Check setup and recover interruptions

Both commands support `--dry-run` without writes.
`configure --check` validates the existing configuration and store directory; it does not guarantee later write access or evaluate record content.
An interrupted setup may leave files already created; inspect that partial state before retrying.
The helper does not initialize Git, authorize commits, install skills, modify catalogs, or publish anything.
All three skills remain independently usable without the helper or AEM.
