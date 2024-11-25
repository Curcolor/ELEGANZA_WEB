from app import ma
from app.models.modelo_suscripcion_vip import SuscripcionVip
from marshmallow import fields

class SuscripcionVipSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SuscripcionVip
        load_instance = True
        include_fk = True
    
    id_suscripcion = fields.Int(dump_only=True)
    id_usuario = fields.Int(required=True)
    id_plan = fields.Int(required=True)
    fecha_inicio = fields.DateTime(required=True)
    fecha_fin = fields.DateTime(required=True)
    estado = fields.Bool()

suscripcion_vip_schema = SuscripcionVipSchema()
suscripciones_vip_schema = SuscripcionVipSchema(many=True) 