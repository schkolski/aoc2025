from dataclasses import dataclass
from pathlib import Path


@dataclass
class Solution:
    part_one: int
    part_two: int

    def __repr__(self):
        return f'Solution - Day 4\n\tPart 1: {self.part_one}\n\tPart 2: {self.part_two}'


@dataclass
class Something:
    pass


def _read_input(file_path) -> list[Something]:
    pass


def solve(filepath: Path) -> Solution:
    pass


if __name__ == '__main__':
    from data import DATA_PATH

    print(solve(DATA_PATH / 'day4_input.txt'))
