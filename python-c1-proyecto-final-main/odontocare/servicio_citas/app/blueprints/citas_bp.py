"""
Blueprint de Gestión de Citas - citas_bp
Maneja CRUD de citas médicas con validaciones de negocio
"""
from flask import Blueprint, request, jsonify, current_app
from functools import wraps
from datetime import datetime
import jwt

from app import db
from app.models.cita import Cita
from app.services.usuarios_client import UsuariosServiceClient

citas_bp = Blueprint('citas', __name__)


def token_required(f):
    """
    Decorador para proteger endpoints que requieren autenticación
    Valida el token con el servicio de usuarios vía REST
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(' ')[1]
            except IndexError:
                return jsonify({'error': 'Formato de token inválido'}), 401

        if not token:
            return jsonify({'error': 'Token no proporcionado'}), 401

        # Validar token con el servicio de usuarios
        resultado = UsuariosServiceClient.validar_token(token)

        if not resultado or not resultado.get('valido'):
            # Si el servicio no está disponible, intentar decodificar localmente
            try:
                data = jwt.decode(
                    token,
                    current_app.config['JWT_SECRET_KEY'],
                    algorithms=['HS256']
                )
                current_user = {
                    'id_usuario': data['id_usuario'],
                    'username': data['username'],
                    'rol': data['rol']
                }
            except jwt.ExpiredSignatureError:
                return jsonify({'error': 'Token expirado'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'error': 'Token inválido'}), 401
        else:
            current_user = resultado.get('usuario')

        # Guardar token para usar en llamadas a otros servicios
        request.token = token
        return f(current_user, *args, **kwargs)

    return decorated


def role_required(*roles):
    """Decorador para verificar roles"""
    def decorator(f):
        @wraps(f)
        def decorated_function(current_user, *args, **kwargs):
            if current_user['rol'] not in roles:
                return jsonify({
                    'error': 'No tienes permisos para acceder a este recurso',
                    'rol_requerido': list(roles),
                    'tu_rol': current_user['rol']
                }), 403
            return f(current_user, *args, **kwargs)
        return decorated_function
    return decorator


@citas_bp.route('', methods=['POST'])
@token_required
@role_required('admin', 'secretaria', 'paciente')
def crear_cita(current_user):
    """
    Crear una nueva cita médica

    Recibe: {
        "fecha": "2024-12-20T10:00:00",
        "motivo": "Limpieza dental",
        "id_paciente": 1,
        "id_doctor": 1,
        "id_centro": 1
    }

    Validaciones:
    - El doctor existe
    - El centro médico existe
    - El paciente existe y está activo
    - No hay conflicto de horario con otras citas del doctor
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Datos no proporcionados'}), 400

    # Campos requeridos
    fecha_str = data.get('fecha')
    id_paciente = data.get('id_paciente')
    id_doctor = data.get('id_doctor')
    id_centro = data.get('id_centro')
    motivo = data.get('motivo', '')

    if not all([fecha_str, id_paciente, id_doctor, id_centro]):
        return jsonify({
            'error': 'Campos requeridos: fecha, id_paciente, id_doctor, id_centro'
        }), 400

    # Parsear fecha
    try:
        fecha = datetime.fromisoformat(fecha_str)
    except ValueError:
        return jsonify({'error': 'Formato de fecha inválido. Use ISO 8601 (YYYY-MM-DDTHH:MM:SS)'}), 400

    token = request.token

    # Validar que el doctor existe (vía REST al servicio de usuarios)
    doctor = UsuariosServiceClient.obtener_doctor(id_doctor, token)
    if not doctor:
        return jsonify({'error': f'Doctor con ID {id_doctor} no encontrado'}), 404

    # Validar que el centro existe
    centro = UsuariosServiceClient.obtener_centro(id_centro, token)
    if not centro:
        return jsonify({'error': f'Centro con ID {id_centro} no encontrado'}), 404

    # Validar que el paciente existe y está activo
    paciente = UsuariosServiceClient.obtener_paciente(id_paciente, token)
    if not paciente:
        return jsonify({'error': f'Paciente con ID {id_paciente} no encontrado'}), 404

    if paciente.get('estado') != 'ACTIVO':
        return jsonify({'error': 'El paciente no está activo'}), 400

    # Validar que no hay conflicto de horario (doble reserva)
    cita_existente = Cita.query.filter(
        Cita.id_doctor == id_doctor,
        Cita.fecha == fecha,
        Cita.estado != 'CANCELADA'
    ).first()

    if cita_existente:
        return jsonify({
            'error': 'El doctor ya tiene una cita programada en esa fecha y hora'
        }), 409

    # Crear la cita
    nueva_cita = Cita(
        fecha=fecha,
        motivo=motivo,
        estado='PROGRAMADA',
        id_paciente=id_paciente,
        id_doctor=id_doctor,
        id_centro=id_centro,
        id_usuario_registra=current_user['id_usuario']
    )

    db.session.add(nueva_cita)
    db.session.commit()

    return jsonify({
        'mensaje': 'Cita creada exitosamente',
        'cita': nueva_cita.to_dict()
    }), 201


