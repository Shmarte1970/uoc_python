import pytest
from flask.testing import FlaskClient
from ej2e2 import create_app


@pytest.fixture
def client() -> FlaskClient:
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_get_text(client):
    response = client.get("/text")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Este es un texto plano"
    assert response.content_type == "text/plain"

def test_get_html(client):
    response = client.get("/html")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "<h1>Este es un fragmento HTML</h1>"
    assert response.content_type == "text/html"

def test_get_json(client):
    response = client.get("/json")
    assert response.status_code == 200
    assert response.json == {"mensaje": "Este es un objeto JSON"}
    assert response.content_type == "application/json"

def test_get_xml(client):
    response = client.get("/xml")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "<mensaje>Este es un documento XML</mensaje>"
    assert response.content_type == "application/xml"

def test_get_image(client):
    response = client.get("/image")
    assert response.status_code == 200
    assert response.content_type == "image/png"
    # Opcional: Verificar el tamaño del archivo o contenido binario si es necesario

def test_get_binary(client):
    response = client.get("/binary")
    assert response.status_code == 200
    assert response.content_type == "application/octet-stream"
    assert len(response.data) > 0, "Los datos binarios no deben estar vacíos"
    assert "Content-Disposition" in response.headers, "Debe incluir el header Content-Disposition"
    assert "attachment" in response.headers["Content-Disposition"], "Content-Disposition debe configurarse como attachment"
