from flask import jsonify, request, render_template
from app import app, db
from app.models.modelo_usuario import Usuario
from app.schemas.schemas_usuario import usuario_schema, usuarios_schema
from werkzeug.security import generate_password_hash

# Rutas de páginas principales
# Rutas de páginas principales
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', title='Inicio')

@app.route('/ayuda.html')
def ayuda():
    return render_template('ayuda.html', title='Ayuda')

@app.route('/carrito.html')
def carrito():
    return render_template('carrito.html', title='Carrito')

@app.route('/catalogo.html')
def catalogo():
    return render_template('catalogo.html', title='Catalogo')

@app.route('/checkout.html')
def checkout():
    return render_template('checkout.html', title='Checkout')

@app.route('/cuenta.html')
def cuenta():
    return render_template('cuenta.html', title='Cuenta')


@app.route('/producto.html')
def producto():
    return render_template('producto.html', title='Producto')

@app.route('/registro.html')
def registro():
    return render_template('registro.html', title='Registro')

@app.route('/servicios.html')
def servicios():
    return render_template('servicios.html', title='Servicios')


@app.route('/sobre-nosotros.html')
def sobre_nosotros():
    return render_template('sobre-nosotros.html', title='Sobre Nosotros')

@app.route('/vip.html')
def vip():
    return render_template('vip.html', title='VIP')


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