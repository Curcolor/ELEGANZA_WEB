from app import ma
from app.models.modelo_opinion import Opinion
from marshmallow import fields

class OpinionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Opinion
        load_instance = True
        include_fk = True
    
    id_opinion = fields.Int(dump_only=True)
    id_usuario = fields.Int(required=True)
    id_producto = fields.Int(required=True)
    calificacion = fields.Int(required=True)
    comentario = fields.Str()
    fecha = fields.DateTime(dump_only=True)
    estado = fields.Bool()

opinion_schema = OpinionSchema()
opiniones_schema = OpinionSchema(many=True) 