@citas_bp.route('', methods=['GET'])
@token_required
def listar_citas(current_user):
    """
    Listar citas según el rol del usuario

    - Doctor: solo ve sus propias citas
    - Secretaria: puede filtrar por fecha
    - Admin: puede filtrar por doctor, centro, fecha, estado o paciente

    Query params: fecha, id_doctor, id_centro, id_paciente, estado
    """
    query = Cita.query

    # Filtros según rol
    if current_user['rol'] == 'medico':
        # El doctor solo ve sus citas
        # Buscar el id_doctor asociado al usuario
        token = request.token
        doctores = UsuariosServiceClient.listar_doctores(token)
        if doctores and 'doctores' in doctores:
            doctor_usuario = next(
                (d for d in doctores['doctores'] if d.get('id_usuario') == current_user['id_usuario']),
                None
            )
            if doctor_usuario:
                query = query.filter(Cita.id_doctor == doctor_usuario['id_doctor'])
            else:
                return jsonify({'total': 0, 'citas': []}), 200

    elif current_user['rol'] == 'secretaria':
        # Secretaria puede filtrar por fecha
        fecha = request.args.get('fecha')
        if fecha:
            try:
                fecha_filtro = datetime.fromisoformat(fecha).date()
                query = query.filter(db.func.date(Cita.fecha) == fecha_filtro)
            except ValueError:
                pass

    elif current_user['rol'] == 'admin':
        # Admin puede aplicar todos los filtros
        id_doctor = request.args.get('id_doctor')
        id_centro = request.args.get('id_centro')
        id_paciente = request.args.get('id_paciente')
        estado = request.args.get('estado')
        fecha = request.args.get('fecha')

        if id_doctor:
            query = query.filter(Cita.id_doctor == int(id_doctor))
        if id_centro:
            query = query.filter(Cita.id_centro == int(id_centro))
        if id_paciente:
            query = query.filter(Cita.id_paciente == int(id_paciente))
        if estado:
            query = query.filter(Cita.estado == estado.upper())
        if fecha:
            try:
                fecha_filtro = datetime.fromisoformat(fecha).date()
                query = query.filter(db.func.date(Cita.fecha) == fecha_filtro)
            except ValueError:
                pass

    elif current_user['rol'] == 'paciente':
        # El paciente solo ve sus propias citas
        token = request.token
        pacientes = UsuariosServiceClient.listar_pacientes(token)
        if pacientes and 'pacientes' in pacientes:
            paciente_usuario = next(
                (p for p in pacientes['pacientes'] if p.get('id_usuario') == current_user['id_usuario']),
                None
            )
            if paciente_usuario:
                query = query.filter(Cita.id_paciente == paciente_usuario['id_paciente'])
            else:
                return jsonify({'total': 0, 'citas': []}), 200

    # Ordenar por fecha
    query = query.order_by(Cita.fecha.desc())

    citas = query.all()
    return jsonify({
        'total': len(citas),
        'citas': [c.to_dict() for c in citas]
    }), 200


