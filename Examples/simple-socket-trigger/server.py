import socket

# Sunucu haberleşmesinde 3000 portunu kullanacağız...
port = 3000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Tüm ağlarda(0.0.0.0) 3000 portu üzerinden yayın aç
serverSocket.bind(("0.0.0.0", port))
serverSocket.listen(1)

print("Hosted on 0.0.0.0:" + str(port))

clientSocket, clientAddr = serverSocket.accept()
print("New connection from: %s" % str(clientAddr))
connectionMessage = "Welcome to server. Waiting for 'light' command."
clientSocket.send(connectionMessage.encode('utf-8'))

while True:
    received = clientSocket.recv(1024).decode('utf-8')
    if not received:
        break
    print("Received: %s" % str(received))

    resultMessage = "Waiting another command!"

    if(received == "light"):
        print("LIGHT LED!")
        resultMessage = "Lighting led!"

    clientSocket.send(resultMessage.encode('utf-8'))

clientSocket.close()
serverSocket.close()
