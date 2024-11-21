from app import ma
from app.models.modelo_detalle_pedido import DetallePedido
from marshmallow import fields

class DetallePedidoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DetallePedido
        load_instance = True
        include_fk = True
    
    id_detalle = fields.Int(dump_only=True)
    id_pedido = fields.Int(required=True)
    id_producto = fields.Int(required=True)
    cantidad = fields.Int(required=True)
    precio_unitario = fields.Decimal(required=True)
    subtotal = fields.Decimal(required=True)

detalle_pedido_schema = DetallePedidoSchema()
detalles_pedido_schema = DetallePedidoSchema(many=True) 