from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash
from config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Importar modelos y schemas después de crear db
from app.models.modelo_usuario import Usuario
from app.schemas.schemas_usuario import usuario_schema, usuarios_schema

# Rutas de páginas principales
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Inicio')

@app.route('/otros')
def otros():
    return render_template('otros.html', title='Otros')

@app.route('/registro')
def registro():
    return render_template('registro.html', title='Registro')

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