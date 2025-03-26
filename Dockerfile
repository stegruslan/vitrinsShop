FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && \
    pip install --upgrade pip poetry==1.7.0

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root --no-interaction

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


