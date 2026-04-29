from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


def generate_numbers():
    return [1, 2, 3, 4, 5]


def calculate_sum(ti):
    numbers = ti.xcom_pull(task_ids="generate_numbers")
    return sum(numbers)


def print_result(ti):
    result = ti.xcom_pull(task_ids="calculate_sum")
    print(f"Final sum is: {result}")


with DAG(
    dag_id="sum_numbers_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args={"retries": 1, "retry_delay": timedelta(minutes=1)},
) as dag:
    t1 = PythonOperator(
        task_id="generate_numbers",
        python_callable=generate_numbers,
    )

    t2 = PythonOperator(
        task_id="calculate_sum",
        python_callable=calculate_sum,
    )

    t3 = PythonOperator(
        task_id="print_result",
        python_callable=print_result,
    )

    t1 >> t2 >> t3