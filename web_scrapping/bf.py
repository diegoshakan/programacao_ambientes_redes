from bs4 import BeautifulSoup
import urllib.request

page = urllib.request.urlopen('http://todo-insight.herokuapp.com')

soup = BeautifulSoup(page, 'lxml')
# # tag_title = soup.a # variável recebe a primeira tag 'a'
# tag_title = soup.find_all('a') # cria lista com todas as tags 'a'
# for tag_a in tag_title: # percorre a lista e imprime as tags 'a'
#     print(tag_a)

# print(soup.title) # printa a tag 'title'
# print(soup.a) # printa a tag 'a'
# print(soup.img)
# print(soup.prettify()) # printa o arquivo html
# print(soup.get_text()) # printa todo o texto da página
# print(soup.h1.get_text()) # printa o texto somente da tag selecionada.

# print(soup.nav.contents) # printa todas as tags filhas de 'nav'

# # Visitando as posições/tags através do FOR
# for child in soup.nav.contents:
#     print(child)
# for child in soup.nav.contents:
#     if child.name == 'div':
#         print(child)

# print(len(list(soup.children))) # filhos diretos
# print(len(list(soup.descendants))) # filhos dos filhos

# for child in soup.div.ul.li.descendants:
#     print(child)

# # Visitando as tags filhas (diretas) através do método children
# print(type(soup.children))
# for child in soup.div.ul.children:
#     if child.name == 'li':
#         print(child.a.get('href') + ' texto: ' + child.a.get_text())

# print(type(soup.nav.contents))
# print(len(soup.nav.contents))
# print(len(soup.nav.contents[3].contents))
# print(soup.nav.contents[3].contents[1].get_text()) #percorrendo as tags e imprimindo somente os textos
# print(soup.nav.contents[1].span)
# print(soup.nav.contents[1].span.string)
