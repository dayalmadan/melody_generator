import pytest

from melodygenerator.config.get import get_config
from melodygenerator.enums import DataType


@pytest.mark.parametrize(
    "section, option, data_type, expected",
    (
        ("common", "beats_per_bar", DataType.INT, 4),
        ("random", "silence_probability", DataType.FLOAT, 0.25),
        ("common", "melody_patterns", DataType.LIST, "AABA,ABAB,ABAC,ABCB,AAAB".split(",")),
    ),
)
def test_get_config(section, option, data_type, expected):
    actual = get_config(section, option, data_type)
    assert actual == expected
