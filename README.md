# airflow-local

## 1. Build custom docker file
```bash
docker compose build
```

## 2. Initialize the DB
```bash
docker compose up airflow-init
```

## 3. Running Airflow
```bash
docker compose up -d
```

## Cleaning up
```bash
docker compose down --volumes --rmi all
```

---

### How to add Python packgaes?
Just add package name to the requirements.txt file

