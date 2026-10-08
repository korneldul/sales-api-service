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