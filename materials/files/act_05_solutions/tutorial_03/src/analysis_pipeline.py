# obc

from __future__ import annotations

from pathlib import Path
import matplotlib.pyplot as plt


def load_numbers(file_path: Path) -> list[float]:
    """Load one float per line from a text file."""
    values: list[float] = []
    for line in file_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        values.append(float(stripped))
    return values


def moving_average(values: list[float], window: int) -> list[float]:
    """Compute a simple moving average."""
    if window <= 0:
        raise ValueError("window must be positive")
    if window > len(values):
        return []

    averages: list[float] = []
    # DONE: Fix loop bounds so every valid window is included.
    for index in range(0, len(values) - window + 1):
        segment = values[index : index + window]
        averages.append(sum(segment) / window)
    return averages


def summarize(values: list[float]) -> dict[str, float]:
    """Return min, max, and mean for a list of values."""
    if not values:
        raise ValueError("values cannot be empty")

    # DONE: Fix the mean calculation.
    mean_value = sum(values) / len(values)
    return {
        "min": min(values),
        "max": max(values),
        "mean": mean_value,
    }


def create_line_plot(values: list[float], output_path: Path) -> None:
    """Create a line chart and save to disk."""
    plt.figure(figsize=(6, 3))
    plt.plot(values, marker="o")
    plt.title("Input Values")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Saved line plot to {output_path}")
    plt.close()


def run_pipeline(input_file: Path, output_dir: Path, window: int = 3) -> dict[str, object]:
    """Run the full analysis workflow and return summary data."""
    output_dir.mkdir(parents=True, exist_ok=True)
    values = load_numbers(input_file)
    summary = summarize(values)
    averages = moving_average(values, window)

    # DONE: Fix the file name to match test expectations.
    plot_path = output_dir / "trend.png"
    create_line_plot(values, plot_path)

    return {
        "summary": summary,
        "moving_average": averages,
        "plot_path": plot_path,
    }