# **ITMO DevOps Lab 2: Apache Airflow + Spark Pipeline.**

## **Этот проект:**

 - разворачивает локальный Airflow-кластер с помощью Docker Compose,

 - поднимает Apache Spark master и worker,

 - создаёт кастомный Docker-образ Airflow с Java, PySpark и Spark provider,

 - инициализирует Airflow, создаёт пользователя и подключение `spark_local`,

 - сохраняет DAG первой лабораторной `sum_numbers_dag`,

 - добавляет новый DAG `spark_sum_numbers_dag`, который запускает PySpark job через Spark.

## **Что делает Spark DAG:**

`spark_sum_numbers_dag` запускает файл `spark/sum_numbers_job.py` через `SparkSubmitOperator`.

Spark job:

 - создаёт `SparkSession`,

 - подключается к master-ноду `spark://spark-master:7077`,

 - создаёт DataFrame со списком чисел,

 - считает сумму средствами PySpark,

 - выводит результат `Final Spark sum is: 15` в логах.

## **Архитектура проекта:**

```text
itmo-devops-labs/
│
├── dags/
│   ├── my_first_dag.py             # DAG первой лабораторной
│   └── spark_sum_numbers_dag.py    # DAG второй лабораторной
│
├── spark/
│   └── sum_numbers_job.py          # PySpark job
│
├── Dockerfile                      # Кастомный образ Airflow
├── docker-compose.yml              # Airflow + Postgres + Spark
├── README.md                       # Документация проекта
└── CHANGES.md                      # История изменений
```

## **Используемые технологии:**

 - Apache Airflow 2.7.1

 - Apache Spark 3.5.0

 - PySpark 3.5.0

 - PostgreSQL 13

 - LocalExecutor

## **Как задеплоить сервис локально:**

1. Клонировать репозиторий:
```
git clone https://github.com/OlMiore/Itmo-devops-labs.git
cd Itmo-devops-labs
git checkout lab2
```

2. Собрать Docker-образ:

```
docker-compose build
```

3. Инициализировать Airflow (миграции БД + создание пользователя):

```
docker-compose up airflow-init
```

4. Запустить все сервисы:

```
docker-compose up -d
```

5. Открыть Airflow UI:

```
http://localhost:8080
```

Логин: airflow  
Пароль: airflow

6. Открыть Spark UI:

```
http://localhost:4040
```

7. Включить и запустить DAG `spark_sum_numbers_dag` в интерфейсе Airflow.

После успешного запуска в Spark UI должен быть виден worker и выполненное Spark-приложение.

## **Airflow Connection для Spark:**

При запуске `airflow-init` подключение создаётся автоматически:

 - Conn Id: `spark_local`

 - Conn Type: `Spark`

 - Host: `spark://spark-master`

 - Port: `7077`

Если нужно создать подключение вручную, откройте Airflow UI: Admin → Connections → + New.

## **DAG: sum_numbers_dag:**

Это DAG из первой лабораторной. Он состоит из трёх задач:

 - generate_numbers — создаёт список чисел,

 - calculate_sum — считает сумму,

 - print_result — выводит результат в лог.
Пример результата в логах: Final sum is: 15.

## **DAG: spark_sum_numbers_dag:**

Этот DAG состоит из одной задачи `spark_sum_numbers`, которая отправляет `spark/sum_numbers_job.py` в Spark-кластер через `SparkSubmitOperator`.





