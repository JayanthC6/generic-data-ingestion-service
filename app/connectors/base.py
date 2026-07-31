from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseConnector(ABC):
    """
    Base class for all API connectors.
    Every connector must implement these methods.
    """

    def __init__(self, endpoint: str, headers=None, params=None):
        self.endpoint = endpoint
        self.headers = headers or {}
        self.params = params or {}

    @abstractmethod
    async def fetch_data(self) -> Any:
        """
        Fetch data from the external API.
        """
        pass

    @abstractmethod
    def normalize(self, data: Any) -> Dict:
        """
        Convert API response into a common format.
        """
        pass