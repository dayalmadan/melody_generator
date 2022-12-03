from typing import Dict, List

from melodygenerator.data.enums import Model


BEATS_PER_BAR: int = 4
VOLUME: int = 100

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

NOTE_DURATION_MAP: Dict[str, float] = {  # indicates length of note as percent of 1 beat
    "1/16": 1 / 16,
    "1/8": 1 / 8,
    "1/4": 1 / 4,
    "1/2": 1 / 2,
    "1": 1,
}

MODEL_MAP: Dict[str, Model] = {"random": Model.RANDOM}
