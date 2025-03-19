from kafka import KafkaProducer
import json
import time

TOPIC_NAME = "test_topic"
BROKER = "kafka:9092"

producer = KafkaProducer(
    bootstrap_servers=[BROKER],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Kafka Producer started...")

count = 0
while True:
    data = {"message": f"Hello Kafka {count}"}
    producer.send(TOPIC_NAME, value=data)
    print(f"Sent: {data}")
    count += 1
    time.sleep(2)
