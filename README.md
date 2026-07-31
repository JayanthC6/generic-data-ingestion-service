# Generic Data Ingestion Service

A scalable, extensible, and Dockerized data ingestion framework built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**.

This project ingests data from multiple external APIs through a connector-based architecture, normalizes the data, and stores it in PostgreSQL using a generic JSONB schema.

---

## Features

- FastAPI REST API
- Generic Connector Architecture
- Factory Design Pattern
- PostgreSQL Persistence
- SQLAlchemy ORM
- JSONB Storage
- Docker Support
- Retry Mechanism
- Automatic Table Creation
- Swagger API Documentation

---

## Architecture

```
                Client
                   │
                   ▼
             FastAPI Endpoint
                   │
                   ▼
           Ingestion Service
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
 JsonPlaceholder      RandomUser
     Connector          Connector
         │                   │
         └─────────┬─────────┘
                   ▼
             Normalize Data
                   │
                   ▼
            SQLAlchemy ORM
                   │
                   ▼
             PostgreSQL JSONB
```

---

## Project Structure

```
generic-data-ingestion-service/
│
├── app/
│   ├── api/
│   ├── connectors/
│   ├── database/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Supported Connectors

| Connector | Description |
|------------|-------------|
| JsonPlaceholder | Demo REST API |
| RandomUser | Random User Generator |

---

## Tech Stack

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose
- HTTPX

---

## Local Setup

### Clone Repository

```bash
git clone <repository-url>
cd generic-data-ingestion-service
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/ingestion_db
```

### Run

```bash
uvicorn app.main:app --reload
```

---

## Docker Setup

```bash
docker compose up --build
```

Swagger:

```
http://localhost:8000/docs
```

---

## API Endpoint

### POST /ingest

Sample Request

```json
{
  "sources": [
    {
      "name": "jsonplaceholder",
      "endpoint": "https://jsonplaceholder.typicode.com/posts"
    }
  ]
}
```

---

## Sample Response

```json
{
  "status": "success",
  "total_sources": 1,
  "results": [
    {
      "source": "jsonplaceholder",
      "records_ingested": 100
    }
  ]
}
```

---

## Database Schema

Table:

```
ingested_records
```

Columns

- id
- source
- payload (JSONB)
- fetched_at

---

## Design Patterns Used

- Factory Pattern
- Connector Pattern
- Service Layer Pattern
- Dependency Injection (FastAPI)

---

## Future Improvements

- Authentication
- Background Jobs
- Kafka Integration
- Scheduled Ingestion
- Metrics Dashboard
- Cloud Deployment

---

## Author

**Jayanth C**

MCA Graduate – Bangalore Institute of Technology