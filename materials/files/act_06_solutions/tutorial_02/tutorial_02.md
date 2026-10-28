# Tutorial 2: Google-Style Docstrings, Extensions, and Themes

## Overview

In Tutorial 1, `sphinx-quickstart` made the documentation project for you. In this tutorial the `docs/` folder is **already provided**, and it has several pages instead of one. You will:

- document a program that has two modules and a **class**,
- learn the popular **Google-style** docstring format,
- turn on the **napoleon** extension so that Sphinx understands that format,
- switch the website to the modern **Furo** theme, and
- link pages together with a table of contents and **cross-references**.

## Part 1: Use the Shared Environment

You already created the shared environment in Tutorial 1, so there is nothing to install. Move into the Tutorial 2 folder:

```bash
cd Act06_sphinx/tutorials/tutorial_02
```

Note: `uv run` finds the `pyproject.toml` file in `Act06_sphinx` automatically. Do **not** run `uv init` here.

## Part 2: Meet Google-Style Docstrings

Open `src/student.py` and `src/gradebook.py`. Their docstrings look a little different from the ones in Tutorial 1:

```python
def letter_grade(score: float) -> str:
    """Convert a numeric score into a letter grade.

    The cutoffs are stored in :data:`GRADE_CUTOFFS`.

    Args:
        score: A score from 0 to 100.

    Returns:
        One of ``"A"``, ``"B"``, ``"C"``, ``"D"``, or ``"F"``.
    """
```

This is the **Google style**. Instead of `:param score:`, it uses section headings such as `Args:`, `Returns:`, and `Raises:`, with the details indented underneath. Many programmers find this style easier to read in the source code.

Here is the same information in both styles:

| Tutorial 1 (reST field list) | Tutorial 2 (Google style) |
| --- | --- |
| `:param score: A score from 0 to 100.` | `Args:` then, indented, `score: A score from 0 to 100.` |
| `:returns: The letter grade.` | `Returns:` then, indented, `The letter grade.` |
| `:raises ValueError: If ...` | `Raises:` then, indented, `ValueError: If ...` |

There is a catch: Sphinx does **not** understand Google-style docstrings by itself. You will see this for yourself in the next part.

Also notice the `class Student:` docstring in `src/student.py`. A class docstring describes the arguments given to the constructor (`Args:`) and the data that every object stores (`Attributes:`).

## Part 3: Build *Before* Making Changes

Build the provided documentation exactly as it is:

```bash
uv run sphinx-build -b html docs docs/_build/html
```

Open `docs/_build/html/api.html` in your browser (see Tutorial 1, Part 7 for the commands). Look at the `add_score()` method. You will see something like this:

```text
add_score(score)
    Record one new assignment score.
    Args:
        score: The score to record. It must be between MIN_SCORE and MAX_SCORE (inclusive).
    Raises:ValueError: If score is below MIN_SCORE or above MAX_SCORE.
    Parameters:
        score (float)
    Return type:
        None
```

Sphinx does not know that `Args:` and `Raises:` are special, so it shows them as ordinary text, exactly as they were typed, and the `Raises:` line runs together. The `Parameters:` list at the bottom comes only from the type hint (`score: float`), so it has no description. The information is all there, but it is split up and hard to read. Keep this page open so you can compare it with the result after Part 5. You may also notice that the `gradebook` section of the page is empty; you will fix that in Part 6.

## Part 4: Complete the TODOs in the Code

First, run the program:

```bash
uv run src/gradebook.py
```

### Example Output (Before the Fix)

```text
Class Gradebook
---------------
Ada Lovelace: 94.5 (A)
Alan Turing: 84.0 (B)
Grace Hopper: 74.0 (C)
Class average: 84.2
Top student:   Ada Lovelace (3 scores)
Uh oh: a negative score was accepted!
```

The last line shows a bug: the docstring of `add_score()` *promises* to raise a `ValueError` for scores below 0, but the code does not do it. Documentation is a promise to the people who use your code, so the code must keep that promise!

Complete these TODOs:

1. **`src/student.py`**: fix the condition in `add_score()` so that scores below `MIN_SCORE` are also rejected.
2. **`src/gradebook.py`**: write a Google-style docstring for `class_average()`, following the hint in the TODO comment.

Remove each `TODO` comment once it is done, and replace `Add Your Name Here` at the top of both files with your name. Run the program again. The last line should now be:

```text
Rejected a bad score: score must be between 0.0 and 100.0
```

