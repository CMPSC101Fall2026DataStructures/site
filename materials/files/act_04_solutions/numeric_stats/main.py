# Instructor solution for demonstrations

from __future__ import annotations

from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from scipy import stats
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

app = typer.Typer()
console = Console()


def load_data(file_path: Path) -> pd.DataFrame:
    """Load the iris dataset from a CSV file."""
    if not file_path.exists():
        console.print(f"Data file not found: {file_path}")
        raise typer.Exit(code=1)
    return pd.read_csv(file_path)


def get_numeric_columns(df: pd.DataFrame) -> list[str]:
    """Return a list of numeric column names."""
    return [col for col in df.columns if col != "species"]


def summarize_by_species(df: pd.DataFrame, numeric_cols: list[str]) -> dict[str, dict[str, float]]:
    """Compute mean values for each species."""
    summaries: dict[str, dict[str, float]] = {}
    for species in sorted(df["species"].unique()):
        summaries[species] = df[df["species"] == species][numeric_cols].mean().to_dict()
    return summaries


def run_ttest(df: pd.DataFrame, column: str, species_a: str, species_b: str) -> tuple[float, float]:
    """Run an independent t-test for two species and one measurement column."""
    species_values = set(df["species"].unique())
    if species_a not in species_values or species_b not in species_values:
        console.print("Invalid species name. Use one of: " + ", ".join(sorted(species_values)))
        raise typer.Exit(code=1)

    group_a = df[df["species"] == species_a][column]
    group_b = df[df["species"] == species_b][column]
    t_stat, p_value = stats.ttest_ind(group_a, group_b, equal_var=False)
    return t_stat, p_value


def print_summary_table(summaries: dict[str, dict[str, float]], numeric_cols: list[str]) -> None:
    """Print a summary table of mean values by species."""
    table = Table(title="Mean Measurements by Species")
    table.add_column("Species", style="bold")
    for col in numeric_cols:
        table.add_column(col, justify="right")

    for species, stats_dict in summaries.items():
        row = [species] + [f"{stats_dict[col]:.2f}" for col in numeric_cols]
        table.add_row(*row)

    console.print(table)


def create_plots(df: pd.DataFrame, numeric_cols: list[str], out_dir: Path) -> None:
    """Create plots using seaborn, matplotlib, pandas, and plotly."""
    out_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(6, 4))
    sns.histplot(data=df, x="sepal_length", hue="species", kde=True)
    plt.title("Sepal Length Distribution")
    plt.tight_layout()
    plt.savefig(out_dir / "sepal_length_hist.png")
    plt.close()

    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df, x="species", y="petal_length")
    plt.title("Petal Length by Species")
    plt.tight_layout()
    plt.savefig(out_dir / "petal_length_box.png")
    plt.close()

    pairplot = sns.pairplot(df, hue="species")
    pairplot.savefig(out_dir / "pairplot.png")
    plt.close()

    ax = df[numeric_cols].plot(kind="box", figsize=(7, 4), title="All Measurements")
    ax.get_figure().tight_layout()
    ax.get_figure().savefig(out_dir / "all_measurements_box.png")
    plt.close(ax.get_figure())

    fig = px.scatter(
        df,
        x="sepal_width",
        y="petal_width",
        color="species",
        title="Sepal Width vs Petal Width",
    )
    fig.write_html(out_dir / "scatter_plotly.html")


@app.command()
def analyze(
    data_file: Path = typer.Argument(..., help="Path to the iris CSV file"),
    out_dir: Path = typer.Option(Path("output"), help="Directory for saved plots"),
    ttest_column: str = typer.Option("petal_length", help="Column for t-test"),
    species_a: str = typer.Option("setosa", help="First species for t-test"),
    species_b: str = typer.Option("versicolor", help="Second species for t-test"),
) -> None:
    """Run summary statistics, plots, and a simple t-test."""
    df = load_data(data_file)
    numeric_cols = get_numeric_columns(df)

    console.print(Panel.fit("Summary statistics and plots"))
    summaries = summarize_by_species(df, numeric_cols)
    print_summary_table(summaries, numeric_cols)

    t_stat, p_value = run_ttest(df, ttest_column, species_a, species_b)
    console.print(
        f"T-test for {ttest_column}: t={t_stat:.3f}, p={p_value:.4f} "
        f"({species_a} vs {species_b})"
    )

    create_plots(df, numeric_cols, out_dir)
    console.print(f"Saved plots to {out_dir}")


if __name__ == "__main__":
    app()
