from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict


class SourceConfig(BaseModel):
    name: str
    endpoint: HttpUrl
    headers: Optional[Dict[str, str]] = None
    params: Optional[Dict[str, str]] = None


class IngestionRequest(BaseModel):
    sources: List[SourceConfig]