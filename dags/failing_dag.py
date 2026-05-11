from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


def fail_on_purpose():
    raise RuntimeError("Intentional failure for monitoring demo")


with DAG(
    dag_id="failing_dag",
    description="DAG that always fails — used to populate Loki errors and Prometheus failed_status metric",
    start_date=datetime(2026, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args={"retries": 0, "retry_delay": timedelta(seconds=5)},
    tags=["lab4", "demo"],
) as dag:
    PythonOperator(
        task_id="always_fails",
        python_callable=fail_on_purpose,
    )
