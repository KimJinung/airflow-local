import json
import pendulum
from tasks.demo import Demo

from airflow.decorators import dag, task


KST = pendulum.timezone("Asia/Seoul")


@dag(
    dag_id="demo",
    description="Demo dag",
    start_date=pendulum.datetime(2021, 1, 1, tz=KST),
    schedule="* * * * *",
    catchup=False
)
def demo_taskflow_api():
    @task(task_id="extract")
    def extract():
        response = Demo.get_data()

        return json.loads(response)

    @task(task_id="transform", multiple_outputs=True)
    def transform(order_data_dict: dict):
        total_order_value = 0

        for v in order_data_dict.values():
            total_order_value += v

        return {"total_order_value": total_order_value}

    @task(task_id="load")
    def load(total_order_value: float):
        print(f"Total order value is: {total_order_value:.2f}")

    order_data = extract()
    order_summary = transform(order_data)
    load(order_summary["total_order_value"])


demo_taskflow_api()
