from bs4 import BeautifulSoup
import requests

url = 'https://www.comparegames.com.br/'

print('-------------------------------------------------')
print('''Olá! Seja bem-vindo ao seu buscador de games''')
print('-------------------------------------------------')
while True:
    cod = int(input('''Qual Plataforma deseja fazer a busca:
    1. Xbox One
    2. Xbox 360
    3. PS4
    4. PS3
    5. PS Vita
    6. WI U
    7. WII
    8. 3DS
    9. PC
    10. Switch
    0. Sair
    '''))
    # console = ''
    if cod == 1:
        console = 'xbox-one'
    elif cod == 2:
        console = 'xbox360'
    elif cod == 3:
        console = 'ps4'
    elif cod == 4:
        console = 'ps3'
    elif cod == 5:
        console = 'ps-vita'
    elif cod == 6:
        console = 'wii-u'
    elif cod == 7:
        console = 'wii'
    elif cod == 8:
        console = 'ds-3ds'
    elif cod == 9:
        console = 'pc'
    elif cod == 10:
        console = 'nintendo-switch'
    elif cod == 0:
        break
    else:
        print('Não existe esta plataforma! (Ainda)')

    name_game = input('Qual o game: ')
    name_game = name_game.replace(' ','-')

    url = url + console + '/' + name_game

    req = requests.get(url)
    html = req.content

    soup = BeautifulSoup(html, 'lxml')
    tag_title = soup.title.string
    
    print('----------')
    print(tag_title)
    print('----------')

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
    # if not tag_title == 'Compare Games - Página não encontrada.':
    print('-----------------------------------------------------------------------------------------------------')
    print(f'Loja 1: {lista_detalhe[0][0]} \nPreço: {lista_detalhe[0][1]} \nSite da Loja/Produto: {lista_detalhe[0][2]}')
    print('-----------------------------------------------------------------------------------------------------')
    print(f'Loja 2: {lista_detalhe[1][0]} \nPreço: {lista_detalhe[1][1]} \nSite da Loja/Produto: {lista_detalhe[1][2]}')
    print('-----------------------------------------------------------------------------------------------------')
    print(f'Loja 3: {lista_detalhe[2][0]} \nPreço: {lista_detalhe[2][1]} \nSite da Loja/Produto: {lista_detalhe[2][2]}')
    print('-----------------------------------------------------------------------------------------------------')