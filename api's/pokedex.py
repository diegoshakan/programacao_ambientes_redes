from bs4 import BeautifulSoup
import requests
import json


pokemon = input('Nome Pokemon: ')
pokemon = pokemon.replace(' ', '-')


req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')

dic = json.loads(req.text)

url = f'https://www.pokemon.com/br/pokedex/{pokemon}'
reqBS4 = requests.get(url)
html = reqBS4.content

soup = BeautifulSoup(html, 'html.parser')
img = soup.find(class_='active')
src = img['src']
print(f'Imagem: {src}')

print('----------------------')
# Nome
nome = dic['forms'][0]['name'] 
print(f'Informações sobre: {nome}')

# Tipo
tipo = dic['types'][0]['type']['name']
print(f'Tipo: {tipo}')


# Altura
altura = dic['height']
print(f'Altura: {altura/10} m')

# Peso
peso = dic['weight']
print(f'Peso: {peso/10} kg')

# Índice
indice = dic['game_indices'][0]['game_index']
print(f'Indice na Pokedex: {indice}')
print('----------------------')

# Imagens frente e trás
img_frente = dic['sprites']['front_default']
img_tras = dic['sprites']['back_default']
print(f'Imagem de frente = {img_frente}')
print(f'Imagem de frente = {img_tras}')



index = dic['game_indices'][0]['game_index']

req1 = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{index}/')
dic1 = json.loads(req1.text)

# # Cor
cor = dic1['color']['name']
print(f'Cor : {cor}')

print('----------------------')

# Descrição Rápida

desc_rap = dic1['genera']
tam_list_desc_rap = len(dic1['genera'])

for i in range(tam_list_desc_rap):
    if desc_rap[i]['language']['name'] == 'en':
        print('Descrição Rápida:', desc_rap[i]['genus'])
        break

desc_comp = dic1['flavor_text_entries']
tam_list_desc_comp = len(desc_comp)

for i in range(tam_list_desc_comp):
    if desc_comp[i]['language']['name'] == 'en':
        print('Descrição:', desc_comp[i]['flavor_text'])
        break
print('----------------------')
# Onde pode ser encontrado
habitat = dic1['habitat']['name']
print(f'Onde Encontrar: {habitat}')
print('----------------------')
list_moves = (dic['moves'])
tam_list_moves = len(list_moves)

print('Golpes e Movimentos:' )
for i in range(tam_list_moves):
    print(list_moves[i]['move']['name'])
print('----------------------')
print(f'Para mais informações: {url}')
print('----------------------')