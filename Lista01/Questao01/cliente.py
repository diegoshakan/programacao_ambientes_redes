#!/usr/bin/env python
#-*-coding:utf-8;-*-

from socket import *
 
servidor = 'localhost'
porta = 5000
 
mySocket = socket()
mySocket.connect((servidor, porta))

message = input('->')

while message != 'q':
    mySocket.send(message.encode())
    data = mySocket.recv(1024).decode()
    print('Recebendo do servidor: ' + data)
    message = input('->')
    if message in 'q':
        print('Adios muchacho!')

mySocket.close()