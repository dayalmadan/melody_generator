import pytest

from mock import patch

from melodygenerator.models import RandomGenerator


@pytest.mark.parametrize(
    "mock_randint, mock_uniform, expected",
    (
        ([5, 0], 0.5, (5, 0)),
        ([0, 1], 0.5, (0, 1)),
        ([1], 0.05, (None, 1)),
    ),
)
def test_random_generator(mock_randint, mock_uniform, expected):
    with patch("random.randint", side_effect=mock_randint), patch("random.uniform", return_value=mock_uniform):
        random_generator = RandomGenerator(note_len_prob=[0.8, 0.2], silence_prob=0.25, notes_per_scale=12)
        actual = random_generator.next_note()
        assert actual == expected
