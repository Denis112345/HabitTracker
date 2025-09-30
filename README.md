# HabbitTracker

## Общая информация

**HabbitTracker** — это серверная часть приложения для отслеживания привычек.
Приложение предоставляет REST API для взаимодействия с клиентской частью и имеет авто-генерируемую документацию в **Swagger UI**.

---

## Архитектура и подход

### Основной подход

**Namespaces + Application Factory + MVC**

* **Application Factory**
  Позволяет создавать экземпляр Flask-приложения с конфигурацией и подключением всех расширений (SQLAlchemy, Flask-RESTX, др.).

* **Namespaces (Flask-RESTX)**
  Используются вместо Blueprints для структурирования API по модулям. Каждый модуль (например, пользователи, привычки) имеет свой namespace с маршрутизацией и документацией.

* **MVC-подход**

  * **Models (`models/`)** — работа с базой данных (SQLAlchemy)
  * **Controllers (`controllers/`)** — обработка запросов, бизнес-логика и подключение namespace
  * **Schemas (`schemas/`)** — описание данных для Swagger и валидации

---

## Документация API

Swagger UI доступен по адресу:

```
http://<host>:<port>/docs
```

Документация отображает все namespace, модели и поля, которые можно заполнять через JSON body или form-data (в зависимости от конфигурации).

---

## Пример структуры проекта

```
HabbitTracker/
├─ app.py                  # Application Factory
├─ config.py               # Flask configuration
├─ modules/
│  ├─ User/
│  │  ├─ __init__.py
│  │  ├─ models.py          # SQLAlchemy models
│  │  ├─ routes.py          # Flask-RESTX routes
│  │  ├─ schemas.py         # Swagger and TypedDict schemas
│  │  ├─ services.py         # Полезные функции для работы с пользователями
│  │  └─ reqparsers_restx.py    # RequestParser for form-data
│  ├─ Habit/
│  │  ├─ __init__.py
│  │  ├─ models.py          # SQLAlchemy models
│  │  ├─ routes.py          # Flask-RESTX routes
│  │  ├─ schemas.py         # Swagger and TypedDict schemas
│  │  ├─ services.py         # Полезные функции для работы с habit
│  │  └─ reqparsers_restx.py    # RequestParser for form-data
│  └─ extensions.py         # db, api, other extensions
├─ requirements.txt
└─ README.md
```
