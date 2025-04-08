FROM python:3.9-slim

WORKDIR /app

# Системные зависимости
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Зависимости Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопировать все файлы проекта
COPY . .

# Установить PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Запустить программу
CMD ["python", "-m", "src.main"]