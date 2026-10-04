#!/usr/bin/env python3
"""Initialize a case store or connect device-local recording settings (Python 3.11+)."""

import argparse
import json
from pathlib import Path
import sys
import tomllib

MODES = ("automatic", "proposals", "disabled")
TEMPLATE = Path(__file__).resolve().parents[1] / "templates" / "store"


def read_config(path):
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    recording = data.get("case_recording", {})
    if not isinstance(recording, dict) or data.get("version") != 1 or recording.get("audience") != "personal":
        raise ValueError("Expected version = 1 and audience = 'personal'.")
    if recording.get("mode") not in MODES:
        raise ValueError("Unsupported recording mode.")
    root = recording.get("root")
    if not isinstance(root, str) or not Path(root).is_absolute():
        raise ValueError("The configured root must be an absolute path for this environment.")
    return recording


def validate_root(root):
    if not root.is_absolute():
        raise ValueError("--root must be an absolute path; shell home expansion is supported.")
    if root.exists() and not root.is_dir():
        raise ValueError("The store path exists and is not a directory.")


def initialize(root):
    """Plan initial files only; an existing nonempty store keeps its organization."""
    if root.exists() and any(path.name != ".git" for path in root.iterdir()):
        print(f"Preserve existing store organization: {root}")
        return []
    return [(root / "README.md", (TEMPLATE / "README.md").read_text(encoding="utf-8")),
            (root / "templates" / "case.md", (TEMPLATE / "case.md").read_text(encoding="utf-8")),
            (root / "cases" / ".gitkeep", ""),
            (root / "evidence" / ".gitkeep", "")]


def configure(args, config):
    """Connect an existing local directory or AEM link without modifying its contents."""
    existing = read_config(config) if config.exists() else None
    root = args.root or (Path(existing["root"]) if existing else Path.home() / "agent-loop")
    mode = args.mode or (existing["mode"] if existing else "proposals")
    validate_root(root)
    if not root.is_dir():
        raise ValueError("Store is unavailable; install/connect it with AEM or prepare it independently first.")
    if existing and (Path(existing["root"]) != root or existing["mode"] != mode):
        raise ValueError(f"Existing configuration differs; review its owner and edit it explicitly: {config}")
    print(f"Store: {root}\nRecording mode: {mode}")
    if args.check:
        if existing is None:
            raise ValueError("Recording configuration is missing.")
        print(f"Valid personal recording configuration: {config}")
        return []
    if mode == "automatic":
        print("Automatic authorizes material personal case records and necessary evidence across tasks.")
    if existing:
        print(f"Preserve existing configuration: {config}")
        return []
    content = ('version = 1\n\n[case_recording]\n'
               f'root = {json.dumps(str(root), ensure_ascii=False)}\n'
               f'mode = "{mode}"\naudience = "personal"\n')
    return [(config, content)]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    init = commands.add_parser("init", help="Initialize shared store content once; do not write local recording settings.")
    init.add_argument("--root", type=Path, required=True, help="Absolute source store path; AEM owns subsequent delivery and links.")
    init.add_argument("--dry-run", action="store_true", help="Show planned files without writing.")
    local = commands.add_parser("configure", help="Connect this device to an existing store without changing store contents.")
    local.add_argument("--root", type=Path, help="Absolute installed store path; defaults to ~/agent-loop or existing configuration.")
    local.add_argument("--mode", choices=MODES, help="Recording permission; defaults to proposals or existing configuration.")
    action = local.add_mutually_exclusive_group()
    action.add_argument("--dry-run", action="store_true", help="Show planned settings without writing.")
    action.add_argument("--check", action="store_true", help="Validate existing configuration and store without writing.")
    args = parser.parse_args(argv)
    try:
        if args.command == "init":
            validate_root(args.root)
            files = initialize(args.root)
        else:
            files = configure(args, Path.home() / ".config" / "agent-loop" / "config.toml")
        for path, _ in files:
            print(f"Create file: {path}")
        if args.dry_run:
            print("Preview only; no files written.")
            return 0
        for path, content in files:
            path.parent.mkdir(parents=True, exist_ok=True)
            # Exclusive creation also protects files introduced after planning.
            with path.open("x", encoding="utf-8", newline="\n") as stream:
                stream.write(content)
        print("Complete. No AEM state, Git initialization, commits, or publication changed.")
        return 0
    except (OSError, ValueError) as error:
        print(f"Setup failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
