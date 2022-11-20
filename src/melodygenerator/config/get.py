import os

from configparser import ConfigParser
from enum import Enum
from typing import Any, Optional

_CONFIG_DATA = ConfigParser()
_CONFIG_FILE = os.path.join(os.path.dirname(__file__), "data.ini")


class DataType(Enum):
    INT = 1
    FLOAT = 2
    BOOL = 3
    LIST = 4


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


BEATS_PER_BAR = get_config(option="beats_per_bar", data_type=DataType.INT)
MELODY_PATTERNS = get_config(option="melody_patterns", data_type=DataType.LIST)
NOTE_LENGTHS = get_config(option="note_lengths", data_type=DataType.LIST)

C_MAJOR = get_config(section="midiutil", option="c_major", data_type=DataType.LIST)
C_MINOR = get_config(section="midiutil", option="c_minor", data_type=DataType.LIST)

NOTE_PROBABILITIES = get_config(section="random", option="note_probabilities", data_type=DataType.LIST)
SILENCE_PROBABILITY = get_config(section="random", option="silence_probability", data_type=DataType.FLOAT)
