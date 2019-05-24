import urllib.request

page = urllib.request.urlopen('http://todo-insight.herokuapp.com')
for linha in page.readlines():
    print(linha)