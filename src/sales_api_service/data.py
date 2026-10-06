import csv
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "sales.csv"


def load_sales(path: Path = DATA_PATH) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"Sales file not found: {path}")
    with open(path, newline="", encoding="utf-8") as f:
        return [parse_row(row) for row in csv.DictReader(f)]


def parse_row(row: dict) -> dict:
    return {
        "order_id": row["order_id"],
        "date": row["date"],
        "product": row["product"],
        "category": row["category"],
        "units": int(row["units"]),
        "unit_price": float(row["unit_price"]),
        "region": row["region"],
    }