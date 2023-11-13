## Парсер форм на FastAPI
### Стек:
- Python 3.11
- FastAPI
- TinyDB
### Установка и запуск приложения:
```bash
pip install requirements.txt
cd app
uvicorn main:app
```
### Простой тест использую requests, запускать с запущенным приложением:
```bash
python3 test_main.py
```

#### Скрипт отправляет два запроса, первый должен вернуть название шаблона, второй - поля с типами значений