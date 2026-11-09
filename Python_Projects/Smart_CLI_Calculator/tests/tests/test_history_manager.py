
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

import history_manager


class TestHistoryManager(unittest.TestCase):

    def test_save_and_load_history(self):
        sample = [{"operation": "Addition", "result": 30}]

        with tempfile.TemporaryDirectory() as folder:
            file_path = Path(folder) / "history.json"

            with patch.object(history_manager, "HISTORY_FILE", file_path):
                history_manager.save_history(sample)
                data, available = history_manager.load_history()

        self.assertEqual(data, sample)
        self.assertTrue(available)

    def test_load_missing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            file_path = Path(folder) / "missing.json"

            with patch.object(history_manager, "HISTORY_FILE", file_path):
                data, available = history_manager.load_history()

        self.assertEqual(data, [])
        self.assertTrue(available)

    def test_load_invalid_json(self):
        with tempfile.TemporaryDirectory() as folder:
            file_path = Path(folder) / "history.json"
            file_path.write_text("{invalid", encoding="utf-8")

            with patch.object(history_manager, "HISTORY_FILE", file_path):
                data, available = history_manager.load_history()

        self.assertEqual(data, [])
        self.assertFalse(available)


if __name__ == "__main__":
    unittest.main()
