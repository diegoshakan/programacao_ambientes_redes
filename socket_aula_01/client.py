from socket import *
 
serverHost = 'localhost'
serverPort = 50007
 
# Mensagem a ser mandada
mensagem = [b'Oi, tudo bem?']
 
# Criação do socket e o conectamos ao servidor
server = socket(AF_INET, SOCK_STREAM)
server.connect((serverHost, serverPort))
 
# Mandamos a menssagem linha por linha
for linha in mensagem:
    server.send(linha)
 
    # Depois de mandar uma linha esperamos uma resposta
    # do servidor
    data = server.recv(1024)
    print('Cliente recebeu:', data)
 

server.close()