import pytest

from data import DATA_PATH
from day7.solution import read_input, TachyonManifold


@pytest.fixture
def example_data():
    return read_input(DATA_PATH / 'day7_example.txt')


@pytest.fixture
def real_data():
    return read_input(DATA_PATH / 'day7_input.txt')


def test_part_1_example(example_data):
    tm = TachyonManifold(example_data)
    assert tm.splits_count() == 21


def test_part_1_real(real_data):
    tm = TachyonManifold(real_data)
    assert tm.splits_count() == 1649


def test_part_2_example(example_data):
    tm = TachyonManifold(example_data)
    assert tm.total_paths() == 40


def test_part_2_real(real_data):
    tm = TachyonManifold(real_data)
    assert tm.total_paths() == 16937871060075
