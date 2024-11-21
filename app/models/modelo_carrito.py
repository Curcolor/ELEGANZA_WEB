from app import db
from datetime import datetime, UTC
from sqlalchemy import Numeric  # Importamos Numeric

class CarritoItem(db.Model):
    __tablename__ = 'carrito_items'
    
    id_item = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id_producto'), nullable=False)
    cantidad = db.Column(db.Integer, default=1, nullable=False)
    precio_unitario = db.Column(Numeric(10,2), nullable=False)  # Cambiado a Numeric
    total = db.Column(Numeric(10,2), nullable=False)  # Cambiado a Numeric
    fecha_agregado = db.Column(db.DateTime, default=lambda: datetime.now(UTC), nullable=False)

    def __init__(self, id_usuario, id_producto, cantidad=1, precio_unitario=0.00):
        self.id_usuario = id_usuario
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.total = precio_unitario * cantidad

    def __repr__(self):
        return f'<CarritoItem {self.id_item}>' 