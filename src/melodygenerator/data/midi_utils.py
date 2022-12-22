from io import BytesIO
from time import sleep
from typing import Dict, List

import pygame

from midiutil import MIDIFile

import melodygenerator.data.constants as const

from melodygenerator.data.enums import MidiData


def play_melody(melody_pattern: str, pattern_memo: Dict[str, List[MidiData]], bpm: int) -> None:
    midi = MIDIFile(1)
    midi.addTempo(0, 0, bpm)
    bar_number = 0
    for pattern in melody_pattern:
        for midi_data in pattern_memo[pattern]:
            time = midi_data.start_time + bar_number * const.BEATS_PER_BAR
            midi.addNote(0, 0, midi_data.note, time, midi_data.duration, const.VOLUME)
        bar_number += 1

    mem_file = BytesIO()
    midi.writeFile(mem_file)
    pygame.init()
    pygame.mixer.init()
    mem_file.seek(0)  # THIS IS CRITICAL, OTHERWISE YOU GET THAT ERROR!
    pygame.mixer.music.load(mem_file)

    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        sleep(1)
    print("Done!")
