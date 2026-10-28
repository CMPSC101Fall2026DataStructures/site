from sequence_tools import even_numbers, running_total, unique_in_order


def test_even_numbers_filters_correct_values() -> None:
    assert even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_running_total_builds_cumulative_sums() -> None:
    assert running_total([1, 2, 3]) == [1, 3, 6]


def test_unique_in_order_preserves_first_appearance() -> None:
    assert unique_in_order(["a", "b", "a", "c", "b", "d"]) == ["a", "b", "c", "d"]


def test_even_numbers_empty_input() -> None:
    assert even_numbers([]) == []
