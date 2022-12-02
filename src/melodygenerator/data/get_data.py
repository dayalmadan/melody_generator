import random

from typing import Optional

import melodygenerator.config.get as mcg
import melodygenerator.data.constants as const
from melodygenerator.data.enums import DataType, Model
from melodygenerator.models import Generator, RandomGenerator


def get_melody_pattern() -> str:
    """
    Fetches possible patterns from config and returns one randomly selected melody pattern
    """
    melody_patterns = mcg.get_config(option="melody_patterns", data_type=DataType.LIST)
    if not melody_patterns:
        raise IndexError("Cannot fetch list of possible melody patterns from config!")
    return melody_patterns[random.randint(0, len(melody_patterns) - 1)]


def get_duration_from_id(duration_id: int) -> float:
    # TODO
    # if midi_time + note_duration > BEATS_PER_BAR:
    #     note_duration = BEATS_PER_BAR - midi_time
    return 0.0


def get_note_number_from_id(scale: str, note_id: Optional[int] = None) -> int:
    # TODO
    return 0


def initialise_model(model_name: str) -> Optional[Generator]:
    model_id = _get_model_from_name(model_name)
    if model_id == Model.RANDOM:
        note_len_prob = mcg.get_config(section="random", option="note_probabilities", data_type=DataType.LIST)
        silence_prob = mcg.get_config(section="random", option="silence_probability", data_type=DataType.FLOAT)
        return RandomGenerator(
            note_len_prob=note_len_prob, silence_prob=silence_prob, notes_per_scale=len(const.MAJOR_SCALE)
        )
    return None


def _get_model_from_name(model_name: str) -> Model:
    model_name = model_name.lower()
    if model_name not in const.MODEL_MAP:
        raise ValueError(f"Model name {model_name} is not a valid model!")
    return const.MODEL_MAP[model_name]
