# Tutorial 4: The Guild Roster (TEACHER SOLUTION)

> **TEACHER / INSTRUCTOR VERSION -- SOLUTIONS INCLUDED**
> This copy contains completed, bug-free code. Do not distribute this
> version to students; share the student-facing
> `02_activity_data_structures/` project instead.

In this tutorial, students help organize an adventurer's guild by
writing their own sets, list comprehensions, and dictionary
comprehensions -- compact tools for building and filtering collections
of data.

## Setup Instructions

1. Navigate to this directory:
   ```bash
   cd tutorials/tutorial_04_sets_and_comprehensions
   ```

2. Initialize the UV project (if not already done):
   ```bash
   uv init
   ```

3. Run the program:
   ```bash
   uv run roster.py
   ```

## What Students Will Learn

- How to build a `set` from a list to remove duplicates
- How to combine sets with the intersection (`&`) and difference (`-`)
  operators
- How to write a list comprehension to transform every item in a list
- How to write a list comprehension with an `if` filter to keep only
  matching items
- How to write a dictionary comprehension to build a new dictionary
  from a list or another dictionary

## Solutions

All 5 TODOs from the student starter file have been filled in:

1. `unique_attendees()` - `return set(sign_in_sheet)`
2. `guild_overlap()` - `return guild_a & guild_b`
3. `guild_a_exclusive()` - `return guild_a - guild_b`
4. `double_damage()` - `return [value * 2 for value in attack_powers]`
5. `name_lengths()` - `return {name: len(name) for name in names}`

`strong_fighters()` and `rank_by_level()` are provided complete in the
student version as worked examples.

## Expected Output

Run `uv run roster.py` and confirm every printed result matches its
`# Expected:` comment in `roster.py`.
