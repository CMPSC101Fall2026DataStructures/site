# Tutorial 3: A Complete Documentation Site with Tested Examples

## Overview

In this tutorial you will document a larger program: a Python **package** named `weather` that reads a week of weather measurements and prints a report. The documentation site uses many more of Sphinx's features:

| Feature | Extension | What it gives you |
| --- | --- | --- |
| Tested examples | `sphinx.ext.doctest` | Runs the `>>>` examples in your docstrings and reports any that are wrong. |
| Math formulas | `sphinx.ext.mathjax` | Displays formulas written in LaTeX, such as the formula for the mean. |
| Links to Python's docs | `sphinx.ext.intersphinx` | Turns names like `float` and `list` into links to <https://docs.python.org>. |
| Summary tables | `sphinx.ext.autosummary` | Builds a table of functions and classes with a one-line description of each. |
| Including files | `literalinclude` directive | Copies a source file straight into a page so it is never out of date. |
| Custom colors and logo | Furo theme options | Makes the site look like *your* project. |

You will fix two bugs that the documentation itself finds, document one more function, choose your own colors, and write a page of your own from scratch.

## Part 1: Use the Shared Environment

Move into the Tutorial 3 folder:

```bash
cd Act06_sphinx/tutorials/tutorial_03
```

As before, `uv run` uses the shared environment from Tutorial 1. Nothing new needs to be installed, because every extension in this tutorial comes with Sphinx.

## Part 2: Explore the Program

The code is organized like this:

```text
tutorial_03/
├── data/
│   └── readings.csv        <- one week of weather measurements
├── docs/                   <- the documentation project
│   ├── _static/
│   │   └── weather_logo.png
│   ├── about.rst           <- a page that YOU will write
│   ├── api.rst
│   ├── conf.py
│   ├── guide.rst
│   └── index.rst
└── src/
    ├── weather/            <- a package: a folder of modules with __init__.py
    │   ├── __init__.py
    │   ├── analysis.py
    │   ├── readings.py
    │   └── report.py
    └── weather_demo.py     <- the program that you run
```

A **package** is a folder of related modules plus an `__init__.py` file. You import a module from a package with a dot, for example `from weather.analysis import mean`. Sphinx documents packages the same way: `.. automodule:: weather.analysis`.

Run the program:

```bash
uv run src/weather_demo.py
```

### Example Output (Before the Fixes)

```text
Weather Station Report
======================
Monday     18.5 C /  9.0 C   0.0 mm
Tuesday    21.0 C / 11.5 C   2.4 mm
Wednesday  24.5 C / 13.0 C   0.0 mm
Thursday   19.0 C / 12.5 C  11.8 mm
Friday     16.5 C /  8.0 C   6.2 mm
Saturday   22.0 C / 10.5 C   0.0 mm
Sunday     26.0 C / 14.5 C   0.6 mm

Average high:     21.1 C
Hottest day:      Sunday (26.0 C)
Biggest swing:    Wednesday (11.5 C)
Total rainfall:   21.0 mm
3-day highs:     21.3, 21.5, 20.0, 19.2
```

Seven days with a 3-day window should give five smoothed values, but the last line only shows four. Can you spot why? Do not fix it yet; let the documentation find it for you.

## Part 3: Let the Documentation Test the Code

Open `src/weather/analysis.py`. Many docstrings have an `Example:` section like this:

```python
    Example:
        >>> moving_average([1.0, 2.0, 3.0, 4.0, 5.0], 3)
        [2.0, 3.0, 4.0]
```

A line that starts with `>>>` is code, exactly as you would type it into the interactive Python prompt. The line underneath is the output that Python should print. This format is called a **doctest**. Examples like these are the most helpful part of the documentation for many readers, but an example that is *wrong* is worse than no example at all. Sphinx's `doctest` builder solves that problem by running every example and comparing the real output with the documented output.

Run the `doctest` builder (note the `-b doctest` instead of `-b html`):

```bash
uv run sphinx-build -b doctest docs docs/_build/doctest
```

### Example Output (Before the Fixes)

```text
Document: api
-------------
**********************************************************************
File "../src/weather/analysis.py", line ?, in default
Failed example:
    mean([2.0, 4.0, 9.0])
Expected nothing
Got:
    5.0
**********************************************************************
File "../src/weather/analysis.py", line ?, in default
Failed example:
    moving_average([1.0, 2.0, 3.0, 4.0, 5.0], 3)
Expected:
    [2.0, 3.0, 4.0]
Got:
    [2.0, 3.0]
**********************************************************************
...
Doctest summary
===============
   12 tests
    2 failures in tests
    0 failures in setup code
    0 failures in cleanup code
build finished with problems, ...
```

The `doctest` builder found two problems:

1. The `mean()` example has **no expected output**, so it "expected nothing" but got `5.0`. The *documentation* is incomplete.
2. The `moving_average()` example expected three averages but got two. The *code* has a bug.

Notice how `doctest_global_setup` in `docs/conf.py` imports the functions before the examples run, so each example does not need its own `import` line.

Now complete the TODOs in the code:

1. **`src/weather/analysis.py`**, `mean()`: add the expected output to the doctest.
2. **`src/weather/analysis.py`**, `moving_average()`: fix the loop bounds.
3. **`src/weather/report.py`**, `format_reading()`: write a Google-style docstring. For an extra challenge, include an `Example:` section with a doctest; the `doctest` builder will check it for you.

Remove each `TODO` comment once it is done, and replace `Add Your Name Here` at the top of every file in `src/weather/` with your name.

