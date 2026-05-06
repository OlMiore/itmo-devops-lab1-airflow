# **ITMO DevOps Lab 3: GitLab CI/CD.**

## Описание.
В рамках лабораторной работы был настроен CI / CD pipeline в GitLab, обеспечивающий автоматическую проверку, сборку и деплой проекта.

## Архитектура проекта.

```
itmo-devops-labs/
│
├── spark/                   # Spark-приложение
│
├── .gitlab-ci.yml           # CI/CD pipeline
├── CHANGES.md               # История изменений по ЛР3
└── README.md                # Документация проекта
```

## Используемые технологии:

 - GitLab CI/CD,

 - GitLab Runner (Docker executor),

 - Docker & Docker Compose,

 - Python / Spark,

 - Linux окружение.

## Что сделано.

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

## Особенности.

- Используется tagged runner: `devops-lab-runner`
- Добавлена очистка окружения перед деплоем (`docker-compose down`)
- Исправлены проблемы:
  - доступ к Docker API
  - конфликт порта 8080

## CHANGES.md.

Внесены следующие изменения:
 - добавлен .gitlab-ci.yml,
 - добавлены стадии `test`, `build`, `deploy`,
 - добавлены правила выполнения (rules),
 - настроен tagged runner `devops-lab-runner`,
 - добавлена очистка окружения перед деплоем,
 - исправлены ошибки доступа к Docker API и конфликт порта.

## Результат.

Pipeline успешно выполняется:

- https://gitlab.com/aspnmrv/itmo-devops-labs/-/pipelines/2502089765
- https://gitlab.com/aspnmrv/itmo-devops-labs

## Скриншот выполнения пайплайна.

<img width="1280" height="534" alt="Скриншот выполнения пайплайна" src="https://github.com/user-attachments/assets/ef830d91-ebf7-41ed-8e52-b0aa87f9e7d4" />
