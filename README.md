# airflow-local
This is a quck-start project for easily customizing Airflow

- How to add Python packgaes? Simply include package name in the `requirements.txt` file.
- By default, Use 2 Workers with Celery executor. if you have insufficient memory, comment out `airflow-worker-2` in the `docker-compose.yaml` file.
- Basically, updates the DAG directory every 30 seconds.
- Default Timezone is Asia/Seoul.
- How to choose Python and Airflow versions? Adjust the arguments in the `Dockerfile`. (The current Python version is 3.10, and Airflow version is 2.7.0.)

---
# Prerequisite
- [Docker](https://www.docker.com/products/docker-desktop/)

# How to run?

## 1. Clone repository

## 2. Build custom docker file
```bash
docker compose build
```

## 3. Initialize the DB
```bash
docker compose up airflow-init
```

## 4. Start Airflow
```bash
docker compose up -d
```
- Airflow Web Server: http://localhost:8080
- Flower(Worker monitoring tool): http://localhost:5555

## Cleaning up
```bash
docker compose down --volumes --rmi all
```

