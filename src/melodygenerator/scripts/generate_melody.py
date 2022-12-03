import click

from typing import Dict, List

import melodygenerator.data.get_data as data

from melodygenerator.data.constants import BEATS_PER_BAR
from melodygenerator.data.enums import MidiData
from melodygenerator.data.midi_utils import play_melody


@click.command()
@click.option("--model_name", default="random", help="Only 'random' supported!")
@click.option("--scale", default="C", help="Pick a harmonic scale (e.g., C, D#, Ab etc)")
@click.option(
    "--minor_scale",
    is_flag=True,
    show_default=False,
    default=False,
    help="Set this flag to generate melody in minor scale",
)
@click.option("--bpm", default=126, help="Tempo of melody")
def generate_melody(model_name: str, scale: str, bpm: int, minor_scale: bool):
    model = data.initialise_model(model_name)
    melody_pattern = data.get_melody_pattern()
    scale = scale.upper()

    pattern_memo: Dict[str, List[MidiData]] = {}

    for pattern in melody_pattern:

        if pattern in pattern_memo:
            continue

        midi_time = 0
        pattern_memo[pattern] = []

        while midi_time < BEATS_PER_BAR:
            note_id, duration_id = model.next_note()

            note_duration = data.get_duration_from_id(duration_id, midi_time)
            note_number = data.get_note_number_from_id(scale, minor_scale, note_id)

            if note_number is not None:
                pattern_memo[pattern].append(MidiData(note=note_number, start_time=midi_time, duration=note_duration))

            midi_time += note_duration

    play_melody(melody_pattern, pattern_memo, bpm)


if __name__ == "main":
    generate_melody()
