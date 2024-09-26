from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'

# Usuario de ejemplo con nombre de usuario y contraseña
usuarios_validos = {
    'usuario1': 'contraseña123'
}

# Ruta para la página de inicio (login)
@app.route('/')
def home():
    return render_template('login.html')

# Ruta para manejar el inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    username = reque