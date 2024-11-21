from app import db
from datetime import datetime

class CarritoItem(db.Model):
    __tablename__ = 'carrito_items'
    
    id_carrito_item = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario', ondelete='CASCADE'), nullable=False)
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id_producto', ondelete='CASCADE'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False, default=1)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    # Relaciones
    usuario = db.relationship('Usuario', backref=db.backref('carrito_items', lazy=True))
    producto = db.relationship('Producto', backref=db.backref('carrito_items', lazy=True))

    def __init__(self, id_usuario, id_producto, cantidad=1):
        self.id_usuario = id_usuario
        self.id_producto = id_producto
        self.cantidad = cantidad

    def __repr__(self):
        return f'<CarritoItem {self.id_carrito_item}>' 