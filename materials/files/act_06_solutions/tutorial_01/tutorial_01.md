# Tutorial 1: Your First Documentation Website

## Overview

In this tutorial you will create your very first documentation website with **Sphinx**. A small temperature-conversion program is provided in `src/temperature.py`. You will finish two small TODOs in the code, ask Sphinx to create a starter documentation project, connect that project to your code, and build a real HTML website that you can open in your web browser.

## What Is Sphinx?

When you write a function, you usually add a **docstring**: the triple-quoted text directly under the `def` line that explains what the function does. Docstrings are useful when you read the code, but most people who *use* your code will never open the source file. They want a website with a search box, links, and nicely formatted descriptions.

[Sphinx](https://www.sphinx-doc.org/) is a program that builds that website for you. It reads your docstrings, combines them with pages that you write by hand, and produces a set of HTML files. The official Python documentation at <https://docs.python.org> is built with Sphinx, and so are the documentation sites of many popular libraries, such as NumPy and Flask.

```text
  src/temperature.py           docs/conf.py + docs/index.rst
  (code + docstrings)          (settings + hand-written pages)
            \                         /
             \                       /
              +---> sphinx-build <--+
                         |
                         v
            docs/_build/html/index.html   <-- open this in a browser!
```

### Key Vocabulary

| Term | Meaning |
| --- | --- |
| **docstring** | The triple-quoted string at the top of a module, class, or function. |
| **reStructuredText** (reST) | The plain-text markup language that Sphinx reads. Files end in `.rst`. It is similar to Markdown. |
| **source directory** | The folder that holds your documentation files (`docs/` in this tutorial). |
| **`conf.py`** | A Python file with the settings for your documentation project. Sphinx runs it before every build. |
| **`index.rst`** | The home page of your documentation website. |
| **extension** | A plug-in that gives Sphinx a new feature. |
| **autodoc** | The extension that imports your Python code and copies its docstrings into your pages. |
| **directive** | A reST command that starts with `..` and ends with `::`, such as `.. automodule::`. |
| **builder** | The type of output that Sphinx makes. In this activity you will mostly use the `html` builder. |
| **build directory** | The folder where Sphinx writes the finished website (`docs/_build/html/`). |

## Part 1: Create the Shared Project Environment

Unlike Activity 05, this activity uses **one** virtual environment for all three tutorials. You create it **once**, at the top of the activity folder, and every tutorial uses it.

Move into the top folder of the activity (the folder that contains this activity's `README.md`):

```bash
cd Act06_sphinx
```

Initialize the project:

```bash
uv init --bare
```

Note: `uv init --bare` creates a bare starter project with only a `pyproject.toml` file in it.

Install Sphinx and the Furo theme (you will use Furo in Tutorials 2 and 3):

```bash
uv add sphinx furo
```

Note: this command creates a `.venv/` folder (the virtual environment), and it records the libraries that you installed in `pyproject.toml` and `uv.lock`. Commit both of those files, because GitHub Actions uses them to rebuild your documentation.

These tutorials intentionally avoid `source .venv/bin/activate` because activation commands vary across operating systems and shells. Run commands with `uv run <program>` so setup works the same on macOS, Linux, and Windows.

Check that Sphinx is installed:

```bash
uv run sphinx-build --version
```

### Example Output

```text
sphinx-build 9.2.0
```

Your version number may be a little different. That is fine.

> **Important:** Do **not** run `uv init` inside the tutorial folders. When you run `uv run` from inside `tutorials/tutorial_01`, `uv` searches upward through the parent folders, finds the `pyproject.toml` file in `Act06_sphinx`, and uses that one shared environment. This is how a single environment serves all three tutorials.

## Part 2: Review and Complete the Code

Move into the Tutorial 1 folder:

```bash
cd tutorials/tutorial_01
```

Open `src/temperature.py`. Read the docstrings at the top of the file and above each function. These docstrings use the reStructuredText **field list** style that Sphinx understands without any extra extensions:

```python
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    The formula is ``fahrenheit = celsius * 9 / 5 + 32``.

    :param celsius: A temperature measured in degrees Celsius.
    :returns: The same temperature measured in degrees Fahrenheit.
    """
```

- The first line is a **one-line summary** that ends with a period.
- A blank line separates the summary from the details.
- `:param celsius:` describes the parameter named `celsius`.
- `:returns:` describes the value that the function gives back.
- Text wrapped in double backticks, like ``` ``celsius`` ```, is shown in a code font.

Notice also the lines that start with `#:` above `FREEZING_POINT_C` and `BOILING_POINT_C`. Those special comments are how you document a *variable* so that Sphinx includes it on the website.

Now complete the two TODOs in `src/temperature.py`:

1. **`fahrenheit_to_celsius()`** returns `0.0` no matter what. Replace that line with the formula from its docstring.
2. **`describe_temperature()`** has no docstring. Write one by following the shape of the other docstrings in the file.

Remove each `TODO` comment once it is done, and replace `Add Your Name Here` at the top of the file with your name.

Run the program to check your work:

```bash
uv run src/temperature.py
```

### Example Output

```text
Temperature Tools
-----------------
 -10 C =  14.0 F  (freezing)
  20 C =  68.0 F  (warm)
  50 C = 122.0 F  (warm)
  80 C = 176.0 F  (warm)
  212 F = 100.0 C
```

If the last line still says `0.0 C`, look at `fahrenheit_to_celsius()` again.

## Part 3: Create the Documentation Project with `sphinx-quickstart`

Sphinx includes a helper program, `sphinx-quickstart`, that creates a starter documentation project for you. From inside the `tutorial_01` folder, run (as a single line):

```bash
uv run sphinx-quickstart docs --quiet --project "Temperature Tools" --author "Add Your Name Here" --release 0.1 --language en --ext-autodoc --ext-viewcode --no-makefile --no-batchfile
```

Here is what each part of the command means:

| Part of the command | What it does |
| --- | --- |
| `docs` | Create the documentation project in a new folder named `docs/`. |
| `--quiet` | Do not ask questions; use the answers given on the command line instead. |
| `--project "Temperature Tools"` | The name shown at the top of every page. |
| `--author "Add Your Name Here"` | The author of the documentation. Put your own name here (or fix it in `conf.py` later). |
| `--release 0.1` | The version number of the project. |
| `--language en` | The documentation is written in English. |
| `--ext-autodoc` | Turn on **autodoc**, which reads docstrings from your code. |
| `--ext-viewcode` | Turn on **viewcode**, which adds `[source]` links to your code. |
| `--no-makefile --no-batchfile` | Skip the helper scripts; we will run `sphinx-build` directly with `uv`. |

Note: if you run `uv run sphinx-quickstart docs` *without* `--quiet`, Sphinx asks you each of these questions one at a time instead.

You now have this new structure:

```text
tutorial_01/
├── docs/
│   ├── _build/       <- the finished website will be written here
│   ├── _static/      <- images and CSS files for the website
│   ├── _templates/   <- custom page layouts (not used in this activity)
│   ├── conf.py       <- the settings for your documentation
│   └── index.rst     <- the home page of your documentation
├── src/
│   └── temperature.py
└── tutorial_01.md
```

## Part 4: Tell Sphinx Where Your Code Lives

Open `docs/conf.py`. It is an ordinary Python file. Find the `extensions` list and notice that `sphinx.ext.autodoc` and `sphinx.ext.viewcode` are already turned on, thanks to the options you gave `sphinx-quickstart`.

The autodoc extension *imports* your code to read its docstrings, just like an `import` statement in Python. But Python does not know to look inside the `src/` folder, so you must add that folder to Python's search path. Add these lines near the **top** of `docs/conf.py`, just above the `# -- Project information` comment:

```python
import os
import sys

sys.path.insert(0, os.path.abspath("../src"))
```

- `sys.path` is the list of folders where Python looks for modules to import.
- `os.path.abspath("../src")` turns the path *from `docs/` up one level and into `src/`* into a full path.
- `sys.path.insert(0, ...)` puts that folder at the front of the list.

If you did not put your name in the `sphinx-quickstart` command, replace `Add Your Name Here` in the `copyright` and `author` lines of `conf.py` with your name now.

## Part 5: Write the Home Page

Open `docs/index.rst`. Replace **everything** in it with the following, and then replace `Add Your Name Here` with your name:

```rst
Temperature Tools
=================

Welcome to the documentation for **Temperature Tools**, a small Python
module that converts temperatures between Celsius and Fahrenheit.

This website was built with Sphinx by Add Your Name Here.

Quick example
-------------

.. code-block:: python

   from temperature import celsius_to_fahrenheit

   print(celsius_to_fahrenheit(100))   # prints 212.0

.. note::

   Every description below was copied automatically from the docstrings in
   ``src/temperature.py``. Change a docstring, rebuild, and this page changes too!

.. toctree::
   :maxdepth: 2
   :caption: Contents:

API Reference
-------------

.. automodule:: temperature
   :members:
```

Let's understand the reStructuredText that you just wrote:

- **Headings** are made by underlining text. `=====` makes a page title and `-----` makes a section. The underline must be at least as long as the text.
- `**Temperature Tools**` makes **bold** text, just like Markdown.
- `.. code-block:: python` is a **directive** that shows highlighted Python code. The code must be indented (three spaces) and there must be a blank line after the directive.
- `.. note::` is a directive that draws a colored "Note" box. Boxes like this are called **admonitions**.
- `.. toctree::` builds a table of contents. You will add more pages to it in Tutorial 2.
- `.. automodule:: temperature` is the magic line. It tells autodoc to import the `temperature` module and insert its docstring here. The `:members:` **option** says "also include every documented function and variable in the module."

## Part 6: Build the Website

Build the documentation with the `html` builder:

```bash
uv run sphinx-build -b html docs docs/_build/html
```

The command reads: "Using the **b**uilder named `html`, take the source files in `docs` and write the website to `docs/_build/html`."

### Example Output

```text
Running Sphinx v9.2.0
loading translations [en]... done
making output directory... done
...
reading sources... [100%] index
...
writing output... [100%] index
generating indices... genindex py-modindex done
highlighting module code... [100%] temperature
writing additional pages... search done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded.

The HTML pages are in docs/_build/html.
```

## Part 7: Open the Website

Open `docs/_build/html/index.html` in your web browser. Use the command for your operating system:

```bash
open docs/_build/html/index.html        # macOS
xdg-open docs/_build/html/index.html    # Linux
start docs/_build/html/index.html       # Windows (PowerShell)
```

Alternatively, you can serve the website from a tiny web server (this works on every operating system) and then visit <http://localhost:8000> in your browser. Press `Ctrl+C` in the terminal to stop the server:

```bash
uv run python -m http.server --directory docs/_build/html 8000
```

Explore your new website:

- Find all four functions and both constants in the **API Reference** section.
- Click a `[source]` link to see the highlighted code (this is the viewcode extension at work).
- Type `boiling` into the search box.
- Click **Index** to see an alphabetical index that Sphinx built for you.

## Understanding the Output

- `reading sources` means Sphinx is reading your `.rst` files.
- `writing output` means Sphinx is creating the HTML files.
- `highlighting module code... temperature` means viewcode is making the `[source]` pages for `src/temperature.py`.
- `build succeeded.` means everything worked. If you see `build succeeded, 1 warning.` instead, read the `WARNING:` line above it; it tells you the file and line number of the problem.
- A common warning is `failed to import 'temperature'`. That means the `sys.path.insert` lines in Part 4 are missing or are not correct.
- The `docs/_build/` folder is listed in `.gitignore`, so the generated website is **not** committed to GitHub. Only the *source* files (`conf.py`, `index.rst`, and your code) are committed, and anyone can rebuild the website from them.

## Try It: Change a Docstring

Open `src/temperature.py` and add a sentence to the docstring of `celsius_to_fahrenheit()`. Rebuild the website, then refresh the page in your browser. Your new sentence appears on the website, even though you never touched `index.rst`. Documentation that lives *inside* the code is much easier to keep up to date.

## What You Accomplished

You created a shared `uv` environment, completed and documented a Python module, generated a Sphinx project with `sphinx-quickstart`, connected it to your code with autodoc, and built your first documentation website.

Next tutorial: [tutorial_02.md](../tutorial_02/tutorial_02.md)
