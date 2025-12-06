import math
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Solution:
    part_one: int
    part_two: int

    def __repr__(self):
        return f'Solution - Day 6\n\tPart 1: {self.part_one}\n\tPart 2: {self.part_two}'


def read_input(file_path: Path) -> list[str]:
    lines = []
    with open(file_path) as file:
        for line in file:
            lines.append(line)
    return lines


def parse_input(lines: list[str]) -> tuple[list[str], list[str]]:
    operators = [elem.strip() for elem in lines[-1].strip().split()]
    return lines[:-1], operators


def math_solution(numbers: list[int], operator: str) -> int:
    return sum(numbers) if operator == '+' else math.prod(numbers)


def solve_part1(numbers: list[str], operators: list[str]) -> int:
    grand_total = 0
    numbers = [list(map(int, line.split())) for line in numbers]
    for col_idx, op in enumerate(operators):
        column_values = [numbers[row_idx][col_idx] for row_idx in range(len(numbers))]
        grand_total += math_solution(column_values, op)
    return grand_total


def solve_part2(numbers: list[str], operators: list[str]) -> int:
    grand_total = 0
    column_values = []
    operators = (op for op in operators)

    for i, _ in enumerate(numbers[0]):
        number = ''.join(ch for ch in [numbers[j][i] for j in range(len(numbers))])
        if not number.strip():
            grand_total += math_solution(column_values, next(operators))
            column_values = []
        else:
            column_values.append(int(number.strip()))
    if len(column_values) > 0:
        grand_total += math_solution(column_values, next(operators))

    return grand_total


def solve(filepath: Path) -> Solution:
    numbers, operators = parse_input(read_input(filepath))
    return Solution(
        part_one=solve_part1(numbers, operators),
        part_two=solve_part2(numbers, operators))


if __name__ == '__main__':
    from data import DATA_PATH

    print(solve(DATA_PATH / 'day6_input.txt'))
