from socket import*
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
whiel True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode
	capitalizedSentence = sentence.upper()
	connetionSocket.send(captializedSentence.encode())
    connetionSocket.close()
