import httpx

from app.connectors.base import BaseConnector


class RandomUserConnector(BaseConnector):

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

        users = data.get("results", [])

        return {
            "records": users,
            "record_count": len(users)
        }