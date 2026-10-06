# Sales API Service

A small REST API that exposes sales data over HTTP, built with FastAPI.

## Project brief

Sales data stored in a CSV file is hard to reuse: every program that needs it has to open the file and parse it by itself. This project solves that by putting a simple API in front of the data, so any client can ask for exactly what it needs over HTTP. The service reads the synthetic dataset `data/sales.csv` (300 orders with product, category, units, unit price and region) and returns it as JSON. It will offer a few endpoints, for example a list of all sales, a single order by its ID and a list filtered by region, and it will answer with proper error codes when something is wrong, such as 404 for an order that does not exist.


## Run the server

bash
uv run uvicorn sales_api_service.main:app --app-dir src --reload


Then open http://127.0.0.1:8000/sales for the data and http://127.0.0.1:8000/docs for the interactive documentation.

*More documentation (installation, usage, examples) will be added during the project.*