# CS101 Instructor

"""Tools for converting and describing temperatures.

This module is the program that you will document in Tutorial 1. Every
function below has a *docstring*: the triple-quoted text placed directly
under the ``def`` line. Sphinx reads these docstrings and turns them into
web pages for you.

The docstrings in this file use the reStructuredText "field list" style
that Sphinx understands without any extra extensions. Each field begins
with a colon, for example ``:param celsius:`` or ``:returns:``.
"""

from __future__ import annotations

#: The temperature (in degrees Celsius) at which water freezes.
FREEZING_POINT_C = 0.0

#: The temperature (in degrees Celsius) at which water boils at sea level.
BOILING_POINT_C = 100.0


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    The formula is ``fahrenheit = celsius * 9 / 5 + 32``.

    :param celsius: A temperature measured in degrees Celsius.
    :returns: The same temperature measured in degrees Fahrenheit.
    """
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a temperature from Fahrenheit to Celsius.

    The formula is ``celsius = (fahrenheit - 32) * 5 / 9``.

    :param fahrenheit: A temperature measured in degrees Fahrenheit.
    :returns: The same temperature measured in degrees Celsius.
    """
    return (fahrenheit - 32) * 5 / 9


def describe_temperature(celsius: float) -> str:
    """Describe a temperature with a single word.

    :param celsius: A temperature measured in degrees Celsius.
    :returns: One of ``"freezing"``, ``"cold"``, ``"warm"``, or ``"boiling"``.
    """
    if celsius <= FREEZING_POINT_C:
        return "freezing"
    if celsius < 20:
        return "cold"
    if celsius < BOILING_POINT_C:
        return "warm"
    return "boiling"


def conversion_table(start: int, stop: int, step: int = 10) -> list[tuple[int, float]]:
    """Build a table of Celsius values paired with their Fahrenheit values.

    :param start: The first Celsius value in the table.
    :param stop: The table stops before reaching this Celsius value.
    :param step: The distance between Celsius values. Defaults to ``10``.
    :returns: A list of ``(celsius, fahrenheit)`` tuples.
    :raises ValueError: If ``step`` is zero or negative.
    """
    if step <= 0:
        raise ValueError("step must be positive")
    return [(celsius, celsius_to_fahrenheit(celsius)) for celsius in range(start, stop, step)]


if __name__ == "__main__":
    print("Temperature Tools")
    print("-----------------")
    for celsius, fahrenheit in conversion_table(-10, 110, 30):
        print(f"{celsius:>4} C = {fahrenheit:>5.1f} F  ({describe_temperature(celsius)})")
    print(f"  212 F = {fahrenheit_to_celsius(212):>5.1f} C")
