"""
Enunciado:
Desarrolla una aplicación web con Flask que demuestre diferentes formas de acceder a la
información enviada en las solicitudes HTTP. Esta aplicación te permitirá entender cómo
procesar diferentes tipos de datos proporcionados por los clientes.

Tu aplicación debe implementar los siguientes endpoints:

1. `GET /headers`: Devuelve los encabezados (headers) de la solicitud en formato JSON.
   - Muestra información como User-Agent, Accept-Language, etc.

2. `GET /browser`: Analiza el encabezado User-Agent y devuelve información sobre:
   - El navegador que está usando el cliente
   - El sistema operativo
   - Si es un dispositivo móvil o no

3. `POST /echo`: Acepta cualquier tipo de datos y devuelve exactamente los mismos datos
   en la misma forma que fueron enviados. Debe manejar:
   - JSON
   - Datos de formulario (form data)
   - Texto plano

4. `POST /validate-id`: Valida un documento de identidad según estas reglas:
   - Debe recibir un JSON con un campo "id_number"
   - El ID debe tener exactamente 9 caracteres
   - Los primeros 8 caracteres deben ser dígitos
   - El último carácter debe ser una letra
   - Devuelve JSON indicando si es válido o no

Esta actividad te enseñará cómo acceder y manipular datos de las solicitudes HTTP,
una habilidad fundamental para crear APIs robustas y aplicaciones web interactivas.
"""

import re

from flask import Flask, Response, jsonify, request


def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route("/headers", methods=["GET"])
    def get_headers():
        """
        Devuelve los encabezados (headers) de la solicitud en formato JSON.
        Convierte el objeto headers de la solicitud en un diccionario.
        """
        return jsonify(dict(request.headers))

    @app.route("/browser", methods=["GET"])
    def get_browser_info():
        """
        Analiza el encabezado User-Agent y devuelve información sobre el navegador,
        sistema operativo y si es un dispositivo móvil.
        """
        ua = request.headers.get("User-Agent", "")

        # Navegador
        if "Chrome" in ua:
            browser = "Chrome"
        elif "Firefox" in ua:
            browser = "Firefox"
        elif "Safari" in ua and "Chrome" not in ua:
            browser = "Safari"
        else:
            browser = "Unknown"

        # Sistema operativo
        if "Windows" in ua:
            os = "Windows"
        elif "iPhone" in ua or "iOS" in ua:
            os = "iOS"
        elif "Android" in ua:
            os = "Android"
        elif "Mac OS" in ua:
            os = "macOS"
        else:
            os = "Unknown"

        is_mobile = any(x in ua for x in ["Mobile", "Android", "iPhone"])

        return jsonify({"browser": browser, "os": os, "is_mobile": is_mobile})

    @app.route("/echo", methods=["POST"])
    def echo():
        """
        Devuelve exactamente los mismos datos que recibe.
        Debe detectar el tipo de contenido y procesarlo adecuadamente.
        """
        if request.is_json:
            return jsonify(request.get_json())

        if (
            request.content_type
            and "application/x-www-form-urlencoded" in request.content_type
        ):
            return jsonify(request.form.to_dict())

        # Texto plano
        return Response(request.data, content_type=request.content_type)

    @app.route("/validate-id", methods=["POST"])
    def validate_id():
        """
        Valida un documento de identidad según reglas específicas:
        - Debe tener exactamente 9 caracteres
        - Los primeros 8 caracteres deben ser dígitos
        - El último carácter debe ser una letra
        """
        data = request.get_json()
        if not data or "id_number" not in data:
            return jsonify({"error": "id_number is required"}), 400

        id_number = data["id_number"]

        valid = bool(re.fullmatch(r"\d{8}[A-Za-z]", id_number))

        return jsonify({"valid": valid})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
