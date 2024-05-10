# soil-compaction
Это приложения для учета измерений плотномера и формирования протокола испытаний.

Возможности приложения: 
- учет испытаний по уплотнению грунта
- формирование протокола испытаний
- контроль выставления счетов заказчикам

## Environment Variables
Чтобы запустить этот проект, вам нужно добавить следующие переменные окружения в файл .env

`DJANGO_SECRET='django-secret-key'`

`DEBUG=False`

`ALLOWED_HOSTS=<ip>`

`DJANGO_LOG_LEVEL=WARNING`

`DB_ENGINE=django.db.backends.postgresql`

`POSTGRES_DB=dbname`

`POSTGRES_USER=dbuser`

`POSTGRES_PASSWORD=password`

`DB_HOST=db`

`DB_PORT=5432`

`CELERY_BROKER_URL=redis://redis:6379/0`

## Deployment

Клонируй проект

```bash
  git clone git@github.com:Stryukov/soil-compaction.git
```
Переходи в каталог проекта, собери и запусти контейнеры

```bash
  docker compose up --build
```

## Tech Stack

**Client:** Django Admin

**Server:** Django, Celery, Redis, Postgres, Nginx, Docker, python-docx-template


## Authors

- [@stryukov](https://www.github.com/stryukov)