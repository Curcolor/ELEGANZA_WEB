from app import db
from datetime import datetime, UTC

class SuscripcionVip(db.Model):
    __tablename__ = 'suscripciones_vip'
    
    id_suscripcion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_plan = db.Column(db.Integer, db.ForeignKey('planes_vip.id_plan'), nullable=False)
    fecha_inicio = db.Column(db.DateTime, default=lambda: datetime.now(UTC), nullable=False)
    fecha_fin = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.Boolean, default=True, nullable=True)

    def __init__(self, id_usuario, id_plan, fecha_inicio, fecha_fin, estado=True):
        self.id_usuario = id_usuario
        self.id_plan = id_plan
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado

    def __repr__(self):
        return f'<SuscripcionVip {self.id_usuario}>' 