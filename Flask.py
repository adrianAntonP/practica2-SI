import os


from flask import Flask, render_template, request, redirect
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import Ejercicio1
import matplotlib.pyplot as plt


import ejercicio3
import conexionSqlite3 as connsql3

# instancia Flask
app = Flask(__name__, static_url_path='/static')
app.secret_key = 'flaskeandobby_81'


# ruta principal del panel de control
@app.route('/')
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


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('passwordInput')

    if connsql3.check_credentials(username, password):
        return render_template('index.html')
    else:
        return render_template('login/loginError.html')


@app.route('/formSignUp', methods=['POST'])
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

    connsql3.sign_up(username, numberphone, password, province, permissions, totalEmails, phishingEmails, clickEmails, date, ips)

    return render_template('login/login.html')


# ruta para mostrar el top X de usuarios críticos
@app.route('/usuarios_criticos', methods=['GET', 'POST'])
def mostrar_usuarios_criticos():
    ruta_diccionario = 'rockyou-20.txt'  # Ruta al diccionario de contraseñas
    if request.method == 'POST':
        num_usuarios_criticos = int(request.form['num_usuarios'])
    else:
        num_usuarios_criticos = 5  # Valor default

    conexion = Ejercicio1.conexion_bd()  # conexión a  base de datos
    usuarios_criticos, phishing_50 = Ejercicio1.obtener_usuarios_con_contrasenas_debiles(conexion.cursor(),
                                                                                         ruta_diccionario,
                                                                                         top=num_usuarios_criticos)
    conexion.close()  # Cerrar conexión la base de datos
    # Generar gráfico de pastel
    plt.figure(figsize=(6, 6))
    plt.pie([phishing_50.count(True), phishing_50.count(False)], labels=['Spam > 50%', 'Spam <= 50%'],
            autopct='%1.1f%%')
    plt.title('Porcentaje de usuarios que clickaron > 50% phishing')

    # Guardar la imagen en el directorio static
    static_dir = os.path.join(app.root_path, 'static')
    image_path = os.path.join(static_dir, 'pie_chart.png')
    plt.savefig(image_path)
    # Convertir el DataFrame en una lista
    return render_template('usuarios_criticos.html', usuarios=usuarios_criticos, phishing_50=phishing_50)


# Define la ruta para mostrar el top X de páginas web desactualizadas
@app.route('/paginas_desactualizadas', methods=['GET', 'POST'])
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
def last_vulnerabilities():
    vulnerabilidades = ejercicio3.last_10_vulnerabilities()
    if vulnerabilidades:
        return render_template('lastVulnerabilities.html', vulnerabilidades=vulnerabilidades)
    else:
        return 'error', 500

if __name__ == '__main__':
    app.run(debug=True)
