from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash
from config import Config
import os
import logging

# Configurar logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuración de la aplicación
try:
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = os.environ.get('SECRET_KEY') or 'tu_clave_secreta'
    
    logger.info(f"Conectando a la base de datos: {Config.SQLALCHEMY_DATABASE_URI}")
    
    # Inicializar extensiones
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    
    # Ruta de healthcheck básica
    @app.route('/health')
    def health_check():
        try:
            # Verificar conexión a la base de datos
            db.session.execute('SELECT 1')
            return jsonify({'status': 'healthy', 'database': 'connected'}), 200
        except Exception as e:
            logger.error(f"Error en health check: {str(e)}")
            return jsonify({'status': 'unhealthy', 'error': str(e)}), 500

    @app.route('/')
    def index():
        return jsonify({'status': 'ok'}), 200

    # Manejadores de errores
    @app.errorhandler(500)
    def handle_500(error):
        logger.error(f"Error 500: {str(error)}")
        return jsonify({'error': 'Internal Server Error'}), 500

    @app.errorhandler(404)
    def handle_404(error):
        return jsonify({'error': 'Not Found'}), 404

    # Importar modelos y schemas después de crear db
    from app.models.modelo_usuario import Usuario
    from app.schemas.schemas_usuario import usuario_schema, usuarios_schema
    from app.models.modelo_carrito import CarritoItem
    from app.schemas.schemas_carrito import carrito_item_schema, carrito_items_schema

    # Importar rutas después de definir db
    from app.routes import *

    logger.info("Aplicación inicializada correctamente")

except Exception as e:
    logger.error(f"Error al inicializar la aplicación: {str(e)}")
    raise