Run the `doctest` builder again until it reports no failures:

### Example Output (After the Fixes)

```text
Doctest summary
===============
   12 tests
    0 failures in tests
    0 failures in setup code
    0 failures in cleanup code
build succeeded.
```

If you added a doctest to `format_reading()`, you will see `13 tests` instead of `12`. Run `uv run src/weather_demo.py` again; the `3-day highs` line should now show five values.

## Part 4: Customize the Website

Open `docs/conf.py` and read through it. Compare the `extensions` list with the one from Tutorial 2. Each extension has a comment that says what it does.

Look at the HTML options at the bottom of the file:

- `html_static_path = ["_static"]` copies everything in `docs/_static/` into the finished website.
- `html_logo` puts `weather_logo.png` at the top of the sidebar.
- `html_theme_options` changes Furo's colors using **CSS variables**. Furo has separate colors for its light and dark modes.

Complete the TODO in `docs/conf.py` by choosing your own brand colors for both modes. Colors are written as **hex codes**: a `#` followed by six characters, such as `#1e90ff` (bright blue) or `#e4572e` (orange-red). Search the web for "color picker" to find codes for colors that you like. Also replace `Add Your Name Here` in the `author` line with your name.

## Part 5: Complete the API Reference

Open `docs/api.rst`. It begins with two new directives:

- `.. automodule:: weather` shows the docstring from `src/weather/__init__.py`, which describes the whole package.
- `.. autosummary::` builds a table that lists several functions and classes with the first line of each docstring. This is why the **one-line summary** at the top of every docstring matters so much: it is what readers see first.

Complete the TODO at the bottom of `docs/api.rst` by adding an `.. automodule::` directive for `weather.report`.

## Part 6: Read the User Guide

Open `docs/guide.rst` and look for these new tools. Each is explained on the page itself:

- `.. contents::` makes a small table of contents for the current page.
- `.. literalinclude:: ../src/weather_demo.py` copies the whole demo program into the page with line numbers, and highlights lines 18-21.
- `.. doctest::` is a doctest written directly in a page instead of in a docstring. The `doctest` builder tested it in Part 3 (look for `Document: guide` in the output).
- `.. math::` and the `:math:` role display formulas. `\frac{1}{k} \sum_{i=j}^{j+k-1} x_i` is written in **LaTeX**, the language that scientists use to typeset math.
- `` :class:`float` `` links to the official Python documentation. That link was made by the `intersphinx` extension, which downloads a list of everything that is documented at <https://docs.python.org>.
- `` :func:`~weather.analysis.mean` `` uses a `~` so that only `mean()` appears on the page.

## Part 7: Write Your Own Page

Open `docs/about.rst`. This page is yours! The TODO comment lists everything the page must contain:

1. a page title,
2. a short paragraph introducing yourself as the author,
3. a bulleted list of at least three things you learned about Sphinx,
4. a `.. note::` admonition, and
5. a `.. code-block:: bash` that shows the command you use to build the website.

Here is a reminder of the reST that you need. Pay close attention to blank lines and the three-space indents:

```rst
My Page Title
=============

A paragraph is just lines of text. Leave a blank line between paragraphs.

* The first item in a bulleted list
* The second item

.. note::

   This sentence is inside the note box because it is indented.
```

The page is already listed in the toctree in `docs/index.rst`, so it appears in the sidebar automatically. Delete all of the TODO comments when you are finished.

## Part 8: Build and Explore

Build the website:

```bash
uv run sphinx-build -b html docs docs/_build/html
```

### Example Output

```text
Running Sphinx v9.2.0
...
loading intersphinx inventory 'python' from https://docs.python.org/3/objects.inv ...
...
writing output... [ 25%] about
writing output... [ 50%] api
writing output... [ 75%] guide
writing output... [100%] index
generating indices... genindex py-modindex done
highlighting module code... [ 33%] weather.analysis
highlighting module code... [ 67%] weather.readings
highlighting module code... [100%] weather.report
...
build succeeded.

The HTML pages are in docs/_build/html.
```

Open `docs/_build/html/index.html` and explore:

- Your logo and your brand colors in both light and dark modes.
- The summary table at the top of the **API Reference**; every name in it should be a link.
- The math formula in the docstring of `mean()`.
- The `Example` sections with their `>>>` doctests.
- Any `float` link, which takes you to the official Python documentation.
- Your own **About** page.

Run both builders one final time to make sure everything is complete. These are the same commands that GitHub Actions runs when you push your work:

```bash
uv run sphinx-build -b html docs docs/_build/html
uv run sphinx-build -b doctest docs docs/_build/doctest
```

## Understanding the Output

- `loading intersphinx inventory 'python'` means Sphinx downloaded the list of objects in Python's own documentation. You need an internet connection for this step. Without one, the build still succeeds, but you will see a warning and the links to Python's documentation will be missing.
- The `doctest` builder writes its full results to `docs/_build/doctest/output.txt`.
- A failing doctest makes the build "finish with problems" and return an error code. That is how GitHub Actions knows that your examples are wrong.
- If the summary table shows a name without a link, the matching `.. automodule::` directive is probably missing.

## What You Accomplished

You documented a multi-module package, used the documentation to test the code, fixed bugs that the doctests uncovered, displayed math formulas, linked to Python's documentation, customized your site's look, and wrote a reStructuredText page from scratch. These are the same tools that professional Python projects use for their documentation.

When you are finished, complete the [reflection](../../writing/reflection.md).
