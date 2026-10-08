import csv
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "sales.csv"


def load_sales(path: Path = DATA_PATH) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"Sales file not found: {path}")
    with open(path, newline="", encoding="utf-8") as f:
        sales = [parse_row(row) for row in csv.DictReader(f)]
    if not sales:
        raise ValueError(f"Sales file contains no data: {path}")
    return sales


def parse_row(row: dict) -> dict:
    try:
        return {
            "order_id": row["order_id"],
            "date": row["date"],
            "product": row["product"],
            "category": row["category"],
            "units": int(row["units"]),
            "unit_price": float(row["unit_price"]),
            "region": row["region"],
        }
    except (KeyError, ValueError, TypeError) as error:
        raise ValueError(f"Invalid sales row: {row}") from error