from app.connectors.factory import ConnectorFactory


class IngestionService:

    async def ingest(self, sources):

        results = []

        for source in sources:

            connector = ConnectorFactory.get_connector(source)

            raw_data = await connector.fetch_data()

            normalized_data = connector.normalize(raw_data)

            results.append({
                "source": source.name,
                "records_ingested": normalized_data["record_count"],
                "data": normalized_data["records"]
            })

        return results