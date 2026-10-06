import csv
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "sales.csv"


def load_sales(path: Path = DATA_PATH) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))