# CS101 Instructor

"""Turn weather statistics into a report that people can read."""

from __future__ import annotations

from weather.analysis import daily_range, hottest_day, mean, moving_average, total_rain
from weather.readings import Reading

#: The number of days averaged together by the moving average in the report.
SMOOTHING_WINDOW = 3


def format_reading(reading: Reading) -> str:
    """Format one reading as a single line of the report.

    Args:
        reading: The day to format.

    Returns:
        The day, high temperature, low temperature, and rainfall lined up in
        columns so that several lines form a neat table.

    Example:
        >>> format_reading(Reading("Monday", 18.5, 9.0, 0.0))
        'Monday     18.5 C /  9.0 C   0.0 mm'
    """
    return (
        f"{reading.day:<10} {reading.high_c:>4.1f} C / {reading.low_c:>4.1f} C"
        f" {reading.rain_mm:>5.1f} mm"
    )


def build_report(readings: list[Reading]) -> str:
    """Build a multi-line weather report for a list of readings.

    The report contains one line per day followed by a summary that uses
    :func:`~weather.analysis.mean`, :func:`~weather.analysis.hottest_day`,
    :func:`~weather.analysis.total_rain`, and
    :func:`~weather.analysis.moving_average`.

    Args:
        readings: The readings to report on. The list must not be empty.

    Returns:
        The complete report as a single string with newline characters
        between lines.
    """
    highs = [reading.high_c for reading in readings]
    smoothed = ", ".join(f"{value:.1f}" for value in moving_average(highs, SMOOTHING_WINDOW))
    hottest = hottest_day(readings)
    widest = max(readings, key=daily_range)

    lines = ["Weather Station Report", "======================"]
    lines.extend(format_reading(reading) for reading in readings)
    lines.append("")
    lines.append(f"Average high:     {mean(highs):.1f} C")
    lines.append(f"Hottest day:      {hottest.day} ({hottest.high_c:.1f} C)")
    lines.append(f"Biggest swing:    {widest.day} ({daily_range(widest):.1f} C)")
    lines.append(f"Total rainfall:   {total_rain(readings):.1f} mm")
    lines.append(f"{SMOOTHING_WINDOW}-day highs:     {smoothed}")
    return "\n".join(lines)
