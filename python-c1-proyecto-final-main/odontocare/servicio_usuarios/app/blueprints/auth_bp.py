"""
Blueprint de Autenticación - auth_bp
Maneja login, registro y validación de tokens JWT
"""
from flask import Blueprint, request, jsonify, current_app
from functools import wraps
import jwt
from datetime import datetime, timedelta, timezone

from app import db
from app.models.usuario import Usuario

auth_bp = Blueprint('auth', __name__)


def token_required(f):
    """
    Decorador para proteger endpoints que requieren autenticación

    Verifica el token JWT en el header Authorization: Bearer <token>
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Obtener token del header Authorization
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(' ')[1]  # Bearer <token>
            except IndexError:
                return jsonify({'error': 'Formato de token inválido'}), 401

        if not token:
            return jsonify({'error': 'Token no proporcionado'}), 401

        try:
            # Decodificar token
            data = jwt.decode(
                token,
                current_app.config['JWT_SECRET_KEY'],
                algorithms=['HS256']
            )
            current_user = Usuario.query.get(data['id_usuario'])

            if not current_user:
                return jsonify({'error': 'Usuario no encontrado'}), 401

        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token inválido'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


def role_required(*roles):
    """
    Decorador para verificar que el usuario tiene uno de los roles permitidos

    Args:
        roles: Lista de roles permitidos
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(current_user, *args, **kwargs):
            if current_user.rol not in roles:
                return jsonify({
                    'error': 'No tienes permisos para acceder a este recurso',
                    'rol_requerido': list(roles),
                    'tu_rol': current_user.rol
                }), 403
            return f(current_user, *args, **kwargs)
        return decorated_function
    return decorator


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Endpoint de login

    Recibe: {"username": "...", "password": "..."}
    Retorna: {"token": "...", "usuario": {...}}
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Datos no proporcionados'}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username y password son requeridos'}), 400

    # Buscar usuario
    usuario = Usuario.query.filter_by(username=username).first()

    if not usuario or not usuario.check_password(password):
        return jsonify({'error': 'Credenciales inválidas'}), 401

    # Generar token JWT
    token_payload = {
        'id_usuario': usuario.id_usuario,
        'username': usuario.username,
        'rol': usuario.rol,
        'exp': datetime.now(timezone.utc) + timedelta(hours=24)
    }

    token = jwt.encode(
        token_payload,
        current_app.config['JWT_SECRET_KEY'],
        algorithm='HS256'
    )

    return jsonify({
        'mensaje': 'Login exitoso',
        'token': token,
        'usuario': usuario.to_dict()
    }), 200


@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Endpoint de registro público (solo crea usuarios con rol 'paciente')

    Recibe: {"username": "...", "password": "..."}
    Retorna: {"mensaje": "...", "usuario": {...}}
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Datos no proporcionados'}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username y password son requeridos'}), 400

    # Verificar si el usuario ya existe
    if Usuario.query.filter_by(username=username).first():
        return jsonify({'error': 'El usuario ya existe'}), 409

    # Crear nuevo usuario con rol paciente
    nuevo_usuario = Usuario(
        username=username,
        rol='paciente'
    )
    nuevo_usuario.set_password(password)

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({
        'mensaje': 'Usuario registrado exitosamente',
        'usuario': nuevo_usuario.to_dict()
    }), 201


@auth_bp.route('/validate', methods=['GET'])
@token_required
def validate_token(current_user):
    """
    Endpoint para validar un token y obtener info del usuario

    Requiere: Header Authorization: Bearer <token>
    Retorna: {"valido": true, "usuario": {...}}
    """
    return jsonify({
        'valido': True,
        'usuario': current_user.to_dict()
    }), 200


@auth_bp.route('/usuario/<int:id_usuario>', methods=['GET'])
@token_required
def get_usuario(current_user, id_usuario):
    """
    Obtener información de un usuario por ID
    Solo admin puede ver otros usuarios, los demás solo su propio perfil
    """
    if current_user.rol != 'admin' and current_user.id_usuario != id_usuario:
        return jsonify({'error': 'No tienes permisos para ver este usuario'}), 403

    usuario = Usuario.query.get(id_usuario)
    if not usuario:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    return jsonify(usuario.to_dict()), 200
