"""
Enunciado:
Desarrolla una aplicación web básica con Flask que muestre el uso del sistema de registro (logging).

En el desarrollo web es fundamental tener un buen sistema de registro de eventos,
que permita hacer seguimiento de lo que ocurre en nuestra aplicación. Flask proporciona
un objeto logger integrado (app.logger) que permite registrar mensajes con diferentes
niveles de importancia.

Tu tarea es implementar los siguientes endpoints:

1. `GET /info`: Registra un mensaje de nivel INFO y devuelve un mensaje en texto plano.
2. `GET /warning`: Registra un mensaje de nivel WARNING y devuelve un mensaje en texto plano.
3. `GET /error`: Registra un mensaje de nivel ERROR y devuelve un mensaje en texto plano.
4. `GET /critical`: Registra un mensaje de nivel CRITICAL y devuelve un mensaje en texto plano.

Esta actividad te enseñará a utilizar el sistema de registro de Flask,
una habilidad crucial para el desarrollo y depuración de aplicaciones web.
"""

from flask import Flask, Response


def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    # Configuración básica del logger
    # Por defecto, los mensajes se registrarán en la consola

    @app.route("/info", methods=["GET"])
    def log_info():
        """
        Registra un mensaje de nivel INFO
        """
        app.logger.info("Mensaje de nivel INFO")
        return Response("Mensaje INFO registrado", mimetype="text/plain")

    @app.route("/warning", methods=["GET"])
    def log_warning():
        """
        Registra un mensaje de nivel WARNING
        """
        app.logger.warning("Mensaje de nivel WARNING")
        return Response("Mensaje WARNING registrado", mimetype="text/plain")

    @app.route("/error", methods=["GET"])
    def log_error():
        """
        Registra un mensaje de nivel ERROR
        """
        app.logger.error("Mensaje de nivel ERROR")
        return Response("Mensaje ERROR registrado", mimetype="text/plain")

    @app.route("/critical", methods=["GET"])
    def log_critical():
        """
        Registra un mensaje de nivel CRITICAL
        """
        app.logger.critical("Mensaje de nivel CRITICAL")
        return Response("Mensaje CRITICAL registrado", mimetype="text/plain")

    @app.route("/status", methods=["GET"])
    def status():
        """
        Endpoint adicional que registra diferentes mensajes según el parámetro de consulta 'level'
        Ejemplo: /status?level=warning
        """

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
