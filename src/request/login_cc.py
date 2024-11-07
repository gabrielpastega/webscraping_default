import requests
import os
from bs4 import BeautifulSoup
from pathlib import Path

# iniciar a sessão
with requests.Session() as s:
    url = 'https://www.codechef.com'
    login_url = 'https://www.codechef.com/api/codechef/login'
    dashboard_url = 'https://www.codechef.com/api/learn/dashboard'

    proxy = {
        'http': 'http://localhost:8080',
        'https': 'https://localhost:8080'
    }

    # solicitação para capturar o token CSRF
    context = s.get(login_url, proxies=proxy, verify=False)

    # procurar pelo token CSRF
    soup = BeautifulSoup(context.content, 'html.parser')
    csrf_token = soup.find_all('input')[3]['value']
    cleaned_token = csrf_token.replace('\\"', '')
    # form_id = soup.find_all('input')[4]['value']
    # cleaned_form_id = form_id.replace('\\"', '')
        
    # dados de login da página
    payload = {
        'name': os.getenv('login'),
        'pass': os.getenv('senha'),
        'csrfToken': cleaned_token,
        'form_build_id': 'form-UxTJOZN2gx4Evue-H3udXKEhVRNy5Civ9gEXP59jyV4',
        'form_id': 'ajax_login_form'
    }

    # post para login na página
    login = s.post(url=login_url, data=payload, proxies=proxy, verify=False)

    if login.status_code == 200:
        print("Login com sucesso!")
        dashboard = s.get(url=dashboard_url, proxies=proxy, verify=False)
        if dashboard.status_code == 200:
            print(f"Sucesso ao chegar no Dashboard: Status Code - {dashboard.status_code}")
            print(dashboard.text)
        else:
            print(f'Falha ao tentar acessar o Dashboard: Status Code - {dashboard.status_code}')
    else:
        print("Falha de login")
        print(login.status_code)
        print(login.text)