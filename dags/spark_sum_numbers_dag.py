from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}


with DAG(
    dag_id="spark_sum_numbers_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args=default_args,
) as dag:
    spark_sum_numbers = SparkSubmitOperator(
        task_id="spark_sum_numbers",
        application="/opt/airflow/spark/sum_numbers_job.py",
        name="spark_sum_numbers_job",
        conn_id="spark_local",
    )
