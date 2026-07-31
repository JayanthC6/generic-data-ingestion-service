from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func

from app.database.db import Base


class IngestedRecord(Base):
    __tablename__ = "ingested_records"

    id = Column(Integer, primary_key=True, index=True)

    source = Column(String, nullable=False)

    payload = Column(JSONB, nullable=False)

    fetched_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )