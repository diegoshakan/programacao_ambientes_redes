from Tarefa import *
from time import *

t1 = Tarefa("Cara")
t2 = Tarefa("Coroa")


t1.start()
sleep(1)
t2.start()

t1.join()
t2.join()
