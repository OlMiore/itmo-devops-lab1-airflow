# CHANGES

## Lab 4 – Loki + Prometheus + Grafana

### Added
- Сервис **Loki** (`grafana/loki:3.2.0`) в `docker-compose.yml` для хранения логов на порту 3100.
- Сервис **Alloy** (`grafana/alloy:v1.5.1`) в `docker-compose.yml` для сбора логов Airflow через volume `./logs:/opt/logs`.
- Сервис **Prometheus** (`prom/prometheus:v2.48.1`) в `docker-compose.yml` на порту 9090.
- Сервис **Grafana** (`grafana/grafana:11.2.0`) в `docker-compose.yml` на порту 3000 с анонимным доступом и правами Admin.
- Volume `grafana-data` для сохранения датасорсов и дашбордов между рестартами.
- Файл `alloy.conf` с конфигом сбора логов Airflow по маске `/opt/logs/dag_id=*/run_id=*/task_id=*/*.log` и форвардингом в Loki.
- Файл `prometheus.yml` с тремя scrape-job'ами: `airflow`, `spark-master`, `spark-worker`.
- Файл `spark/metrics.properties` со встроенным `PrometheusServlet` Spark.
- Монтирование `spark/metrics.properties` в `/opt/spark/conf/metrics.properties` для `spark-master` и `spark-worker`.
- Проброс порта 8081 у `spark-worker` для доступа к Worker UI и метрикам.
- DAG `failing_dag` (`dags/failing_dag.py`) — специально падающий DAG для генерации ERROR-логов и метрики `airflow_dag_status{status="failed"}`.

### Changed
- В `Dockerfile` добавлен пакет `airflow-exporter==1.5.3` — плагин Airflow, публикующий метрики в формате Prometheus на эндпоинте `/admin/metrics/`.
- В `spark-master` и `spark-worker` добавлена переменная окружения `SPARK_DAEMON_JAVA_OPTS=-Dspark.metrics.conf=/opt/spark/conf/metrics.properties` — Spark не находит файл метрик автоматически, требуется явный JVM-флаг.

### Fixed
- В `prometheus.yml` для Spark `metrics_path` указан с trailing slash (`/metrics/master/prometheus/` и `/metrics/prometheus/`) — без него Spark возвращает 302 редирект, который Prometheus по умолчанию не следует.

### Notes
- Стек разворачивается одной командой `docker-compose up -d` после `build` и `up airflow-init`.
- Подключение Data sources в Grafana и создание дашборда выполняется руками через UI согласно методичке.
- Дашборд содержит две плитки: Logs (Loki) с запросом `{job="airflow_logs"} |= "ERROR"` и Time series (Prometheus) с запросом `airflow_dag_status{status="failed"}`.

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
