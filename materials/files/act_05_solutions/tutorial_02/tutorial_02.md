# Tutorial 2: Find and Fix TODO Bugs with pytest

## Overview

In this tutorial, tests are already provided. The implementation file contains simple TODO-marked bugs involving loops and lists. Your task is to run tests, read failures, and fix the code.

## Part 1: Create the Project Environment

Move into the tutorial folder:

```bash
cd Act05_pytest/tutorials/tutorial_02
```

Initialize the project:

```bash
uv init --bare
```

Note: `uv init` creates a bare starter directory with only `pyproject.toml` in it.

These tutorials intentionally avoid `source .venv/bin/activate` because activation commands vary across operating systems and shells. Run commands with `uv run <program>` so setup works the same on macOS, Linux, and Windows.

Install dependencies:

```bash
uv add pytest
```

## Part 2: Run the Tests First

Run:

```bash
uv run pytest -q src/test_sequence_tools.py
```

You should see multiple failing tests before fixing TODOs.

## Example Failing Output

```text
FF.F                                                                    [100%]
=================================== FAILURES ===================================
...
E       assert [1, 3, 5] == [2, 4, 6]
...
E       assert [1, 2, 3] == [1, 3, 6]
...
3 failed, 1 passed in 0.03s
```

## Part 3: Fix TODOs in `src/sequence_tools.py`

Open `src/sequence_tools.py` and repair each TODO section.

TODO focus areas:

- Correct the even-number filtering condition
- Update cumulative total logic inside a loop
- Preserve first-seen order while removing duplicates

## Part 4: Re-run Tests

After fixing TODOs, run:

```bash
uv run pytest -q src/test_sequence_tools.py
```

## Example Passing Output

```text
....                                                                     [100%]
4 passed in 0.02s
```

## Understanding the Output

- The failure message shows expected vs actual values.
- The test name tells you which function to inspect.
- Re-running after each fix confirms progress quickly.

## What You Accomplished

You used test failures to locate logic errors and repaired loop/list behavior with confidence.

Next tutorial: [tutorial_03.md](../tutorial_03/tutorial_03.md)
