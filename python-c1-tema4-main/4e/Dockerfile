# Este Dockerfile es para una aplicación Flask.
# Los estudiantes deben completarlo para construir su imagen Docker.

# PASO 1: Especifica la imagen base de Python.
# Pista: Usa una versión 'slim' para un tamaño de imagen más pequeño.
# Pista: Usa la misma versión de Python que tenga tu entorno local.
FROM python:3.9-slim

# PASO 2: Establece el directorio de trabajo dentro del contenedor.
# Todos los comandos posteriores se ejecutarán en este directorio.
WORKDIR /app
RUN useradd -m usertest

# PASO 3: Copia el archivo de requisitos e instala las dependencias.
# Primero, copia solo el archivo de requisitos para aprovechar el cache de Docker.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# PASO 4: Copia el resto de los archivos de la aplicación al directorio de trabajo.
COPY . .

# PASO 5: Expone el puerto en el que la aplicación Flask escucha.
# Asegúrate de que este puerto coincida con el puerto configurado en tu aplicación Flask.
EXPOSE 5000

# PASO 6: Crea un usuario no root llamado "usertest" y configura los permisos adecuados.
# Pista: Usa la instrucción RUN para crear el usuario y cambiar la propiedad de los archivos.
RUN chown -R usertest:usertest /app
USER usertest

# PASO 7: Define el comando para ejecutar la aplicación Flask cuando el contenedor se inicie.
# Pista: Ejecuta el script Python principal de tu aplicación.
CMD ["python", "el_flask.py"]
