# obc

from __future__ import annotations


def even_numbers(values: list[int]) -> list[int]:
    """Return only even numbers from the input list."""
    result: list[int] = []
    for value in values:
        # DONE: Fix this condition so only even values are appended.
        if value % 2 == 0:
            result.append(value)
    return result


def running_total(values: list[int]) -> list[int]:
    """Return cumulative totals for the input list."""
    totals: list[int] = []
    total = 0
    for value in values:
        # DONE: Fix this update so total accumulates previous values.
        total += value
        totals.append(total)
    return totals


def unique_in_order(values: list[str]) -> list[str]:
    """Return unique strings while preserving original order."""
    # DONE: Fix this implementation so order is preserved.
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result
