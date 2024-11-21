import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'tu_clave_secreta')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://root:lunarspace@localhost/eleganza_ecommerce')
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
