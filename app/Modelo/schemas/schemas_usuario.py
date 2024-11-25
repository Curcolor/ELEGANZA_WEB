from app import ma, db
from app.models.modelo_usuario import Usuario
from marshmallow import fields

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True
        include_fk = True
        sqla_session = db.session
    
    id_usuario = fields.Int(dump_only=True)
    id_rol = fields.Int()
    nombre = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    es_vip = fields.Bool()
    estado = fields.Bool()
    fecha_registro = fields.DateTime(dump_only=True)

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)