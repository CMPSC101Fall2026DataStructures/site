# CS101 Instructor

"""A class that stores one student's name and assignment scores.

The docstrings in this module use the **Google style**. Instead of
``:param name:`` fields, Google-style docstrings use plain section headings
such as ``Args:``, ``Returns:``, and ``Raises:``. They are easy for people to
read in the source code, and the ``sphinx.ext.napoleon`` extension teaches
Sphinx how to turn them into nicely formatted web pages.
"""

from __future__ import annotations

#: The lowest score that a student can earn on an assignment.
MIN_SCORE = 0.0

#: The highest score that a student can earn on an assignment.
MAX_SCORE = 100.0


class Student:
    """A student and the scores they earned on assignments.

    Args:
        name: The student's full name.
        scores: Starting scores for the student. Defaults to an empty list.

    Attributes:
        name: The student's full name.
        scores: Every score that has been recorded for the student.
    """

    def __init__(self, name: str, scores: list[float] | None = None) -> None:
        self.name = name
        self.scores: list[float] = []
        for score in scores or []:
            self.add_score(score)

    def add_score(self, score: float) -> None:
        """Record one new assignment score.

        Args:
            score: The score to record. It must be between ``MIN_SCORE`` and
                ``MAX_SCORE`` (inclusive).

        Raises:
            ValueError: If ``score`` is below ``MIN_SCORE`` or above ``MAX_SCORE``.
        """
        if score < MIN_SCORE or score > MAX_SCORE:
            raise ValueError(f"score must be between {MIN_SCORE} and {MAX_SCORE}")
        self.scores.append(score)

    def average(self) -> float:
        """Calculate the student's average score.

        Returns:
            The mean of all recorded scores, or ``0.0`` if there are no scores yet.
        """
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

    def __str__(self) -> str:
        """Return a short, readable description such as ``Ada (3 scores)``."""
        return f"{self.name} ({len(self.scores)} scores)"
