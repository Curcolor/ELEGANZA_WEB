from app import ma
from app.models.modelo_rol import Rol
from marshmallow import fields

class RolSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rol
        load_instance = True
        include_fk = True
    
    id_rol = fields.Int(dump_only=True)
    nombre_de_rol = fields.Str(required=True)

rol_schema = RolSchema()
roles_schema = RolSchema(many=True) 