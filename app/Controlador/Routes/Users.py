from flask import jsonify, request, render_template, Flask, url_for, redirect, flash, session
from app import app, db
from app.Modelo.models import *
from app.Controlador.Controllers.User import *  # Importar las funciones del servicio dump_usuario, dump_usuarios  # Importar funciones de schemas
from werkzeug.security import generate_password_hash, check_password_hash

# Rutas de páginas principales

# Formulario de registro
@app.route('/')
@app.route('/registro')
def registro():
    return render_template('registro.html', title='Registro')

# Formulario de inicio de sesión
@app.route('/login')
def login():
    return render_template('login.html', title='Iniciar Sesión')


# Verificar si hay un usuario en sesión
@app.route('/cuenta')
def cuenta():    
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    try:
        # Obtener el usuario de la base de datos
        usuario = Usuario.query.get(session['usuario_id'])
        if not usuario:
            return redirect(url_for('login'))
        return render_template('cuenta.html', title='Mi Cuenta', usuario=usuario)
    except Exception as e:
        print(f"Error al cargar datos de usuario: {str(e)}")
        return redirect(url_for('login'))
    

@app.route('/api/login', methods=['POST'])
def api_login():
    try:
        datos = request.get_json()
        email = datos.get('email')
        password = datos.get('password')
        
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario and check_password_hash(usuario.password, password):
            # Guardar ID del usuario en la sesión
            session['usuario_id'] = usuario.id_usuario
            
            return jsonify({
                'success': True,
                'mensaje': 'Inicio de sesión exitoso',
                'usuario': dump_usuario(usuario)
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
    
# Rutas de API para usuarios - Obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return dump_usuarios(usuarios)

# Obtener un usuario por ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return dump_usuario(usuario)

# Crear un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    try:
        datos = request.get_json()
        nuevo_usuario = crear_nuevo_usuario(datos)  # Usar la función del servicio
        return dump_usuario(nuevo_usuario), 201
    except Exception as e:
        print("Error:", str(e))
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
    
# Actualizar un usuario existente por ID

@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = obtener_usuario_por_id(id)  # Usar la función del servicio
    datos = request.get_json()
    
    try:
        usuario_actualizado = actualizar_usuario(usuario, datos)  # Usar la función del servicio
        return dump_usuario(usuario_actualizado)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Eliminar un usuario por ID    
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = obtener_usuario_por_id(id)  # Usar la función del servicio
    eliminar_usuario(usuario)  # Usar la función del servicio
    return '', 204

# Buscar un usuario por email
@app.route('/usuarios/email/<string:email>', methods=['GET'])
def buscar_usuario_por_email(email):
    usuario = Usuario.query.filter_by(email=email).first_or_404()
    return dump_usuario(usuario)

# Cerrar sesión
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))