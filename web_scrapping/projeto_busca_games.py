from bs4 import BeautifulSoup
import requests
import os

class BuscaJogo:
    def __init__(self, console, game):
        self.console = console
        self.game = game
        self.url = 'https://www.comparegames.com.br/' + self.console + '/' + self.game
        self.tag_title = ''
        self.detalhes = []
        self.lista_detalhe = []
        

    def page(self):
        req = requests.get(self.url)
        html = req.content

        soup = BeautifulSoup(html, 'lxml')
        self.tag_title = soup.title.string

        detalhes = soup.find_all('div', {'class': 'prc-list-hd-price'})

        for detalhe in detalhes:
            price = detalhe.a.text
            price = price.replace('\n', '')
            price = price.replace('\t', '')
            nome = detalhe.a['data-store']
            url_loja = detalhe.a['href']
            info = [nome, price, url_loja]
            self.lista_detalhe.append(info)

        self.mostraTela()

    def mostraTela(self):
        print('----------')
        print(self.tag_title)
        print('----------')

        tam = len(self.lista_detalhe)
        for i in range(tam):
            print('-'*101)
            print(f'Loja {i+1}: {self.lista_detalhe[i][0]} \nPreço: {self.lista_detalhe[i][1]} \nSite da Loja/Produto: {self.lista_detalhe[i][2]}')
            print('-'*101)

consoles = ['xbox-one', 'xbox360', 'ps4', 'ps3', 'ps-vita', 'wii-u', 'wii', 'ds-3ds', 'pc', 'nintendo-switch']

print('-------------------------------------------------')
print('''Olá! Seja bem-vindo ao seu buscador de games''')
print('-------------------------------------------------')
def main():
    while True:
        print('''    1. Xbox One
    2. Xbox 360
    3. PS4
    4. PS3
    5. PS Vita
    6. WI U
    7. WII
    8. 3DS
    9. PC
    10. Switch
    0. Sair''')
        cod = int(input('Qual Plataforma deseja fazer a busca: '))
        if cod == 0:
            break
        elif cod < 0 and cod > 10:
            print('Não existe esta plataforma! (Ainda)')
            main()
        else:
            console = consoles[cod-1]

        name_game = input('Qual o game: ')
        name_game = name_game.replace(' ','-')

        BJ = BuscaJogo(console, name_game)
        BJ.page()

        dnv = input('Aperte enter para pesquisar novamente\n[0]Zero para para o programa: ')
        if dnv == '0':
            break
        os.system('cls')

main()