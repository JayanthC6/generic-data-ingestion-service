from fastapi import FastAPI

from app.api.routes import router
from app.database.db import Base, engine

import app.database.models

print(Base.metadata.tables.keys())
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Generic Data Ingestion Service",
    version="1.0.0",
    description="A generic and extensible API ingestion framework."
)

app.include_router(router)