import pytest

from data import DATA_PATH
from day5.solution import read_input, solve_part1, solve_part2


@pytest.fixture
def example_data():
    return read_input(DATA_PATH / "day5_example.txt")


@pytest.fixture
def real_data():
    return read_input(DATA_PATH / 'day5_input.txt')


def test_part_1_example(example_data):
    ranges, queries = example_data
    assert solve_part1(ranges, queries) == 3


def test_part_1_real(real_data):
    ranges, queries = real_data
    assert solve_part1(ranges, queries) == 638


def test_part_2_example(example_data):
    ranges, queries = example_data
    assert solve_part2(ranges) == 14


def test_part_2_real(real_data):
    ranges, queries = real_data
    assert solve_part2(ranges) == 352946349407338
