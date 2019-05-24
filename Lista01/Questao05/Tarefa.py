from threading import *

class Tarefa(Thread):
    def __init__(self, nome):
        Thread.__init__(self)
        self.nome = nome

    def run(self):
        for i in range(10):
            print(f'{i} processo de {self.nome}')
      