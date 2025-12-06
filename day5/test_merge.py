from day5.solution import merge


def test_merge_empty_list_of_ranges():
    assert merge([]) == []


def test_merge_one_range_should_return_the_same_range():
    assert merge([(1, 5)]) == [(1, 5)]


def test_merge_two_not_overlapping_ranges():
    assert merge([(1, 2), (5, 6)]) == [(1, 2), (5, 6)]


def test_merge_two_not_overlapping_unordered_ranges():
    assert merge([(5, 6), (1, 2)]) == [(1, 2), (5, 6)]


def test_merge_two_end_overlapping_ranges():
    assert merge([(1, 5), (3, 10)]) == [(1, 10)]


def test_merge_two_overlapping_ranges_when_one_is_fully_contained():
    assert merge([(1, 10), (3, 5)]) == [(1, 10)]


def test_two_ranges_touching_at_edges():
    assert merge([(1, 5), (6, 10)]) == [(1, 10)]


def test_merge_multiple_ordered_ranges():
    assert merge([(1, 3), (2, 4), (5, 7), (6, 8)]) == [(1, 8)]


def test_merge_multiple_not_ordered_overlapping_ranges():
    assert merge([(6, 8), (1, 3), (5, 7), (20, 24), (2, 4)]) == [(1, 8), (20, 24)]
