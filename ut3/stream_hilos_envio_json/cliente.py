import json
import socket

direccion_server = ("127.0.0.1", 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(direccion_server)

datos_json = json.loads(sock.recv(1024))

print(datos_json)
# asdfnoa