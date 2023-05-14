# Flask - Sync vs Async

Comparison of how Flask works in synchronous and asynchronous mode when interacting with external APIs.

---

Сравнение работы Flask в синхронном и асинхронном режиме при взаимодействии с внешними API.

Выполняет серию запросов проверки чисел на четность от 0 до указанного числа к 
сервису: [isevenapi.xyz](https://isevenapi.xyz/) с измерением потраченного на это времени.

---
## Зависимости и используемые библиотеки:

- Flask[async]
- asyncio
- httpx

### Запуск
#### При наличии Docker:
<code>docker-compose up --build -d</code>

#### Остановка:
<code>docker-compose rm -fs</code>

---
#### Без Docker
| Mac, Linux                                   | Windows                                      |
|----------------------------------------------|----------------------------------------------|
| <code>python3 -m venv venv</code>            | <code>python -m venv venv</code>             |
| <code>source venv/bin/activate</code>        | <code>venv\Scripts\activate</code>           |
| <code>pip install -r requirements.txt</code> | <code>pip install -r requirements.txt</code> |
| <code>python3 app.py</code>                  | <code>python app.py</code>                   |
---
**Работает по адресу: [localhost](http://localhost)**