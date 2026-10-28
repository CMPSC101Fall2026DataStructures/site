# obc

from __future__ import annotations


def fibonacci_number(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n

    previous = 0
    current = 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current


def fibonacci_sequence(length: int) -> list[int]:
    """Return a Fibonacci sequence of the requested length."""
    if length < 0:
        raise ValueError("length must be non-negative")
    return [fibonacci_number(index) for index in range(length)]
