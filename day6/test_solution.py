import pytest

from data import DATA_PATH
from day6.solution import read_input, parse_input, solve_part1, solve_part2


@pytest.fixture
def example_data():
    return """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.lstrip().split('\n')


@pytest.fixture
def real_data():
    return read_input(DATA_PATH / 'day6_input.txt')


def test_part_1_example(example_data):
    nums, ops = parse_input(example_data)
    assert solve_part1(nums, ops) == 4277556


def test_part_1_real(real_data):
    nums, ops = parse_input(real_data)
    assert solve_part1(nums, ops) == 5335495999141


def test_part_2_example(example_data):
    nums, ops = parse_input(example_data)
    assert solve_part2(nums, ops) == 3263827


def test_part_2_real(real_data):
    nums, ops = parse_input(real_data)
    assert solve_part2(nums, ops) == 10142723156431
