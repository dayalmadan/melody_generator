from typing import Dict, List

from melodygenerator.data.enums import Model


BEATS_PER_BAR: int = 4

MAJOR_SCALE: List[int] = [0, 2, 4, 5, 7, 9, 11, 12]
MINOR_SCALE: List[int] = [0, 2, 3, 5, 7, 8, 10, 12]

NOTE_MAP: Dict[str, int] = {
    "C": 60,
    "C#": 61,
    "Db": 61,
    "D": 62,
    "D#": 63,
    "Eb": 63,
    "E": 64,
    "F": 65,
    "F#": 66,
    "Gb": 66,
    "G": 67,
    "G#": 68,
    "Ab": 68,
    "A": 69,
    "A#": 70,
    "Bb": 70,
    "B": 71,
}

MODEL_MAP: Dict[str, Model] = {"random": Model.RANDOM}
