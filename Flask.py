import os
from datetime import timedelta

import googlemaps
from flask import Flask, render_template, request, redirect, session, url_for, flash
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import Ejercicio1
import matplotlib.pyplot as plt
from functools import wraps


import ejercicio3
import Ejercicio4

# instancia Flask
app = Flask(__name__, static_url_path='/static')
app.secret_key = 'flaskeandobby_81'
app.permanent_session_lifetime = timedelta(minutes=30)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Debes iniciar sesión para acceder a esta página.', 'error')
            return redirect(url_for('showLogin'))
        return f(*args, **kwargs)
    return decorated_function
# ruta principal del panel de control
@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/showLogin')
def showLogin():
    return render_template('login/login.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('login/sign_up.html')


@app.route('/showForgotPass')
def showForgotPass():
    return render_template('login/forgot.html')


@app.route('/showErrorLogIn')
def showErrorLogIn():
    return render_template('login/loginError.html')

@app.route('/showMap')
@login_required
def showMap():
    usuarios_criticos = Ejercicio4.getCriticalUser()

    gmaps = googlemaps.Client(key='AIzaSyC5ZSrloY6H5iKMELsk1hMTib-vV676i-Q')


    marcadores = []
    for usuario in usuarios_criticos:
        email_phishing, email_clicados, provincia = usuario
        if provincia is not None:
            geocode_result = gmaps.geocode(provincia)
            if geocode_result:
                latitud = geocode_result[0]['geometry']['location']['lat']
                longitud = geocode_result[0]['geometry']['location']['lng']
                marcadores.append({'lat': latitud, 'lng': longitud,
                                   'infowindow': f'Phishing: {email_phishing}, Clicados: {email_clicados}, Provincia: {provincia}'})


    return render_template('map.html', marcadores=marcadores)


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('passwordInput')

    if Ejercicio4.check_credentials(username, password):
        session['logged_in'] = True
        session['username'] = username
        return render_template('index.html')
    else:
        return render_template('login/loginError.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('login/loginError.html')




@app.route('/formSignUp', methods=['GET', 'POST'])
def formSignUp():
    username = request.form.get('Username')
    province = request.form.get('Province')
    ips = request.form.get('ips')
    numberphone = request.form.get('NumberPhone')
    totalEmails = request.form.get('TotalEmails')
    phishingEmails = request.form.get('PhishingEmails')
    clickEmails = request.form.get('ClickEmails')
    date = request.form.get('Dates')
    permissions = request.form.get('Permissions')
    password = request.form.get('passwordInput')

    Ejercicio4.sign_up(username, numberphone, password, province, permissions, totalEmails, phishingEmails, clickEmails, date, ips)

    return render_template('login/login.html')


# ruta para mostrar el top X de usuarios críticos
@app.route('/usuarios_criticos', methods=['GET', 'POST'])
@login_required
def mostrar_usuarios_criticos():
    ruta_diccionario = 'rockyou-20.txt'  # Ruta al diccionario de contraseñas
    if request.method == 'POST':
        num_usuarios_criticos = int(request.form['num_usuarios'])
    else:
        num_usuarios_criticos = 5  # Valor default

    conexion = Ejercicio1.conexion_bd()
    usuarios_criticos, phishing_50 = Ejercicio1.obtener_usuarios_criticos(conexion.cursor(),
                                                                                         ruta_diccionario,
                                                                                         top=num_usuarios_criticos)
    conexion.close()
    # Generar gráfico de pastel
    plt.figure(figsize=(6, 6))
    plt.pie([phishing_50.count(True), phishing_50.count(False)], labels=['Spam > 50%', 'Spam <= 50%'],
            autopct='%1.1f%%')
    plt.title('Porcentaje de usuarios que clickaron > 50% phishing')

    # Guardar la imagen en el directorio static
    static_dir = os.path.join(app.root_path, 'static')
    image_path = os.path.join(static_dir, 'pie_chart.png')
    plt.savefig(image_path)
    return render_template('usuarios_criticos.html', usuarios=usuarios_criticos, phishing_50=phishing_50)


# Define la ruta para mostrar el top X de páginas web desactualizadas
@app.route('/paginas_desactualizadas', methods=['GET', 'POST'])
@login_required
def mostrar_paginas_desactualizadas():
    if request.method == 'POST':
        num_paginas_desactualizadas = int(request.form['num_paginas'])
    else:
        num_paginas_desactualizadas = 5  # Valor default

    conexion = Ejercicio1.conexion_bd()  # conexión a base de datos
    paginas_desactualizadas = Ejercicio1.obtener_top_paginas_desactualizadas(conexion.cursor(),
                                                                             top=num_paginas_desactualizadas)
    conexion.close()  # Cerrar conexión abase de datos
    return render_template('paginas_desactualizadas.html', paginas=paginas_desactualizadas)


@app.route('/lastVulnerabilities')
@login_required
def last_vulnerabilities():
    vulnerabilidades = ejercicio3.last_10_vulnerabilities()
    if vulnerabilidades:
        return render_template('lastVulnerabilities.html', vulnerabilidades=vulnerabilidades)
    else:
        return 'error', 500


@app.route('/analizarUsuario', methods=['GET', 'POST'])
@login_required
def formulario_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        provincia = request.form['provincia']
        permisos = request.form['permisos']
        total_emails = request.form['total_emails']
        phishing_emails = request.form['phishing_emails']
        clicados_emails = request.form['clicados_emails']
        return render_template('esCriticoOno.html')

    return render_template('analizarUsuario.html')







if __name__ == '__main__':
    app.run(debug=True)
