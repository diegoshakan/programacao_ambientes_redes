import urllib.request

page = urllib.request.urlopen('http://todo-insight.herokuapp.com')
for linha in page.readlines():
    print(linha)

# import requests

# url = 'http://todo-insight.herokuapp.com'
# req = requests.get(url)
# print(req.text)