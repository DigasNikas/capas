```
poetry install
poetry add lib
docker-compose up -d
alembic revision --autogenerate -m <message>
alembic upgrade head
psql --host=localhost --user=root --password=root
```