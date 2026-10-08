from sales_api_service.queries import filter_by_region, find_order

SALES = [
    {"order_id": "ORD-1", "region": "EU-West"},
    {"order_id": "ORD-2", "region": "EU-East"},
    {"order_id": "ORD-3", "region": "EU-West"},
]


def test_find_order_returns_match():
    assert find_order(SALES, "ORD-2")["region"] == "EU-East"


def test_find_order_returns_none_for_unknown_id():
    assert find_order(SALES, "ORD-999") is None


def test_filter_by_region_returns_only_matching():
    result = filter_by_region(SALES, "EU-West")
    assert [sale["order_id"] for sale in result] == ["ORD-1", "ORD-3"]


def test_filter_by_region_ignores_case():
    assert len(filter_by_region(SALES, "eu-west")) == 2


def test_filter_by_region_unknown_region_returns_empty_list():
    assert filter_by_region(SALES, "Mars") == []