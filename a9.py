import requests


url =  "https://numpy.org/pt/install/"

response = requests.get(url)


print(f'Código de Status: {response.status_code}')
