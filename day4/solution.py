from dataclasses import dataclass
from pathlib import Path


@dataclass
class Solution:
    part_one: int
    part_two: int

    def __repr__(self):
        return f'Solution - Day 4\n\tPart 1: {self.part_one}\n\tPart 2: {self.part_two}'


@dataclass
class PrintingDepartmentMap:
    grid: list[str]

    def moveable_positions(self):
        count = 0
        n, m = len(self.grid), len(self.grid[0])
        for i in range(0, n):
            for j in range(m):
                if self.grid[i][j] == '@' and self._is_moveable(i, j, n, m):
                    count += 1
        return count

    def trim(self):
        count = 0
        n, m = len(self.grid), len(self.grid[0])

        while True:
            removable = set()
            for i in range(0, n):
                for j in range(m):
                    if self.grid[i][j] == '@' and self._is_moveable(i, j, n, m):
                        removable.add((i, j))
            if not removable:
                break

            count += len(removable)
            for i, j in removable:
                str_i = self.grid[i]
                self.grid[i] = str_i[:j] + '.' + str_i[j + 1:]
        return count

    def _is_moveable(self, i, j, n, m) -> bool:
        all_directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        count_rolls = 0
        for di, dj in all_directions:
            ni, mj = i + di, j + dj
            if not (0 <= ni < n and 0 <= mj < m):
                continue
            if self.grid[ni][mj] == '@':
                count_rolls += 1

        return count_rolls < 4


def _read_input(file_path) -> PrintingDepartmentMap:
    with open(file_path) as file:
        grid = [line.strip() for line in file]
        return PrintingDepartmentMap(grid=grid)


def solve(filepath: Path) -> Solution:
    pd_map = _read_input(filepath)
    return Solution(part_one=pd_map.moveable_positions(), part_two=pd_map.trim())


if __name__ == '__main__':
    from data import DATA_PATH

    print(solve(DATA_PATH / 'day4_input.txt'))
