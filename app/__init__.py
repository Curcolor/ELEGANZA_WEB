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

# Importar rutas después de definir db
from app.routes import *

