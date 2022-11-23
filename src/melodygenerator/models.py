import random

from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

class Generator(ABC):

    def __init__(self, notes_per_scale: int, note_lens: int):
        self.notes_per_scale = notes_per_scale
        self.note_lens = note_lens

    @abstractmethod
    def next_note(self):
        pass


class RandomGenerator(Generator):
    """
    A Generator to generate notes at random.
    """
    def __init__(self, note_len_prob: List[float], silence_prob: float, notes_per_scale: int):
        """
        :param note_len_prob: list of note length probabilities
        :param silence_prob: probability of next note being silence
        :param notes_per_scale: number of notes in a scale
        """
        self.note_len_prob = note_len_prob
        self.silence_prob = silence_prob
        super().__init__(notes_per_scale, len(note_len_prob))

    def next_note(self) -> Tuple[Optional[int], int]:
        """
        Returns a Tuple for next note and its length.
        """
        if self._is_silence():
            return None, random.randint(0, self.note_lens - 1)
        return random.randint(0, self.notes_per_scale - 1), random.randint(0, self.note_lens - 1)

    def _is_silence(self) -> bool:
        return random.uniform(0, 1) <= self.silence_prob
