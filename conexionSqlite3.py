import sqlite3
import json

def create_db_table():
    # Connect to SQLite database
    conn = sqlite3.connect('ETL_system.db')
    c = conn.cursor()
    
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (usuario TEXT PRIMARY KEY, telefono INTEGER, contrasena TEXT, provincia TEXT, permisos INTEGER, total_emails INTEGER, phishing_emails INTEGER, clicados_emails INTEGER, fechas TEXT, ips TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS legal
                 (web TEXT PRIMARY KEY, cookies INTEGER, aviso INTEGER, proteccion_datos INTEGER, creacion INTEGER)''')

    c.execute('''CREATE TABLE IF NOT EXISTS usuariosclas
                 (usuario TEXT PRIMARY KEY, telefono INTEGER, contrasena TEXT, provincia TEXT, permisos INTEGER, total_emails INTEGER, phishing_emails INTEGER, clicados_emails INTEGER, fechas TEXT, ips TEXT, critico INTEGER)''')
    
    conn.commit()
    conn.close()

def insert_data_users(json_file):
    # Connect to SQLite database
    conn = sqlite3.connect('ETL_system.db')
    c = conn.cursor()

    # Open JSON file and load data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Insert data into tables
    for usuario in data['usuarios']:
        for usuario_data in usuario.values():
            username = list(usuario.keys())[0]
            telefono = usuario_data['telefono']
            contrasena = usuario_data['contrasena']
            provincia = usuario_data['provincia']
            permisos = usuario_data['permisos']
            total_emails = usuario_data['emails']['total']
            phishing_emails = usuario_data['emails']['phishing']
            cliclados_emails = usuario_data['emails']['cliclados']
            fechas = str(usuario_data['fechas'])
            ips = str(usuario_data['ips'])

            c.execute("INSERT OR IGNORE INTO usuarios VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (username, telefono, contrasena, provincia, permisos, total_emails, phishing_emails, cliclados_emails, fechas, ips))

    
    conn.commit()
    conn.close()

def insert_data_legal(json_file):
    # Connect to SQLite database
    conn = sqlite3.connect('ETL_system.db')
    c = conn.cursor()

    # Open JSON file and load data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Insert data into tables
    for web in data['legal']:
        for web_data in web.values():
            name = list(web.keys())[0]
            cookies = web_data['cookies']
            aviso = web_data['aviso']
            proteccion = web_data['proteccion_de_datos']
            creacion = web_data['creacion']

            c.execute("INSERT OR IGNORE INTO legal VALUES (?, ?, ?, ?, ?)",
                      (name, cookies, aviso, proteccion, creacion))

    
    conn.commit()
    conn.close()


def insert_data_users_clas(json_file):
    # Connect to SQLite database
    conn = sqlite3.connect('ETL_system.db')
    c = conn.cursor()

    # Open JSON file and load data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Insert data into tables
    for usuario in data['usuarios']:
        for usuario_data in usuario.values():
            username = list(usuario.keys())[0]
            telefono = usuario_data['telefono']
            contrasena = usuario_data['contrasena']
            provincia = usuario_data['provincia']
            permisos = usuario_data['permisos']
            total_emails = usuario_data['emails']['total']
            phishing_emails = usuario_data['emails']['phishing']
            cliclados_emails = usuario_data['emails']['cliclados']
            fechas = str(usuario_data['fechas'])
            ips = str(usuario_data['ips'])
            critico = usuario_data['critico']

            c.execute("INSERT OR IGNORE INTO usuariosclas VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (username, telefono, contrasena, provincia, permisos, total_emails, phishing_emails,
                       cliclados_emails, fechas, ips, critico))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db_table()
    insert_data_users('users_data_online.json')
    insert_data_legal('legal_data_online.json')
    insert_data_users_clas('users_data_online_clasificado.json')
    print("Data inserted successfully.")
