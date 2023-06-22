import requests

def get_institutions():
    url = "https://assist.org/api/institutions"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None


