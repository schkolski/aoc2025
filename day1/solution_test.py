from dataclasses import dataclass

import pytest

from data import DATA_PATH
from .solution import Command, Vault, CommandDirection


@dataclass
class DataSet:
    commands: list[Command]


@pytest.fixture(scope='function')
def vault():
    return Vault()


@pytest.fixture(scope='session')
def example_data() -> DataSet:
    commands_as_text = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82"
    ]
    return DataSet(commands=list(
        Command.from_text(cmd_text) for cmd_text in commands_as_text))


@pytest.fixture(scope='session')
def real_data() -> DataSet:
    commands = []
    filepath = DATA_PATH / 'day1_input.txt'
    with open(filepath, 'r') as f:
        for line in f:
            cmd_text = line.strip()
            commands.append(Command.from_text(cmd_text))
    return DataSet(commands=commands)


def test_parse_left_command():
    cmd = Command.from_text("L68")
    assert cmd.value == 68
    assert cmd.direction == CommandDirection.LEFT


def test_parse_right_command():
    cmd = Command.from_text("R12")
    assert cmd.value == 12
    assert cmd.direction == CommandDirection.RIGHT


def test_parse_right_command_with_full_rotation():
    cmd = Command.from_text("R120")
    assert cmd.value == 20
    assert cmd.direction == CommandDirection.RIGHT
    assert cmd.full_rotations == 1


def test_parse_left_command_with_full_rotation():
    cmd = Command.from_text("L250")
    assert cmd.value == 50
    assert cmd.direction == CommandDirection.LEFT
    assert cmd.full_rotations == 2


def test_parse_command_with_invalid_direction_raises():
    with pytest.raises(ValueError) as excinfo:
        Command.from_text("X50")
    assert str(excinfo.value) == 'Invalid command direction: X'
    assert str(excinfo.value) == 'Invalid command direction: X'


def test_new_vault_has_state_50(vault: Vault):
    assert vault.state == 50


def test_turn_the_vault_to_the_right_increases_the_state_value(vault: Vault):
    vault.turn(Command.from_text("R1"))

    assert vault.state == 51


def test_turn_twice_in_right_direction(vault: Vault):
    vault.turn(Command.from_text("R1"))
    vault.turn(Command.from_text("R1"))

    assert vault.state == 52


def test_turn_to_the_left_decreases_the_state_value(vault: Vault):
    vault.turn(Command.from_text("L1"))

    assert vault.state == 49


def test_turn_to_the_left_twice(vault: Vault):
    vault.turn(Command.from_text("L1"))
    vault.turn(Command.from_text("L1"))

    assert vault.state == 48


def test_if_state_above_100_wraps_around(vault: Vault):
    vault.turn(Command.from_text("R60"))

    assert vault.state == 10


def test_if_state_below_0_wraps_around(vault: Vault):
    vault.turn(Command.from_text("L60"))

    assert vault.state == 90


def test_full_rotation_right(vault: Vault):
    vault.turn(Command.from_text("R100"))

    assert vault.state == 50


def test_full_rotation_left(vault: Vault):
    vault.turn(Command.from_text("L100"))

    assert vault.state == 50


def test_lending_on_zero_should_increase_zeros_count(vault: Vault):
    vault.turn(Command.from_text("L50"))

    assert vault.zeros_count == 1


def test_landing_on_zero_multiple_times(vault: Vault):
    vault.turn(Command.from_text("L50"))
    vault.turn(Command.from_text("R100"))
    vault.turn(Command.from_text("L100"))

    assert vault.zeros_count == 3


def _bulk_turn(vault: Vault, commands: list[Command]):
    for cmd in commands:
        vault.turn(cmd)


def test_part_1_given_example(vault: Vault, example_data: DataSet):
    _bulk_turn(vault, example_data.commands)

    assert vault.zeros_count == 3
    assert vault.state == 32


def test_part_1_real_input(vault: Vault, real_data: DataSet):
    _bulk_turn(vault, real_data.commands)

    assert vault.zeros_count == 1147
    assert vault.state == 70


def test_turn_over_zero_once_right(vault: Vault):
    vault.turn(Command.from_text("R60"))

    assert vault.over_zero_count == 1
    assert vault.state == 10


def test_turn_over_zero_two_times_turning_right(vault: Vault):
    vault.turn(Command.from_text("R70"))
    vault.turn(Command.from_text("R90"))

    assert vault.over_zero_count == 2
    assert vault.state == 10


def test_turn_over_zero_once_turning_left(vault: Vault):
    vault.turn(Command.from_text("L70"))

    assert vault.over_zero_count == 1
    assert vault.state == 80


def test_turn_over_zero_two_times_turning_left(vault: Vault):
    vault.turn(Command.from_text("L70"))
    vault.turn(Command.from_text("L90"))

    assert vault.over_zero_count == 2
    assert vault.state == 90


def test_turn_over_zero_should_be_counted_if_we_land_on_zero(vault: Vault):
    vault.turn(Command.from_text("L50"))

    assert vault.over_zero_count == 1
    assert vault.state == 0


def test_turn_right_when_on_zero_should_not_increase_over_zero_count(vault: Vault):
    vault.turn(Command.from_text("L50"))  # now on 0
    vault.turn(Command.from_text("R10"))

    assert vault.over_zero_count == 1
    assert vault.state == 10


def test_turn_left_when_on_zero_should_not_increase_over_zero_count(vault: Vault):
    vault.turn(Command.from_text("L50"))  # now on 0
    vault.turn(Command.from_text("L10"))

    assert vault.over_zero_count == 1
    assert vault.state == 90


def test_turn_with_multiple_full_circles_per_command_right(vault: Vault):
    vault.turn(Command.from_text("R240"))

    assert vault.over_zero_count == 2
    assert vault.state == 90


def test_turn_with_multiple_full_circles_per_command_and_semi_over_zero_turn_right(vault: Vault):
    vault.turn(Command.from_text("R260"))

    assert vault.over_zero_count == 3
    assert vault.state == 10


def test_turn_with_multiple_full_circles_per_command_left(vault: Vault):
    vault.turn(Command.from_text("L230"))

    assert vault.over_zero_count == 2
    assert vault.state == 20


def test_turn_with_multiple_full_circles_per_command_and_semi_over_zero_turn_left(vault: Vault):
    vault.turn(Command.from_text("L260"))

    assert vault.over_zero_count == 3
    assert vault.state == 90


def test_on_zero_turn_full_circle_right(vault: Vault):
    vault.turn(Command.from_text("L50"))
    vault.turn(Command.from_text("R100"))

    assert vault.over_zero_count == 2
    assert vault.state == 0


def test_on_zero_turn_full_circle_left(vault: Vault):
    vault.turn(Command.from_text("L50"))
    vault.turn(Command.from_text("L100"))

    assert vault.over_zero_count == 2
    assert vault.state == 0


def test_experimental(vault: Vault):
    vault.turn(Command.from_text("L50"))
    vault.turn(Command.from_text("L1"))
    vault.turn(Command.from_text("R2"))
    vault.turn(Command.from_text("L2"))

    assert vault.over_zero_count == 3
    assert vault.state == 99


def test_part_2_example_data(vault: Vault, example_data: DataSet):
    _bulk_turn(vault, example_data.commands)

    assert vault.over_zero_count == 6


def test_part_2_real_input(vault: Vault, real_data: DataSet):
    _bulk_turn(vault, real_data.commands)

    assert vault.over_zero_count == 6789


def test_vault_repr(vault: Vault):
    assert repr(vault) == 'Vault(state=50, zeros_count=0, over_zero_count=0)'
