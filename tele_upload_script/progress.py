import json
from pathlib import Path

PROGRESS_FILE = Path("progress.json")


def load_progress():
    if not PROGRESS_FILE.exists():
        return []

    with open(PROGRESS_FILE, "r") as file:
        return json.load(file)


def save_progress(uploaded):
    with open(PROGRESS_FILE, "w") as file:
        json.dump(uploaded, file, indent=4)