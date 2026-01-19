"""
Servicio de Usuarios - Inicialización de la aplicación Flask
Maneja autenticación y administración de usuarios, pacientes, doctores y centros
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
    from app.blueprints.auth_bp import auth_bp
    from app.blueprints.admin_bp import admin_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # Crear tablas en la base de datos
    with app.app_context():
        db.create_all()
        # Crear usuario admin por defecto si no existe
        from app.models.usuario import Usuario
        admin = Usuario.query.filter_by(username='admin').first()
        if not admin:
            admin = Usuario(
                username='admin',
                rol='admin'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()

    # Ruta de health check
    @app.route('/health')
    def health():
        return {'status': 'ok', 'service': 'servicio_usuarios'}, 200

    return app
