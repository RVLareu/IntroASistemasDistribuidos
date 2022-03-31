import socket
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Es el socket de bienvenida
serverSocket.bind(("localhost", serverPort))

# Esperamos a que un socket cliente "toque la puerta".

serverSocket.listen(1)
print("The server is ready to receive")
while True:

 # Cuando un cliente "toca la puerta" se invoca accept(), que crea un nuevo
 # socket en el servidor dedicado a ese cliente en particular
 connectionSocket, addr = serverSocket.accept()
 sentence = connectionSocket.recv(1024).decode()
 capitalizedSentence = sentence.upper()
 connectionSocket.send(capitalizedSentence.encode())
 # Cerramos el socket dedicado al cliente, pero el de bienvenida
 # sigue abierto, por lo que pueden conectarse nuevos clientes
 connectionSocket.close()