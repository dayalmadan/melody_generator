from abc import ABC, abstractmethod
from random import randint, uniform
from typing import List, Optional, Tuple


class Generator(ABC):

    def __init__(self, notes_per_scale: int, note_lens: int):
        self.notes_per_scale = notes_per_scale
        self.note_lens = note_lens

    @abstractmethod
    def next_note(self):
        pass


class RandomGenerator(Generator):
    def __init__(self, note_prob: List[float], silence_prob: float, notes_per_scale: int, note_lens: int):
        self.note_prob = note_prob
        self.silence_prob = silence_prob
        super().__init__(notes_per_scale, note_lens)

    def next_note(self) -> Tuple[Optional[int], int]:
        if self._is_silence():
            return None, randint(0, self.note_lens)
        return randint(0, self.notes_per_scale), randint(0, self.note_lens)

    def _is_silence(self) -> bool:
        return uniform(0, 1) <= self.silence_prob
