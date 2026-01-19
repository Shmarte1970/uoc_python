"""
Modelo de Usuario para autenticación y autorización
"""
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(db.Model):
    """
    Modelo de Usuario del sistema OdontoCare

    Roles disponibles: admin, medico, secretaria, paciente
    """
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(20), nullable=False, default='paciente')

    # Relaciones
    paciente = db.relationship('Paciente', backref='usuario', uselist=False)
    doctor = db.relationship('Doctor', backref='usuario', uselist=False)

    def set_password(self, password):
        """Hashea y guarda la contraseña"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Verifica la contraseña"""
        return check_password_hash(self.password, password)

    def to_dict(self):
        """Convierte el usuario a diccionario (sin password)"""
        return {
            'id_usuario': self.id_usuario,
            'username': self.username,
            'rol': self.rol
        }

    def __repr__(self):
        return f'<Usuario {self.username}>'
