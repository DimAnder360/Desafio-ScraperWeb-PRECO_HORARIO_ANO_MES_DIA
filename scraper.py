import requests
from bs4 import BeautifulSoup

url = 'https://www.ccee.org.br/precos/painel-precos'

headers = {'User-Agent': "Chrome/96.0.4664.45 64 bits"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content,'html.parser')

tabela1 = soup.find_all('div', id_="tab-dashboard-region")
tabela = soup.find_all('div', class_="tab-dashboard tab-widget is-dashboard")
text = soup.find_all('span', class_="text-primary")
dados = soup.find_all('a', href_="https://www.ccee.org.br/documents/80415/919444/ccee_lista_preco_horario_17%20de%20abril%20de%202018%20a%2011%20de%20novembro%20de%202021_Site.xls/175fb9d4-8162-f630-d700-a453665accc8")

print(tabela1)
