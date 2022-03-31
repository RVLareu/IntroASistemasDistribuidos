import socket
serverName = "localhost"
serverPort = 12000

# SOCK_STREAM: TCP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establece conexion TCP. El handshake ocurre aca
clientSocket.connect((serverName, serverPort))
sentence = input("Input lowercase sentence: ")

# Notar no se aclara la dirección IP destino
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("From Server: ", modifiedSentence.decode())

# Genera un mensaje TCP al TCP en el servidor
clientSocket.close()