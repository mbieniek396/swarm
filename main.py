import socket

HOST = '3.75.158.163'
PORT = 9907

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    client_socket, adress = server.accept()
    print(f"Connected to {adress}")