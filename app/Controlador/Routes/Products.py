from flask import jsonify, request, render_template
from app import app, db
from app.Modelo.models import *
from app.Controlador.Controllers.Product import *  # Importar las funciones del servicio
# Información de los productos
@app.route('/producto')
def producto():
    return render_template('producto.html', title='Producto')

# Obtener productos de la base de datos
@app.route('/catalogo')
def catalogo():
    productos = Producto.query.filter_by(estado=True).all()
    return render_template('catalogo.html', title='Catalogo', productos=productos)

# Formulario de envío de productos
@app.route('/checkout')
def checkout():
    user_id = 1  # ID temporal fijo
    total = 100  # Total temporal fijo
    
    return render_template(
        'checkout.html', 
        title='Checkout',
        user_id=user_id,
        total=total
    )

# Rutas de API para productos - Obtener todos los productos
@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    productos = Producto.query.filter_by(estado=True).all()
    return dump_productos(productos)  # Usar la función del schema

# Crear un nuevo producto
@app.route('/api/productos', methods=['POST'])
def crear_producto():
    try:
        datos = request.get_json()
        nuevo_producto = crear_nuevo_producto(datos)  # Usar la función del servicio
        return dump_producto(nuevo_producto), 201  # Usar la función del schema
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'mensaje': str(e)}), 400

# Actualizar un producto existente por ID
@app.route('/api/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    producto = obtener_producto_por_id(id)  # Usar la función del servicio
    datos = request.get_json()
    
    try:
        producto_actualizado = actualizar_producto(producto, datos)  # Usar la función del servicio
        return dump_producto(producto_actualizado)  # Usar la función del schema
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'mensaje': str(e)}), 400

# Eliminar un producto existente por ID
@app.route('/api/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    try:
        producto = obtener_producto_por_id(id)  # Usar la función del servicio
        eliminar_producto(producto)  # Usar la función del servicio
        return jsonify({'success': True, 'mensaje': 'Producto eliminado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'mensaje': str(e)}), 400

# Buscar productos por nombre
@app.route('/api/productos/buscar', methods=['GET'])
def buscar_productos():
    try:
        termino = request.args.get('q', '')
        productos = Producto.query.filter(
            Producto.estado == True,
            Producto.nombre.ilike(f'%{termino}%')
        ).all()
        
        return jsonify({
            'success': True,
            'productos': dump_productos(productos)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400

# Obtener productos por categoría
@app.route('/api/productos/categoria/<string:categoria>', methods=['GET'])
def productos_por_categoria(categoria):
    try:
        productos = Producto.query.filter_by(categoria=categoria, estado=True).all()
        return jsonify({
            'success': True,
            'productos': dump_productos(productos)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400

# Obtener productos destacados
@app.route('/api/productos/destacados', methods=['GET'])
def productos_destacados():
    try:
        productos = Producto.query.filter_by(destacado=True, estado=True).all()
        return jsonify({
            'success': True,
            'productos': dump_productos(productos)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400

# Actualizar stock de un producto
@app.route('/api/productos/actualizar-stock/<int:id>', methods=['PATCH'])
def actualizar_stock(id):
    try:
        producto = obtener_producto_por_id(id)  # Usar la función del servicio
        datos = request.get_json()
        
        if 'stock' not in datos:
            return jsonify({
                'success': False,
                'mensaje': 'Se requiere el campo stock'
            }), 400
            
        producto.stock = datos['stock']
        db.session.commit()
        
        return jsonify({
            'success': True,
            'mensaje': 'Stock actualizado exitosamente',
            'producto': dump_producto(producto)  # Usar la función del schema
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400
    
