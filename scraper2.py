import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.ccee.org.br/precos/painel-precos")

soup = BeautifulSoup( res.text,'html.parser')

sudeste = soup.find_all('div', class_="tab-zone tab-widget tabZoneSelected tabZone-viz fade-bg", id_="tabZoneId6")
preco_se = soup.find_all('div', class_="tab-tvView tvimagesNS")
hora_se = soup.find_all('div', class_="tab-tvBottomAxis tvimagesNS")

sul = soup.find_all('div', class_="tab-zone tab-widget tabZone-viz fade-bg", id_="tabZoneId17")
preco_sul = soup.find_all('div', class_="tab-tvView tvimagesNS")
hora_sul = soup.find_all('div', class_="tab-tvBottomAxis tvimagesNS")

nordeste = soup.find_all('div', href_="tab-zone tab-widget tabZone-viz fade-bg", id_="tabZoneId11")
preco_ne = soup.find_all('div', class_="tab-tvView tvimagesNS")
hora_ne = soup.find_all('div', class_="tab-tvBottomAxis tvimagesNS")

norte = soup.find_all('div', class_="tab-zone tab-widget tabZone-viz fade-bg", id="tabZoneId15")
preco_nt = soup.find_all('div', class_="tab-tvView tvimagesNS")
hora_nt = soup.find_all('div', class_="tab-tvBottomAxis tvimagesNS")

print(sudeste, preco_se, hora_se)