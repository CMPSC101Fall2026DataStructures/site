# Tutorial 3: Automate Testing for a Data Pipeline

## Overview

In this tutorial, you will test a longer Python module that performs numeric analysis and plotting. Several TODO bugs are intentionally included in the code. You will also run an automation script that executes pytest and writes a test report.

## Part 1: Create the Project Environment

Move into the tutorial folder:

```bash
cd Act05_pytest/tutorials/tutorial_03
```

Initialize the project:

```bash
uv init --bare
```

Note: `uv init` creates a bare starter directory with only `pyproject.toml` in it.

These tutorials intentionally avoid `source .venv/bin/activate` because activation commands vary across operating systems and shells. Run commands with `uv run <program>` so setup works the same on macOS, Linux, and Windows.

Install dependencies:

```bash
uv add pytest matplotlib
```

## Part 2: Run Tests and Inspect Failures

Run:

```bash
uv run pytest -q src/test_analysis_pipeline.py
```

You should initially see failures connected to TODO sections in:

- moving-average calculations
- summary statistics
- output file naming

## Part 3: Fix TODOs in `src/analysis_pipeline.py`

Open `src/analysis_pipeline.py` and repair the TODO-marked lines.

The tests isolate each bug so you can fix one area at a time.

## Part 4: Re-run Tests Until Passing

```bash
uv run pytest -q src/test_analysis_pipeline.py
```

Expected when all TODOs are fixed:

```text
.....                                                                    [100%]
5 passed in 0.06s
```

## Part 5: Automate Test Execution

Run the automation script:

```bash
uv run src/run_tests.py
```

This script runs pytest and writes a plain-text report to `src/test_report.txt`.

## Example Automation Output

```text
Running automated tests...
Saved test report: src/test_report.txt
```

## Understanding the Output

- Test failures point to exact assertions and expected values.
- Passing tests verify both numeric logic and generated output files.
- Automation is useful when you repeatedly test after incremental code edits.

## What You Accomplished

You debugged a larger module with focused tests and automated your testing workflow from a Python script.
