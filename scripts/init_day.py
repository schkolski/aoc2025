import sys
from argparse import ArgumentParser
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / 'data'


def create_day(day_num: int):
    day_str = f"{int(day_num):d}"

    init_template = f'''from .solution import solve'''

    solution_template = f'''from dataclasses import dataclass
from pathlib import Path


@dataclass
class Solution:
    part_one: int
    part_two: int

    def __repr__(self):
        return f'Solution - Day {day_str}\\n\\tPart 1: {{self.part_one}}\\n\\tPart 2: {{self.part_two}}'


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
    print(solve(DATA_PATH / 'day{day_str}_example.txt'))
    print("Real data")
    print(solve(DATA_PATH / 'day{day_str}_input.txt'))
'''

    test_template = f'''import pytest

from data import DATA_PATH
from day{day_str}.solution import read_input, solve_part1, solve_part2


@pytest.fixture
def example_data():
    return read_input(DATA_PATH / 'day{day_str}_example.txt')


@pytest.fixture
def real_data():
    return read_input(DATA_PATH / 'day{day_str}_input.txt')


def test_part_1_example(example_data):
    assert False  # Implement test for part 1 example


def test_part_1_real(real_data):
    assert False  # Implement test for part 1 real


def test_part_2_example(example_data):
    assert False  # Implement test for part 2 example


def test_part_2_real(real_data):
    assert False  # Implement test for part 2 real
'''

    init_file = Path(f"day{day_str}/__init__.py")
    solution_file = Path(f"day{day_str}/solution.py")
    test_file = Path(f"day{day_str}/test_solution.py")

    # Ensure directories exist
    init_file.parent.mkdir(parents=True, exist_ok=True)
    solution_file.parent.mkdir(parents=True, exist_ok=True)
    test_file.parent.mkdir(parents=True, exist_ok=True)

    file_creation(init_file, init_template)
    file_creation(solution_file, solution_template)
    file_creation(test_file, test_template)

    create_empty_example_input_file(day_str)


def create_empty_example_input_file(day_str: str):
    input_file = DATA_PATH / f'day{day_str}_example.txt'
    input_file.parent.mkdir(parents=True, exist_ok=True)
    if not input_file.exists():
        input_file.touch()
        print(f"✅ Created empty input file {input_file}")


def file_creation(file_: Path, file_template: str):
    if file_.exists():
        print(f"⚠️  {file_} already exists. Skipping.")
    else:
        file_.write_text(file_template)
        print(f"✅ Created {file_}")


def main():
    parser = ArgumentParser(description="Initialize boilerplate files for an Advent of Code day.")

    parser.add_argument(
        "day",
        type=int,
        help="The day number to initialize (1-25)"
    )

    args = parser.parse_args()

    # Validate day range for AoC
    if not (1 <= args.day <= 25):
        print(f"❌ Error: Day must be between 1 and 25. You provided {args.day}.")
        sys.exit(1)

    create_day(args.day)


if __name__ == "__main__":
    main()
