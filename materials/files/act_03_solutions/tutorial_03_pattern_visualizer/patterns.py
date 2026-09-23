"""
Tutorial 3: The Pattern Visualizer (Capstone)
================================================

Every function in this file is already complete and correct -- there
are no TODOs here! Instead, your job is to READ the code, run it, and
study how the loops, conditionals, string manipulation, and dictionaries
you practiced in Tutorials 1 and 2 come together to create three very
different kinds of visualizations:

1. A Sierpinski triangle fractal, built one random point at a time
   using a for loop and simple conditionals (the "chaos game").
2. An interactive heatmap grid that classifies every number in a range
   as prime, even, or odd using the same conditional logic from
   Tutorial 1.
3. A word-frequency bar chart built from the same string-and-dictionary
   techniques you debugged in Tutorial 2.

Learning Objectives:
- See loops and conditionals used to generate a fractal pattern
- See conditionals used to classify a whole grid of numbers at once
- See string manipulation + dictionaries power a real visualization
- Practice reading someone else's working code and explaining it

Instructions:
- No TODOs to fix! Just run: uv run patterns.py
- Open the generated files and read the code + comments to see how
  each visualization was built.
"""

import math
import random

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go


# ---------------------------------------------------------------------------
# Part 1: Sierpinski Triangle (loops + conditionals)
# ---------------------------------------------------------------------------

def generate_sierpinski_points(num_points=20000):
    """
    Generate points on a Sierpinski triangle using the "chaos game".

    The rule is simple: start anywhere inside the triangle, then
    repeatedly jump halfway toward a randomly chosen corner. A loop
    drives the repetition, and a conditional (via random.choice) picks
    which corner to jump toward each time.

    Args:
        num_points (int): how many points to generate

    Returns:
        tuple: (x_values, y_values) lists of point coordinates
    """
    # The three corners of the triangle
    corners = [(0, 0), (1, 0), (0.5, math.sqrt(3) / 2)]

    x_values = []
    y_values = []

    # Start at the centroid of the triangle
    current_x, current_y = 0.5, 0.5

    for _ in range(num_points):
        # Randomly choose one of the three corners to jump toward
        target_x, target_y = random.choice(corners)

        # Jump halfway from the current point to the chosen corner
        current_x = (current_x + target_x) / 2
        current_y = (current_y + target_y) / 2

        x_values.append(current_x)
        y_values.append(current_y)

    return x_values, y_values


def plot_sierpinski_triangle(x_values, y_values):
    """
    Save the Sierpinski triangle as a static matplotlib scatter plot.
    """
    plt.figure(figsize=(8, 8))
    plt.scatter(x_values, y_values, s=0.5, c=y_values, cmap="magma")
    plt.title("Sierpinski Triangle (Chaos Game)", fontsize=14, fontweight="bold")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("sierpinski_triangle.png", dpi=300, bbox_inches="tight")
    print("✓ Saved sierpinski_triangle.png")
    plt.close()


# ---------------------------------------------------------------------------
# Part 2: Number Classification Heatmap (conditionals from Tutorial 1)
# ---------------------------------------------------------------------------

def is_prime(n):
    """
    Check if a number is prime. Same logic style as Tutorial 1's
    is_prime_check(), just written for any n >= 2.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def classify_grid(limit):
    """
    Classify every number from 0 up to `limit` as prime, even, or odd.

    This reuses the exact same conditional ideas from Tutorial 1's
    classify_number() and is_prime_check(), just applied to a whole
    range of numbers at once so we can visualize the pattern.

    Args:
        limit (int): the highest number to classify

    Returns:
        list: a numeric "category code" for each number, where
              2 = prime, 1 = even, 0 = odd
    """
    categories = []

    for number in range(limit + 1):
        if is_prime(number):
            categories.append(2)
        elif number % 2 == 0:
            categories.append(1)
        else:
            categories.append(0)

    return categories


def plot_number_heatmap(categories, columns=25):
    """
    Arrange the classified numbers into a grid and display them as an
    interactive plotly heatmap.
    """
    rows = len(categories) // columns + 1
    padded = categories + [0] * (rows * columns - len(categories))
    grid = np.array(padded).reshape(rows, columns)

    fig = go.Figure(
        data=go.Heatmap(
            z=grid,
            colorscale=[[0, "lightgray"], [0.5, "steelblue"], [1, "crimson"]],
            showscale=True,
            colorbar=dict(title="0=odd, 1=even, 2=prime"),
            hovertemplate="Row: %{y}, Col: %{x}<br>Category: %{z}<extra></extra>",
        )
    )
    fig.update_layout(
        title="Number Classification Grid (prime / even / odd)",
        xaxis_title="Column",
        yaxis_title="Row",
        height=600,
        width=1000,
    )
    fig.write_html("number_heatmap.html")
    print("✓ Saved number_heatmap.html (open in web browser)")


# ---------------------------------------------------------------------------
# Part 3: Word Frequency Bar Chart (strings + dictionaries from Tutorial 2)
# ---------------------------------------------------------------------------

def count_words(text):
    """
    Clean up and count word frequency in `text`, using the same
    normalize -> split -> strip -> count pipeline from Tutorial 2.

    Args:
        text (str): raw text to analyze

    Returns:
        dict: maps each cleaned word to how many times it appears
    """
    normalized = text.lower()
    raw_words = normalized.split()
    clean_words = [word.strip(".,!?\"'") for word in raw_words]

    word_counts = {}
    for word in clean_words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def plot_word_frequency(word_counts, top_n=10):
    """
    Save a bar chart of the most frequent words using plotly.
    """
    # Sort words by frequency, highest first, and keep the top N
    sorted_words = sorted(word_counts.items(), key=lambda pair: pair[1], reverse=True)
    top_words = sorted_words[:top_n]

    words = [pair[0] for pair in top_words]
    counts = [pair[1] for pair in top_words]

    fig = go.Figure(data=[
        go.Bar(
            x=words,
            y=counts,
            marker=dict(color=counts, colorscale="Viridis", showscale=True),
            text=counts,
            textposition="auto",
        )
    ])
    fig.update_layout(
        title="Word Frequency in the Detective's Report",
        xaxis_title="Word",
        yaxis_title="Count",
        template="plotly_white",
        height=500,
    )
    fig.write_html("word_frequency.html")
    print("✓ Saved word_frequency.html (open in web browser)")


def main():
    """
    Run all three visualizations and report on what was created.
    """
    print("\n" + "=" * 60)
    print("Tutorial 3: The Pattern Visualizer")
    print("=" * 60)

    print("\n[Part 1] Generating a Sierpinski triangle with the chaos game...")
    x_values, y_values = generate_sierpinski_points(num_points=20000)
    plot_sierpinski_triangle(x_values, y_values)

    print("\n[Part 2] Classifying numbers 0-499 as prime, even, or odd...")
    categories = classify_grid(limit=499)
    plot_number_heatmap(categories, columns=25)

    print("\n[Part 3] Counting word frequency in a sample report...")
    report = (
        "The culprit left a clue in the hallway. The culprit dropped a "
        "glove near the window, and the glove had a torn thread. "
        "Detectives followed the thread to the culprit's hideout!"
    )
    word_counts = count_words(report)
    plot_word_frequency(word_counts, top_n=8)

    print("\n" + "=" * 60)
    print("All visualizations created successfully!")
    print("=" * 60)
    print("\nOutput files created:")
    print("  - sierpinski_triangle.png")
    print("  - number_heatmap.html (open in browser for interactive view)")
    print("  - word_frequency.html (open in browser for interactive view)")
    print("\n")


if __name__ == "__main__":
    main()
