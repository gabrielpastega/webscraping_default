import requests


url = 'https://api.vendas.gpa.digital/pa/search/popular?maxResults=2'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

content = requests.get(url, headers=headers)

print(content)