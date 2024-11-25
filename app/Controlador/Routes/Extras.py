from flask import render_template
from app import app
from Modelo.models import *

# Pagina Principal
@app.route('/index')
def index():
    return render_template('index.html', title='Inicio')

# Informacion sobre nuestros servicios
@app.route('/servicios')
def servicios():
    return render_template('servicios.html', title='Servicios')

# Informacion sobre nosotros
@app.route('/sobre_nosotros')
def sobre_nosotros():
    return render_template('sobre_nosotros.html', title='Sobre Nosotros')

# Informacion sobre los planes VIP
@app.route('/vip')
def vip():
    return render_template('vip.html', title='VIP')

# Informacion sobre preguntas frecuentes
@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html', title='Ayuda')

# Vista de la base de la pagina (footer y header)
@app.route('/base.html')
def base():
    return render_template('base.html', title='Base')

