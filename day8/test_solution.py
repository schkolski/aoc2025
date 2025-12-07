import pytest

from data import DATA_PATH
from day8.solution import read_input, solve_part1, solve_part2


@pytest.fixture
def example_data():
    return read_input(DATA_PATH / 'day8_example.txt')


@pytest.fixture
def real_data():
    return read_input(DATA_PATH / 'day8_input.txt')


def test_part_1_example(example_data):
    assert False  # Implement test for part 1 example


def test_part_1_real(real_data):
    assert False  # Implement test for part 1 real


def test_part_2_example(example_data):
    assert False  # Implement test for part 2 example


def test_part_2_real(real_data):
    assert False  # Implement test for part 2 real
