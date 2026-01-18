# ХОРОШИЙ докерфайл

# Закрепление базового образа на конкретной версии для воспроизводимости
FROM python:3.12.8-slim-bookworm

# Безопасные настройки по умолчанию
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Копируем только необходимые файлы
COPY app/server.py /app/server.py

# Запускаем не через рут
RUN useradd --create-home --shell /usr/sbin/nologin appuser \
    && chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

# Exec-form CMD
CMD ["python", "/app/server.py"]
