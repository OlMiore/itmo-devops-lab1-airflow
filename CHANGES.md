# Changes

## Lab 2

- Added Spark master and Spark worker services to `docker-compose.yml`.
- Added `spark/` volume mounts for Airflow services.
- Updated `Dockerfile` to install `procps`, `default-jre`, `apache-airflow-providers-apache-spark==4.1.1`, and `pyspark==3.5.0`.
- Added Airflow DAG `spark_sum_numbers_dag` that runs a Spark job with `SparkSubmitOperator`.
- Added PySpark job `spark/sum_numbers_job.py` that uses `SparkSession` and calculates the sum of numbers.
- Added automatic creation of Airflow connection `spark_local`.

## Lab 1

- Initial Airflow + Docker Compose setup.
- Added `sum_numbers_dag` with generate, calculate, and print tasks.
