from pathlib import Path

from analysis_pipeline import load_numbers, moving_average, run_pipeline, summarize


def test_load_numbers_reads_all_values(tmp_path: Path) -> None:
    data_file = tmp_path / "numbers.txt"
    data_file.write_text("1\n2\n3\n", encoding="utf-8")
    assert load_numbers(data_file) == [1.0, 2.0, 3.0]


def test_moving_average_window_three() -> None:
    values = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert moving_average(values, 3) == [2.0, 3.0, 4.0]


def test_summarize_returns_correct_mean_min_max() -> None:
    summary = summarize([2.0, 4.0, 6.0])
    assert summary == {"min": 2.0, "max": 6.0, "mean": 4.0}


def test_run_pipeline_creates_expected_plot_file(tmp_path: Path) -> None:
    input_file = tmp_path / "numbers.txt"
    output_dir = tmp_path / "output"
    input_file.write_text("1\n2\n3\n4\n", encoding="utf-8")

    result = run_pipeline(input_file, output_dir, window=2)
    expected_plot = output_dir / "trend.png"

    assert result["plot_path"] == expected_plot
    assert expected_plot.exists()


def test_moving_average_large_window_returns_empty() -> None:
    assert moving_average([1.0, 2.0], 3) == []
