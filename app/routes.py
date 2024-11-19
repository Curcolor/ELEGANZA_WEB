from flask import jsonify, request, render_template
from app import app, db
from app.models.modelo_usuario import Usuario
from app.schemas.schemas_usuario import usuario_schema, usuarios_schema
from werkzeug.security import generate_password_hash

# Rutas de páginas principales
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Inicio')

@app.route('/otros')
def otros():
    return render_template('otros.html', title='Otros')

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
        
        # Verificar si el email ya existe
        if Usuario.query.filter_by(email=datos['email']).first():
            return jsonify({'error': 'El email ya está registrado'}), 400
            
        nuevo_usuario = Usuario(
            nombre=datos['nombre'],
            apellido=datos['apellido'],
            email=datos['email'],
            password=generate_password_hash(datos['password'])
        )
        
        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify(usuario_schema.dump(nuevo_usuario)), 201
        
    except Exception as e:
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
    usuario.activo = False  # Borrado lógico
    db.session.commit()
    return '', 204

@app.route('/usuarios/email/<string:email>', methods=['GET'])
def buscar_usuario_por_email(email):
    usuario = Usuario.query.filter_by(email=email).first_or_404()
    return jsonify(usuario_schema.dump(usuario))