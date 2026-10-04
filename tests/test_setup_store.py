"""Exercise setup against isolated homes, source stores, and installed links."""

import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("setup_store", Path(__file__).resolve().parents[1] / "scripts" / "setup_store.py")
setup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(setup)


class SetupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name)
        self.config = self.home / ".config/agent-loop/config.toml"
        self.source = self.home / "source"
        self.root = self.home / "agent-loop"

    def run_setup(self, *args):
        with patch.object(setup.Path, "home", return_value=self.home), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return setup.main(list(args))

    def snapshot(self, root):
        return {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}

    def test_init_preview_writes_nothing(self):
        self.assertEqual(self.run_setup("init", "--root", str(self.source), "--dry-run"), 0)
        self.assertEqual(list(self.home.iterdir()), [])

    def test_init_is_repeatable_and_does_not_configure_device(self):
        self.assertEqual(self.run_setup("init", "--root", str(self.source)), 0)
        before = self.snapshot(self.source)
        self.assertIn(Path("cases/.gitkeep"), before)
        self.assertIn(Path("evidence/.gitkeep"), before)
        self.assertEqual(self.run_setup("init", "--root", str(self.source)), 0)
        self.assertEqual(self.snapshot(self.source), before)
        self.assertFalse(self.config.exists())

    def test_existing_alternate_layout_is_preserved(self):
        self.source.mkdir()
        (self.source / "notes.txt").write_text("original")
        self.assertEqual(self.run_setup("init", "--root", str(self.source)), 0)
        self.assertEqual(self.snapshot(self.source), {Path("notes.txt"): b"original"})

    def test_configure_missing_store_never_creates_it(self):
        self.assertEqual(self.run_setup("configure"), 1)
        self.assertEqual(self.run_setup("configure", "--dry-run"), 1)
        self.assertEqual(list(self.home.iterdir()), [])

    def test_configure_preview_and_repeat_preserve_store(self):
        self.root.mkdir()
        (self.root / "data.txt").write_text("original")
        self.assertEqual(self.run_setup("configure", "--mode", "automatic", "--dry-run"), 0)
        self.assertFalse(self.config.exists())
        self.assertEqual(self.run_setup("configure", "--mode", "automatic"), 0)
        before = self.snapshot(self.home)
        self.assertEqual(self.run_setup("configure"), 0)
        self.assertEqual(self.run_setup("configure", "--check"), 0)
        self.assertEqual(self.snapshot(self.home), before)
        self.assertEqual(setup.read_config(self.config)["mode"], "automatic")

    def test_configure_default_mode_is_proposals(self):
        self.root.mkdir()
        self.assertEqual(self.run_setup("configure"), 0)
        self.assertEqual(setup.read_config(self.config)["mode"], "proposals")
        self.assertEqual(list(self.root.iterdir()), [])

    def test_conflicting_config_is_preserved(self):
        self.root.mkdir()
        self.assertEqual(self.run_setup("configure"), 0)
        before = self.config.read_bytes()
        self.assertEqual(self.run_setup("configure", "--mode", "automatic"), 1)
        self.assertEqual(self.config.read_bytes(), before)

    def test_invalid_config_does_not_affect_init(self):
        self.config.parent.mkdir(parents=True)
        self.config.write_text("invalid = [")
        self.assertEqual(self.run_setup("init", "--root", str(self.source)), 0)
        self.assertEqual(self.run_setup("configure", "--root", str(self.source)), 1)
        self.assertEqual(self.config.read_text(), "invalid = [")

    def test_invalid_recording_table_is_rejected(self):
        self.root.mkdir()
        self.config.parent.mkdir(parents=True)
        self.config.write_text('version = 1\ncase_recording = []\n')
        self.assertEqual(self.run_setup("configure"), 1)

    def test_relative_root_and_file_root_are_rejected(self):
        self.assertEqual(self.run_setup("init", "--root", "relative"), 1)
        self.root.write_text("keep")
        self.assertEqual(self.run_setup("init", "--root", str(self.root)), 1)
        self.assertEqual(self.run_setup("configure"), 1)
        self.assertEqual(self.root.read_text(), "keep")

    def test_check_missing_configuration_or_store_does_not_create_them(self):
        self.root.mkdir()
        self.assertEqual(self.run_setup("configure", "--check"), 1)
        self.assertFalse(self.config.exists())
        self.assertEqual(self.run_setup("configure"), 0)
        self.root.rmdir()
        self.assertEqual(self.run_setup("configure", "--check"), 1)
        self.assertFalse(self.root.exists())

    def test_absolute_path_with_quotes_round_trips(self):
        root = self.home / 'store "quoted" 한글'
        root.mkdir()
        self.assertEqual(self.run_setup("configure", "--root", str(root), "--mode", "disabled"), 0)
        self.assertEqual(setup.read_config(self.config)["root"], str(root))

    def test_installed_link_preserves_link_and_source(self):
        self.assertEqual(self.run_setup("init", "--root", str(self.source)), 0)
        before = self.snapshot(self.source)
        try:
            self.root.symlink_to(self.source, target_is_directory=True)
        except OSError as error:
            self.skipTest(f"Directory symlinks unavailable: {error}")
        self.assertEqual(self.run_setup("configure", "--mode", "automatic"), 0)
        self.assertTrue(self.root.is_symlink())
        self.assertEqual(setup.read_config(self.config)["root"], str(self.root))
        self.assertEqual(self.snapshot(self.source), before)

    def test_init_supports_empty_git_checkout(self):
        self.source.mkdir()
        (self.source / ".git").mkdir()
        self.assertEqual(self.run_setup("init", "--root", str(self.source)), 0)
        self.assertTrue((self.source / ".git").is_dir())
        self.assertTrue((self.source / "README.md").is_file())
        self.assertFalse(self.config.exists())


if __name__ == "__main__":
    unittest.main()
