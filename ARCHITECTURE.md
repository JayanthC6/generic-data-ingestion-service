# Architecture & Engineering Decisions

## Introduction

The objective of this project was not simply to ingest data from two REST APIs, but to design a reusable ingestion framework that could evolve into a production-ready platform.

While the assignment could have been completed with a straightforward implementation, I intentionally focused on extensibility, maintainability, and separation of concerns.

This document explains the architectural decisions, trade-offs, and future evolution of the system.

---

# System Overview

The application follows a layered architecture where each layer has a single responsibility.

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
         ┌─────────┴─────────┐
         ▼                   ▼
 JSONPlaceholder      RandomUser
      Connector         Connector
         │                   │
         └─────────┬─────────┘
                   ▼
            HTTPX Async Client
                   ▼
          Response Normalization
                   ▼
        PostgreSQL Storage (JSONB)
```

The ingestion service never directly communicates with external APIs. Instead, it delegates that responsibility to connectors created through the factory.

---

# Design Principles

The implementation follows several software engineering principles.

## Separation of Concerns

Each layer has a clearly defined responsibility.

- API layer handles HTTP requests.
- Service layer coordinates ingestion.
- Connectors interact with external APIs.
- Storage layer manages persistence.
- Database layer defines models.
- Utility layer provides reusable functionality.

This separation makes the application easier to maintain and extend.

---

## Open/Closed Principle

The ingestion service remains unchanged when introducing new connectors.

Only the connector implementation and factory registration require modification.

This minimizes the impact of future changes.

---

## Single Responsibility Principle

Every component performs one well-defined task.

Examples:

- Connector → Retrieve and normalize data.
- Service → Coordinate ingestion workflow.
- Storage → Persist records.
- Retry Utility → Handle transient failures.

This keeps components small, testable, and reusable.

---

# Why Factory Pattern?

Instead of creating connectors directly inside the service layer, the application uses a Factory Pattern.

Benefits:

- Centralized connector creation.
- Simplified dependency management.
- Easy addition of future connectors.
- Business logic remains independent of connector implementation.

Without the factory, the service would require conditional logic every time a new connector was added.

---

# Why Connector Pattern?

External APIs differ significantly.

Each API may expose:

- Different response structures
- Different authentication methods
- Different pagination styles
- Different endpoints

Encapsulating these differences inside connectors prevents API-specific logic from leaking into the ingestion pipeline.

---

# Why PostgreSQL JSONB?

External APIs rarely return identical schemas.

Rather than designing separate relational tables for every API, the project stores normalized payloads using PostgreSQL JSONB.

Advantages:

- Flexible schema
- Supports heterogeneous payloads
- Simplifies onboarding of new APIs
- Future indexing support

This design favors adaptability over premature normalization.

---

# Why Async HTTP?

The application uses HTTPX with asynchronous requests.

Advantages include:

- Non-blocking I/O
- Better scalability
- Efficient handling of external API latency
- Suitable for future concurrent ingestion

Although only two connectors are implemented, asynchronous communication provides a strong foundation for future expansion.

---

# Retry Strategy

External APIs are inherently unreliable.

Temporary failures such as network interruptions or rate limiting should not immediately fail an ingestion job.

A retry utility with exponential backoff was implemented to improve resilience.

This provides a simple yet effective reliability mechanism without introducing unnecessary complexity.

---

# Configuration-Driven Direction

As an architectural improvement, connector definitions were externalized into YAML configuration files.

Current configuration includes:

- jsonplaceholder.yaml
- randomuser.yaml

This demonstrates the intended evolution toward configuration-driven onboarding where new REST APIs can be introduced with minimal code changes.

Although the current implementation still uses dedicated connector classes, the configuration layer establishes a clear path toward a fully generic ingestion engine.

---

# Engineering Trade-offs

This assignment intentionally balances engineering quality with implementation scope.

Several capabilities were intentionally deferred.

## GraphQL Support

The current implementation focuses exclusively on REST APIs.

The connector architecture allows GraphQL support to be introduced without changing the ingestion pipeline.

---

## Incremental Synchronization

The project currently performs complete retrieval for supported APIs.

Future work could introduce:

- ETag support
- Last-Modified headers
- Cursor persistence
- Delta synchronization

---

## Scheduling

Automatic scheduling was intentionally excluded.

In a production system, ingestion would typically be triggered through:

- APScheduler
- Celery
- Cron Jobs
- Kubernetes CronJobs

---

## Multiple Storage Destinations

Only PostgreSQL persistence was implemented.

Future storage adapters could include:

- Amazon S3
- Kafka
- Elasticsearch
- Parquet Files

without changing connector implementations.

---

# AI Usage

Artificial Intelligence was used as an engineering assistant throughout development.

It contributed to:

- Architecture exploration
- Design pattern evaluation
- Documentation refinement
- Code review
- Debugging support

Every generated suggestion was manually reviewed, validated, and tested before integration.

One example where AI guidance required correction involved Docker startup sequencing. The initial suggestion assumed PostgreSQL would be immediately available after container startup, which resulted in connection failures. Runtime log analysis exposed the issue, and the startup workflow was refined until reliable initialization was achieved.

The final implementation reflects manually verified engineering decisions rather than blindly accepted AI-generated code.

---

# Future Evolution

The current architecture naturally supports future enhancements such as:

- Generic REST Connector
- GraphQL Connector
- OpenAPI-driven Connector Generation
- Authentication Strategies
- Dynamic Pagination Strategies
- Incremental Synchronization
- Structured Logging
- Metrics Dashboard
- Health Monitoring
- Background Scheduling

These enhancements can be introduced incrementally while preserving the existing architecture.

---

# Conclusion

The objective of this project was not merely to satisfy functional requirements, but to demonstrate sound software engineering practices.

The design prioritizes:

- Maintainability
- Extensibility
- Separation of concerns
- Clean architecture
- Production-oriented thinking

The resulting system serves as a foundation for a reusable data ingestion platform rather than a one-off API integration.