from flask import Flask, render_template, request, redirect
import Ejercicio1

#instancia Flask
app = Flask(__name__)
app.secret_key = 'flaskeandobby_81'

#ruta principal del panel de control
@app.route('/')
def index():
    return render_template('index.html')

#ruta para mostrar el top X de usuarios críticos
@app.route('/usuarios_criticos', methods=['GET', 'POST'])
def mostrar_usuarios_criticos():
    ruta_diccionario = 'rockyou-20.txt'  #Ruta al diccionario de contraseñas
    if request.method == 'POST':
        num_usuarios_criticos = int(request.form['num_usuarios'])
    else:
        num_usuarios_criticos = 5  #Valor default

    conexion = Ejercicio1.conexion_bd()  #conexión a  base de datos
    usuarios_criticos, phishing_50 = Ejercicio1.obtener_usuarios_con_contrasenas_debiles(conexion.cursor(), ruta_diccionario, top=num_usuarios_criticos)
    conexion.close()  #Cerrar conexión la base de datos
    # Convertir el DataFrame en una lista
    return render_template('usuarios_criticos.html', usuarios=usuarios_criticos, phishing_50=phishing_50)


# Define la ruta para mostrar el top X de páginas web desactualizadas
@app.route('/paginas_desactualizadas', methods=['GET', 'POST'])
def mostrar_paginas_desactualizadas():
    if request.method == 'POST':
        num_paginas_desactualizadas = int(request.form['num_paginas'])
    else:
        num_paginas_desactualizadas = 5  #Valor default

    conexion = Ejercicio1.conexion_bd()  #conexión a base de datos
    paginas_desactualizadas = Ejercicio1.obtener_top_paginas_desactualizadas(conexion.cursor(), top=num_paginas_desactualizadas)
    conexion.close()  #Cerrar conexión abase de datos
    return render_template('paginas_desactualizadas.html', paginas=paginas_desactualizadas)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if validar_credenciales(username, password):
            session['username'] = username
            return redirect('/perfil')
        else:
            return render_template('login.html', mensaje='Credenciales inválidas')
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
