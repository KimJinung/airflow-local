ARG PYTHON_VERSION=3.10
ARG AIRFLOW_VERSION=2.7.0

FROM apache/airflow:$AIRFLOW_VERSION-python$PYTHON_VERSION

COPY requirements.txt .

RUN pip install -r requirements.txt
