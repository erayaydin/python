import socket

# Bağlanılacak sunucunun bilgileri
host = "127.0.0.1"
port = 3000

mySocket = socket.socket()
mySocket.connect((host, port))

welcomeMsg = mySocket.recv(1024).decode('utf-8')
print("Server: " + welcomeMsg)

message = input(">")
while message != 'q':
    mySocket.send(message.encode('utf-8'))
    result = mySocket.recv(1024).decode('utf-8')
    print("Server: " + result)
    message = input(">")

mySocket.close()
