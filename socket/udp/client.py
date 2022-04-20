from socket import *
serverName = 'hostname'
serverPort = 12000

clientSocket = socket(AF_INET, SOCKET_DGRAM)
message = raw_input('Input lowercase sentence:')
#attach server name, port to message; send into socket
clientSocket.sendto(message.encode(), (serverName, serverPort))
#read reply characters from socket into string
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modefiedMessage.decode()
clientSocket.close()
