# obc

from fibonacci import fibonacci_number, fibonacci_sequence


def test_fibonacci_number_zero() -> None:
    assert fibonacci_number(0) == 0


def test_fibonacci_number_seven() -> None:
    assert fibonacci_number(7) == 13


def test_fibonacci_sequence_first_six() -> None:
    assert fibonacci_sequence(6) == [0, 1, 1, 2, 3, 5]


def test_fibonacci_negative_input_raises_error() -> None:
    import pytest

    with pytest.raises(ValueError):
        fibonacci_number(-1)


def test_fibonacci_sequence_zero_length() -> None:
    assert fibonacci_sequence(0) == []
