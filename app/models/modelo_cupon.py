from app import db
from datetime import datetime, UTC

class Cupon(db.Model):
    __tablename__ = 'cupones'
    
    id_cupon = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigo = db.Column(db.String(20), nullable=False, unique=True)
    valor = db.Column(db.Decimal(10,2), nullable=False)
    solo_vip = db.Column(db.Boolean, default=True, nullable=True)
    fecha_inicio = db.Column(db.DateTime, nullable=False)
    fecha_fin = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.Boolean, default=True, nullable=True)

    def __init__(self, codigo, valor, fecha_inicio, fecha_fin, solo_vip=True, estado=True):
        self.codigo = codigo
        self.valor = valor
        self.solo_vip = solo_vip
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado

    def __repr__(self):
        return f'<Cupon {self.codigo}>' 