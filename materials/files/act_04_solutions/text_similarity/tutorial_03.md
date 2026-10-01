# Tutorial 3: Text Similarity Challenge

## Overview

In this challenge you will compare two text files by computing cosine similarity and mutual information. You will complete TODOs that require list comprehensions, dictionary-style counting, and numeric updates inside loops.

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 1: Create the Project Environment

Move into the project folder:

```bash
cd Act04_analysis/text_similarity
```

Initialize the project and create a virtual environment:

```bash
uv init
```

Install the required packages:

```bash
uv add rich typer
```

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 2: Review the Code and Complete TODOs

Open [text_similarity/main.py](../text_similarity/main.py). The TODOs include:

- Building a token list with a list comprehension
- Updating dot products and norms in a loop
- Adding mutual information contributions inside a loop

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 3: Run the Program

To get online help, you can use the following command.

``` bash
uv run main.py --help
```

To work with data, use the CLI to pass two input files:

```bash
uv run main.py data/sherlock_holmes.txt data/pride_prejudice.txt
```

This command prints cosine similarity and mutual information scores.

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Example Output (After Completing TODOs)

```text
Text similarity results
Text Similarity Summary
Metric               Value
Cosine similarity    0.5248
Mutual information   0.6131
```

![--- --- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Understanding the Output

The program computes two complementary similarity metrics to compare the texts:

### Cosine Similarity

**Range**: 0.0 to 1.0

- **1.0**: The documents use words in exactly the same proportions (identical vocabulary distribution)
- **0.0**: The documents share no common words
- **0.5248** (example): Indicates **moderate similarity**—the texts share some vocabulary and themes but have distinct content

Cosine similarity measures the angle between document vectors in word-frequency space. It's particularly useful for comparing documents of different lengths because it normalizes for document size.

### Mutual Information

**Range**: 0.0 to 1.0 (normalized version)

- **Higher values**: Greater information overlap—knowing word frequencies in one document tells you more about the other
- **Lower values**: The documents are more independent in their word usage
- **0.6131** (example): Suggests **substantial shared information**—the texts likely cover related topics or share stylistic elements

Mutual information quantifies how much knowing the word distribution in one text reduces uncertainty about the other text.

### Interpreting the Results Together

In this example:
- Both metrics (~0.52 and ~0.61) indicate the Sherlock Holmes and Pride & Prejudice excerpts share **moderate to substantial similarity**
- They likely share common literary English, formal vocabulary, and narrative structures
- However, the values below 0.8 confirm they remain distinct texts with different themes, characters, and styles

When comparing texts:
- **High values** (>0.7): Texts are very similar (same author, genre, or topic)
- **Moderate values** (0.4-0.7): Some relationship exists (same time period, language style, or broad genre)
- **Low values** (<0.4): Texts are quite different (different genres, languages, or domains)

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Challenge Hints

- Dot product update: `dot_product += count_a * count_b`
- Norm updates: `norm_a += count_a ** 2` and `norm_b += count_b ** 2`
- Mutual information contributions:
  - For doc A: `p_xy = count_a / total` then `mi += p_xy * log2(p_xy / (p_word * p_doc_a))`
  - For doc B: `p_xy = count_b / total` then `mi += p_xy * log2(p_xy / (p_word * p_doc_b))`

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## What You Accomplished

You compared two documents with similarity metrics and practiced building text vectors for statistical comparisons.
