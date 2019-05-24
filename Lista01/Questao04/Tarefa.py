from threading import *
from time import *
from random import *

class Tarefa(Thread):
    def __init__(self, nome):
        Thread.__init__(self)
        self.nome = nome

    def run(self):
        while True:
            print(f'Joga a moeda e deu: {self.nome}')
            sleep(uniform(0.0, 0.3))        
