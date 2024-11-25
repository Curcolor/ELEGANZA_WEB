from app import ma
from app.models.modelo_plan_vip import PlanVip
from marshmallow import fields

class PlanVipSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PlanVip
        load_instance = True
    
    id_plan = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    descripcion = fields.Str()
    precio = fields.Decimal(required=True)
    duracion_meses = fields.Int(required=True)
    estado = fields.Bool()

plan_vip_schema = PlanVipSchema()
planes_vip_schema = PlanVipSchema(many=True) 