# 1. Imagen base de Python (estable y optimizada)
FROM python:3.11-slim

# 2. Etiquetas de metadatos (Buena práctica de DevOps)
LABEL maintainer="Julio Gomez"
LABEL project="SENTINEL-AI"

# 3. Variables de entorno para evitar archivos basura y ver logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4. Establecer directorio de trabajo
WORKDIR /app

# 5. Instalar dependencias del sistema (necesarias para procesos de red y compilación)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# 6. Copiar requirements e instalar (antes que el código para aprovechar el cache de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copiar el resto del proyecto (incluyendo el CSV de Big Data)
COPY . .

# 8. Exponer el puerto que usa Streamlit
EXPOSE 8501

# 9. Healthcheck: Para que el sistema sepa si la App está viva (Nivel Senior)
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# 10. Comando para arrancar el Dashboard
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]