from app import ma
from app.models.modelo_opinion_mod import OpinionMod
from marshmallow import fields

class OpinionModSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OpinionMod
        load_instance = True
        include_fk = True
    
    id_opinion_mod = fields.Int(dump_only=True)
    id_opinion = fields.Int(required=True)
    id_moderador = fields.Int(required=True)
    accion = fields.Str(required=True)
    motivo = fields.Str()
    fecha = fields.DateTime(dump_only=True)

opinion_mod_schema = OpinionModSchema()
opiniones_mod_schema = OpinionModSchema(many=True) 