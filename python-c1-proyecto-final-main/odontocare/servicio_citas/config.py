"""
Configuración del Servicio de Citas
"""
import os
from datetime import timedelta

class Config:
    """Configuración base"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'odontocare-secret-key-2024')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-odontocare-secret')

    # Base de datos SQLite (separada del servicio de usuarios)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'sqlite:///odontocare_citas.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # URL del servicio de usuarios para comunicación REST
    SERVICIO_USUARIOS_URL = os.environ.get(
        'SERVICIO_USUARIOS_URL',
        'http://localhost:5001'
    )


class DevelopmentConfig(Config):
    """Configuración de desarrollo"""
    DEBUG = True


class ProductionConfig(Config):
    """Configuración de producción"""
    DEBUG = False


# Diccionario de configuraciones
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
