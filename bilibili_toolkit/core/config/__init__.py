from pathlib import Path

from dynaconf import Dynaconf

from bilibili_toolkit.exceptions import FileNotFoundError

_settings_files = [
    Path(__file__).parent / "default_settings.toml",
    Path.home() / "/.bilibili_toolkit/settings.toml",
]

settings = Dynaconf(
    core_loaders=["TOML"],
    # Loaded at the first
    preload=[],
    # Loaded second (the main file)
    settings_files=_settings_files,
    # If False, can't use `settings.foo`, but can only use `settings.FOO`
    lowercase_read=False,
    # Always reloaded from source without the need to reload the application
    # eg: fresh_vars=["password"]
    fresh_vars=[],
)


def load_file(config_path, settings=settings):
    if not config_path:
        raise FileNotFoundError("config file not found")
    settings.load_file(config_path)
