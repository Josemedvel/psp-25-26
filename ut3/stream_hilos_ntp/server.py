from threading import Thread
from datetime import datetime
import socket

def peticion(sock_cliente, dir_cliente):
    hora = datetime.now().time()
    sock_cliente.send(f"{hora}".encode())
    print(f"Cliente: {dir_cliente} servido")
    sock_cliente.close()

direccion = ("127.0.0.1", 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(direccion)

sock.listen()
print(f"Servidor NTP escuchando en {direccion}...")
while True:
    cliente, direccion = sock.accept()
    Thread(target=peticion, args=(cliente, direccion)).start()


