from app import db
from datetime import datetime, UTC

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    
    id_pedido = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    fecha_pedido = db.Column(db.DateTime, default=lambda: datetime.now(UTC), nullable=False)
    estado_pedido = db.Column(db.String(50), nullable=False)
    total = db.Column(db.Decimal(10,2), nullable=False)
    direccion_envio = db.Column(db.Text, nullable=False)
    metodo_pago = db.Column(db.String(50), nullable=False)

    def __init__(self, id_usuario, total, direccion_envio, metodo_pago, estado_pedido='Pendiente'):
        self.id_usuario = id_usuario
        self.total = total
        self.direccion_envio = direccion_envio
        self.metodo_pago = metodo_pago
        self.estado_pedido = estado_pedido

    def __repr__(self):
        return f'<Pedido {self.id_pedido}>' 