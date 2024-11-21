FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar solo los archivos necesarios primero
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Variables de entorno
ENV PORT=8080
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Exponer puerto
EXPOSE 8080

# Comando para iniciar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "run:app", "--log-level=debug"]