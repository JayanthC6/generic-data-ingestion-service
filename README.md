# Generic Data Ingestion Service

> An AI-native, extensible data ingestion platform built with **FastAPI**, **PostgreSQL**, **Docker**, and **SQLAlchemy**. The service provides a connector-based architecture to ingest data from heterogeneous REST APIs, normalize responses, and persist them into PostgreSQL through a scalable and production-inspired pipeline.

---

## Overview

Modern applications frequently integrate with multiple third-party APIs, each exposing different response formats, authentication mechanisms, and schemas. Writing custom ingestion logic for every API quickly becomes difficult to maintain.

This project addresses that challenge by introducing a **plugin-based connector architecture**, allowing new data sources to be integrated with minimal code changes while maintaining a clean separation of concerns.

The current implementation supports:

- JSONPlaceholder API
- RandomUser API

and is designed to easily support additional REST APIs in the future.

---

## Features

- REST API built with FastAPI
- Asynchronous data ingestion using HTTPX
- Connector-based architecture
- Factory Pattern for connector selection
- Generic ingestion pipeline
- Automatic response normalization
- PostgreSQL persistence using JSONB
- SQLAlchemy ORM
- Retry mechanism with exponential backoff
- Dockerized application
- Docker Compose support
- Swagger/OpenAPI documentation
- Unit tests using Pytest
- Environment-based configuration

---

## Architecture

```text
                    Client

                       │
                       ▼

                 FastAPI Router
                       │
                       ▼

              Ingestion Service
                       │
                       ▼

              Connector Factory
         ┌─────────────┴─────────────┐
         │                           │
         ▼                           ▼

 JSONPlaceholder Connector    RandomUser Connector
         │                           │
         ▼                           ▼

       Fetch API Data (HTTPX Async)

                    │
                    ▼

              Normalize Response

                    │
                    ▼

          Retry on Transient Failure

                    │
                    ▼

           PostgreSQL Storage (JSONB)
```

---

# Project Structure

```
generic-data-ingestion-service
│
├── app
│   ├── api
│   │     └── routes.py
│   │
│   ├── connectors
│   │     ├── base.py
│   │     ├── factory.py
│   │     ├── jsonplaceholder.py
│   │     └── randomuser.py
│   │
│   ├── database
│   │     ├── db.py
│   │     └── models.py
│   │
│   ├── schemas
│   │     └── ingestion.py
│   │
│   ├── services
│   │     └── ingestion_service.py
│   │
│   ├── storage
│   │     ├── base_storage.py
│   │     └── postgres_storage.py
│   │
│   ├── utils
│   │     └── retry.py
│   │
│   └── main.py
│
├── tests
│     └── test_api.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env.example
```

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.12 | Programming Language |
| FastAPI | REST Framework |
| HTTPX | Async HTTP Client |
| SQLAlchemy | ORM |
| PostgreSQL | Database |
| JSONB | Flexible Payload Storage |
| Docker | Containerization |
| Docker Compose | Multi-container Orchestration |
| Pytest | Testing |

---

# Design Decisions

## Connector Pattern

Every external API implements its own connector responsible for:

- Fetching data
- Normalizing responses

This isolates source-specific logic from the ingestion pipeline.

---

## Factory Pattern

The application never directly instantiates connectors.

Instead, it delegates connector creation to a factory.

Benefits:

- Open for extension
- Closed for modification
- Easy onboarding of new APIs

Adding another connector requires:

1. Create connector
2. Register in factory

No business logic changes are required.

---

## JSONB Storage

Different APIs return completely different payloads.

Instead of creating individual relational schemas, the application stores normalized payloads inside PostgreSQL using JSONB.

Benefits:

- Flexible schema
- Supports heterogeneous APIs
- Easy querying
- Future-proof

---

## Async Architecture

External API calls are performed asynchronously using HTTPX.

Advantages:

- Better scalability
- Non-blocking I/O
- Suitable for concurrent ingestion

---

## Retry Mechanism

The ingestion pipeline includes retry support for transient network failures.

Features:

- Exponential Backoff
- Automatic Retry
- Improved Reliability

---

# Getting Started

## Clone Repository

```bash
git clone https://github.com/JayanthC6/generic-data-ingestion-service.git

cd generic-data-ingestion-service
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create

```
.env
```

Example

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/ingestion_db
```

---

## Run Application

```bash
uvicorn app.main:app --reload
```

Open

```
http://localhost:8000/docs
```

---

# Running with Docker

Build

```bash
docker compose up --build
```

Run

```bash
docker compose up
```

Stop

```bash
docker compose down
```

---

# API Documentation

Swagger

```
http://localhost:8000/docs
```

OpenAPI

```
http://localhost:8000/openapi.json
```

---

# Example Request

```json
{
  "sources": [
    {
      "name": "jsonplaceholder",
      "endpoint": "https://jsonplaceholder.typicode.com/posts"
    },
    {
      "name": "randomuser",
      "endpoint": "https://randomuser.me/api/?results=10"
    }
  ]
}
```

---

# Example Response

```json
{
  "status": "success",
  "total_sources": 2,
  "results": [
    {
      "source": "jsonplaceholder",
      "records_ingested": 100
    },
    {
      "source": "randomuser",
      "records_ingested": 10
    }
  ]
}
```

---

# Database

Table

```
ingested_records
```

Columns

| Column | Type |
|---------|------|
| id | Integer |
| source | String |
| payload | JSONB |
| fetched_at | Timestamp |

---

# Testing

Run all tests

```bash
pytest
```

Current status

```
2 tests passed
```

The test suite validates:

- API availability
- OpenAPI endpoint
- Successful request handling

---

# Current Connectors

| Connector | Status |
|------------|--------|
| JSONPlaceholder | Implemented |
| RandomUser | Implemented |

---

# Extending the Platform

To add a new API:

1. Create a connector inside `app/connectors`
2. Implement `fetch_data()`
3. Implement `normalize()`
4. Register the connector in `factory.py`

No changes are required in the ingestion service.

---

# AI Usage

AI was used as an engineering assistant throughout the development process.

It assisted with:

- Architecture exploration
- Design pattern selection
- Code reviews
- Documentation improvements
- Testing strategy

One incorrect suggestion involved assuming immediate PostgreSQL readiness during Docker startup. Runtime testing exposed the issue, and it was resolved by refining the startup workflow and validating container behavior before application initialization.

This project was developed by validating AI-generated suggestions through testing rather than accepting them without verification.

---

# Future Improvements

- GraphQL Connector
- OpenAPI-driven Connector Generation
- Automatic Schema Mapping
- Incremental Synchronization
- Kafka Storage
- S3 Storage
- Prometheus Metrics
- Structured JSON Logging
- LLM-assisted API Discovery

---

# Author

**Jayanth C**

MCA Graduate

GitHub: https://github.com/JayanthC6

LinkedIn: https://www.linkedin.com/in/jayanthc18/

---

# License

This project was developed as part of an AI Software Engineering take-home assignment and is intended for educational and evaluation purposes.
