from time import sleep
from random import *
from threading import *


tempoMassa = []
class Task01(Thread):
    def run(self):
        for i in range(65):
            tempo = uniform(0 , 1)
            sleep(tempo)
            tempo = round(tempo, 2)
            print(f"Felipe Massa na volta {i}")
            sleep(1)
            tempoMassa.append(tempo)

tempoHamilton = []
class Task02(Thread):
    def run(self):
        for i in range(65):
            tempo = uniform(0, 1)
            sleep(tempo)
            tempo = round(tempo, 2)
            print(f"Lewis Hamilton na volta {i}")
            sleep(1)
            tempoHamilton.append(tempo)


t1 = Task01()
t2 = Task02()

t1.start()
sleep(0.2)
t2.start()


t1.join()
t2.join()

tempoTotalMassa = sum(tempoMassa)
tempoTotalHamilton = sum(tempoHamilton)

print('\n')
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
print('Bandeirada!!! Que corrida emocionante, e o vencedor é...')

if tempoTotalMassa < tempoTotalHamilton:
    print(f'''Felipe Massa vence a corrida com o tempo de {tempoTotalMassa:.2f}.
Lewis Hamilton fica em segundo lugar com o tempo de {tempoTotalHamilton:.2f}''')
else:
    print(f'''Lewis Hamilton vence a corrida com o tempo de {tempoTotalHamilton:.2f}. 
Felipe Massa fica em segundo lugar com o tempo de {tempoTotalMassa:.2f}''')
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
# print(tempoMassa)
# print(f'Tempo Total Massa {tempoTotalMassa:.2f}')
# print(tempoHamilton)
# print(f'Tempo Total Hamilton {tempoTotalHamilton:.2f}')
print('\n')
print('Fiquem agora com o Globo Rural!')