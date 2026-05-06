# **ITMO DevOps Lab 1: Apache Airflow Pipeline.**

## **Этот проект:**

 - разворачивает локальный Airflow‑кластер с помощью Docker Compose,

 - создаёт кастомный Docker‑образ Airflow,

 - инициализирует Airflow и создаёт пользователя,

 - запускает простой DAG sum_numbers_dag, который:

   - генерирует список чисел,

   - вычисляет сумму,

   - выводит результат в логах.

## **Архитектура проекта:**

```text
itmo-devops-lab1-airflow/
│
├── dags/                     # DAG с тремя Python задачами
│   └── my_first_dag.py
│
├── Dockerfile                # Кастомный образ Airflow
├── docker-compose.yml        # Оркестрация Airflow + Postgres
├── README.md                 # Документация проекта
└── CHANGES.md                # История изменений (опционально)
```

## **Используемые технологии:**

 - Apache Airflow 2.7+

 - Python 3.8

 - Docker & Docker Compose

 - PostgreSQL 13

 - LocalExecutor.

## **Как задеплоить сервис локально:**

1. Клонировать репозиторий:
```
git clone https://github.com/OlMiore/itmo-devops-lab1-airflow.git
cd itmo-devops-lab1-airflow
```
2. Собрать Docker‑образ:
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

6. Включить и запустить DAG sum_numbers_dag в интерфейсе Airflow.

## **DAG: sum_numbers_dag:**

DAG состоит из трёх задач:

 - generate_numbers — создаёт список чисел,

 - calculate_sum — считает сумму,

 - print_result — выводит результат в лог.
Пример результата в логах: Final sum is: 15.

## **Скриншоты:**

<img width="925" height="254" alt="image" src="https://github.com/user-attachments/assets/1da5448f-1276-4376-aa5b-8336e55bb293" />


<img width="926" height="502" alt="image" src="https://github.com/user-attachments/assets/a9dca8f9-5281-43cd-98f8-b9aad87a6d12" />


<img width="921" height="500" alt="image" src="https://github.com/user-attachments/assets/d77e1698-1b5b-4d91-a0c4-d0a2586c8717" />


## **Проблемы и решения:**

Была Ошибка 403 при просмотре логов.

Решение: добавление единого AIRFLOW__WEBSERVER__SECRET_KEY во все сервисы.





fix pipeline



# **ITMO DevOps Lab 3: GitLab CI/CD**

## Описание
В рамках лабораторной работы был настроен CI / CD pipeline в GitLab

## Что сделано
- Поднят и настроен GitLab Runner (Docker executor)
- Добавлен `.gitlab-ci.yml`
- Реализованы стадии:
  - `test` – проверка структуры проекта (наличие папок `dags/`, `spark/`)
  - `build` – сборка Docker-образа
  - `deploy` – деплой приложения через docker-compose
- Настроены правила выполнения:
  - `test` выполняется всегда
  - `build` не выполняется автоматически для веток `feature/*`
  - `deploy` выполняется только для `main`, `master`, `develop`

## Особенности
- Используется tagged runner: `devops-lab-runner`
- Добавлена очистка окружения перед деплоем (`docker-compose down`)
- Исправлены проблемы:
  - доступ к Docker API
  - конфликт порта 8080

## Результат
Pipeline успешно выполняется:

- https://gitlab.com/aspnmrv/itmo-devops-labs/-/pipelines/2502089765
- https://gitlab.com/aspnmrv/itmo-devops-labs

## Скриншот

![img.png](img.png)
