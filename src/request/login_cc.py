import requests
from bs4 import BeautifulSoup

with requests.Session() as s:

    login_url = 'https://www.codechef.com/api/codechef/login'

    context = s.get(login_url)

    soup = BeautifulSoup(context.content, 'html.parser')
    csrf_token = soup.find_all('input')[3]['value']
    cleaned_token = csrf_token.replace('\\"', '')
    form_id = soup.find_all('input')[4]['value']
    cleaned_form_id = form_id.replace('\\"', '')
        
    payload = {
        'name': 'gabrielpastega',
        'pass': 'Kobake123!',
        'csrfToken': cleaned_token,
        'form_build_id': cleaned_form_id,
        'form_id': 'ajax_login_form'
    }

    response = s.post(url=login_url, data=payload)

    if response.status_code == 200:
        dashboard = s.get(url='https://www.codechef.com/dashboard')

        if dashboard.status_code == 200:
            print(dashboard.content)