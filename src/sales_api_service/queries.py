def find_order(sales: list[dict], order_id: str) -> dict | None:
    for sale in sales:
        if sale["order_id"] == order_id:
            return sale
    return None


def filter_by_region(sales: list[dict], region: str) -> list[dict]:
    return [sale for sale in sales if sale["region"].lower() == region.lower()]