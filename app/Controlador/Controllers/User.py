from app.Modelo.models import Usuario, db
from werkzeug.security import generate_password_hash

def obtener_usuario_por_id(usuario_id):
    return Usuario.query.get(usuario_id)

def crear_nuevo_usuario(datos):
    nuevo_usuario = Usuario(
        nombre=datos['nombre'],
        email=datos['email'],
        password=generate_password_hash(datos['password']),
        id_rol=datos.get('id_rol', 2),
        es_vip=datos.get('es_vip', False),
        estado=datos.get('estado', True)
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return nuevo_usuario

def actualizar_usuario(usuario, datos):
    if 'nombre' in datos:
        usuario.nombre = datos['nombre']
    if 'apellido' in datos:
        usuario.apellido = datos['apellido']
    if 'email' in datos:
        if Usuario.query.filter_by(email=datos['email']).first() and datos['email'] != usuario.email:
            raise ValueError('El email ya está registrado')
        usuario.email = datos['email']
    if 'password' in datos:
        usuario.password = generate_password_hash(datos['password'])
    if 'activo' in datos:
        usuario.activo = datos['activo']
    db.session.commit()
    return usuario

def eliminar_usuario(usuario):
    usuario.activo = False
    db.session.commit()

from app.Modelo.models import Usuario
from marshmallow import Schema, fields

class UsuarioSchema(Schema):
    id_usuario = fields.Int()
    nombre = fields.Str()
    email = fields.Str()
    es_vip = fields.Bool()
    estado = fields.Bool()

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

def dump_usuario(usuario):
    return usuario_schema.dump(usuario)

def dump_usuarios(usuarios):
    return usuarios_schema.dump(usuarios)