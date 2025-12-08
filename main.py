from dataclasses import dataclass
from functools import partial
from pathlib import Path
from typing import Callable

from day1 import solve as day1_solve
from day2 import solve as day2_solve
from day3 import solve as day3_solve
from day4 import solve as day4_solve
from day5 import solve as day5_solve
from day6 import solve as day6_solve
from day7 import solve as day7_solve
from day8 import solve as day8_solve



DATA_PATH = Path(__file__).parent / 'data'


@dataclass
class Solver:
    solve: Callable
    day: str


def print_solutions(solvers: list[Solver]):
    print("Solutions:")
    print()
    for solver in solvers:
        print(solver.solve(filepath=DATA_PATH / f"{solver.day}_input.txt"))
        print('-' * 30)


if __name__ == '__main__':
    print_solutions(
        solvers=[
            Solver(solve=day1_solve, day='day1'),
            Solver(solve=day2_solve, day='day2'),
            Solver(solve=day3_solve, day='day3'),
            Solver(solve=day4_solve, day='day4'),
            Solver(solve=day5_solve, day='day5'),
            Solver(solve=day6_solve, day='day6'),
            Solver(solve=day7_solve, day='day7'),
            Solver(solve=partial(day8_solve, k=1000), day='day8'),
        ]
    )
