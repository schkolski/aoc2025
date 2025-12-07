from day7.solution import TachyonManifold


def test_simple_no_splits():
    tm = TachyonManifold(lines=[
        "S",
        "."
    ])
    assert tm.splits_count() == 0
    assert tm.total_paths() == 1


def test_one_split():
    tm = TachyonManifold(lines=[
        ".S.",
        ".^.",
        "..."
    ])
    assert tm.splits_count() == 1
    assert tm.total_paths() == 2


def test_split_at_end_does_not_count():
    tm = TachyonManifold(lines=[
        ".S.",
        ".^.",
    ])
    assert tm.splits_count() == 0
    assert tm.total_paths() == 1


def test_overlapping_splits():
    tm = TachyonManifold(lines=[
        "..S..",
        "..^..",
        ".^.^.",
        ".....",
    ])
    assert tm.splits_count() == 3
    assert tm.total_paths() == 4


def test_new_split_overlapping_with_falldown_path():
    tm = TachyonManifold(lines=[
        "...S...",
        "...^...",
        "..^....",
        "...^...",
        ".......",
    ])
    assert tm.splits_count() == 3
    assert tm.total_paths() == 4


def test_left_boundary():
    tm = TachyonManifold(lines=[
        ".S...",
        ".^...",
        "^.^..",
        ".....",
    ])
    assert tm.splits_count() == 3
    assert tm.total_paths() == 3


def test_right_boundary():
    tm = TachyonManifold(lines=[
        "..S",
        "^.^",
        "...",
    ])
    assert tm.splits_count() == 1
    assert tm.total_paths() == 1
