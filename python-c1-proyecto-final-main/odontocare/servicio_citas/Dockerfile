# Dockerfile para el Servicio de Citas
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Variables de entorno
ENV FLASK_ENV=production
ENV PORT=5002
ENV SERVICIO_USUARIOS_URL=http://servicio_usuarios:5001

# Exponer puerto
EXPOSE 5002

# Comando para ejecutar la aplicación
CMD ["python", "run.py"]
