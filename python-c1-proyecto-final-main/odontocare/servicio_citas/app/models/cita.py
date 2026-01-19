"""
Modelo de Cita Médica
"""
from app import db
from datetime import datetime


class Cita(db.Model):
    """
    Modelo de Cita Médica del sistema OdontoCare

    Estados: PROGRAMADA, COMPLETADA, CANCELADA
    """
    __tablename__ = 'citas'

    id_cita = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    motivo = db.Column(db.String(500), nullable=True)
    estado = db.Column(db.String(20), nullable=False, default='PROGRAMADA')

    # Foreign keys (referencias a IDs de otros servicios)
    id_paciente = db.Column(db.Integer, nullable=False)
    id_doctor = db.Column(db.Integer, nullable=False)
    id_centro = db.Column(db.Integer, nullable=False)
    id_usuario_registra = db.Column(db.Integer, nullable=False)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        """Convierte la cita a diccionario"""
        return {
            'id_cita': self.id_cita,
            'fecha': self.fecha.isoformat() if self.fecha else None,
            'motivo': self.motivo,
            'estado': self.estado,
            'id_paciente': self.id_paciente,
            'id_doctor': self.id_doctor,
            'id_centro': self.id_centro,
            'id_usuario_registra': self.id_usuario_registra,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f'<Cita {self.id_cita} - {self.fecha}>'
