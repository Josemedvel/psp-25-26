import socket

direccion = ("127.0.0.1", 3000)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
server.bind(direccion)


while True:
    data, address = server.recvfrom(1024)
    datos = data.decode()
    print(f"El cliente[{address}] ha mandado:", datos)
    texto = input("Ingresa tu respuesta:\t")
    server.sendto(texto.encode(), address)
