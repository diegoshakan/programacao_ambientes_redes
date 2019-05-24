#!/usr/bin/env python
#-*-coding:utf-8;-*-

from socket import *

servidor = ''
porta = 57003

mySocket = socket()
mySocket.bind((servidor, porta))
mySocket.listen(1)

conexao, endereco = mySocket.accept()
arq = open('/home/shakan/Documentos/Período 3/ProgramacaoAmbientesRedes/Lista01/Questao02/teste1.txt', 'rb')

for i in arq.readlines():
    conexao.send(i)

print('Enviando Arquivo!')

arq.close()
conexao.close()