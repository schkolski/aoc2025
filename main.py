from pathlib import Path

from day1 import solve as day1_solve

BASE_PATH = Path(__file__).parent


def print_solutions():
    print("Solutions:")
    print("    Day 1:", day1_solve(BASE_PATH / "data" / "day1_input.txt"))


if __name__ == '__main__':
    print_solutions()
