from dataclasses import dataclass
from pathlib import Path


@dataclass
class Solution:
    part_one: int
    part_two: int

    def __repr__(self):
        return f'Solution - Day 5\n\tPart 1: {self.part_one}\n\tPart 2: {self.part_two}'


def read_input(file_path):
    with open(file_path) as file:
        all_lines = file.readlines()
        ranges = []
        queries = []
        for line in all_lines:
            line = line.strip()
            if not line:
                continue
            elif '-' in line:
                parts = line.split('-')
                ranges.append((int(parts[0]), int(parts[1])))
            else:
                queries.append(int(line))
    return ranges, queries


def merge(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not ranges:
        return []

    sorted_ranges = sorted(ranges)
    merged_ranges = [sorted_ranges[0]]
    for (curr_start, curr_end) in sorted_ranges[1:]:
        (latest_merged_start, latest_merged_end) = merged_ranges[-1]
        if latest_merged_end < curr_start - 1:
            merged_ranges.append((curr_start, curr_end))
        else:
            merged_ranges[-1] = (latest_merged_start, max(latest_merged_end, curr_end))
    return merged_ranges


def in_any(query: int, ranges: list[tuple[int, int]]) -> bool:
    for (sr, er) in ranges:
        if sr <= query <= er:
            return True
    return False


def solve_part1(ranges, queries) -> int:
    return sum(in_any(q, ranges) for q in queries)


def solve_part2(ranges) -> int:
    merged_ranges = merge(ranges)
    return sum((re - rs + 1) for (rs, re) in merged_ranges)


def solve(filepath: Path) -> Solution:
    ranges, queries = read_input(filepath)
    return Solution(part_one=solve_part1(ranges, queries), part_two=solve_part2(ranges))


if __name__ == '__main__':
    from data import DATA_PATH

    print(solve(DATA_PATH / 'day5_input.txt'))
