from app.Modelo.models import Pedido
from marshmallow import Schema, fields
from app.Modelo.models import Pedido, db

def obtener_pedido_por_id(pedido_id):
    return Pedido.query.get(pedido_id)

def crear_nuevo_pedido(datos):
    nuevo_pedido = Pedido(
        id_usuario=datos['id_usuario'],
        total=datos['total'],
        direccion_envio=datos['direccion_envio'],
        metodo_pago=datos['metodo_pago']
    )
    db.session.add(nuevo_pedido)
    db.session.commit()
    return nuevo_pedido

def actualizar_pedido(pedido, datos):
    if 'total' in datos:
        pedido.total = datos['total']
    if 'direccion_envio' in datos:
        pedido.direccion_envio = datos['direccion_envio']
    if 'metodo_pago' in datos:
        pedido.metodo_pago = datos['metodo_pago']
    if 'estado' in datos:
        pedido.estado = datos['estado']
    
    db.session.commit()
    return pedido

def eliminar_pedido(pedido):
    db.session.delete(pedido)
    db.session.commit()



class PedidoSchema(Schema):
    id_pedido = fields.Int()
    id_usuario = fields.Int()
    total = fields.Float()
    direccion_envio = fields.Str()
    metodo_pago = fields.Str()
    estado = fields.Str()
    fecha = fields.DateTime()

pedido_schema = PedidoSchema()
pedidos_schema = PedidoSchema(many=True)

def dump_pedido(pedido):
    return pedido_schema.dump(pedido)

def dump_pedidos(pedidos):
    return pedidos_schema.dump(pedidos)
