# Kafka Pub/Sub System

## Introduction
This project is a simple Kafka Publish/Subscribe (Pub/Sub) system, consisting of a data producer (Producer) and a data consumer (Consumer) that communicate through Kafka.

## Architecture
```
+------------+        +----------+        +------------+
|  Producer  | --->   |  Kafka   | --->   |  Consumer  |
+------------+        +----------+        +------------+
```
- **Producer**: Publishes messages to a Kafka topic.
- **Kafka**: Acts as a message broker, managing topics and message transmission.
- **Consumer**: Subscribes to a Kafka topic, receives, and processes messages.

## Tech Stack
- **Kafka**: Message broker
- **Docker**: Containerization of Kafka, Producer, and Consumer
- **Python**: Used to implement Producer and Consumer
- **kafka-python**: Kafka client library for Python

## Prerequisites
- Docker & Docker Compose
- Python 3.9 or later

## Quick Start

### 1. Start Kafka Services
Start Kafka and Zookeeper using `docker-compose.yml`:
```sh
docker-compose up -d
```

### 2. Start Producer and Consumer
Build and run the Producer and Consumer containers:
```sh
docker-compose up --build
```

### 3. Check Logs
Check if the Producer is sending data correctly:
```sh
docker logs -f producer
```
Check if the Consumer is receiving data correctly:
```sh
docker logs -f consumer
```

## Project Structure
```
├── consumer
│   ├── consumer.py     # Kafka Consumer script
│   ├── Dockerfile      # Dockerfile for Consumer
│   ├── requirements.txt # Dependencies for Consumer
│
├── producer
│   ├── producer.py     # Kafka Producer script
│   ├── Dockerfile      # Dockerfile for Producer
│   ├── requirements.txt # Dependencies for Producer
│
├── docker-compose.yml  # Docker Compose configuration file
└── README.md           # Project documentation
```

