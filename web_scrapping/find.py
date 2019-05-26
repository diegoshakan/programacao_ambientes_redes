from bs4 import BeautifulSoup
import urllib.request

page = urllib.request.urlopen('http://todo-insight.herokuapp.com')

soup = BeautifulSoup(page, 'lxml')
# tag = soup.find(string='Todo')
# tag = soup.find('h1')
tags = soup.find_all('div')
for tag in tags:
    print(tag)
# print(tag)'