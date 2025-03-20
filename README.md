# Kafka Pub/Sub System in Python

## Overview
This project implements a simple Kafka-based Pub/Sub system using Python. The system consists of:

- Data Producer: Generates sample data and publishes it to a Kafka topic.
- Data Consumer: Subscribes to the Kafka topic and processes/display the received data.
- Kafka with Docker: Kafka is containerized using Docker to simplify deployment.
- Containerized Applications: Kafka, along with both the producer and consumer, are containerized for easy execution.

## Technologies Used
- Kafka (via Docker)
- Python
- Kafka-Python (for Kafka interaction)
- Docker & Docker Compose

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/zoe-yeh/Kafka-Pub-Sub-System-in-Python.git
cd kafka-pubsub-python
```

### 2. Start Kafka with Docker Compose
Ensure Docker is installed, then run:
```bash
docker-compose up -d
```
This starts Kafka and Zookeeper as needed.

### 3. Build and Run the Producer & Consumer
#### Producer
```bash
docker build -t kafka-producer -f producer.Dockerfile .
docker run --network=host kafka-producer
```
#### Consumer
```bash
docker build -t kafka-consumer -f consumer.Dockerfile .
docker run --network=host kafka-consumer
```

## Architecture
```
+--------------+      +----------+      +--------------+
| Data Producer| ---> |  Kafka   | ---> | Data Consumer|
+--------------+      +----------+      +--------------+
```
- Producer: Publishes messages to a Kafka topic.
- Kafka: Manages message distribution.
- Consumer: Listens to the topic and processes messages.