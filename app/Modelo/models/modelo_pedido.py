from app import db
from datetime import datetime
from sqlalchemy import DECIMAL

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    
    id_pedido = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    total = db.Column(DECIMAL(10,2), nullable=False)
    direccion_envio = db.Column(db.String(255), nullable=False)
    metodo_pago = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(50), default='Pendiente')
    id_detalle = db.Column(db.Integer, nullable=True)

    # Relaciones
    usuario = db.relationship('Usuario', backref=db.backref('pedidos', lazy=True))

    def __init__(self, id_usuario, total, direccion_envio, metodo_pago):
        self.id_usuario = id_usuario
        self.total = total
        self.direccion_envio = direccion_envio
        self.metodo_pago = metodo_pago
        self.estado = 'Pendiente'

    def __repr__(self):
        return f'<Pedido {self.id_pedido}>' 