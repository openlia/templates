import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import validate_catalog


class CatalogConsistencyTests(unittest.TestCase):
    def test_check_is_read_only_and_explicit_generation_is_required(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "catalog.json"
            expected = {"profiles": [], "features": [], "skills": []}
            with patch.object(validate_catalog, "CATALOG_PATH", path), patch.object(
                validate_catalog, "build_catalog", return_value=expected
            ), patch.object(validate_catalog, "validate_all", side_effect=lambda **_: []), contextlib.redirect_stderr(io.StringIO()), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(validate_catalog.main(["--no-self-test"]), 1)
                self.assertFalse(path.exists())
                path.write_text('{"stale": true}\n')
                before = path.read_bytes()
                self.assertEqual(validate_catalog.main(["--no-self-test"]), 1)
                self.assertEqual(path.read_bytes(), before)
                self.assertEqual(validate_catalog.main(["--write-catalog", "--no-self-test"]), 0)
                self.assertEqual(json.loads(path.read_text()), expected)
                self.assertEqual(validate_catalog.main(["--no-self-test"]), 0)

    def test_invalid_manifests_do_not_overwrite_catalog(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "catalog.json"
            path.write_text('{"existing": true}\n')
            before = path.read_bytes()
            with patch.object(validate_catalog, "CATALOG_PATH", path), patch.object(
                validate_catalog, "build_catalog", return_value={}
            ), patch.object(validate_catalog, "validate_all", return_value=["invalid manifest"]), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(validate_catalog.main(["--write-catalog", "--no-self-test"]), 1)
            self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
