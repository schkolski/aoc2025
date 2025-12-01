import enum
from dataclasses import dataclass
from pathlib import Path

MAX_VALUE = 100


class CommandDirection(enum.Enum):
    LEFT = 'L'
    RIGHT = 'R'

    @staticmethod
    def from_text(text: str) -> 'CommandDirection':
        if text == 'L':
            return CommandDirection.LEFT
        elif text == 'R':
            return CommandDirection.RIGHT
        else:
            raise ValueError(f'Invalid command direction: {text}')


@dataclass
class Command:
    value: int
    direction: CommandDirection
    full_rotations: int

    @staticmethod
    def from_text(text: str) -> 'Command':
        val = int(text[1:])
        direction_text = text[0]
        return Command(
            value=val % MAX_VALUE,
            direction=CommandDirection.from_text(direction_text),
            full_rotations=val // MAX_VALUE)


class Vault:
    def __init__(self):
        self._over_zero_count = 0
        self._landed_on_zero = 0
        self._state = 50

    @property
    def state(self):
        """Current state of the vault (0-99)."""
        return self._state

    @property
    def zeros_count(self):
        """Number of times the vault has landed on zero."""
        return self._landed_on_zero

    @property
    def over_zero_count(self):
        """Number of times the vault has passed over zero."""
        return self._over_zero_count

    def turn(self, cmd: Command):
        """Turn the vault according to the command."""
        _starting_state = self._state
        if cmd.direction == CommandDirection.LEFT:
            self._state -= cmd.value
        else:
            self._state += cmd.value
        self._update_state(
            prev_state=_starting_state,
            full_rotations=cmd.full_rotations
        )

    def _update_state(self, prev_state: int, full_rotations: int = 0):
        self._over_zero_count += full_rotations
        if self.state >= MAX_VALUE:
            self._over_zero_count += (self.state // MAX_VALUE)
        elif self.state <= 0 and prev_state != 0:
            self._over_zero_count += 1

        self._state = self._state % MAX_VALUE
        self._landed_on_zero += 1 if self._state == 0 else 0

    def __repr__(self):
        return f'Vault(state={self.state}, zeros_count={self.zeros_count}, over_zero_count={self.over_zero_count})'


@dataclass
class Solution:
    part_one: int
    part_two: int


def solve(filepath: Path) -> Solution:
    vault = Vault()
    with open(filepath, 'r') as f:
        for line in f:
            cmd_text = line.strip()
            cmd = Command.from_text(cmd_text)
            vault.turn(cmd)

    return Solution(
        part_one=vault.zeros_count,
        part_two=vault.over_zero_count
    )
