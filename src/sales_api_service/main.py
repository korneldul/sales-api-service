from fastapi import FastAPI, HTTPException

from sales_api_service.data import load_sales

app = FastAPI(title="Sales API Service")


@app.get("/")
def root() -> dict:
    return {"service": "Sales API Service", "endpoints": ["/sales", "/docs"]}


@app.get("/sales")
def list_sales() -> list[dict]:
    try:
        return load_sales()
    except (FileNotFoundError, ValueError) as error:
        raise HTTPException(status_code=503, detail=str(error)) from error