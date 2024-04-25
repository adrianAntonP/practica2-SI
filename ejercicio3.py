import requests

URL_cve = "https://cve.circl.lu/api/last/10"

def last_10_vulnerabilities():
    try:
        response = requests.get(URL_cve)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("error", e)
        return None
