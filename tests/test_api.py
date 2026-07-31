from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_swagger_docs():
    response = client.get("/docs")
    assert response.status_code == 200
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_swagger_docs():
    response = client.get("/docs")
    assert response.status_code == 200


def test_openapi():
    response = client.get("/openapi.json")
    assert response.status_code == 200


def test_invalid_ingest_request():
    response = client.post("/ingest", json={})
    assert response.status_code in [422, 400]

def test_openapi():
    response = client.get("/openapi.json")
    assert response.status_code == 200