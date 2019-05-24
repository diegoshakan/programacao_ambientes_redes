#!/usr/bin/env python
#-*-coding:utf-8;-*-

from socket import *
 
servidor = ""
porta = 5000

mySocket = socket()
mySocket.bind((servidor, porta))
mySocket.listen(5)

print('Esperando conexão...')
conexao, endereco = mySocket.accept()

print('Conetando: ' + str(endereco))

while True:
    data = conexao.recv(1024).decode()
    if not data:
        break
    print('Conectado do usuário: ' + str(data))

    data = f'<{str(endereco[0])}> ' + str(data)
    print(f'Enviando: ' + str(data))
    conexao.send(data.encode())

print('Conexão encerrada!')

conexao.close()