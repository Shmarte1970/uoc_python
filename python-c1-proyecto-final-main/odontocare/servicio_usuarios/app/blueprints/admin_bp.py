"""
Blueprint de Administración - admin_bp
Maneja CRUD de usuarios, pacientes, doctores y centros médicos
"""
from flask import Blueprint, request, jsonify

from app import db
from app.models.usuario import Usuario
from app.models.paciente import Paciente
from app.models.doctor import Doctor
from app.models.centro import Centro
from app.blueprints.auth_bp import token_required, role_required

admin_bp = Blueprint('admin', __name__)


# ==================== USUARIOS ====================

@admin_bp.route('/usuario', methods=['POST'])
@token_required
@role_required('admin')
def crear_usuario(current_user):
    """
    Crear un nuevo usuario (admin o secretaria)

    Recibe: {"username": "...", "password": "...", "rol": "admin|secretaria"}
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Datos no proporcionados'}), 400

    username = data.get('username')
    password = data.get('password')
    rol = data.get('rol', 'secretaria')

    if not username or not password:
        return jsonify({'error': 'Username y password son requeridos'}), 400

    if rol not in ['admin', 'secretaria']:
        return jsonify({'error': 'Rol debe ser admin o secretaria'}), 400

    if Usuario.query.filter_by(username=username).first():
        return jsonify({'error': 'El usuario ya existe'}), 409

    nuevo_usuario = Usuario(username=username, rol=rol)
    nuevo_usuario.set_password(password)

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({
        'mensaje': 'Usuario creado exitosamente',
        'usuario': nuevo_usuario.to_dict()
    }), 201


@admin_bp.route('/usuarios', methods=['GET'])
@token_required
@role_required('admin')
def listar_usuarios(current_user):
    """Listar todos los usuarios"""
    usuarios = Usuario.query.all()
    return jsonify({
        'total': len(usuarios),
        'usuarios': [u.to_dict() for u in usuarios]
    }), 200


@admin_bp.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
@token_required
@role_required('admin')
def eliminar_usuario(current_user, id_usuario):
    """Eliminar un usuario"""
    # No permitir eliminar al propio usuario
    if current_user.id_usuario == id_usuario:
        return jsonify({'error': 'No puede eliminar su propio usuario'}), 400

    usuario = Usuario.query.get(id_usuario)
    if not usuario:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario eliminado exitosamente'}), 200


# ==================== DOCTORES ====================

@admin_bp.route('/doctores', methods=['POST'])
@token_required
@role_required('admin')
def crear_doctor(current_user):
    """
    Crear un nuevo doctor (crea también usuario con rol 'medico')

    Recibe: {"nombre": "...", "especialidad": "...", "username": "...", "password": "..."}
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Datos no proporcionados'}), 400

    nombre = data.get('nombre')
    especialidad = data.get('especialidad', '')
    username = data.get('username')
    password = data.get('password')

    if not nombre:
        return jsonify({'error': 'Nombre es requerido'}), 400

    id_usuario = None

    # Si se proporcionan credenciales, crear usuario
    if username and password:
        if Usuario.query.filter_by(username=username).first():
            return jsonify({'error': 'El username ya existe'}), 409

        nuevo_usuario = Usuario(username=username, rol='medico')
        nuevo_usuario.set_password(password)
        db.session.add(nuevo_usuario)
        db.session.flush()  # Para obtener el ID
        id_usuario = nuevo_usuario.id_usuario

    nuevo_doctor = Doctor(
        nombre=nombre,
        especialidad=especialidad,
        id_usuario=id_usuario
    )

    db.session.add(nuevo_doctor)
    db.session.commit()

    return jsonify({
        'mensaje': 'Doctor creado exitosamente',
        'doctor': nuevo_doctor.to_dict()
    }), 201


@admin_bp.route('/doctores', methods=['GET'])
@token_required
def listar_doctores(current_user):
    """Listar todos los doctores"""
    doctores = Doctor.query.all()
    return jsonify({
        'total': len(doctores),
        'doctores': [d.to_dict() for d in doctores]
    }), 200


@admin_bp.route('/doctores/<int:id_doctor>', methods=['GET'])
@token_required
def obtener_doctor(current_user, id_doctor):
    """Obtener un doctor por ID"""
    doctor = Doctor.query.get(id_doctor)
    if not doctor:
        return jsonify({'error': 'Doctor no encontrado'}), 404
    return jsonify(doctor.to_dict()), 200


@admin_bp.route('/doctores/<int:id_doctor>', methods=['PUT'])
@token_required
@role_required('admin')
def actualizar_doctor(current_user, id_doctor):
    """Actualizar un doctor"""
    doctor = Doctor.query.get(id_doctor)
    if not doctor:
        return jsonify({'error': 'Doctor no encontrado'}), 404

    data = request.get_json()
    if data.get('nombre'):
        doctor.nombre = data['nombre']
    if data.get('especialidad'):
        doctor.especialidad = data['especialidad']

    db.session.commit()
    return jsonify({
        'mensaje': 'Doctor actualizado',
        'doctor': doctor.to_dict()
    }), 200


@admin_bp.route('/doctores/<int:id_doctor>', methods=['DELETE'])
@token_required
@role_required('admin')
def eliminar_doctor(current_user, id_doctor):
    """Eliminar un doctor"""
    doctor = Doctor.query.get(id_doctor)
    if not doctor:
        return jsonify({'error': 'Doctor no encontrado'}), 404

    db.session.delete(doctor)
    db.session.commit()
    return jsonify({'mensaje': 'Doctor eliminado exitosamente'}), 200


# ==================== PACIENTES ====================

