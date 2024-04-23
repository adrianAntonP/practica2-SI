from flask import Flask, render_template, request
import Ejercicio1

#instancia Flask
app = Flask(__name__)

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
    usuarios_criticos = Ejercicio1.obtener_usuarios_con_contrasenas_debiles(conexion.cursor(), ruta_diccionario, top=num_usuarios_criticos)
    conexion.close()  #Cerrar conexión la base de datos
    return render_template('usuarios_criticos.html', usuarios=usuarios_criticos)


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

if __name__ == '__main__':
    app.run(debug=True)
