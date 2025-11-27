from confluent_kafka import Consumer
import json, csv

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'activity-group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['user-activity'])

csv_file = 'user_activity.csv'
with open(csv_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['user_id', 'movie_id', 'action', 'timestamp'])
    writer.writeheader()

    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error:", msg.error())
            continue

        event = json.loads(msg.value().decode('utf-8'))
        print("Consumed:", event)
        writer.writerow(event)
        f.flush()  # persist immediately
