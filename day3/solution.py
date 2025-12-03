from dataclasses import dataclass
from pathlib import Path


@dataclass
class Solution:
    part_one: int
    part_two: int

    def __repr__(self):
        return f'Solution - Day 3\n\tPart 1: {self.part_one}\n\tPart 2: {self.part_two}'


class BatteryBank:
    def __init__(self, batteries: str):
        self.batteries = batteries
        self._size = len(batteries)

    def max_jolt(self, k) -> int:
        n_batteries = len(self.batteries)
        dp = [[0] * (k + 1) for _ in range(n_batteries + 1)]

        for i in range(1, n_batteries + 1):
            for j in range(1, min(i, k) + 1):
                current_digit = int(self.batteries[i - 1])
                if j == 1:
                    dp[i][j] = max(dp[i - 1][j], current_digit)
                else:
                    dp[i][j] = max(dp[i - 1][j],
                                   dp[i - 1][j - 1] * 10 + current_digit)
        return max(dp[-1])


def _read_input(file_path) -> list[BatteryBank]:
    with open(file_path, 'r') as file:
        return [BatteryBank(line.strip()) for line in file]


def solve(filepath: Path) -> Solution:
    banks = _read_input(filepath)
    return Solution(
        part_one=sum(bank.max_jolt(k=2) for bank in banks),
        part_two=sum(bank.max_jolt(k=12) for bank in banks)
    )


if __name__ == '__main__':
    from data import DATA_PATH

    print(solve(DATA_PATH / 'day3_input.txt'))
