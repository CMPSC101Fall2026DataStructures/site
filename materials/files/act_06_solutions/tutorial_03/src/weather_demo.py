"""Print a weather report for the sample data in ``data/readings.csv``.

Run this program from inside the ``tutorial_03`` folder with::

    uv run src/weather_demo.py
"""

from __future__ import annotations

from pathlib import Path

from weather.readings import load_readings
from weather.report import build_report

DATA_FILE = Path(__file__).parent.parent / "data" / "readings.csv"


def main() -> None:
    """Load the sample readings and print the report."""
    readings = load_readings(DATA_FILE)
    print(build_report(readings))


if __name__ == "__main__":
    main()
