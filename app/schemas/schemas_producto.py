from app import ma
from app.models.modelo_producto import Producto
from marshmallow import fields

class ProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Producto
        load_instance = True
        include_fk = True
    
    id_producto = fields.Int(dump_only=True)
    id_proveedor = fields.Int(required=True)
    nombre = fields.Str(required=True)
    descripcion = fields.Str()
    precio = fields.Decimal(required=True)
    stock = fields.Int(required=True)
    imagen = fields.Str()
    estado = fields.Bool()

    # Podemos agregar un campo calculado para el precio con descuento
    precio_final = fields.Method("calcular_precio_final")

    def calcular_precio_final(self, obj):
        if obj.descuento:
            descuento = float(obj.precio) * float(obj.descuento)
            return float(obj.precio) - descuento
        return float(obj.precio)

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True) 