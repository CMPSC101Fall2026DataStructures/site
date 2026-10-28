# CS101 Instructor

"""Functions that summarize the scores in a class gradebook.

This module works together with :mod:`student`. Each function receives
:class:`student.Student` objects and returns a summary that a teacher might
want to see.
"""

from __future__ import annotations

from student import Student

#: The lowest score needed to earn each letter grade.
#: Any score below the ``"D"`` cutoff earns an ``"F"``.
GRADE_CUTOFFS = {"A": 90.0, "B": 80.0, "C": 70.0, "D": 60.0}


def letter_grade(score: float) -> str:
    """Convert a numeric score into a letter grade.

    The cutoffs are stored in :data:`GRADE_CUTOFFS`.

    Args:
        score: A score from 0 to 100.

    Returns:
        One of ``"A"``, ``"B"``, ``"C"``, ``"D"``, or ``"F"``.
    """
    for letter, cutoff in GRADE_CUTOFFS.items():
        if score >= cutoff:
            return letter
    return "F"


def class_average(students: list[Student]) -> float:
    """Calculate the average of every student's average score.

    Args:
        students: The students in the class.

    Returns:
        The mean of the students' averages, or ``0.0`` if ``students`` is empty.
    """
    if not students:
        return 0.0
    total = 0.0
    for student in students:
        total += student.average()
    return total / len(students)


def top_student(students: list[Student]) -> Student | None:
    """Find the student with the highest average score.

    Args:
        students: The students to compare.

    Returns:
        The :class:`student.Student` with the highest average, or ``None``
        if ``students`` is empty.
    """
    best: Student | None = None
    for student in students:
        if best is None or student.average() > best.average():
            best = student
    return best


def grade_report(students: list[Student]) -> list[str]:
    """Build one line of text for every student in the class.

    Each line shows the student's name, average, and letter grade, for
    example ``"Ada Lovelace: 94.5 (A)"``.

    Args:
        students: The students to include in the report.

    Returns:
        A list of formatted strings, one per student, in the same order as
        ``students``.
    """
    lines: list[str] = []
    for student in students:
        average = student.average()
        lines.append(f"{student.name}: {average:.1f} ({letter_grade(average)})")
    return lines


if __name__ == "__main__":
    roster = [
        Student("Ada Lovelace", [98, 91, 94.5]),
        Student("Alan Turing", [88, 79, 85]),
        Student("Grace Hopper", [72, 81, 69]),
    ]
    print("Class Gradebook")
    print("---------------")
    for line in grade_report(roster):
        print(line)
    print(f"Class average: {class_average(roster):.1f}")
    print(f"Top student:   {top_student(roster)}")

    try:
        roster[0].add_score(-5)
        print("Uh oh: a negative score was accepted!")
    except ValueError as error:
        print(f"Rejected a bad score: {error}")
