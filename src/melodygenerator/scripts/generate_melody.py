import click

from typing import Dict, List

from melodygenerator.data.constants import BEATS_PER_BAR
from melodygenerator.data.enums import MidiData, Model
from melodygenerator.data.get_data import get_melody_pattern, initialise_model


@click.command()
@click.option("--model", default="random", help="Only 'random' supported!")
@click.option("--scale", default="C", help="Pick a harmonic scale (e.g., C, D#, Ab etc)")
@click.option("--bpm", default=126, help="Tempo of melody")
def generate_melody(model_name: str, scale: str, bpm: int):
    model = initialise_model(model_name)
    melody_pattern = get_melody_pattern()

    pattern_memo: Dict[str, List[MidiData]] = {}
    for pattern in melody_pattern:
        if pattern in pattern_memo:
            continue
        time = 0
        pattern_memo[pattern] = []
        while time < BEATS_PER_BAR:
            pass


if __name__ == "main":
    generate_melody()
