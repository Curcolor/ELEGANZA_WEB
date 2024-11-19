from datetime import datetime, UTC
from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_rol = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    es_vip = db.Column(db.Boolean, default=False, nullable=True)
    estado = db.Column(db.Boolean, default=True, nullable=True)
    fecha_registro = db.Column(db.DateTime, default=lambda: datetime.now(UTC), nullable=True)

    def __init__(self, nombre, email, password, id_rol=2, es_vip=False, estado=True):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.id_rol = id_rol
        self.es_vip = es_vip
        self.estado = estado
        self.fecha_registro = datetime.now(UTC)

    def __repr__(self):
        return f'<Usuario {self.email}>'