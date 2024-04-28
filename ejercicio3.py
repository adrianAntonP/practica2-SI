import requests
def last_10_vulnerabilities():
    url = "https://cve.circl.lu/api/last"
    try:
        response = requests.get(url)
        if response.status_code == 200: #indica que todo bien y podra coger las ultimas 10
            aux = response.json()
            last_10 = aux[:10]
            return last_10
        else:
            return None

    except Exception as error:
        print(f"error, {error}")
        return None
