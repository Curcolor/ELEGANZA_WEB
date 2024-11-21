from app import ma
from app.models.modelo_proveedor import Proveedor
from marshmallow import fields

class ProveedorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Proveedor
        load_instance = True
        include_fk = True
    
    id_proveedor = fields.Int(dump_only=True)
    id_tipo_proveedor = fields.Int(required=True)
    nombre = fields.Str(required=True)
    direccion = fields.Str()
    telefono = fields.Str()
    email = fields.Email()
    estado = fields.Bool()

proveedor_schema = ProveedorSchema()
proveedores_schema = ProveedorSchema(many=True) 