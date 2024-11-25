from app import db

class DetallePedido(db.Model):
    __tablename__ = 'detalles_pedido'
    
    id_detalle = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedidos.id_pedido'), nullable=False)
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id_producto'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Decimal(10,2), nullable=False)
    subtotal = db.Column(db.Decimal(10,2), nullable=False)

    def __init__(self, id_pedido, id_producto, cantidad, precio_unitario):
        self.id_pedido = id_pedido
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = cantidad * precio_unitario

    def __repr__(self):
        return f'<DetallePedido {self.id_detalle}>' 