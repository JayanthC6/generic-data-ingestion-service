<div align="center">

# Generic Data Ingestion Service

### AI-Native | Configuration-Driven | Extensible Data Ingestion Platform

A production-inspired data ingestion framework built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Docker**. The platform provides a scalable connector-based architecture for ingesting heterogeneous REST APIs, normalizing their responses, and persisting them into PostgreSQL through a unified ingestion pipeline.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Pytest](https://img.shields.io/badge/Tests-Pytest-success)

</div>

---

# Problem Statement

Organizations integrate with numerous third-party APIs, each exposing different authentication mechanisms, response formats, pagination strategies, and schemas.

Building a custom ingestion pipeline for every API quickly becomes difficult to maintain and scale.

This project addresses that challenge by providing a **generic, connector-based ingestion framework** where data sources are isolated behind reusable connectors while the ingestion pipeline remains independent of API-specific implementation details.

To further improve extensibility, the project introduces **configuration-driven source definitions** using YAML, allowing API configurations to evolve without modifying core business logic.

---

# Key Features

- Generic Connector Architecture
- Factory Design Pattern
- Configuration-driven source definitions (YAML)
- FastAPI REST API
- Asynchronous data ingestion using HTTPX
- Automatic response normalization
- PostgreSQL persistence using JSONB
- SQLAlchemy ORM
- Retry mechanism for transient failures
- Docker & Docker Compose support
- Swagger / OpenAPI documentation
- Unit testing with Pytest
- Environment-based configuration

---

# Architecture

```
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

         └─────────────┬─────────────┘
                       │
                       ▼

          Async HTTP Data Retrieval

                       │
                       ▼

             Response Normalization

                       │
                       ▼

              Retry on Failure

                       │
                       ▼

            PostgreSQL (JSONB Storage)
```

---

# Project Structure

```
generic-data-ingestion-service

│

├── app

│   ├── api

│   ├── config

│   ├── connectors

│   ├── database

│   ├── schemas

│   ├── services

│   ├── storage

│   ├── utils

│   └── main.py

│

├── configs

│   ├── jsonplaceholder.yaml

│   └── randomuser.yaml

│

├── tests

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
|------------|----------|
| Python 3.12 | Programming Language |
| FastAPI | REST Framework |
| HTTPX | Async HTTP Client |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Docker | Containerization |
| Docker Compose | Multi-container Deployment |
| PyYAML | Configuration Management |
| Pytest | Testing |

---

# Design Decisions

## Connector Pattern

Each external API encapsulates its own retrieval and normalization logic.

This isolates API-specific implementation details from the ingestion pipeline and allows additional connectors to be introduced with minimal changes.

---

## Factory Pattern

The ingestion service never directly creates connectors.

Instead, connector creation is delegated to a factory.

Benefits:

- Open for extension
- Closed for modification
- Centralized connector registration
- Simplified onboarding of new APIs

---

## Configuration-Driven Sources

Instead of hardcoding API metadata inside the application, connector definitions are externalized into YAML configuration files.

Current implementation includes:

- JSONPlaceholder
- RandomUser

Future APIs can be introduced through configuration with minimal application changes.

---

## JSONB Storage

Different APIs expose heterogeneous response schemas.

Rather than designing separate relational schemas for every API, normalized payloads are stored using PostgreSQL JSONB.

Benefits:

- Flexible schema evolution
- Simplified ingestion
- Efficient querying
- Supports heterogeneous data sources

---

## Async HTTP

External API calls use asynchronous HTTPX clients.

Advantages:

- Better scalability
- Non-blocking I/O
- Improved throughput

---

## Retry Mechanism

Network failures are inevitable when communicating with external systems.

The ingestion pipeline includes automatic retry logic for transient failures to improve resilience.

---

# Running Locally

Clone repository

```bash
git clone https://github.com/JayanthC6/generic-data-ingestion-service.git

cd generic-data-ingestion-service
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/ingestion_db
```

Run

```bash
uvicorn app.main:app --reload
```

---

# Docker

Build

```bash
docker compose up --build
```

Application

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

---

# Example Request

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

# Example Response

```json
{
    "status":"success",
    "total_sources":1,
    "results":[
        {
            "source":"jsonplaceholder",
            "records_ingested":100
        }
    ]
}
```

---

# Database Schema

Table

```
ingested_records
```

Columns

| Column | Description |
|---------|-------------|
| id | Primary Key |
| source | Data Source |
| payload | JSONB Payload |
| fetched_at | Timestamp |

---

# Testing

Run

```bash
pytest
```

Current tests verify

- FastAPI availability
- OpenAPI endpoint
- API initialization

---

# Engineering Trade-offs

During development, several design trade-offs were made intentionally.

- The current implementation focuses on REST APIs while keeping the architecture extensible for additional protocols in the future.
- PostgreSQL JSONB was selected instead of relational modeling to accommodate heterogeneous API payloads without frequent schema changes.
- Connector configurations were externalized into YAML files to reduce future onboarding effort while preserving flexibility.
- Retry support was implemented to improve reliability without introducing unnecessary complexity such as distributed queues or circuit breakers.

These decisions prioritize maintainability, extensibility, and clarity within the scope of a two-day engineering assignment.

---

# AI Usage

AI was used as an engineering assistant throughout development.

It assisted with:

- Architecture exploration
- Design pattern evaluation
- Documentation improvements
- Implementation review
- Debugging support

Every AI-generated suggestion was manually validated before integration.

One example where AI required correction involved Docker startup sequencing. An initial implementation assumed PostgreSQL would be immediately available after container startup, resulting in connection failures. Runtime log analysis exposed the issue, and the container startup workflow was refined until consistent initialization was achieved.

This project reflects manually verified engineering decisions rather than blindly generated code.

---

# Future Improvements

- Generic REST Connector
- GraphQL Connector
- OpenAPI-driven Connector Generation
- Incremental Synchronization
- Multiple Storage Destinations
- Structured Logging
- Metrics Dashboard
- Authentication Strategies
- Background Job Scheduling

---

# Why This Project?

This project was developed as a take-home engineering assignment to demonstrate:

- Software architecture fundamentals
- Extensible connector design
- Backend engineering practices
- Asynchronous programming
- Database integration
- Containerized deployment
- Production-oriented thinking

The focus was not only on implementing functionality, but also on making deliberate engineering decisions, documenting trade-offs, and designing a system that can evolve beyond the initial requirements.

---

# Author

**Jayanth C**

Master of Computer Applications (MCA)

Bangalore Institute of Technology

GitHub: https://github.com/JayanthC6

LinkedIn: https://linkedin.com/in/jayanthc18

---

## Final Thoughts

The goal of this project was not simply to ingest data from two APIs, but to design a maintainable ingestion framework that can be extended with additional sources while keeping the ingestion pipeline clean, reusable, and production-oriented.