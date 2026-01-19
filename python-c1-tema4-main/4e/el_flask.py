import getpass
import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    Endpoint principal que devuelve un mensaje de bienvenida e información
    sobre el usuario que está ejecutando el proceso.
    """
    try:
        username = getpass.getuser()
    except Exception as e:
        username = f"Error obteniendo usuario: {str(e)}"

    return jsonify(
        {
            "mensaje": "¡Hola, este es el primer ejemplo con Docker!",
            "usuario": username,
            "pid": os.getpid(),
            "uid": os.getuid(),
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
