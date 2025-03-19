from kafka import KafkaConsumer
import json

TOPIC_NAME = "test_topic"
BROKER = "kafka:9092"

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=[BROKER],
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest"
)

print("Kafka Consumer started...")

for message in consumer:
    print(f"Received: {message.value}")