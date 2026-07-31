from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Generic Data Ingestion Service",
    version="1.0.0",
    description="A generic and extensible API ingestion framework."
)

app.include_router(router)