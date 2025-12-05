import pytest

from data import DATA_PATH
from day4.solution import PrintingDepartmentMap, _read_input


@pytest.fixture
def example_data():
    return PrintingDepartmentMap(
        grid=[
            '..@@.@@@@.',
            '@@@.@.@.@@',
            '@@@@@.@.@@',
            '@.@@@@..@.',
            '@@.@@@@.@@',
            '.@@@@@@@.@',
            '.@.@.@.@@@',
            '@.@@@.@@@@',
            '.@@@@@@@@.',
            '@.@.@@@.@.'
        ]
    )


@pytest.fixture
def real_data():
    return _read_input(DATA_PATH / 'day4_input.txt')


def test_part_1_example(example_data: PrintingDepartmentMap):
    assert example_data.moveable_positions() == 13


def test_part_1_real(real_data: PrintingDepartmentMap):
    assert real_data.moveable_positions() == 1493


def test_part_2_example(example_data: PrintingDepartmentMap):
    assert example_data.trim() == 43


def test_part_2_real(real_data: PrintingDepartmentMap):
    assert real_data.trim() == 9194
