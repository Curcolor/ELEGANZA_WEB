from app import ma
from app.models.modelo_carrito import CarritoItem
from marshmallow import fields

class CarritoItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CarritoItem
        load_instance = True
        include_relationships = True

    id_carrito_item = fields.Int(dump_only=True)
    id_usuario = fields.Int(required=True)
    id_producto = fields.Int(required=True)
    cantidad = fields.Int(required=True)
    fecha_creacion = fields.DateTime(dump_only=True)
    
    # Campos anidados para mostrar información del producto
    producto = fields.Nested('ProductoSchema', only=['nombre', 'precio', 'imagen'])

# Crear instancias del schema para un solo item o múltiples items
carrito_item_schema = CarritoItemSchema()
carrito_items_schema = CarritoItemSchema(many=True) 