import requests
from bs4 import BeautifulSoup

url = 'https://www.ccee.org.br/web/guest/precos/painel-precos'
site = requests.get(url)

soup = BeautifulSoup(site.text, 'lxml')

lista_preco_hora_do_dia = soup.find_all('p', class_="clr-theme-black fs-14 fs-lg-16")

url = 'https://www.ccee.org.br/'
for lista_span in lista_preco_hora_do_dia:
    lista = lista_span.find_all('span')
    for lista_dados in lista:
        if lista_dados.next_element.name == 'a':
            url_phd = '{0}{1}'.format(url, lista_dados.next_element.get('href'))
            print(url_phd)
        else:
            print(lista_dados.next_element)

import pandas as pd

url_phd_xlsx = lista_dados.first_element
dados_tabela = requests.get(url_phd_xlsx)
phd = pd.read_excel('Histórico do Preço Horário 17 de abril de 2018 a 20 de novembro de 2021.xlsx')
print(phd)