from app import ma
from app.models.modelo_carrito import CarritoItem
from marshmallow import fields

class CarritoItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CarritoItem
        load_instance = True
        include_fk = True
    
    id_item = fields.Int(dump_only=True)
    id_usuario = fields.Int(required=True)
    id_producto = fields.Int(required=True)
    cantidad = fields.Int()
    precio_unitario = fields.Decimal(required=True)
    total = fields.Decimal(dump_only=True)
    fecha_agregado = fields.DateTime(dump_only=True)

carrito_item_schema = CarritoItemSchema()
carrito_items_schema = CarritoItemSchema(many=True) 