## Тестовый проект на FastApi  

### Запуск:  

```
docker-compose build
docker-compose up --remove-orphans -d --build
```

### Запуск web интерфейса 
http://localhost:9000/docs

---

### File .env
```
POSTGRES_USERNAME=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=fast_blog
POSTGRES_HOST=postgres
POSTGRES_PORT=15489
```

---

### Используемые инструменты:
* Виртуальное окружение - poetry
* python 3.10
* FastApi 0.89.1
* sqlalchemy 2.0.5.post1
* alembic 1.10.2
* postgres