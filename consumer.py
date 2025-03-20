from kafka import KafkaConsumer
import json
import logging

TOPIC_NAME = "test_topic"
BROKER = "kafka:9092"

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger()

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=[BROKER],
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True
)

logger.info("Kafka Consumer started...")

for message in consumer:
    logger.info(f"INFO: Received: {message.value}")