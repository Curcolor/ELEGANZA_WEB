from app import ma
from app.models.modelo_cupon import Cupon
from marshmallow import fields

class CuponSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cupon
        load_instance = True
    
    id_cupon = fields.Int(dump_only=True)
    codigo = fields.Str(required=True)
    valor = fields.Decimal(required=True)
    solo_vip = fields.Bool()
    fecha_inicio = fields.DateTime(required=True)
    fecha_fin = fields.DateTime(required=True)
    estado = fields.Bool()

cupon_schema = CuponSchema()
cupones_schema = CuponSchema(many=True) 