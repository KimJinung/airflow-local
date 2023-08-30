# airflow-local
This is a quck-start project for easily customizing Airflow

- Use 2 Workers with Celery executor. if you have insufficient memory, comment out `airflow-worker-2` in the `docker-compose.yaml` file.
- Basically, updates the DAG directory every 30 seconds.
- Default Timezone is Asia/Seoul.
- How to add Python packgaes? Just add package name to the requirements.txt file.

---

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

## Cleaning up
```bash
docker compose down --volumes --rmi all
```

