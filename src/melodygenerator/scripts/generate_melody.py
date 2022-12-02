import click

from typing import Dict, List

import melodygenerator.data.get_data as data

from melodygenerator.data.constants import BEATS_PER_BAR
from melodygenerator.data.enums import MidiData


@click.command()
@click.option("--model", default="random", help="Only 'random' supported!")
@click.option("--scale", default="C", help="Pick a harmonic scale (e.g., C, D#, Ab etc)")
@click.option("--bpm", default=126, help="Tempo of melody")
def generate_melody(model_name: str, scale: str, bpm: int):
    model = data.initialise_model(model_name)
    melody_pattern = data.get_melody_pattern()

    pattern_memo: Dict[str, List[MidiData]] = {}
    for pattern in melody_pattern:
        if pattern in pattern_memo:
            continue
        midi_time = 0
        pattern_memo[pattern] = []
        while midi_time < BEATS_PER_BAR:
            note_id, duration_id = model.next_note()
            note_duration = data.get_duration_from_id(duration_id)
            note_number = data.get_note_number_from_id(scale, note_id)
            if note_number is None:
                # insert silence here!
                midi_time += note_duration
                continue
            pattern_memo[pattern].append(MidiData(note=note_number, start_time=midi_time, duration=note_duration))
            midi_time += note_duration


if __name__ == "main":
    generate_melody()
