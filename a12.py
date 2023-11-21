import requests
from bs4 import BeautifulSoup


url = "https://numpy.org/pt/install/"


response = requests.get(url)


if response.status_code == 200:
  
    soup = BeautifulSoup(response.text, 'html.parser')
    
   
    titulo = soup.title.string
    print(f'Título da Página: {titulo}')
else:
    print('A solicitação falhou. Verifique a URL e a conexão com a internet.')