@admin_bp.route('/pacientes', methods=['POST'])
@token_required
@role_required('admin', 'secretaria')
def crear_paciente(current_user):
    """
    Crear un nuevo paciente (opcionalmente crea usuario con rol 'paciente')

    Recibe: {"nombre": "...", "telefono": "...", "username": "...", "password": "..."}
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Datos no proporcionados'}), 400

    nombre = data.get('nombre')
    telefono = data.get('telefono', '')
    estado = data.get('estado', 'ACTIVO')
    username = data.get('username')
    password = data.get('password')

    if not nombre:
        return jsonify({'error': 'Nombre es requerido'}), 400

    id_usuario = None

    # Si se proporcionan credenciales, crear usuario
    if username and password:
        if Usuario.query.filter_by(username=username).first():
            return jsonify({'error': 'El username ya existe'}), 409

        nuevo_usuario = Usuario(username=username, rol='paciente')
        nuevo_usuario.set_password(password)
        db.session.add(nuevo_usuario)
        db.session.flush()
        id_usuario = nuevo_usuario.id_usuario

    nuevo_paciente = Paciente(
        nombre=nombre,
        telefono=telefono,
        estado=estado,
        id_usuario=id_usuario
    )

    db.session.add(nuevo_paciente)
    db.session.commit()

    return jsonify({
        'mensaje': 'Paciente creado exitosamente',
        'paciente': nuevo_paciente.to_dict()
    }), 201


@admin_bp.route('/pacientes', methods=['GET'])
@token_required
def listar_pacientes(current_user):
    """Listar todos los pacientes"""
    pacientes = Paciente.query.all()
    return jsonify({
        'total': len(pacientes),
        'pacientes': [p.to_dict() for p in pacientes]
    }), 200


@admin_bp.route('/pacientes/<int:id_paciente>', methods=['GET'])
@token_required
def obtener_paciente(current_user, id_paciente):
    """Obtener un paciente por ID"""
    paciente = Paciente.query.get(id_paciente)
    if not paciente:
        return jsonify({'error': 'Paciente no encontrado'}), 404
    return jsonify(paciente.to_dict()), 200


@admin_bp.route('/pacientes/<int:id_paciente>', methods=['PUT'])
@token_required
@role_required('admin', 'secretaria')
def actualizar_paciente(current_user, id_paciente):
    """Actualizar un paciente"""
    paciente = Paciente.query.get(id_paciente)
    if not paciente:
        return jsonify({'error': 'Paciente no encontrado'}), 404

    data = request.get_json()
    if data.get('nombre'):
        paciente.nombre = data['nombre']
    if data.get('telefono'):
        paciente.telefono = data['telefono']
    if data.get('estado') in ['ACTIVO', 'INACTIVO']:
        paciente.estado = data['estado']

    db.session.commit()
    return jsonify({
        'mensaje': 'Paciente actualizado',
        'paciente': paciente.to_dict()
    }), 200


@admin_bp.route('/pacientes/<int:id_paciente>', methods=['DELETE'])
@token_required
@role_required('admin')
def eliminar_paciente(current_user, id_paciente):
    """Eliminar un paciente"""
    paciente = Paciente.query.get(id_paciente)
    if not paciente:
        return jsonify({'error': 'Paciente no encontrado'}), 404

    db.session.delete(paciente)
    db.session.commit()
    return jsonify({'mensaje': 'Paciente eliminado exitosamente'}), 200


# ==================== CENTROS MÉDICOS ====================

@admin_bp.route('/centros', methods=['POST'])
@token_required
@role_required('admin')
def crear_centro(current_user):
    """
    Crear un nuevo centro médico

    Recibe: {"nombre": "...", "direccion": "..."}
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Datos no proporcionados'}), 400

    nombre = data.get('nombre')
    direccion = data.get('direccion', '')

    if not nombre:
        return jsonify({'error': 'Nombre es requerido'}), 400

    nuevo_centro = Centro(
        nombre=nombre,
        direccion=direccion
    )

    db.session.add(nuevo_centro)
    db.session.commit()

    return jsonify({
        'mensaje': 'Centro creado exitosamente',
        'centro': nuevo_centro.to_dict()
    }), 201


@admin_bp.route('/centros', methods=['GET'])
@token_required
def listar_centros(current_user):
    """Listar todos los centros médicos"""
    centros = Centro.query.all()
    return jsonify({
        'total': len(centros),
        'centros': [c.to_dict() for c in centros]
    }), 200


@admin_bp.route('/centros/<int:id_centro>', methods=['GET'])
@token_required
def obtener_centro(current_user, id_centro):
    """Obtener un centro por ID"""
    centro = Centro.query.get(id_centro)
    if not centro:
        return jsonify({'error': 'Centro no encontrado'}), 404
    return jsonify(centro.to_dict()), 200


@admin_bp.route('/centros/<int:id_centro>', methods=['PUT'])
@token_required
@role_required('admin')
def actualizar_centro(current_user, id_centro):
    """Actualizar un centro médico"""
    centro = Centro.query.get(id_centro)
    if not centro:
        return jsonify({'error': 'Centro no encontrado'}), 404

    data = request.get_json()
    if data.get('nombre'):
        centro.nombre = data['nombre']
    if data.get('direccion'):
        centro.direccion = data['direccion']

    db.session.commit()
    return jsonify({
        'mensaje': 'Centro actualizado',
        'centro': centro.to_dict()
    }), 200


@admin_bp.route('/centros/<int:id_centro>', methods=['DELETE'])
@token_required
@role_required('admin')
def eliminar_centro(current_user, id_centro):
    """Eliminar un centro médico"""
    centro = Centro.query.get(id_centro)
    if not centro:
        return jsonify({'error': 'Centro no encontrado'}), 404

    db.session.delete(centro)
    db.session.commit()
    return jsonify({'mensaje': 'Centro eliminado exitosamente'}), 200
