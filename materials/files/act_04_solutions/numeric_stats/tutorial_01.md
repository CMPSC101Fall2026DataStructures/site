# Tutorial 1: Numerical Data Analysis with UV

## Overview

In this tutorial you will analyze numeric data from the Iris dataset. The program reads a CSV file, prints summary statistics, creates plots, and performs a simple statistical test. You will complete a few TODOs that practice lists, dictionaries, and conditionals.

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 1: Create the Project Environment

Move into the project folder:

```bash
cd Act04_analysis/numeric_stats
```

Initialize the project and create a virtual environment:

```bash
uv init
```

Install the required packages:

```bash
uv add pandas seaborn matplotlib plotly scipy rich typer
```

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 2: Review the Code and Complete TODOs

Open [numeric_stats/main.py](../numeric_stats/main.py). The TODOs are short and focus on:

- Building a list of numeric columns (list comprehension)
- Creating a dictionary of summary statistics (dictionary values)
- Adding a conditional check for valid species names
- Adding a file existence check

### Hints

- Numeric columns can be identified with a list comprehension like:
  `col for col in df.columns if col != "species"`
- Use `df[df["species"] == species][numeric_cols].mean().to_dict()`
- Check file existence with `file_path.exists()`
- Exit the program with `raise typer.Exit(code=1)` after printing an error

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 3: Run the Program

To get online help, you can use the following command.

```bash
uv run main.py --help
```

Note: errors in your code are likely to be announced at this point.

To load data, use the CLI to provide the input file:

```bash
uv run main.py data/iris.csv --out-dir output
```

This command reads the CSV data, prints summary statistics, runs a t-test, and saves plots into the output folder.

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Example Output (After Completing TODOs)

```text
Summary statistics and plots
Species     sepal_length  sepal_width  petal_length  petal_width
setosa      4.86          3.31         1.45          0.22
versicolor  6.10          2.87         4.37          1.38
virginica   6.57          2.94         5.77          2.04
T-test for petal_length: t=-18.484, p=0.0000 (setosa vs versicolor)
Saved plots to output
```

You should also see several plot files saved in the output folder (PNG images and one HTML plot).

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Understanding the Output

### Summary Statistics Table

The summary statistics table shows the **mean values** for each numeric measurement grouped by species:

- **setosa**: Smaller flowers with shorter petals (petal_length: 1.45, petal_width: 0.22)
- **versicolor**: Medium-sized flowers with intermediate measurements
- **virginica**: Larger flowers with longer, wider petals (petal_length: 5.77, petal_width: 2.04)

These averages reveal clear differences between species, particularly in petal dimensions.

### T-Test Results

The t-test compares two groups to determine if their means are statistically different:

- **t-statistic** (-18.484): A large absolute value indicates a substantial difference between groups. Negative values simply indicate which group has the lower mean.
- **p-value** (0.0000): This extremely small p-value (much less than 0.05) means the difference is **statistically significant**—not due to random chance.

In this example, *setosa* and *versicolor* have significantly different petal lengths.

### Plot Files

The output folder contains several visualizations:

- **Scatter plots**: Show relationships between pairs of measurements (e.g., sepal length vs. petal length), with points colored by species
- **Distribution plots**: Display the spread and frequency of values for each measurement
- **Interactive HTML plot**: An interactive Plotly visualization you can open in a browser to explore the data dynamically

These plots help you visually identify patterns, clusters, and separations between species.

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## What You Accomplished

You used UV to manage a project, loaded structured data with pandas, computed summary statistics, created plots with multiple libraries, and ran a basic t-test.

Next tutorial: [tutorial_02.md](../tutorial_02/tutorial_02.md)
