import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = 'tu_clave_secreta_aqui'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:lunarspace@localhost/eleganza_ecommerce'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
