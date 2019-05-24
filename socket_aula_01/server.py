from socket import *
 
meuHost = ''
 
minhaPort = 50007
 
# Cria um objeto socket. 
#AF_INET faz referência ao IP e o SOCK_STREAM ao TCP
server = socket(AF_INET, SOCK_STREAM)
 
# Vincula o servidor ao número de porto
server.bind((meuHost, minhaPort))
 
#Quantos clientes este servidor irá receber.
server.listen(5)
 
# print(f'Ouvindo IP ${meuHost} e Porta ${minhaPort}')
# data = server.accept()
# print(data)
 
while True:
    # Aceita uma connection quando encontrada e devolve a
    # um novo socket connection e o endereço do cliente
    # conectado
    connection, endereço = server.accept()
    print('Server conectado por', endereço)
     
    while True:
        # Recebe dados enviado pelo cliente
        data = connection.recv(1024)
        if not data: break
 
        # O servidor manda de volta uma resposta
        connection.send('Eco=>' + data.upper())
    
    connection.close()