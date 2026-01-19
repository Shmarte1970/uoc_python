"""
Pruebas simples para el ejercicio 4b1 - Aplicación Flask en Docker

Este archivo contiene pruebas básicas para verificar que:
1. La API está disponible a través de HTTP en el puerto correcto
2. La aplicación se está ejecutando como el usuario correcto (usertest)
"""

import pytest
import requests

# URL de la aplicación
API_URL = "http://localhost:5000"

def test_api_is_running():
    """Verifica que la API está disponible y responde correctamente"""
    response = requests.get(API_URL)
    assert response.status_code == 200
    assert "mensaje" in response.json()
    assert response.json()["mensaje"] == "¡Hola, este es el primer ejemplo con Docker!"

def test_api_running_as_correct_user():
    """Verifica que la API está ejecutándose como el usuario 'usertest'"""
    response = requests.get(API_URL)
    assert response.status_code == 200
    assert "usuario" in response.json()
    assert response.json()["usuario"] == "usertest", f"La aplicación está ejecutándose como '{response.json().get('usuario')}' en lugar de 'usertest'"
