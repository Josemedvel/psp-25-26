import socket

dir_server = ("127.0.0.1", 3000)

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    texto = input("Escribe tu mensaje:\t")
    cliente.sendto(texto.encode(), dir_server)
    respuesta,_ = cliente.recvfrom(1024)
    print("SERVIDOR:", respuesta.decode())
