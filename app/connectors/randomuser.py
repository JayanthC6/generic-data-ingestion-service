import httpx

from app.connectors.base import BaseConnector
from app.utils.retry import retry


class RandomUserConnector(BaseConnector):

    @retry(max_attempts=3, delay=2)
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

        if isinstance(data, dict):

            users = data.get("results", [])

            return {
                "records": users,
                "record_count": len(users)
            }

        if isinstance(data, list):

            return {
                "records": data,
                "record_count": len(data)
            }

        return {
            "records": [data],
            "record_count": 1
        }