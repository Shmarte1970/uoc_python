"""
Blueprints del Servicio de Usuarios
"""
from app.blueprints.auth_bp import auth_bp
from app.blueprints.admin_bp import admin_bp

__all__ = ['auth_bp', 'admin_bp']
