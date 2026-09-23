# Tutorial 2: The Word Detective Case File

> **TEACHER VERSION**: `detective.py` in this folder is already fixed and
> bug-free, for instructor reference and grading.

This tutorial is a "fix-it" challenge built around string manipulation
(`.lower()`, `.upper()`, `.replace()`, `.split()`, `.strip()`) and
dictionaries -- the same concepts covered in this week's slides.

## Setup Instructions

This tutorial only uses Python's standard library, so no UV project or
extra dependencies are needed.

1. Navigate to this directory:
   ```bash
   cd tutorials/tutorial_02_strings_and_dictionaries
   ```

2. Run the program:
   ```bash
   python3 detective.py
   ```

## What You'll Learn

- Using string methods to clean and transform text
- Building a dictionary to count occurrences of items
- Looping over dictionary key-value pairs with `.items()`
- Debugging code that "almost works" instead of writing from scratch

## Tasks

Every function in `detective.py` is already written, but each one has
exactly **one small bug**. Look for the `TODO` comments -- each one has
a `Hint` right above it to point you in the right direction.

1. **normalize_text()**: fix which string method lowercases text
2. **replace_secret_word()**: fix the argument order passed to `.replace()`
3. **split_into_words()**: fix what `.split()` is splitting on
4. **strip_punctuation()**: fix which characters are being stripped
5. **build_word_count_dict()**: fix the dictionary so counts increment
6. **print_dictionary_report()**: fix the order `.items()` is unpacked
7. **find_longest_word()**: fix a comparison that finds the shortest word

## Expected Output

Run `python3 detective.py` and compare each printed line to the
`# Expected:` comment beside the matching `print()` call in `main()`.
Once every line matches, the case is closed!

## Tips

- Read the docstring of each function first -- it tells you exactly
  what the function is supposed to do.
- Only change what the `TODO`/`Hint` tells you to change.
- Run the program often (`python3 detective.py`) to check your progress.
- Remember: `.replace(old, new)` takes the text to find *first*, then
  the text to use instead.
