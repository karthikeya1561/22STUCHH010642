URL Shortener System Design Document

## 1. Introduction

This document outlines the architectural and code design choices for a URL Shortener application. The primary goal is to create a scalable, maintainable, and robust system capable of generating short URLs and redirecting users to original long URLs efficiently.

## 2. Architectural Design

The system employs a monolithic architecture for its initial phase, structured into distinct layers to ensure clear separation of concerns and ease of development. This approach is suitable for a project of this scope, allowing for rapid iteration while maintaining a clear pathway for future microservices decomposition if scalability demands increase significantly.

**Key Architectural Decisions:**

- **Layered Architecture:**
  - **Presentation Layer (API Endpoints):** Handles HTTP requests, input validation, and marshaling responses. Uses FastAPI for rapid API development.
  - **Business Logic Layer (CRUD Operations):** Contains the core logic for URL shortening, storage, retrieval, and deletion.
  - **Data Access Layer (Models & Database Interaction):** Manages interaction with the database using SQLAlchemy ORM.
- **API-First Design:** All interactions with the backend are exposed via well-defined RESTful API endpoints, ensuring clear contracts for client-side applications.
- **Dependency Injection:** FastAPI's dependency injection system is utilized to manage database sessions, promoting testability and modularity.

## 3. Code Design

**Key Code Design Principles:**

- **SOLID Principles:** Applied to ensure code is maintainable, extensible, and robust.
- **Modularity:** Code is organized into logical modules (`api/endpoints`, `crud`, `models`, `schemas`, `core/database`, `middleware`) to enhance readability and separation of responsibilities.
- **Clean Code Practices:** Emphasis on meaningful variable and function names, consistent formatting, and clear function signatures.
- **Error Handling:** Explicit use of FastAPI's `HTTPException` for API error responses, providing clear feedback to clients.
- **Short URL Generation:** A dedicated function handles the generation of short URL codes, ensuring uniqueness (though a more robust collision handling mechanism would be needed for production at scale).

## 4. Data Modeling

The system's core data model revolves around storing the mapping between original and shortened URLs.

**Entity:** URL

| Field        | Data Type | Constraints                          | Description                                   |
| ------------ | --------- | ------------------------------------ | --------------------------------------------- |
| id           | Integer   | Primary Key, Auto-increment, Indexed | Unique identifier for each URL mapping        |
| original_url | String    | Not Null                             | The full, original URL                        |
| short_url    | String    | Unique, Not Null, Indexed            | The generated short URL code. Must be unique  |
| created_at   | DateTime  | Default: Current UTC Timestamp       | Timestamp of when the URL mapping was created |

- **Relationships:** No explicit relationships with other entities are present in this simplified model.
- **Data Storage Strategy:**
  - **Normalization:** The model is normalized to avoid redundancy.
  - **Indexing:** `id` and `short_url` are indexed to facilitate fast lookups for retrieval and redirection.

## 5. Technology Selections & Justifications

- **Backend Framework:** FastAPI (Python)
  - High performance, asynchronous capabilities, automatic interactive API documentation, and strong type hints.
- **Web Server:** Uvicorn
  - ASGI server, highly performant and designed for asynchronous Python web applications.
- **ORM:** SQLAlchemy
  - Powerful and flexible ORM for Python, supporting various database backends.
- **Data Validation/Serialization:** Pydantic
  - Robust data validation and serialization/deserialization using Python type hints.
- **Database:** SQLite (for development/simple deployment)
  - Lightweight, file-based database, excellent for rapid prototyping and local development.
- **CORS Middleware:** FastAPI's CORSMiddleware
  - Essential for allowing cross-origin requests from a frontend application.
- **Hashing for Short URLs:** hashlib (Python standard library)
  - Provides cryptographic hashing functions for generating unique short codes.

## 6. Assumptions Made

- **Database Choice:** Assumed SQLite for initial development simplicity. For production, a more robust database like PostgreSQL or MySQL would be used.
- **Short URL Collision Handling:** The current short URL generation is basic. For a production system, a more sophisticated collision detection and retry mechanism would be required.
- **Scalability:** The current monolithic design is assumed to be sufficient for initial traffic. Horizontal scaling might involve containerization and load balancing.
- **Security:** Standard web security practices are assumed to be implemented as the project evolves.
- **Logging:** Basic request logging middleware is included for operational visibility.
- **No User Authentication:** The current system does not include user authentication or authorization. All operations are publicly accessible.
