"""
Ejercicio 4e1: Aplicación Flask para demostrar Docker

Este ejercicio muestra cómo crear y containerizar una aplicación Flask simple
usando Docker. La aplicación devuelve información sobre el entorno de ejecución.

Los estudiantes deben:
1. Completar el Dockerfile proporcionado
2. Construir la imagen Docker
3. Ejecutar el contenedor Docker
4. Verificar que la aplicación funciona y está ejecutándose como el usuario correcto
"""

import os
import getpass
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Endpoint principal que devuelve un mensaje de bienvenida e información
    sobre el usuario que está ejecutando el proceso.
    """
    # Obtener información del usuario que ejecuta el proceso
    try:
        # getpass.getuser() obtiene el nombre del usuario que ejecuta el proceso
        username = getpass.getuser()
    except Exception as e:
        username = f"Error obteniendo usuario: {str(e)}"

    return jsonify({
        "mensaje": "¡Hola, este es el primer ejemplo con Docker!",
        "usuario": username,
        "pid": os.getpid(),
        "uid": os.getuid()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
