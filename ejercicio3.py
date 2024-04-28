import requests

def last_10_vulnerabilities():
    url = "https://cve.circl.lu/api/last"
    try:
        aux = requests.get(url)
        if aux.status_code == 200:
            return aux.json()[:10]
        else:
            print("error:", aux.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("error:", e)
        return None

last_vulnerabilities = last_10_vulnerabilities()
if last_vulnerabilities:
    for i, vuln in enumerate(last_vulnerabilities, 1):
        print(f"{i}. CVE: {vuln['id']} - Descripción: {vuln.get('summary')}")
else:
    print("error")
