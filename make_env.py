"""Create a local virtual environment and install notebook dependencies."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
VENV_DIR = PROJECT_ROOT / "venv"
REQUIREMENTS_FILE = PROJECT_ROOT / "requirements.txt"


def run(command: list[str]) -> None:
    subprocess.check_call(command, cwd=PROJECT_ROOT)


def get_venv_python() -> Path:
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def main() -> None:
    if not VENV_DIR.exists():
        run([sys.executable, "-m", "venv", str(VENV_DIR)])

    python_executable = get_venv_python()
    run([str(python_executable), "-m", "pip", "install", "--upgrade", "pip"])
    run([str(python_executable), "-m", "pip", "install", "-r", str(REQUIREMENTS_FILE)])


if __name__ == "__main__":
    main()
