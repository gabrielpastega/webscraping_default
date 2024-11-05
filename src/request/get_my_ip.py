import requests as r

url = "http://lumtest.com/myip.json"
url2 = "https://www.globo.com"

response = r.get(url2)

if response.status_code == 200:
    print(response.json())
else: 
    print("Error")