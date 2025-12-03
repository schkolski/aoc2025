import pytest

from data import DATA_PATH
from day3.solution import BatteryBank


@pytest.fixture
def example_banks():
    return [
        BatteryBank(batteries='987654321111111'),
        BatteryBank(batteries='811111111111119'),
        BatteryBank(batteries='234234234234278'),
        BatteryBank(batteries='818181911112111')
    ]


@pytest.fixture
def banks():
    banks = []
    with open(DATA_PATH / 'day3_input.txt', 'r') as file:
        for line in file:
            banks.append(BatteryBank(line.strip()))
    return banks


def test_part_1_example(example_banks):
    assert sum(bank.max_jolt(k=2) for bank in example_banks) == 357


def test_part_1_real(banks):
    assert sum(bank.max_jolt(k=2) for bank in banks) == 17445


def test_part_2_example(example_banks):
    assert sum(bank.max_jolt(k=12) for bank in example_banks) == 3121910778619


def test_part_2_real(banks):
    assert sum(bank.max_jolt(k=12) for bank in banks) == 173229689350551
