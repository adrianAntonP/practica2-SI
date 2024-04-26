import requests

def last_10_vulnerabilities():
    url = "https://cve.circl.lu/api/last"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()[:10]
        else:
            print("Error al obtener los datos de la API:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)
        return None

last_vulnerabilities = last_10_vulnerabilities()
if last_vulnerabilities:
    for i, vuln in enumerate(last_vulnerabilities, 1):
        print(f"{i}. CVE: {vuln['id']} - Descripción: {vuln.get('summary', 'No disponible')}")
else:
    print("No se pudieron obtener las últimas vulnerabilidades.")
