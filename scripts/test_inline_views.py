"""Keep the native data-backed views installable by the inline OpenUI runtime."""

from pathlib import Path
import unittest

from validate_catalog import parse_frontmatter


ROOT = Path(__file__).resolve().parents[1]


class InlineViewTests(unittest.TestCase):
    def test_native_views_are_markdown_not_mini_projects(self):
        for feature, folder, component, template in (
            ("calendar", "calendar", "Calendar", "event-note-template.md"),
            ("personal-finance", "finance", "Finance", "finance-template.md"),
        ):
            with self.subTest(feature=feature):
                root = ROOT / "features" / feature / "workspace" / folder
                view = (root / "overview.md").read_text()
                metadata, body = parse_frontmatter(view)
                template_metadata, template_body = parse_frontmatter((root / template).read_text())
                self.assertEqual(metadata, template_metadata)
                self.assertIn(f"```openui\nroot = {component}([views])", body)
                self.assertNotIn("RecordTable(", body)
                self.assertFalse((root / "ui.openui").exists())
                self.assertFalse((root / "project-manifest.toml").exists())
                # Overview documents honor their folder-local record contracts.
                for line in template_body.splitlines():
                    if line.startswith("## "):
                        self.assertIn(line, body)


if __name__ == "__main__":
    unittest.main()
