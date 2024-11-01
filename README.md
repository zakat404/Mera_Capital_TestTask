# Deribit Client Project

## Описание

Данный проект реализует асинхронный клиент для криптобиржи Deribit, который каждые минуту получает текущие цены `btc_usd` и `eth_usd`, сохраняет их в базу данных, а также предоставляет API на FastAPI для работы с этими данными.

## Функциональность

- **Асинхронный клиент на aiohttp**: Получает текущие цены валют каждые 60 секунд.
- **Сохранение данных**: Тикер валюты, текущая цена и время в UNIX timestamp сохраняются в базу данных.
- **API на FastAPI**:
  - Получение всех сохраненных данных по указанной валюте.
  - Получение последней цены валюты.
  - Получение цены валюты с фильтром по дате.

## Технологии

- Python 3.10
- FastAPI
- aiohttp
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose
- GitHub Actions
- Pytest
- Pydantic
- Uvicorn

## Установка и запуск

### **Требования**

- Docker
- Docker Compose

### **Шаги**

1. **Клонируйте репозиторий**

   ```bash
   git clone https://github.com/yourusername/deribit_client_project.git
   cd deribit_client_project
Создайте файл .env

**Создайте файл .env в корневой директории проекта и добавьте следующие переменные окружения:**
````
DB_HOST=db
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=user_db
DB_NAME=deribit_data
````


**Запустите Docker Compose**
````
docker-compose up --build
````
Это запустит все необходимые сервисы, включая базу данных PostgreSQL и приложение FastAPI.

**Примените миграции базы данных**
В отдельном терминале выполните миграции:

````
docker-compose exec app alembic upgrade head
````
**Запуск клиента**
Клиент автоматически запускается вместе с приложением и начинает собирать данные каждые 60 секунд.

**Использование API**

API предоставляет следующие эндпоинты:

1. Получение всех данных
URL: ```/api/currency```

Метод: GET

Параметры:

`ticker (строка, обязательный): Тикер валюты, например btc_usd или eth_usd.
Пример запроса:`

````commandline
curl -X GET http://localhost:8000/api/currency?ticker=btc_usd
````
Пример ответа:

```
json
Копировать код
[
  {
    "id": 1,
    "ticker": "btc_usd",
    "price": 70000.0,
    "timestamp": "2024-10-30T23:52:46Z"
  },
  {
    "id": 2,
    "ticker": "btc_usd",
    "price": 70500.0,
    "timestamp": "2024-10-30T23:53:46Z"
  }
]
```

2. **Получение последней цены**
URL: ````/api/currency/latest````

Метод: GET

Параметры:

`ticker (строка, обязательный): Тикер валюты, например btc_usd или eth_usd.
Пример запроса:`

Пример ответа:

```{
  "id": 2,
  "ticker": "btc_usd",
  "price": 70500.0,
  "timestamp": "2024-10-30T23:53:46Z"
}
```
Пример запроса
```
curl -X GET "http://localhost:8000/api/currency/latest?ticker=btc_usd"
```
3. **Получение данных по дате**
URL: ````/api/currency/filter````

Метод: GET

Параметры:

`ticker (строка, обязательный): Тикер валюты, например btc_usd или eth_usd.`

`start_date (строка, обязательный): Начальная дата в формате ISO, например 2024-10-30T00:00:00`

`end_date (строка, обязательный): Конечная дата в формате ISO, например 2024-10-31T23:59:59`
````
curl -X GET "http://localhost:8000/api/currency/latest?ticker=btc_usd"
````
Пример ответа:

```

{
  "id": 2,
  "ticker": "btc_usd",
  "price": 70500.0,
  "timestamp": "2024-10-30T23:53:46Z"
}
```
**Структура проекта**
````
deribit_project/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── currency.py
│   ├── clients/
│   │   ├── __init__.py
│   │   └── deribit_client.py
│   ├── dao/
│   │   ├── __init__.py
│   │   └── currency_dao.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── currency_models.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── currency_service.py
│   ├── db/
│       ├── __init__.py
│       └── database.py
│   ├── main.py
├── tests/
│   ├── __init__.py
│   ├── test_clients.py
│   └── test_services.py
│
├── .env
├── .github/
│   └── workflows/
│       └── tests.yml
├── .env
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── README.md

````

***Документация API***
```commandline
http://localhost:8000/docs
```