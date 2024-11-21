from flask import jsonify, request, render_template, Flask, url_for, redirect, flash, session
from app import app, db
from app.models.modelo_usuario import Usuario
from app.schemas.schemas_usuario import usuario_schema, usuarios_schema
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.modelo_producto import Producto
from app.schemas.schemas_producto import producto_schema, productos_schema
from app.models.modelo_carrito import CarritoItem
from app.schemas.schemas_carrito import carrito_item_schema, carrito_items_schema

# Rutas de páginas principales
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Inicio')

@app.route('/base.html')
def base():
    return render_template('base.html', title='Base')

@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html', title='Ayuda')

@app.route('/carrito')
def carrito():
    return render_template('carrito.html', title='Carrito')

@app.route('/catalogo')
def catalogo():
    # Obtener productos de la base de datos
    productos = Producto.query.filter_by(estado=True).all()
    return render_template('catalogo.html', title='Catalogo', productos=productos)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html', title='Checkout')

@app.route('/cuenta')
def cuenta():
    return render_template('cuenta.html', title='Cuenta')


@app.route('/producto')
def producto():
    return render_template('producto.html', title='Producto')

@app.route('/registro')
def registro():
    return render_template('registro.html', title='Registro')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', title='Servicios')


@app.route('/sobre_nosotros')
def sobre_nosotros():
    return render_template('sobre_nosotros.html', title='Sobre Nosotros')

@app.route('/vip')
def vip():
    return render_template('vip.html', title='VIP')

@app.route('/login')
def login():
    return render_template('login.html', title='Iniciar Sesión')

@app.route('/api/login', methods=['POST'])
def api_login():
    try:
        datos = request.get_json()
        email = datos.get('email')
        password = datos.get('password')
        
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario and check_password_hash(usuario.password, password):
            return jsonify({
                'success': True,
                'mensaje': 'Inicio de sesión exitoso',
                'usuario': usuario_schema.dump(usuario)
            })
        else:
            return jsonify({
                'success': False,
                'mensaje': 'Email o contraseña incorrectos'
            }), 401
            
    except Exception as e:
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400

# Rutas de API para usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return jsonify(usuarios_schema.dump(usuarios))

@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify(usuario_schema.dump(usuario))

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    try:
        datos = request.get_json()
        
        nuevo_usuario = Usuario(
            nombre=datos['nombre'],
            email=datos['email'],
            password=generate_password_hash(datos['password']),
            id_rol=datos.get('id_rol', 2),  # valor por defecto 2
            es_vip=datos.get('es_vip', False),  # valor por defecto False
            estado=datos.get('estado', True)  # valor por defecto True
        )
        
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        return usuario_schema.dump(nuevo_usuario), 201
        
    except Exception as e:
        print("Error:", str(e))
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    datos = request.get_json()
    
    if 'nombre' in datos:
        usuario.nombre = datos['nombre']
    if 'apellido' in datos:
        usuario.apellido = datos['apellido']
    if 'email' in datos:
        if Usuario.query.filter_by(email=datos['email']).first() and datos['email'] != usuario.email:
            return jsonify({'error': 'El email ya está registrado'}), 400
        usuario.email = datos['email']
    if 'password' in datos:
        usuario.password = generate_password_hash(datos['password'])
    if 'activo' in datos:
        usuario.activo = datos['activo']
    
    try:
        db.session.commit()
        return jsonify(usuario_schema.dump(usuario))
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    usuario.activo = False
    db.session.commit()
    return '', 204

@app.route('/usuarios/email/<string:email>', methods=['GET'])
def buscar_usuario_por_email(email):
    usuario = Usuario.query.filter_by(email=email).first_or_404()
    return jsonify(usuario_schema.dump(usuario))

