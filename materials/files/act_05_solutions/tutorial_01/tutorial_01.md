# Tutorial 1: First Tests with Fibonacci

## Overview

In this tutorial you will write and run your first `pytest` tests. A Fibonacci implementation is provided in `src/fibonacci.py`. You will copy test code from this tutorial into `src/test_fibonacci.py`, run the tests, and compare your output with the expected result.

## Part 1: Create the Project Environment

Move into the tutorial folder:

```bash
cd Act05_pytest/tutorials/tutorial_01
```

Initialize the project:

```bash
uv init --bare
```

Note: `uv init` creates a bare starter directory with only `pyproject.toml` in it.

These tutorials intentionally avoid setting up a virtual environment with `source .venv/bin/activate` since activation commands vary across operating systems and shells. Run commands with `uv run <program>` so setup works the same on macOS, Linux, and Windows.

Install dependencies:

```bash
uv add pytest
```

## Part 2: Review the Program Under Test

Open `src/fibonacci.py`. This file already contains two functions:

- `fibonacci_number(n)`: returns the nth Fibonacci number
- `fibonacci_sequence(length)`: returns a list of Fibonacci values

You will test both functions from `src/test_fibonacci.py`.

## Part 3: Copy and Paste the Test Code

Open `src/test_fibonacci.py` and replace the placeholder test with the following:

```python
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
```

Note: The `Assert` statement is used to verify test conditions.

## Part 4: Run the Tests

Run:

```bash
uv run pytest -q src/test_fibonacci.py
```

## Example Output

```text
.....                                                                 [100%]
5 passed in 0.02s
```

If your output reports `5 passed`, your setup is working.

## Understanding the Output

- Each `.` means one test passed.
- `100%` indicates all collected tests ran.
- The final line reports total passing tests and elapsed time.

## What You Accomplished

You created and executed a complete, passing test file with `pytest` and verified behavior for return values and exception handling.

Next tutorial: [tutorial_02.md](../tutorial_02/tutorial_02.md)
