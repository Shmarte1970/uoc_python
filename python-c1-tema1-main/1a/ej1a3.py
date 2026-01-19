"""
Enunciado:
Desarrolla un servidor web básico utilizando la biblioteca http.server de Python.
El servidor debe responder a peticiones GET y proporcionar información sobre la IP del cliente.

`GET /ip`: Devuelve la dirección IP del cliente en formato JSON.

Esta es una introducción a los servidores HTTP en Python para entender cómo:
1. Crear una aplicación web básica sin usar frameworks
2. Responder a diferentes rutas en una petición HTTP
3. Procesar encabezados de peticiones HTTP
4. Devolver respuestas en formato JSON

Tu tarea es completar la implementación de la clase MyHTTPRequestHandler.

Nota: Para obtener la IP del cliente, necesitarás examinar los encabezados de la petición HTTP.
Algunos encabezados comunes para esto son: X-Forwarded-For, X-Real-IP o directamente la dirección
del cliente mediante self.client_address.
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Manejador de peticiones HTTP personalizado
    """

    def do_GET(self):
        """
        Método que se ejecuta cuando se recibe una petición GET.

        Rutas implementadas:
        - `/ip`: Devuelve la IP del cliente en formato JSON

        Para otras rutas, devuelve un código de estado 404 (Not Found).
        """
        if self.path == "/ip":
            # Obtener la IP del cliente usando el método auxiliar
            client_ip = self._get_client_ip()

            # Construir la respuesta en formato JSON
            response_data = {"ip": client_ip}
            response_json = json.dumps(response_data)

            # Enviar cabecera de respuesta 200 OK
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            # Enviar el cuerpo de la respuesta
            self.wfile.write(response_json.encode("utf-8"))
        else:
            # Para cualquier otra ruta, devolver 404 Not Found
            self.send_response(404)
            self.end_headers()

    def _get_client_ip(self):
        """
        Método auxiliar para obtener la IP del cliente desde los encabezados.
        Debes implementar la lógica para extraer la IP del cliente desde los encabezados
        de la petición o desde la dirección directa del cliente.

        Returns:
            str: La dirección IP del cliente
        """
        # 1. Verificar encabezado 'X-Forwarded-For' (común cuando hay proxies)
        x_forwarded_for = self.headers.get("X-Forwarded-For")
        if x_forwarded_for:
            # Puede haber varias IP separadas por coma, tomamos la primera
            return x_forwarded_for.split(",")[0].strip()

        # 2. Verificar encabezado 'X-Real-IP'
        x_real_ip = self.headers.get("X-Real-IP")
        if x_real_ip:
            return x_real_ip.strip()

        # 3. Como último recurso, usar la dirección directa del cliente
        return self.client_address[0]


def create_server(host="localhost", port=8000):
    """
    Crea y configura el servidor HTTP
    """
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    return httpd


def run_server(server):
    """
    Inicia el servidor HTTP
    """
    print(f"Servidor iniciado en http://{server.server_name}:{server.server_port}")
    server.serve_forever()


if __name__ == "__main__":
    server = create_server()
    run_server(server)