@citas_bp.route('/<int:id_cita>', methods=['GET'])
@token_required
def obtener_cita(current_user, id_cita):
    """Obtener una cita por ID"""
    cita = Cita.query.get(id_cita)
    if not cita:
        return jsonify({'error': 'Cita no encontrada'}), 404

    return jsonify(cita.to_dict()), 200


@citas_bp.route('/<int:id_cita>', methods=['PUT'])
@token_required
@role_required('admin', 'secretaria')
def actualizar_cita(current_user, id_cita):
    """
    Actualizar o cancelar una cita

    Para cancelar: {"estado": "CANCELADA"}

    Validaciones:
    - La cita existe
    - La cita no está ya cancelada (no se puede modificar)
    """
    cita = Cita.query.get(id_cita)
    if not cita:
        return jsonify({'error': 'Cita no encontrada'}), 404

    if cita.estado == 'CANCELADA':
        return jsonify({'error': 'No se puede modificar una cita cancelada'}), 400

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos no proporcionados'}), 400

    # Actualizar campos permitidos
    if 'motivo' in data:
        cita.motivo = data['motivo']

    if 'estado' in data:
        nuevo_estado = data['estado'].upper()
        if nuevo_estado in ['PROGRAMADA', 'COMPLETADA', 'CANCELADA']:
            cita.estado = nuevo_estado
        else:
            return jsonify({'error': 'Estado inválido. Use: PROGRAMADA, COMPLETADA, CANCELADA'}), 400

    if 'fecha' in data:
        try:
            nueva_fecha = datetime.fromisoformat(data['fecha'])
            # Validar conflicto de horario
            cita_existente = Cita.query.filter(
                Cita.id_doctor == cita.id_doctor,
                Cita.fecha == nueva_fecha,
                Cita.estado != 'CANCELADA',
                Cita.id_cita != id_cita
            ).first()

            if cita_existente:
                return jsonify({
                    'error': 'El doctor ya tiene una cita programada en esa fecha y hora'
                }), 409

            cita.fecha = nueva_fecha
        except ValueError:
            return jsonify({'error': 'Formato de fecha inválido'}), 400

    db.session.commit()

    mensaje = 'Cita cancelada exitosamente' if cita.estado == 'CANCELADA' else 'Cita actualizada exitosamente'
    return jsonify({
        'mensaje': mensaje,
        'cita': cita.to_dict()
    }), 200


@citas_bp.route('/<int:id_cita>', methods=['DELETE'])
@token_required
@role_required('admin')
def eliminar_cita(current_user, id_cita):
    """Eliminar una cita (solo admin)"""
    cita = Cita.query.get(id_cita)
    if not cita:
        return jsonify({'error': 'Cita no encontrada'}), 404

    db.session.delete(cita)
    db.session.commit()

    return jsonify({'mensaje': 'Cita eliminada exitosamente'}), 200


@citas_bp.route('/doctor/<int:id_doctor>/disponibilidad', methods=['GET'])
@token_required
def verificar_disponibilidad(current_user, id_doctor):
    """
    Verificar disponibilidad de un doctor en una fecha específica

    Query params: fecha (YYYY-MM-DD)
    """
    fecha_str = request.args.get('fecha')
    if not fecha_str:
        return jsonify({'error': 'Parámetro fecha es requerido'}), 400

    try:
        fecha = datetime.fromisoformat(fecha_str).date()
    except ValueError:
        return jsonify({'error': 'Formato de fecha inválido'}), 400

    # Buscar citas del doctor en esa fecha
    citas = Cita.query.filter(
        Cita.id_doctor == id_doctor,
        db.func.date(Cita.fecha) == fecha,
        Cita.estado != 'CANCELADA'
    ).all()

    horas_ocupadas = [c.fecha.strftime('%H:%M') for c in citas]

    return jsonify({
        'id_doctor': id_doctor,
        'fecha': fecha.isoformat(),
        'horas_ocupadas': horas_ocupadas,
        'total_citas': len(citas)
    }), 200
