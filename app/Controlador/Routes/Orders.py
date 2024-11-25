# app/Controlador/Routes/Orders.py
from flask import jsonify, request, render_template
from app import app, db
from app.Modelo.models import *
from app.Controlador.Controllers.Order import *  # Importar las funciones del servicio
# Rutas de API para pedidos

@app.route('/api/pedidos', methods=['POST'])
def crear_pedido():
    try:
        datos = request.get_json()
        nuevo_pedido = crear_nuevo_pedido(datos)  # Usar la función del servicio
        return dump_pedido(nuevo_pedido), 201  # Usar la función del schema
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'mensaje': str(e)}), 400

@app.route('/api/pedidos/<int:id>', methods=['PUT'])
def actualizar_pedido_api(id):
    pedido = obtener_pedido_por_id(id)  # Usar la función del servicio
    datos = request.get_json()
    
    try:
        pedido_actualizado = actualizar_pedido(pedido, datos)  # Usar la función del servicio
        return dump_pedido(pedido_actualizado)  # Usar la función del schema
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'mensaje': str(e)}), 400

@app.route('/api/pedidos/<int:id>', methods=['DELETE'])
def eliminar_pedido_api(id):
    try:
        pedido = obtener_pedido_por_id(id)  # Usar la función del servicio
        eliminar_pedido(pedido)  # Usar la función del servicio
        return jsonify({'success': True, 'mensaje': 'Pedido eliminado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'mensaje': str(e)}), 400

@app.route('/api/pedidos', methods=['GET'])
def obtener_pedidos():
    pedidos = Pedido.query.all()
    return dump_pedidos(pedidos)  # Usar la función del schema

@app.route('/api/pedidos/<int:id>', methods=['GET'])
def obtener_pedido(id):
    pedido = obtener_pedido_por_id(id)  # Usar la función del servicio
    if pedido:
        return dump_pedido(pedido)  # Usar la función del schema
    return jsonify({'success': False, 'mensaje': 'Pedido no encontrado'}), 404