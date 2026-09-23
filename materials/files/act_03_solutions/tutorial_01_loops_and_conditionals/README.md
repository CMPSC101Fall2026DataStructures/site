# Tutorial 1: The Loop & Conditional Dungeon

> **TEACHER VERSION**: `dungeon.py` in this folder is already fixed and
> bug-free, for instructor reference and grading.

This tutorial is a "fix-it" challenge built around `for`/`while` loops,
`if`/`elif`/`else` conditionals, nested conditionals, and logical
operators (`and`/`or`/`not`) -- the same concepts covered in this
week's slides.

## Setup Instructions

This tutorial only uses Python's standard library, so no UV project or
extra dependencies are needed.

1. Navigate to this directory:
   ```bash
   cd tutorials/tutorial_01_loops_and_conditionals
   ```

2. Run the program:
   ```bash
   python3 dungeon.py
   ```

## What You'll Learn

- Tracing through `for` and `while` loops to spot logic errors
- Reading `if`/`elif`/`else` chains and nested conditionals
- Using logical operators (`and`, `or`, `not`) correctly
- Debugging code that "almost works" instead of writing from scratch

## Tasks

Every function in `dungeon.py` is already written, but each one has
exactly **one small bug**. Look for the `TODO` comments -- each one has
a `Hint` right above it to point you in the right direction.

1. **classify_number()**: fix a comparison so `0` isn't labeled "positive"
2. **secret_door()**: fix a misspelled string comparison
3. **countdown_blaster()**: fix a `while` loop that never ends
4. **print_even_numbers()**: fix a `range()` call collecting odd numbers
5. **is_prime_check()**: fix a `range()` step size that breaks prime checks
6. **combo_lock()**: fix `and`/`or` logic so both codes are required
7. **treasure_room()**: fix a nested conditional checking the wrong thing

## Expected Output

Run `python3 dungeon.py` and compare each printed line to the `# Expected:`
comment beside the matching `print()` call in `main()`. Once every line
matches, you've cleared the dungeon!

## Tips

- Read the docstring of each function first -- it tells you exactly
  what the function is supposed to do.
- Only change what the `TODO`/`Hint` tells you to change.
- Run the program often (`python3 dungeon.py`) to check your progress.
- If a loop never finishes, press `Ctrl+C` to stop it, then look for a
  missing increment/decrement.
