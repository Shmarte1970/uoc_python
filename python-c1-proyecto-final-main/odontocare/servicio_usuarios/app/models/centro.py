"""
Modelo de Centro Médico
"""
from app import db


class Centro(db.Model):
    """
    Modelo de Centro Médico/Clínica del sistema OdontoCare
    """
    __tablename__ = 'centros'

    id_centro = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        """Convierte el centro a diccionario"""
        return {
            'id_centro': self.id_centro,
            'nombre': self.nombre,
            'direccion': self.direccion
        }

    def __repr__(self):
        return f'<Centro {self.nombre}>'
