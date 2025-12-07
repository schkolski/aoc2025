from dataclasses import dataclass
from pathlib import Path


@dataclass
class Solution:
    part_one: int
    part_two: int

    def __repr__(self):
        return f'Solution - Day 7\n\tPart 1: {self.part_one}\n\tPart 2: {self.part_two}'


def read_input(file_path: Path) -> list[str]:
    lines = []
    with open(file_path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


class TachyonManifold:

    def __init__(self, lines: list[str]):
        self.grid = lines
        self.column_len = len(lines[0])
        self.row_len = len(lines)
        self._splits_count = 0
        self._total_paths = 0
        self._pre_process_the_grid()

    def _pre_process_the_grid(self):
        splits_count = 0
        counts = [0 if c != 'S' else 1 for c in self.grid[0]]
        for row in self.grid[:-1]:
            next_counts = [0] * self.column_len

            for idx, current_char in enumerate(row):
                if current_char == '^':
                    if counts[idx] > 0:
                        splits_count += 1
                    if idx > 0:
                        next_counts[idx - 1] += counts[idx]
                    if idx < self.column_len - 1:
                        next_counts[idx + 1] += counts[idx]
                else:
                    next_counts[idx] += counts[idx]
            counts = next_counts

        self._splits_count = splits_count
        self._total_paths = sum(counts)

    def splits_count(self):
        return self._splits_count

    def total_paths(self):
        return self._total_paths

    def __repr__(self):
        return f'TachyonManifold(splits_count={self._splits_count}, total_paths={self._total_paths})'



def solve(filepath: Path) -> Solution:
    tachyon_manifold = TachyonManifold(lines=read_input(filepath))
    return Solution(
        part_one=tachyon_manifold.splits_count(),
        part_two=tachyon_manifold.total_paths())


if __name__ == '__main__':
    from data import DATA_PATH

    print("Example data")
    print(solve(DATA_PATH / 'day7_example.txt'))
    print("Real data")
    print(solve(DATA_PATH / 'day7_input.txt'))
