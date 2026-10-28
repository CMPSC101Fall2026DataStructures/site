# CS101 Instructor

"""Load daily weather readings from a CSV file.

A CSV ("comma-separated values") file stores a table as plain text. The first
line holds the column names and every other line holds one row::

    day,high_c,low_c,rain_mm
    Monday,18.5,9.0,0.0
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Reading:
    """The weather measured at the station on a single day.

    Attributes:
        day: The name of the day, such as ``"Monday"``.
        high_c: The highest temperature of the day, in degrees Celsius.
        low_c: The lowest temperature of the day, in degrees Celsius.
        rain_mm: The total rainfall for the day, in millimetres.

    Example:
        >>> monday = Reading("Monday", 18.5, 9.0, 0.0)
        >>> monday.high_c
        18.5
    """

    day: str
    high_c: float
    low_c: float
    rain_mm: float


def parse_row(row: dict[str, str]) -> Reading:
    """Convert one row of the CSV file into a :class:`Reading`.

    Args:
        row: A dictionary that maps each column name to the text in that
            column, exactly as :class:`csv.DictReader` produces it.

    Returns:
        A new :class:`Reading` with its numbers converted to :class:`float`.

    Example:
        >>> parse_row({"day": "Friday", "high_c": "16.5", "low_c": "8", "rain_mm": "6.2"})
        Reading(day='Friday', high_c=16.5, low_c=8.0, rain_mm=6.2)
    """
    return Reading(
        day=row["day"],
        high_c=float(row["high_c"]),
        low_c=float(row["low_c"]),
        rain_mm=float(row["rain_mm"]),
    )


def load_readings(csv_path: Path) -> list[Reading]:
    """Read every row of a CSV file into a list of readings.

    Args:
        csv_path: The location of the CSV file to read.

    Returns:
        One :class:`Reading` per row, in the same order as the file.

    Raises:
        FileNotFoundError: If ``csv_path`` does not exist.
    """
    with csv_path.open(encoding="utf-8", newline="") as csv_file:
        return [parse_row(row) for row in csv.DictReader(csv_file)]
