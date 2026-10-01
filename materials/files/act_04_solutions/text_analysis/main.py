# Instructor solution for demonstrations

from __future__ import annotations

from pathlib import Path
import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
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
    cleaned = re.sub(r"[^a-zA-Z\s]", " ", text)
    tokens = [token.lower() for token in cleaned.split() if token]
    return tokens


def letter_frequency(text: str) -> dict[str, int]:
    """Count the frequency of letters in the text."""
    freq: dict[str, int] = {}
    for ch in text.lower():
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1
    return freq


def word_frequency(tokens: list[str]) -> dict[str, int]:
    """Count the frequency of words in the token list."""
    counts: dict[str, int] = {}
    for token in tokens:
        counts[token] = counts.get(token, 0) + 1
    return counts


def print_top_words(word_freq: dict[str, int], top_n: int) -> None:
    """Print a table of the top N words."""
    table = Table(title=f"Top {top_n} Words")
    table.add_column("Rank", justify="right")
    table.add_column("Word")
    table.add_column("Count", justify="right")

    for rank, (word, count) in enumerate(
        sorted(word_freq.items(), key=lambda item: item[1], reverse=True)[:top_n],
        start=1,
    ):
        table.add_row(str(rank), word, str(count))

    console.print(table)


def report_word_lookup(word: str, word_freq: dict[str, int]) -> None:
    """Report how often a word appears in the text."""
    if word in word_freq:
        console.print(f'The word "{word}" appears {word_freq[word]} times.')
    else:
        console.print(f'The word "{word}" does not appear in the text.')


def create_plots(word_freq: dict[str, int], letter_freq: dict[str, int], out_dir: Path) -> None:
    """Create plots for word and letter frequencies."""
    out_dir.mkdir(parents=True, exist_ok=True)

    word_df = pd.DataFrame(
        sorted(word_freq.items(), key=lambda item: item[1], reverse=True)[:15],
        columns=["word", "count"],
    )
    plt.figure(figsize=(7, 4))
    sns.barplot(data=word_df, x="count", y="word")
    plt.title("Top 15 Words")
    plt.tight_layout()
    plt.savefig(out_dir / "top_words.png")
    plt.close()

    letter_df = pd.DataFrame(sorted(letter_freq.items()), columns=["letter", "count"])
    fig = px.bar(letter_df, x="letter", y="count", title="Letter Frequencies")
    fig.write_html(out_dir / "letter_frequencies.html")


def print_stats(tokens: list[str]) -> None:
    """Print simple text statistics."""
    token_count = len(tokens)
    unique_count = len(set(tokens))
    avg_length = sum(len(token) for token in tokens) / max(token_count, 1)

    console.print(
        f"Total tokens: {token_count}\n"
        f"Unique tokens: {unique_count}\n"
        f"Average word length: {avg_length:.2f}"
    )


@app.command()
def analyze(
    file_path: Path = typer.Argument(..., help="Path to the text file"),
    word: str = typer.Option("detective", help="Word to look up"),
    out_dir: Path = typer.Option(Path("output"), help="Directory for saved plots"),
) -> None:
    """Analyze a text file with word and letter statistics."""
    text = read_text(file_path)
    tokens = tokenize(text)

    console.print(Panel.fit("Text analysis results"))
    print_stats(tokens)

    word_freq = word_frequency(tokens)
    letter_freq = letter_frequency(text)
    print_top_words(word_freq, top_n=10)
    report_word_lookup(word, word_freq)

    create_plots(word_freq, letter_freq, out_dir)
    console.print(f"Saved plots to {out_dir}")


if __name__ == "__main__":
    app()
