# CHANGES

## Lab 3 – GitLab CI/CD

- Репозиторий на Gitlab: `https://gitlab.com/aspnmrv/itmo-devops-labs`
- Успешный pipeline: `https://gitlab.com/aspnmrv/itmo-devops-labs/-/pipelines/2502089765`

### Added
- Добавили файл `.gitlab-ci.yml` для настройки CI/CD пайплайна
- Добавили stage `test` перед этапом сборки
- Реализовали проверку наличия директорий `dags/` и `spark/`
- Настроили GitLab Runner через Docker

### Changed
- Обновлен процесс деплоя: добавлена очистка старых контейнеров перед запуском (`docker-compose down`)
- Настроено подключение Docker через `DOCKER_HOST`
- Добавлены правила выполнения пайплайна:
  - deploy выполняется только для веток `main`, `master`, `develop`
  - build не выполняется автоматически для веток `feature/*`
  - test выполняется всегда

### Fixed
- Исправлена ошибка доступа к Docker API в CI
- Исправлен конфликт порта `8080` при деплое

### Notes
- Все этапы пайплайна (test, build, deploy) успешно выполняются
- Пайплайн запускается на tagged runner `devops-lab-runner`