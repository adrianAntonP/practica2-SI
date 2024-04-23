import sqlite3
import pandas as pd
import hashlib

#Función para obtener el top X de usuarios con contraseñas débiles
def obtener_usuarios_con_contrasenas_debiles(cur, ruta_diccionario, top):
    cursor = cur.execute("SELECT usuario, contrasena FROM usuarios")
    df_users = pd.DataFrame(cursor.fetchall(), columns=['usuario', 'contrasena'])

    contrasenas_diccionario_hasheadas = cargar_y_hashear_diccionario(ruta_diccionario)
    df_users["passwd_debil"] = df_users["contrasena"].apply(lambda x: es_contrasena_debil(x, contrasenas_diccionario_hasheadas))
    df_users_passdebil = df_users[df_users["passwd_debil"]]
    df_users_passdebil['phising_ratio'] = df_users_passdebil['phising_emails'] / df_users_passdebil['total_emails']
    df_users_passdebil['click_probability'] = df_users_passdebil['clicados_emails'] / df_users_passdebil['total_emails']
    df_users_passdebil['probability_spam'] = df_users_passdebil['phising_ratio'] * df_users_passdebil['click_probability']
    usuarios_criticos = df_users[df_users["passwd_debil"]]["usuario"].tolist()[:top]  # Obtener solo los nombres de usuario
    return usuarios_criticos

#Función para obtener el top X de páginas web desactualizadas
def obtener_top_paginas_desactualizadas(cur, top):
    query = f'''
        SELECT web, 
       cookies AS cookies_desactualizadas, 
       aviso AS aviso_desactualizado, 
       proteccion_datos AS proteccion_datos_desactualizada
FROM legal
ORDER BY cookies + aviso + proteccion_datos DESC, creacion DESC
LIMIT {top}
    '''
    cursor = cur.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    paginas_desactualizadas = []
    for row in rows:
        pagina = dict(zip(columns, row))
        paginas_desactualizadas.append(pagina)
    return paginas_desactualizadas

#Función para cargar y hashear el diccionario de contraseñas
def cargar_y_hashear_diccionario(ruta_diccionario):
    contrasenas_diccionario_hasheadas = set()
    with open(ruta_diccionario, 'r', encoding='utf-8') as file:
        for line in file:
            contrasena = line.strip()
            contrasena_hasheada = hashlib.md5(contrasena.encode()).hexdigest()
            contrasenas_diccionario_hasheadas.add(contrasena_hasheada)
    return contrasenas_diccionario_hasheadas

#Función para determinar si una contraseña es débil
def es_contrasena_debil(contrasena_hasheada, contrasenas_diccionario_hasheadas):
    return contrasena_hasheada in contrasenas_diccionario_hasheadas

#Función para establecer conexión a la base de datos SQLite
def conexion_bd():
    return sqlite3.connect('ETL_system.db')


if __name__ == '__main__':
    conexion = conexion_bd()
    ruta_diccionario = 'rockyou-20.txt'

    #Solicitar user
    num_usuarios_criticos = int(input("Introduce el número de usuarios críticos que deseas ver: "))

    #print result
    usuarios_con_contrasenas_debiles = obtener_usuarios_con_contrasenas_debiles(conexion.cursor(), ruta_diccionario, top=num_usuarios_criticos)
    print("\nUsuarios con contraseñas débiles:")
    print(usuarios_con_contrasenas_debiles)

    #Solicitar user
    num_paginas_desactualizadas = int(input("\nIntroduce el número de páginas desactualizadas que deseas ver: "))

    #print result
    paginas_desactualizadas = obtener_top_paginas_desactualizadas(conexion.cursor(), top=num_paginas_desactualizadas)
    print("\nPáginas desactualizadas:")
    print(paginas_desactualizadas)

    conexion.close()
