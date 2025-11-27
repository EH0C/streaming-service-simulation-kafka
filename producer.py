from confluent_kafka import Producer
import json, time, random

producer = Producer({'bootstrap.servers': 'localhost:9092'})
topic = 'user-activity'

actions = ['play', 'pause', 'like', 'stop']

def generate_event():
    return {
        "user_id": str(random.randint(100, 200)),
        "movie_id": str(random.randint(1, 50)),
        "action": random.choice(actions),
        "timestamp": int(time.time())
    }

while True:
    event = generate_event()
    producer.produce(topic, key=event['user_id'], value=json.dumps(event))
    print("Produced:", event)
    producer.flush()
    time.sleep(1)
