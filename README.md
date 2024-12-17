# Простой Мессенджер

Этот проект представляет собой простой мессенджер, построенный с использованием FastAPI.

## Настройка

1. Клонируйте репозиторий.
2. Создайте виртуальное окружение.
3. Установите зависимости.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Запуск приложения

1. Запустите приложение:

```bash
uvicorn main:app --reload
```

2. Откройте ваш браузер и перейдите по адресу `http://127.0.0.1:8000/docs`, чтобы увидеть документацию Swagger.

## Эндпоинты

### Регистрация пользователя

- **POST** `/register/`
- Тело запроса: `{ "name": "John Doe", "email": "john@example.com" }`

### Отправка сообщения

- **POST** `/send/`
- Тело запроса: `{ "sender": "john@example.com", "receiver": "jane@example.com", "content": "Hello!" }`

### Получение сообщений

- **GET** `/messages/{email}`
- Параметр пути: `email` (строка)
