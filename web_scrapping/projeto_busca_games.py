from bs4 import BeautifulSoup
import requests

url = 'https://www.comparegames.com.br/'
console = 'ps4'
name_game = 'fifa 19'
name_game = name_game.replace(' ','-')

url = url + console + '/' + name_game

req = requests.get(url)
html = req.content

soup = BeautifulSoup(html, 'lxml')
tag_title = soup.title.string
print(tag_title)

detalhes = soup.find_all('div', {'class': 'prc-list-hd-price'})

lista_detalhe = []

for detalhe in detalhes:
    price = detalhe.a.text
    price = price.replace('\n', '')
    price = price.replace('\t', '')
    nome = detalhe.a['data-store']
    url_loja = detalhe.a['href']
    info = [nome, price, url_loja]
    lista_detalhe.append(info)
print(lista_detalhe)
