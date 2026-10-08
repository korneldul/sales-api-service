import pytest

from sales_api_service.data import load_sales, parse_row

VALID_ROW = {
    "order_id": "ORD-1",
    "date": "2025-01-01",
    "product": "CloudSync",
    "category": "Software",
    "units": "4",
    "unit_price": "2.5",
    "region": "EU-West",
}

HEADER = "order_id,date,product,category,units,unit_price,region\n"


def write_csv(tmp_path, content):
    path = tmp_path / "sales.csv"
    path.write_text(content, encoding="utf-8")
    return path


def test_parse_row_converts_numbers():
    result = parse_row(VALID_ROW)
    assert result["units"] == 4
    assert result["unit_price"] == 2.5


def test_parse_row_rejects_bad_number():
    with pytest.raises(ValueError):
        parse_row({**VALID_ROW, "units": "abc"})


def test_parse_row_rejects_missing_column():
    with pytest.raises(ValueError):
        parse_row({"order_id": "ORD-1"})


def test_load_sales_reads_all_rows(tmp_path):
    content = HEADER + (
        "ORD-1,2025-01-01,CloudSync,Software,1,10.0,EU-West\n"
        "ORD-2,2025-01-02,Router X200,Hardware,2,5.5,EU-East\n"
    )
    sales = load_sales(write_csv(tmp_path, content))
    assert len(sales) == 2
    assert sales[1]["order_id"] == "ORD-2"


def test_load_sales_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_sales(tmp_path / "missing.csv")


def test_load_sales_empty_file(tmp_path):
    with pytest.raises(ValueError):
        load_sales(write_csv(tmp_path, ""))


def test_load_sales_header_only(tmp_path):
    with pytest.raises(ValueError):
        load_sales(write_csv(tmp_path, HEADER))


def test_load_sales_real_dataset():
    assert len(load_sales()) == 300