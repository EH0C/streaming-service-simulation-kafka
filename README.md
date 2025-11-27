

# 🎬 Streaming Service Simulation with Apache Kafka

Real-time analytics using Kafka Producer, Consumer & Streamlit Dashboard

## 📌 Overview

This project simulates real-time user activity events in a streaming platform (like Netflix or Spotify) and processes them through Apache Kafka.
Events such as **play**, **pause**, **stop**, or **finish** are continuously produced and then consumed for **real-time monitoring and analytics**.

The Streamlit dashboard updates automatically without manual refresh, showing the most recent 10 events visually.

---

## 🛠️ Tech Stack

| Component                   | Purpose                      |
| --------------------------- | ---------------------------- |
| **Python**                  | Event producer + consumer    |
| **Apache Kafka**            | Event streaming backbone     |
| **Docker / Docker Compose** | Kafka environment            |
| **Streamlit**               | Real-time UI dashboard       |
| **JSON event messages**     | Standardized event structure |

---

## 📂 Project Structure

```
streaming-service-simulation-kafka/
│
├── compose.yml
├── producer.py
├── consumer.py
├── dashboard.py
└── README.md
```

---

## 📊 Example Event Message

```json
{
  "user_id": "123",
  "movie_id": "456",
  "action": "play",
  "timestamp": "1700000000"
}
```

---

## 🚀 How to Run

### 1️⃣ Start Kafka with Docker

```bash
docker compose up -d
```

### 2️⃣ Start Producer (generate simulated events)

```bash
python producer.py
```

### 3️⃣ Run Streamlit Dashboard (auto-refresh)

```bash
streamlit run dashboard.py
```

Dashboard will automatically update every 2 seconds without refresh.

---

## 📺 Dashboard Preview

* Real-time event table
* Live updates of latest 10 events
* Visual understanding of streaming service behavior

---

## 🎯 Learning Objectives

✔ Understand Kafka basics (producer, consumer, topics)
✔ Learn real-time analytics without databases
✔ Build dynamic visualization dashboards
✔ Simulate real streaming platforms like Netflix / Spotify

---

## 🔮 Future Enhancements

* Integrate Apache Flink for real-time aggregation
* Store events in PostgreSQL / ClickHouse / DuckDB
* Add charts (Top movies, Most active users, Event counts)

---

## 📖 Commands Cheatsheet

```bash
# List topics
kafka-topics --bootstrap-server localhost:9092 --list

# Consume topic from start
kafka-console-consumer --bootstrap-server localhost:9092 --topic demo-topic --from-beginning
```
