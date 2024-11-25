from app import ma
from app.models.modelo_pedido import Pedido
from marshmallow import fields

class PedidoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pedido
        load_instance = True
        include_fk = True
    
    id_pedido = fields.Int(dump_only=True)
    id_usuario = fields.Int(required=True)
    fecha_pedido = fields.DateTime(dump_only=True)
    estado_pedido = fields.Str(required=True)
    total = fields.Decimal(required=True)
    direccion_envio = fields.Str(required=True)
    metodo_pago = fields.Str(required=True)

pedido_schema = PedidoSchema()
pedidos_schema = PedidoSchema(many=True) 