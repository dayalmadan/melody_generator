from enum import Enum, auto
from dataclasses import dataclass


class DataType(Enum):
    INT = auto()
    FLOAT = auto()
    BOOL = auto()
    LIST = auto()


class Model(Enum):
    RANDOM = auto()


@dataclass
class MidiData:
    note: int
    start_time: float
    duration: float
