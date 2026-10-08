from fastapi.testclient import TestClient

from sales_api_service import main

client = TestClient(main.app)


def test_root_lists_endpoints():
    response = client.get("/")
    assert response.status_code == 200
    assert "/sales" in response.json()["endpoints"]


def test_sales_returns_orders():
    response = client.get("/sales")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_sales_returns_503_when_data_missing(monkeypatch):
    def broken_loader():
        raise FileNotFoundError("Sales file not found")

    monkeypatch.setattr(main, "load_sales", broken_loader)
    response = client.get("/sales")
    assert response.status_code == 503


def test_order_returns_single_order():
    response = client.get("/sales/ORD-1001")
    assert response.status_code == 200
    assert response.json()["order_id"] == "ORD-1001"


def test_order_returns_404_for_unknown_id():
    response = client.get("/sales/ORD-0000")
    assert response.status_code == 404


def test_sales_filtered_by_region():
    response = client.get("/sales", params={"region": "EU-West"})
    assert response.status_code == 200
    orders = response.json()
    assert len(orders) > 0
    assert all(order["region"] == "EU-West" for order in orders)


def test_sales_unknown_region_returns_empty_list():
    response = client.get("/sales", params={"region": "Mars"})
    assert response.status_code == 200
    assert response.json() == []