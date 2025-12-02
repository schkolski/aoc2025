from dataclasses import dataclass
from pathlib import Path
from typing import List

SortedList = List


@dataclass
class Range:
    start: int
    end: int


@dataclass
class Solution:
    part_one: int
    part_two: int

    def __repr__(self):
        return f'Solution - Day 2\n\tPart 1: {self.part_one}\n\tPart 2: {self.part_two}'


def _read_input(file_path) -> list[Range]:
    ranges = []
    with open(file_path, 'r') as file:
        lines = file.readline().strip().split(',')
        for range_txt in lines:
            start_end = range_txt.split('-')
            ranges.append(Range(start=int(start_end[0]), end=int(start_end[1])))
    return ranges


def _build_invalid_ids(*, max_digits: int = 6, max_reps: int = 2) -> SortedList[int]:
    if max_digits < 2:
        raise ValueError('max_digits must be >= 2')
    if max_reps < 2:
        raise ValueError('max_reps must be >= 2')

    invalid_ids = set()
    max_value = int('9' * (max_digits // 2))
    for k in range(2, max_reps + 1):
        for curr_number in range(1, max_value + 1):
            number_as_text = str(curr_number) * k
            if len(number_as_text) > max_digits:
                break
            invalid_ids.add(int(number_as_text))

    return sorted(list(invalid_ids))


def _calculate_sum_for_all(ranges: list[Range], invalid_ids: SortedList[int]) -> int:
    return sum(invalid_id
               for current_range in ranges
               for invalid_id in invalid_ids
               if current_range.start <= invalid_id <= current_range.end)


def _solve_part_1(ranges: list[Range]) -> int:
    invalid_ids_part1 = _build_invalid_ids(max_digits=10, max_reps=2)
    return _calculate_sum_for_all(ranges, invalid_ids_part1)


def _solve_part_2(ranges: list[Range]) -> int:
    invalid_ids_part2 = _build_invalid_ids(max_digits=10, max_reps=10)
    return _calculate_sum_for_all(ranges, invalid_ids_part2)


def solve(filepath: Path) -> Solution:
    input_ranges = _read_input(filepath)
    return Solution(
        part_one=_solve_part_1(input_ranges),
        part_two=_solve_part_2(input_ranges)
    )
