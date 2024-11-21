FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Variables de entorno
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# El puerto se configurará desde Railway
EXPOSE 8080

# Comando para iniciar la aplicación
CMD gunicorn --bind 0.0.0.0:$PORT run:app --workers 1 --timeout 60 --log-level debug 