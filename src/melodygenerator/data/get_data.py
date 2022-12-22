import logging
import random

from typing import Optional

import melodygenerator.config.get as mcg
import melodygenerator.data.constants as const

from melodygenerator.data.enums import Model
from melodygenerator.models import Generator, RandomGenerator


def get_melody_pattern() -> str:
    """
    Fetches possible patterns from config and returns one randomly selected melody pattern
    """
    melody_patterns = mcg.MELODY_PATTERNS
    if not melody_patterns:
        raise IndexError("Cannot fetch list of possible melody patterns from config!")
    return melody_patterns[random.randint(0, len(melody_patterns) - 1)]


def get_duration_from_id(duration_id: int, midi_time: float) -> float:
    """
    Identifies duration of the note from the given note_id
    """
    note_len = mcg.NOTE_LENGTHS[duration_id]
    if note_len not in const.NOTE_DURATION_MAP:
        raise ValueError(f"{note_len} not found in NOTE_DURATION_MAP: {const.NOTE_DURATION_MAP}")
    note_duration = const.NOTE_DURATION_MAP[note_len] * const.BEATS_PER_BAR
    # make sure note duration does not overflows in a bar
    if midi_time + note_duration > const.BEATS_PER_BAR:
        note_duration = const.BEATS_PER_BAR - midi_time
    return note_duration


def get_note_number_from_id(scale: str, minor_scale: bool, note_id: Optional[int] = None) -> Optional[int]:
    """
    Identifies the note number from the given note id and scale
    """
    if note_id is None:
        return None
    if scale not in const.NOTE_MAP:
        logging.warning(f"Scale {scale} not recognised. Using default C scale.")
        scale = "C"
    note_number_list = const.MINOR_SCALE if minor_scale else const.MAJOR_SCALE
    return const.NOTE_MAP[scale] + note_number_list[note_id]


def initialise_model(model_name: str) -> Optional[Generator]:
    model_id = _get_model_from_name(model_name)
    if model_id == Model.RANDOM:
        note_len_prob = mcg.NOTE_PROBABILITIES
        silence_prob = mcg.SILENCE_PROBABILITY
        return RandomGenerator(
            note_len_prob=note_len_prob, silence_prob=silence_prob, notes_per_scale=len(const.MAJOR_SCALE)
        )
    return None


def _get_model_from_name(model_name: str) -> Model:
    model_name = model_name.lower()
    if model_name not in const.MODEL_MAP:
        raise ValueError(f"Model name {model_name} is not a valid model!")
    return const.MODEL_MAP[model_name]
