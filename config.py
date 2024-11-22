import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'tu_clave_secreta')
    
    # Construir DATABASE_URL para MySQL con PyMySQL
    DB_USER = os.getenv('MYSQLUSER', 'root')
    DB_PASSWORD = os.getenv('MYSQLPASSWORD', 'lunarspace')
    DB_HOST = os.getenv('MYSQLHOST', 'localhost')
    DB_NAME = os.getenv('MYSQLDATABASE', 'eleganza_ecommerce')
    DB_PORT = os.getenv('MYSQLPORT', '3306')
    
    # Añadir parámetros SSL y timeout
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        "?charset=utf8mb4&ssl_mode=REQUIRED&connect_timeout=60"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'una-clave-secreta-por-defecto')

