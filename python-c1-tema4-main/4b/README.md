# Ejercicio: Introducción a Docker con Python

## Objetivo

Aprender los conceptos básicos de Docker utilizando una imagen oficial de Python desde el registro estándar (Docker Hub), sin crear un Dockerfile personalizado.

## Pasos del ejercicio

1. **Aprender los fundamentos de Docker**
   - ¿Qué es Docker?
   - ¿Para qué sirve?
   - Conceptos clave: imagen, contenedor, registro.

2. **Ejecutar un contenedor Python desde la imagen oficial**
   - Descarga y ejecuta la imagen oficial de Python desde Docker Hub:
     ```zsh
     docker run -it --rm -v "$PWD":/usr/src/app -w /usr/src/app python:3.9 bash
     ```
   - Explicación:
     - `-it`: Modo interactivo.
     - `--rm`: Elimina el contenedor al salir.
     - `-v "$PWD":/usr/src/app`: Monta el directorio actual dentro del contenedor.
     - `-w /usr/src/app`: Establece el directorio de trabajo.
     - `python:3.9`: Imagen oficial de Python.
     - `bash`: Inicia una terminal dentro del contenedor.

3. **Verificar que estás dentro del contenedor**
   - Ejecuta el siguiente comando dentro del contenedor:
     ```zsh
     python --version
     pwd
     ls
     ```
   - Observa que el entorno es diferente al de tu máquina local.

4. **Ejecutar el archivo eh4b1.py dentro del contenedor**
   - Una vez dentro del contenedor, ejecuta:
     ```zsh
     python ej4b1.py
     ```
   - El archivo debe estar en el directorio actual (montado desde tu máquina local).

## Notas
- No se requiere crear un Dockerfile en este ejercicio.
- El objetivo es familiarizarse con el uso de imágenes oficiales y la interacción básica con contenedores.

## Recursos útiles
- [Documentación oficial de Docker](https://docs.docker.com/get-started/)
- [Imágenes oficiales de Python en Docker Hub](https://hub.docker.com/_/python)
