import requests as r

url = "http://lumtest.com/myip.json"

headers = {
    "header": "content"
}

response = r.get(url)

if response.status_code == 200:
    print("Endereço IP:", response.json())
    print("Cidade", response.json()["geo"])
else: 
    print("Erro na requisição: ", response.status_code)