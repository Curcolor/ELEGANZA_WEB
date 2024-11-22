import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class Config:
    # Configuración de la base de datos
    MYSQL_HOST = 'curcolor.mysql.pythonanywhere-services.com'
    MYSQL_USER = 'curcolor'
    MYSQL_PASSWORD = 'lunarspace'
    MYSQL_DB = 'curcolor$eleganza_ecommerce'
    
    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'una-clave-secreta-por-defecto')

