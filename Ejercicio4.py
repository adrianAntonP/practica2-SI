import conexionSqlite3 as connsql3



def check_credentials(username, password):
    conn = connsql3.conectar_db()
    c = conn.cursor()

    c.execute("SELECT contrasena FROM usuarios WHERE usuario = ?", (username,))
    result = c.fetchone()

    if result and result[0] == password:
        conn.close()
        return True
    else:
        conn.close()
        return False



def sign_up(username, telefono, contrasena, provincia, permisos, emailtotal, emailphishing, emailclicados, fechas, ips):
    conn = connsql3.conectar_db()
    c = conn.cursor()

    c.execute('SELECT COUNT(*) FROM usuarios WHERE usuario = ?', (username,))
    c.fetchone()

    if c.fetchone()[0] == 0:
        c.execute("INSERT OR IGNORE INTO usuarios VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (username, telefono, contrasena, provincia, permisos, emailtotal, emailphishing, emailclicados, fechas, ips))

    c.close()


def getCriticalUser():
    conn = connsql3.conectar_db()
    c = conn.cursor()

    c.execute("SELECT phishing_emails, clicados_emails, provincia FROM usuarios")
    results = c.fetchall()

    filtrados = []
    for result in results:
        email_phishing, email_clicados, provincia = result

        if email_phishing > 0:
            ratio = email_clicados / email_phishing
            if ratio > 0.5:
                filtrados.append((email_phishing, email_clicados, provincia))

    c.close()

    return filtrados




