import requests
import pandas as pd

from bs4 import BeautifulSoup


keyword = 'Sabonete'

url = f"https://lista.mercadolivre.com.br/{keyword}"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    search_result = soup.find_all("div", class_="ui-search-result")

    data = []

    for result in search_result:
        title = result.find("h2", class_="poly-box poly-component__title").text.strip()
        link = result.find("a", class_="href")
        price = result.find("span", class_="andes-money-amount__fraction")
        brand = result.find("span", class_="poly-component__brand")

        if link:
            link = link.get("href")

        data.append({"Title": title, "Price":price, "Brand":brand, "Link":link})
    
    print(data)

else:
    print("Error")