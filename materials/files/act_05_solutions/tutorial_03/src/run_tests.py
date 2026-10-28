from __future__ import annotations

from pathlib import Path
import subprocess
import sys


def main() -> None:
    base_dir = Path(__file__).parent
    command = [sys.executable, "-m", "pytest", "-q", str(base_dir / "test_analysis_pipeline.py")]

    print("Running automated tests...")
    result = subprocess.run(command, capture_output=True, text=True, check=False)

    report_path = base_dir / "test_report.txt"
    report_path.write_text(result.stdout + "\n" + result.stderr, encoding="utf-8")
    print(f"Saved test report: {report_path}")


if __name__ == "__main__":
    main()
