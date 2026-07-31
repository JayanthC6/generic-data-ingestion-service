from fastapi import APIRouter, HTTPException

from app.schemas.ingestion import IngestionRequest
from app.services.ingestion_service import IngestionService

router = APIRouter()

service = IngestionService()


@router.post("/ingest")
async def ingest_data(request: IngestionRequest):

    try:

        result = await service.ingest(request.sources)

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