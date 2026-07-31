from sqlalchemy.orm import Session

from app.connectors.factory import ConnectorFactory
from app.database.models import IngestedRecord


class IngestionService:

    async def ingest(self, sources, db: Session):

        results = []

        for source in sources:

            connector = ConnectorFactory.get_connector(source)

            raw_data = await connector.fetch_data()

            normalized_data = connector.normalize(raw_data)

            # Save every record into PostgreSQL
            for record in normalized_data["records"]:

                db_record = IngestedRecord(
                    source=source.name,
                    payload=record
                )

                db.add(db_record)

            db.commit()

            results.append({
                "source": source.name,
                "records_ingested": normalized_data["record_count"],
                "data": normalized_data["records"]
            })

        return results