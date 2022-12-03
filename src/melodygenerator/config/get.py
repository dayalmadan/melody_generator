import os

from configparser import ConfigParser
from typing import Any, Optional

from melodygenerator.data.enums import DataType

_CONFIG_DATA = ConfigParser()
_CONFIG_FILE = os.path.join(os.path.dirname(__file__), "data.ini")


def _read_config() -> None:
    global _CONFIG_DATA
    _CONFIG_DATA.read(_CONFIG_FILE)


def get_config(
    section: str = "common", option: Optional[str] = None, data_type: Optional[DataType] = None
) -> Optional[Any]:
    if not _CONFIG_DATA.has_option(section, option):
        _read_config()

    if data_type is not None:
        if data_type == DataType.INT:
            return _CONFIG_DATA.getint(section, option, fallback=None)

        if data_type == DataType.FLOAT:
            return _CONFIG_DATA.getfloat(section, option, fallback=None)

        if data_type == DataType.BOOL:
            return _CONFIG_DATA.getboolean(section, option, fallback=None)

        if data_type == DataType.LIST:
            data_from_config = _CONFIG_DATA.get(section, option, fallback=None)
            if data_from_config is not None:
                data_from_config = data_from_config.split(",")
            return data_from_config

    return _CONFIG_DATA.get(section, option, fallback=None)


# config common for all models
MELODY_PATTERNS = get_config(option="melody_patterns", data_type=DataType.LIST)
NOTE_LENGTHS = get_config(option="note_lengths", data_type=DataType.LIST)


# Config for random model
NOTE_PROBABILITIES = get_config(section="random", option="note_probabilities", data_type=DataType.LIST)
SILENCE_PROBABILITY = get_config(section="random", option="silence_probability", data_type=DataType.FLOAT)
