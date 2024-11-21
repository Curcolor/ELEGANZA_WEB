from app import ma
from app.models.modelo_tipo_proveedor import TipoProveedor
from marshmallow import fields

class TipoProveedorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TipoProveedor
        load_instance = True
    
    id_tipo_proveedor = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    descripcion = fields.Str()

tipo_proveedor_schema = TipoProveedorSchema()
tipos_proveedor_schema = TipoProveedorSchema(many=True) 