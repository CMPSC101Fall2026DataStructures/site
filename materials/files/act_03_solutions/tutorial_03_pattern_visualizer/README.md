# Tutorial 3: The Pattern Visualizer (Capstone)

This tutorial brings together loops, conditionals, string manipulation,
and dictionaries from Tutorials 1 and 2 to build three fun
visualizations: a fractal, a heatmap, and a bar chart.

## Setup Instructions

1. Navigate to this directory:
   ```bash
   cd tutorials/tutorial_03_pattern_visualizer
   ```

2. Initialize the UV project (if not already done):
   ```bash
   uv init
   ```

3. Add required dependencies:
   ```bash
   uv add matplotlib plotly numpy
   ```

4. Run the program:
   ```bash
   uv run patterns.py
   ```

## What You'll Learn

- How a loop + simple conditional choice can generate a fractal pattern
  (the Sierpinski triangle "chaos game")
- How the same prime/even/odd conditional logic from Tutorial 1 can
  classify an entire grid of numbers at once
- How the string + dictionary pipeline from Tutorial 2 can power a
  real word-frequency visualization

## Tasks

There are **no TODOs** in this tutorial -- every function is complete
and correct. Instead:

1. Run `uv run patterns.py` and open each generated file.
2. Read through `patterns.py` and match each visualization back to the
   loop/conditional/string/dictionary concepts you practiced in
   Tutorials 1 and 2.
3. Be ready to explain, in your own words, how `generate_sierpinski_points()`,
   `classify_grid()`, and `count_words()` each work.

## Expected Output

When complete, the program will generate:
- `sierpinski_triangle.png` - a fractal built one point at a time
- `number_heatmap.html` - an interactive grid of prime/even/odd numbers
- `word_frequency.html` - an interactive bar chart of word counts

## Tips

- Nothing to fix here! Focus on reading and understanding the code.
- Try changing `num_points`, `limit`, or the sample `report` text in
  `main()` and re-running to see how the visualizations change.
- Open the `.html` files in a web browser -- you can hover over the
  heatmap and bar chart for interactive details.
