#!/usr/bin/env python
#-*-coding:utf-8;-*-

import socket

HOST = 'localhost' #coloca o host do servidor
PORT = 57003

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))
arq = open('/home/shakan/Documentos/Período 3/ProgramacaoAmbientesRedes/Lista01/Questao03/testeChegou.txt', 'wb')

while 1:
    dados = s.recv(1024)
    if not dados:
        break
    arq.write(dados)

arq.close()
s.close()