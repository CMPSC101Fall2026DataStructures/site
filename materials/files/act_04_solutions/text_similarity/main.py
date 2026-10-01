# Instructor solution for demonstrations

from __future__ import annotations

from collections import Counter
from math import log2, sqrt
from pathlib import Path
import re
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

app = typer.Typer()
console = Console()


def read_text(file_path: Path) -> str:
    """Read text from a file path."""
    return file_path.read_text(encoding="utf-8")


def tokenize(text: str) -> list[str]:
    """Convert text into a list of lowercase word tokens."""
    cleaned = re.sub(r"[^a-zA-Z\s]", " ", text.lower())
    tokens = [token for token in cleaned.split() if token]
    return tokens


def cosine_similarity(counter_a: Counter, counter_b: Counter) -> float:
    """Compute cosine similarity for two Counter vectors."""
    vocab = set(counter_a) | set(counter_b)
    dot_product = 0.0
    norm_a = 0.0
    norm_b = 0.0

    for word in vocab:
        count_a = counter_a.get(word, 0)
        count_b = counter_b.get(word, 0)
        dot_product += count_a * count_b
        norm_a += count_a ** 2
        norm_b += count_b ** 2

    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0

    return dot_product / (sqrt(norm_a) * sqrt(norm_b))


def mutual_information(counter_a: Counter, counter_b: Counter) -> float:
    """Compute mutual information between token identity and document label."""
    total_a = sum(counter_a.values())
    total_b = sum(counter_b.values())
    total = total_a + total_b
    if total == 0:
        return 0.0

    p_doc_a = total_a / total
    p_doc_b = total_b / total
    vocab = set(counter_a) | set(counter_b)

    mi = 0.0
    for word in vocab:
        count_a = counter_a.get(word, 0)
        count_b = counter_b.get(word, 0)
        p_word = (count_a + count_b) / total
        if p_word == 0:
            continue

        if count_a > 0:
            p_xy = count_a / total
            mi += p_xy * log2(p_xy / (p_word * p_doc_a))
        if count_b > 0:
            p_xy = count_b / total
            mi += p_xy * log2(p_xy / (p_word * p_doc_b))

    return mi


def print_similarity_table(cos_sim: float, mi: float) -> None:
    """Print a summary table of similarity scores."""
    table = Table(title="Text Similarity Summary")
    table.add_column("Metric")
    table.add_column("Value", justify="right")
    table.add_row("Cosine similarity", f"{cos_sim:.4f}")
    table.add_row("Mutual information", f"{mi:.4f}")
    console.print(table)


@app.command()
def compare(
    file_a: Path = typer.Argument(..., help="First text file"),
    file_b: Path = typer.Argument(..., help="Second text file"),
) -> None:
    """Compare two text files with mutual information and cosine similarity."""
    text_a = read_text(file_a)
    text_b = read_text(file_b)

    tokens_a = tokenize(text_a)
    tokens_b = tokenize(text_b)

    counter_a = Counter(tokens_a)
    counter_b = Counter(tokens_b)

    console.print(Panel.fit("Text similarity results"))
    cos_sim = cosine_similarity(counter_a, counter_b)
    mi = mutual_information(counter_a, counter_b)
    print_similarity_table(cos_sim, mi)


if __name__ == "__main__":
    app()
