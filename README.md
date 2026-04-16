# OmniSync Engine

OmniSync Engine is a high-performance, distributed order processing and inventory management system built with a microservices architecture. The project demonstrates modern backend patterns, including event-driven communication, asynchronous I/O, and containerized orchestration.

## 🚀 Key Features
- **Microservices Architecture:** Decoupled services for Order Management and Warehouse Operations.
- **Asynchronous Ingestion:** High-throughput order intake using **FastAPI** and **asyncio**.
- **Event-Driven Communication:** Real-time data synchronization between services via **Apache Kafka**.
- **Robust Messaging:** Implements the **at-least-once delivery** pattern with a focus on consumer idempotency.
- **Containerization:** Fully dockerized environment for seamless deployment and scaling.

## 🛠 Tech Stack
- **Language:** Python 3.10+
- **Frameworks:** FastAPI, (Django/DRF for Admin - coming soon)
- **Message Broker:** Apache Kafka (KRaft mode)
- **Library:** AIOKafka (Async Python client for Kafka)
- **Infrastructure:** Docker, Docker Compose

## 🏗 Architecture
1. **Order Service:** Validates incoming requests and produces events to the `orders` Kafka topic.
2. **Warehouse Service:** Consumes events, manages stock reservations, and simulates inventory logic.
3. **Kafka:** Acts as the central event bus for reliable inter-service communication.

## 🚦 Getting Started
To run the entire cluster locally, ensure you have Docker installed and execute:

```bash
docker-compose up --build
