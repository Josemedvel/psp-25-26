import socket


direccion_server = ("127.0.0.1", 5000)

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_cliente.connect(direccion_server)

socket_cliente.send("hola".encode())
hora = socket_cliente.recv(1024).decode()
print(f"La hora actual del servidor es: {hora}")