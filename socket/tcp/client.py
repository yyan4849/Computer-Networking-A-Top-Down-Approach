from socket import *
serverName = 'serverName'
serverPort = 12000
clientSocket = socket(AF_INET, SOCKET_STREM)
clientSocket.connet((serverName, serverPort))
sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
clientSocket.close()
