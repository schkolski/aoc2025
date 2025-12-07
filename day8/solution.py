from dataclasses import dataclass
from pathlib import Path


@dataclass
class Solution:
    part_one: int
    part_two: int

    def __repr__(self):
        return f'Solution - Day 8\n\tPart 1: {self.part_one}\n\tPart 2: {self.part_two}'


def read_input(file_path: Path):
    pass  # Implement


def solve_part1(data) -> int:
    pass  # Implement


def solve_part2(data) -> int:
    pass  # Implement


def solve(filepath: Path) -> Solution:
    data = read_input(filepath)
    return Solution(
        part_one=solve_part1(data),
        part_two=solve_part2(data))


if __name__ == '__main__':
    from data import DATA_PATH

    print("Example data")
    print(solve(DATA_PATH / 'day8_example.txt'))
    print("Real data")
    print(solve(DATA_PATH / 'day8_input.txt'))
