from time import sleep
from threading import *

class Task01(Thread):
    def run(self):
        while True:
        # for i in range(10):
            sleep(0.5)
            # print("Tarefa 01 - Rodando!")
            print('Tarefa Thread')

# class Task02(Thread):
#     def run(self):
#         while True:
#         # for i in range(10):
#             sleep(0.5)
#             print("Tarefa 02 - Rodando!")

t1 = Task01()
# t2 = Task02()

t1.start()
sleep(0.2)
# t2.start()

# t1.join()
# t2.join()


while True:
    sleep(0.5)
    print("Tarefa Principal")
    if KeyboardInterrupt == True:
        print('Fim!')

print(KeyboardInterrupt == True)