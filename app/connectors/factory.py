from app.connectors.jsonplaceholder import JsonPlaceholderConnector
from app.connectors.randomuser import RandomUserConnector


class ConnectorFactory:

    @staticmethod
    def get_connector(source):

        connectors = {
            "jsonplaceholder": JsonPlaceholderConnector,
            "randomuser": RandomUserConnector,
        }

        connector_class = connectors.get(source.name.lower())

        if not connector_class:
            raise ValueError(f"Unsupported source: {source.name}")

        return connector_class(
            endpoint=str(source.endpoint),
            headers=source.headers,
            params=source.params
        )