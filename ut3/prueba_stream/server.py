import socket
from datetime import datetime

direccion = ("127.0.0.1", 5000)
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_server.bind(direccion)

socket_server.listen()

print(datetime.now().time())

while True:
    cliente, address_cliente = socket_server.accept()
    print(address_cliente)
    hora = datetime.now().time()
    print(hora)
    cliente.send(f"{hora}".encode())
    cliente.close()