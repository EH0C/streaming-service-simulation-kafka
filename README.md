
```markdown
# Streaming Service Simulation with Kafka 🎬

![Python](https://img.shields.io/badge/python-3.11-blue)
![Kafka](https://img.shields.io/badge/kafka-Confluent-orange)
![Docker](https://img.shields.io/badge/docker-yes-lightblue)

A **real-time streaming simulation** of a streaming service, built with **Kafka, Python, and Streamlit**.  
This project demonstrates how user activity (play, pause, like, stop) can be streamed, consumed, and visualized live.

---

## **Project Overview**

This dashboard simulates a **real-time analytics pipeline** like those used by Netflix or YouTube:

- Python Producer → Kafka Topic → Python Consumer → CSV → Streamlit Dashboard
- Real-time metrics and interactive charts
- Fully containerized using Docker Compose

---

## **Architecture**

```

[Python Producer] --> [Kafka Topic: user-activity] --> [Python Consumer] --> [CSV / Streamlit Dashboard]

````

---

## **Features**

- Simulates user actions: `play`, `pause`, `like`, `stop`
- Streams events to **Kafka topic** in real-time
- Python consumer stores events in a **rolling CSV**
- Interactive **Streamlit dashboard** shows:
  - Events over time
  - Top active users
  - Action distribution
  - Summary metrics
- Filters for users and actions
- Auto-refreshing dashboard (every 2 seconds)
- Fully Dockerized (Kafka + Zookeeper)

---

## **Getting Started**

### 1. Clone the Repo
```bash
git clone https://github.com/<your-username>/streaming-service-simulation-kafka.git
cd streaming-service-simulation-kafka
````

### 2. Start Kafka & Zookeeper

```bash
docker compose up -d
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Producer

```bash
python producer.py
```

### 5. Run Consumer

```bash
python consumer.py
```

### 6. Run Streamlit Dashboard

```bash
streamlit run app.py
```

* Open your browser at `http://localhost:8501/`
* Charts and metrics update automatically as new events are generated.

---

## **Portfolio Highlights**

* Real-time streaming architecture using **Kafka**
* Interactive **visualizations with Plotly**
* **Rolling window** for efficient streaming analytics
* Mimics **real-world streaming service dashboards**

---

## **Optional Enhancements**

* Replace CSV with in-memory database or Redis for production-ready streaming
* Add alert system for specific events (e.g., spikes or errors)
* Extend metrics: average session length, most watched movies, etc.
* Deploy on cloud for live demo

---

## **Repo Structure**

```
streaming-service-simulation-kafka/
│
├── docker-compose.yml        # Kafka + Zookeeper
├── producer.py               # Produces random user activity events
├── consumer.py               # Consumes events from Kafka and writes CSV
├── app.py                    # Streamlit dashboard
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── user_activity.csv         # Rolling CSV (ignored in Git)
```