## Part 5: Turn On Napoleon and Change the Theme

Open `docs/conf.py` and complete its two TODOs.

1. **Add the napoleon extension.** Add the string `"sphinx.ext.napoleon"` to the `extensions` list. Napoleon translates Google-style (and NumPy-style) docstrings into the reST that Sphinx understands, *before* autodoc puts them on the page.
2. **Change the theme.** A **theme** controls the colors, fonts, and layout of every page. Change `html_theme` from `"alabaster"` (the plain default theme) to `"furo"`.

Also replace `Add Your Name Here` in the `author` line with your name.

While you are in `conf.py`, read the other settings that are provided for you:

| Setting | What it does |
| --- | --- |
| `sys.path.insert(0, os.path.abspath("../src"))` | Lets autodoc import the modules in `src/` (you added this by hand in Tutorial 1). |
| `autodoc_member_order = "bysource"` | Lists functions in the same order as the source file, instead of alphabetically. |
| `autodoc_typehints = "description"` | Moves type hints such as `float` out of the function signature and into the parameter descriptions. |
| `html_title` | The title shown in the browser tab and at the top of the sidebar. |

## Part 6: Finish the Hand-Written Pages

This documentation project has three `.rst` pages:

| File | Becomes | Purpose |
| --- | --- | --- |
| `docs/index.rst` | `index.html` | The home page with the table of contents. |
| `docs/usage.rst` | `usage.html` | A guide written by hand. |
| `docs/api.rst` | `api.html` | The reference generated from docstrings. |

Open `docs/index.rst` and find the `toctree` directive:

```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents

   usage
   api
```

The **toctree** ("table of contents tree") lists the other pages by file name, without the `.rst` ending. Sphinx uses it to build the sidebar menu and the "Next" and "Previous" links. Every page should be listed in some toctree; if it is not, Sphinx warns you with `document isn't included in any toctree`.

Now complete the TODOs in the two other pages. In reStructuredText, a line that starts with `.. ` followed by ordinary text (not a directive name and `::`) is a **comment**, so the TODOs do not appear on the website.

1. **`docs/api.rst`**: add an `.. automodule::` directive for the `gradebook` module.
2. **`docs/usage.rst`**: write a `.. tip::` admonition with one piece of advice for a classmate who is learning Sphinx.

Delete each TODO comment when you are done with it.

While you have `docs/usage.rst` open, look for text like this:

```rst
Every student is stored in a :class:`student.Student` object.
```

`` :class:`student.Student` `` is a **cross-reference** (also called a *role*). On the website it becomes a link to the documentation of the `Student` class. Other roles include `:func:` for functions, `:meth:` for methods, `:mod:` for modules, `:data:` for variables, and `:doc:` for whole pages. If you misspell a name, Sphinx cannot make the link, so cross-references also help you catch mistakes.

## Part 7: Rebuild and Compare

```bash
uv run sphinx-build -b html docs docs/_build/html
```

### Example Output

```text
Running Sphinx v9.2.0
loading translations [en]... done
loading pickled environment... done
...
reading sources... [100%] usage
...
writing output... [100%] usage
generating indices... genindex py-modindex done
highlighting module code... [ 50%] gradebook
highlighting module code... [100%] student
writing additional pages... search done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded.

The HTML pages are in docs/_build/html.
```

Refresh `api.html` in your browser. You should now see:

- the new **Furo** theme, with a sidebar, a search box, and a light/dark mode button at the top of the page,
- `Parameters`, `Returns`, and `Raises` shown as neat, bold lists instead of squashed sentences,
- type hints such as `float` and `list[Student]` beside each parameter, and
- the `gradebook` module documented beneath the `student` module.

Click the light/dark mode button. Then visit the **Usage Guide** page and click each cross-reference link.

## Understanding the Output

- `loading pickled environment... done` means Sphinx remembered your previous build and only re-read the files that changed. This makes rebuilding fast.
- If you see `WARNING: Unknown directive type`, a directive name is misspelled, or the `::` is missing.
- If you see `WARNING: Explicit markup ends without a blank line`, add a blank line after the indented content of a directive.
- If your theme does not change, check the spelling of `"furo"` in `conf.py`.

## What You Accomplished

You documented a class and a second module with Google-style docstrings, enabled the napoleon extension, gave your site a modern theme, organized several pages with a toctree, and linked them together with cross-references.

Next tutorial: [tutorial_03.md](../tutorial_03/tutorial_03.md)
