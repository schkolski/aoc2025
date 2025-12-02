from pathlib import Path

from day2 import solve

DATA_PATH = Path(__file__).parent.parent / 'data'


def test_final_solution():
    solution = solve(DATA_PATH / 'day2_input.txt')

    assert solution.part_one == 64215794229
    assert solution.part_two == 85513235135
