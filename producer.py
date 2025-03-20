from kafka import KafkaProducer
import json
import time
import logging

TOPIC_NAME = "test_topic"
BROKER = "kafka:9092"

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger()

producer = KafkaProducer(
    bootstrap_servers=[BROKER],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

logger.info("Kafka Producer started...")

count = 0
while True:
    data = {"message": f"Hello Kafka {count}"}
    producer.send(TOPIC_NAME, value=data)
    logger.info(f"INFO: Sent: {data}")
    count += 1
    time.sleep(2)
