"""
Servicio de Citas - Inicialización de la aplicación Flask
Maneja la gestión operativa de citas médicas
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Inicializar extensiones
db = SQLAlchemy()


def create_app(config_name='default'):
    """
    Factory function para crear la aplicación Flask

    Args:
        config_name: Nombre de la configuración a usar

    Returns:
        Instancia de la aplicación Flask configurada
    """
    app = Flask(__name__)

    # Cargar configuración
    from config import config
    app.config.from_object(config[config_name])

    # Inicializar extensiones con la app
    db.init_app(app)

    # Registrar blueprints
    from app.blueprints.citas_bp import citas_bp
    app.register_blueprint(citas_bp, url_prefix='/citas')

    # Crear tablas en la base de datos
    with app.app_context():
        db.create_all()

    # Ruta de health check
    @app.route('/health')
    def health():
        return {'status': 'ok', 'service': 'servicio_citas'}, 200

    return app
