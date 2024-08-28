import socket

HOST = "172.31.25.1"
PORT = 9090
ENCODING = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

print(f"Host: {socket.gethostbyname(socket.gethostname())}")

while True:
    client_socket, adress = server.accept()
    print(f"Connected to {adress}")
    message = client_socket.recv(1024).decode(ENCODING)
    print(f"Cilent said: {message}")
    client_socket.send("Hi my nigga".encode(ENCODING))
    client_socket.close()
    print(f"Connection to {adress} closed")
