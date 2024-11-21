from app import db
from sqlalchemy import Numeric

class Producto(db.Model):
    __tablename__ = 'productos'
    
    id_producto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_proveedor = db.Column(db.Integer, db.ForeignKey('proveedores.id_proveedor'), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(Numeric(10,2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    imagen = db.Column(db.String(255), nullable=True)
    estado = db.Column(db.Boolean, default=True, nullable=True)
    descuento = db.Column(Numeric(5,2), default=0.00, nullable=False)

    def __init__(self, nombre, id_proveedor, precio, stock, 
                 descripcion=None, imagen=None, estado=True, descuento=0.00):
        self.nombre = nombre
        self.id_proveedor = id_proveedor
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.imagen = imagen
        self.estado = estado
        self.descuento = descuento

    def __repr__(self):
        return f'<Producto {self.nombre}>' 