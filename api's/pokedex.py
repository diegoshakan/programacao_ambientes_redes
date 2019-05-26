import requests
import json

req = requests.get('https://pokeapi.co/api/v2/pokemon/mewtwo')

dic = json.loads(req.text)

print(dic['height'])
print(dic['moves'][0]['move']['name'])
print(dic['moves'][0]['move']['name'])