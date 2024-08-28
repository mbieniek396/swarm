import socket

HOST = "0.0.0.0"
PORT = 9907

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    client_socket, adress = server.accept()
    print(f"Connected to {adress}")