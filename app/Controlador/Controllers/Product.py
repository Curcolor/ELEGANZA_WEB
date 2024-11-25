from app.Modelo.models import Producto
from marshmallow import Schema, fields
from app.Modelo.models import Producto, db

def obtener_producto_por_id(producto_id):
    return Producto.query.get(producto_id)

def crear_nuevo_producto(datos):
    nuevo_producto = Producto(
        nombre=datos['nombre'],
        id_proveedor=datos['id_proveedor'],
        precio=datos['precio'],
        stock=datos['stock'],
        categoria=datos['categoria'],
        descripcion=datos.get('descripcion'),
        imagen_url=datos.get('imagen_url'),
        descuento=datos.get('descuento', 0.00),
        destacado=datos.get('destacado', False)
    )
    db.session.add(nuevo_producto)
    db.session.commit()
    return nuevo_producto

def actualizar_producto(producto, datos):
    if 'nombre' in datos:
        producto.nombre = datos['nombre']
    if 'descripcion' in datos:
        producto.descripcion = datos['descripcion']
    if 'precio' in datos:
        producto.precio = datos['precio']
    if 'stock' in datos:
        producto.stock = datos['stock']
    if 'imagen_url' in datos:
        producto.imagen_url = datos['imagen_url']
    if 'categoria' in datos:
        producto.categoria = datos['categoria']
    if 'estado' in datos:
        producto.estado = datos['estado']
    if 'descuento' in datos:
        producto.descuento = datos['descuento']
    if 'destacado' in datos:
        producto.destacado = datos['destacado']
    
    db.session.commit()
    return producto

def eliminar_producto(producto):
    producto.estado = False  # Soft delete
    db.session.commit()


class ProductoSchema(Schema):
    id_producto = fields.Int()
    nombre = fields.Str()
    precio = fields.Float()
    stock = fields.Int()
    categoria = fields.Str()
    descripcion = fields.Str()
    imagen_url = fields.Str()
    descuento = fields.Float()
    destacado = fields.Bool()

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

def dump_producto(producto):
    return producto_schema.dump(producto)

def dump_productos(productos):
    return productos_schema.dump(productos)