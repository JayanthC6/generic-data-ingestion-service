import httpx

from app.connectors.base import BaseConnector


class JsonPlaceholderConnector(BaseConnector):

    async def fetch_data(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                self.endpoint,
                headers=self.headers,
                params=self.params,
                timeout=30
            )

            response.raise_for_status()

            return response.json()

    def normalize(self, data):

        if isinstance(data, list):
            return {
                "records": data,
                "record_count": len(data)
            }

        return {
            "records": [data],
            "record_count": 1
        }