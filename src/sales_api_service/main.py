from fastapi import FastAPI

from sales_api_service.data import load_sales

app = FastAPI(title="Sales API Service")


@app.get("/sales")
def list_sales() -> list[dict]:
    return load_sales()
    

@app.get("/")
def root() -> dict:
    return {"service": "Sales API Service", "endpoints": ["/sales", "/docs"]}