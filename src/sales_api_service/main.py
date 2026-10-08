from fastapi import FastAPI, HTTPException

from sales_api_service.data import load_sales
from sales_api_service.queries import find_order

app = FastAPI(title="Sales API Service")


def get_sales() -> list[dict]:
    try:
        return load_sales()
    except (FileNotFoundError, ValueError) as error:
        raise HTTPException(status_code=503, detail=str(error)) from error


@app.get("/")
def root() -> dict:
    return {
        "service": "Sales API Service",
        "endpoints": ["/sales", "/sales/{order_id}", "/docs"],
    }


@app.get("/sales")
def list_sales() -> list[dict]:
    return get_sales()


@app.get("/sales/{order_id}")
def get_order(order_id: str) -> dict:
    order = find_order(get_sales(), order_id)
    if order is None:
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
    return order