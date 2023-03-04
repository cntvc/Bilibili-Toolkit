import unittest
from pathlib import Path

from bilibili_toolkit.core.config import load_file, settings
from bilibili_toolkit.exceptions import FileNotFoundError

CONFIG_FILE = Path(__file__).parent / "test_config.toml"


class TestConfig(unittest.TestCase):
    def test_load_file_error(self):
        with self.assertRaises(FileNotFoundError):
            load_file("")

    def test_load_config_val(self):
        load_file(CONFIG_FILE)
        assert settings.NAME == "BILIBILI"
