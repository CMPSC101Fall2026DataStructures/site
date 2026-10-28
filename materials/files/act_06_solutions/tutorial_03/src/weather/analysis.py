# CS101 Instructor

r"""Calculate statistics about a list of weather readings.

Many docstrings in this module contain an ``Example:`` section with lines that
start with ``>>>``. These are *doctests*: tiny Python sessions that show what a
function returns. When you build the documentation with Sphinx's ``doctest``
builder, every example is actually run and checked, so the documentation can
never quietly fall out of date with the code.
"""

from __future__ import annotations

from weather.readings import Reading


def mean(values: list[float]) -> float:
    r"""Calculate the arithmetic mean (the average) of some numbers.

    The mean of :math:`n` values :math:`x_1, x_2, \ldots, x_n` is

    .. math::

       \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i

    Args:
        values: The numbers to average. The list must not be empty.

    Returns:
        The mean of ``values``.

    Raises:
        ValueError: If ``values`` is empty.

    Example:
        >>> mean([2.0, 4.0, 9.0])
        5.0
    """
    if not values:
        raise ValueError("values cannot be empty")
    return sum(values) / len(values)


def daily_range(reading: Reading) -> float:
    """Find how much the temperature changed during one day.

    Args:
        reading: The day to measure.

    Returns:
        The high temperature minus the low temperature, in degrees Celsius.

    Example:
        >>> daily_range(Reading("Monday", 18.5, 9.0, 0.0))
        9.5
    """
    return reading.high_c - reading.low_c


def hottest_day(readings: list[Reading]) -> Reading:
    """Find the reading with the highest temperature.

    Args:
        readings: The readings to search. The list must not be empty.

    Returns:
        The :class:`~weather.readings.Reading` with the largest ``high_c``.
        If two days tie, the earlier day is returned.

    Example:
        >>> week = [Reading("Mon", 18.5, 9.0, 0.0), Reading("Tue", 24.0, 12.0, 1.0)]
        >>> hottest_day(week).day
        'Tue'
    """
    return max(readings, key=lambda reading: reading.high_c)


def total_rain(readings: list[Reading]) -> float:
    """Add up the rainfall for every reading.

    Args:
        readings: The readings to total.

    Returns:
        The total rainfall in millimetres, rounded to one decimal place.

    Example:
        >>> total_rain([Reading("Mon", 18.5, 9.0, 2.4), Reading("Tue", 24.0, 12.0, 1.1)])
        3.5
    """
    return round(sum(reading.rain_mm for reading in readings), 1)


def moving_average(values: list[float], window: int) -> list[float]:
    """Smooth a list of numbers by averaging each group of neighbors.

    A moving average with a ``window`` of 3 averages items 0-2, then items
    1-3, then items 2-4, and so on, until the window reaches the end of the
    list.

    Args:
        values: The numbers to smooth.
        window: How many neighboring numbers to average together.

    Returns:
        A list with ``len(values) - window + 1`` averages, or an empty list
        if ``window`` is larger than ``len(values)``.

    Raises:
        ValueError: If ``window`` is zero or negative.

    Example:
        >>> moving_average([1.0, 2.0, 3.0, 4.0, 5.0], 3)
        [2.0, 3.0, 4.0]
    """
    if window <= 0:
        raise ValueError("window must be positive")
    averages: list[float] = []
    for start in range(len(values) - window + 1):
        averages.append(mean(values[start : start + window]))
    return averages
