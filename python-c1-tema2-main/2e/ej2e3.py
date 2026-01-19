"""
Enunciado:
Desarrolla una aplicación web con Flask que procese diferentes tipos MIME (Multipurpose Internet Mail Extensions)
recibidos en solicitudes HTTP. Esta aplicación te permitirá entender cómo recibir y procesar
diferentes formatos de datos enviados por los clientes.

Los tipos MIME son fundamentales en el desarrollo web ya que indican cómo interpretar los datos
recibidos en las solicitudes HTTP. Una API robusta debe poder manejar diversos formatos de entrada.

Tu aplicación debe implementar los siguientes endpoints:

1. `POST /text`: Recibe un texto plano con el tipo MIME `text/plain` y lo devuelve en la respuesta.
   - Ejemplo de uso: Procesar mensajes simples o logs enviados por el cliente.

2. `POST /html`: Recibe un fragmento HTML con el tipo MIME `text/html` y lo devuelve en la respuesta.
   - Ejemplo de uso: Recibir contenido HTML para almacenar o procesar.

3. `POST /json`: Recibe un objeto JSON con el tipo MIME `application/json` y lo devuelve en la respuesta.
   - Ejemplo de uso: Procesar datos estructurados en APIs RESTful.

4. `POST /xml`: Recibe un documento XML con el tipo MIME `application/xml` y lo devuelve en la respuesta.
   - Ejemplo de uso: Procesar configuraciones o datos estructurados en formato XML.

5. `POST /image`: Recibe una imagen con el tipo MIME `image/png` o `image/jpeg` y la guarda en el servidor.
   - Ejemplo de uso: Subir imágenes para un perfil de usuario o una galería.

6. `POST /binary`: Recibe datos binarios con el tipo MIME `application/octet-stream` y confirma su recepción.
   - Ejemplo de uso: Recibir archivos genéricos como PDFs o archivos comprimidos.

Tu tarea es completar la implementación de la función create_app() y de los endpoints solicitados,
asegurándote de identificar correctamente el tipo MIME de cada solicitud y procesarla adecuadamente.

Esta actividad te enseñará cómo recibir y manejar diferentes tipos de datos en solicitudes HTTP,
una habilidad esencial para desarrollar APIs web que interactúan con diversos clientes.
"""

import os
import uuid

from flask import Flask, Response, jsonify, request

try:
    from scipy import misc

    if not hasattr(misc, "face"):
        import numpy as np

        def fake_face():
            # Crear imagen RGB simple (256x256)
            img = np.zeros((256, 256, 3), dtype=np.uint8)
            img[:, :] = [128, 128, 128]  # gris
            return img

        misc.face = fake_face
except Exception:
    pass


def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    # Crear un directorio para guardar archivos subidos si no existe
    uploads_dir = os.path.join(app.instance_path, "uploads")
    os.makedirs(uploads_dir, exist_ok=True)

    @app.route("/text", methods=["POST"])
    def post_text():
        """
        Recibe un texto plano con el tipo MIME `text/plain` y lo devuelve en la respuesta.
        """
        if request.content_type != "text/plain":
            return Response("Tipo MIME no soportado", status=415)

        text = request.data.decode("utf-8")
        return Response(text, content_type="text/plain")

    @app.route("/html", methods=["POST"])
    def post_html():
        """
        Recibe un fragmento HTML con el tipo MIME `text/html` y lo devuelve en la respuesta.
        """
        if request.content_type != "text/html":
            return Response("Tipo MIME no soportado", status=415)

        html = request.data.decode("utf-8")
        return Response(html, content_type="text/html")

    @app.route("/json", methods=["POST"])
    def post_json():
        """
        Recibe un objeto JSON con el tipo MIME `application/json` y lo devuelve en la respuesta.
        """
        data = request.get_json()
        return jsonify(data)

    @app.route("/xml", methods=["POST"])
    def post_xml():
        """
        Recibe un documento XML con el tipo MIME `application/xml` y lo devuelve en la respuesta.
        """
        if request.content_type != "application/xml":
            return Response("Tipo MIME no soportado", status=415)

        xml_data = request.data.decode("utf-8")
        return Response(xml_data, content_type="application/xml")

    @app.route("/image", methods=["POST"])
    def post_image():
        """
        Recibe una imagen con el tipo MIME `image/png` o `image/jpeg` y la guarda en el servidor.
        """
        if request.content_type not in ("image/png", "image/jpeg"):
            return jsonify({"error": "Tipo de imagen no soportado"}), 415

        image_data = request.data
        extension = "png" if request.content_type == "image/png" else "jpg"
        filename = f"{uuid.uuid4()}.{extension}"
        filepath = os.path.join(uploads_dir, filename)

        with open(filepath, "wb") as f:
            f.write(image_data)

        return jsonify(
            {"mensaje": "Imagen guardada correctamente", "archivo": filename}
        )

    @app.route("/binary", methods=["POST"])
    def post_binary():
        """
        Recibe datos binarios con el tipo MIME `application/octet-stream` y confirma su recepción.
        """
        if request.content_type != "application/octet-stream":
            return jsonify({"error": "Tipo MIME no soportado"}), 415

        binary_data = request.data
        size = len(binary_data)

        return jsonify(
            {"mensaje": "Datos binarios recibidos correctamente", "tamaño": size}
        )

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
