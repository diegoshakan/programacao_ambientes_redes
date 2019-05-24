from Tarefa import *
from time import *
import os

t1 = Tarefa("cara")
t2 = Tarefa("coroa")

palpite = input("Qual é o seu palpite: ")
palpite = palpite.lower()

t1.start()
sleep(1)
t2.start()

t1.join()
t2.join()

lista = []
lista.append(t1.join())
print(lista)


resposta = "fim"
print(resposta)