# Rutas para productos
@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    try:
        # Obtener parámetros de consulta
        categoria = request.args.get('categoria')
        destacados = request.args.get('destacados')
        
        query = Producto.query.filter_by(estado=True)
        
        if categoria:
            query = query.filter_by(categoria=categoria)
        if destacados:
            query = query.filter_by(destacado=True)
            
        productos = query.all()
        return jsonify({
            'success': True,
            'productos': productos_schema.dump(productos)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400

@app.route('/api/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    try:
        producto = Producto.query.get_or_404(id)
        return jsonify({
            'success': True,
            'producto': producto_schema.dump(producto)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 404

@app.route('/api/productos', methods=['POST'])
def crear_producto():
    try:
        datos = request.get_json()
        
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
        
        return jsonify({
            'success': True,
            'mensaje': 'Producto creado exitosamente',
            'producto': producto_schema.dump(nuevo_producto)
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400

@app.route('/api/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    try:
        producto = Producto.query.get_or_404(id)
        datos = request.get_json()
        
        # Actualizar campos si están presentes en la solicitud
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
        
        return jsonify({
            'success': True,
            'mensaje': 'Producto actualizado exitosamente',
            'producto': producto_schema.dump(producto)
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400

@app.route('/api/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    try:
        producto = Producto.query.get_or_404(id)
        producto.estado = False  # Soft delete
        db.session.commit()
        
        return jsonify({
            'success': True,
            'mensaje': 'Producto eliminado exitosamente'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400

# Rutas adicionales para funcionalidades específicas
@app.route('/api/productos/categoria/<string:categoria>', methods=['GET'])
def productos_por_categoria(categoria):
    try:
        productos = Producto.query.filter_by(categoria=categoria, estado=True).all()
        return jsonify({
            'success': True,
            'productos': productos_schema.dump(productos)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400

@app.route('/api/productos/destacados', methods=['GET'])
def productos_destacados():
    try:
        productos = Producto.query.filter_by(destacado=True, estado=True).all()
        return jsonify({
            'success': True,
            'productos': productos_schema.dump(productos)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400

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
            'productos': productos_schema.dump(productos)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400

@app.route('/api/productos/actualizar-stock/<int:id>', methods=['PATCH'])
def actualizar_stock(id):
    try:
        producto = Producto.query.get_or_404(id)
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
            'producto': producto_schema.dump(producto)
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400

@app.route('/api/carrito', methods=['POST'])
def agregar_al_carrito():
    try:
        datos = request.get_json()
        
        nuevo_item = CarritoItem(
            id_usuario=datos['id_usuario'],
            id_producto=datos['id_producto'],
            cantidad=datos.get('cantidad', 1)
        )
        
        db.session.add(nuevo_item)
        db.session.commit()
        
        # Obtener el total de items en el carrito
        total_items = CarritoItem.query.filter_by(
            id_usuario=datos['id_usuario']
        ).count()
        
        return jsonify({
            'success': True,
            'mensaje': 'Producto agregado al carrito',
            'total_items': total_items
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400

@app.route('/api/carrito/<int:id_usuario>', methods=['GET'])
def obtener_carrito(id_usuario):
    try:
        items = CarritoItem.query.filter_by(id_usuario=id_usuario).all()
        return jsonify({
            'success': True,
            'items': carrito_items_schema.dump(items)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400

@app.route('/api/productos', methods=['POST'])
def agregar_producto():
    try:
        datos = request.get_json()
        
        nuevo_producto = Producto(
            nombre=datos['nombre'],
            id_proveedor=datos['id_proveedor'],
            precio=datos['precio'],
            stock=datos['stock'],
            descripcion=datos.get('descripcion'),
            imagen=datos.get('imagen'),
            estado=datos.get('estado', True),
            descuento=datos.get('descuento', 0.00),
            destacado=datos.get('destacado', False)
        )
        
        db.session.add(nuevo_producto)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'mensaje': 'Producto agregado exitosamente',
            'producto': {
                'id': nuevo_producto.id_producto,
                'nombre': nuevo_producto.nombre,
                'precio': str(nuevo_producto.precio)
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'mensaje': str(e)
        }), 400

@app.route('/agregar-carrito/<int:id_producto>', methods=['POST'])
def agregar_carrito(id_producto):
    if 'carrito' not in session:
        session['carrito'] = {}
    
    # Obtener datos del form
    cantidad = int(request.form.get('cantidad', 1))
    
    producto = Producto.query.get_or_404(id_producto)
    if producto.stock < cantidad:
        return jsonify({
            'success': False,
            'message': 'No hay suficiente stock disponible'
        })
    
    carrito = session['carrito']
    if str(id_producto) in carrito:
        carrito[str(id_producto)] += cantidad
    else:
        carrito[str(id_producto)] = cantidad
    
    session['carrito'] = carrito
    
    return jsonify({
        'success': True,
        'message': 'Producto agregado al carrito'
    })

@app.route('/obtener-total-carrito')
def obtener_total_carrito():
    carrito = session.get('carrito', {})
    total = sum(carrito.values())
    return jsonify({'total': total})