from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.ingestion import IngestionRequest
from app.services.ingestion_service import IngestionService

router = APIRouter()

service = IngestionService()


@router.post("/ingest")
async def ingest_data(
    request: IngestionRequest,
    db: Session = Depends(get_db)
):

    try:

        result = await service.ingest(request.sources, db)

        return {
            "status": "success",
            "total_sources": len(request.sources),
            "results": result
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )