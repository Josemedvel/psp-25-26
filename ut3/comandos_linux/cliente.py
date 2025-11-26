import socket
import json
import sys

if len(sys.argv) < 2:
    print("Hace falta especificar el comando a ejecutar")
    sys.exit(-1)

dir_server = ("127.0.0.1", 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(dir_server)

print("Conexión establecida")

paquete = json.dumps({"comm" : sys.argv[1]})

sock.send(paquete.encode())

print("Paquete enviado")

respuesta = sock.recv(1024)

if respuesta:
    respuesta_dict = json.loads(respuesta)
    if "ERROR" in respuesta_dict["status"]:
        print("Ha habido un error: ", respuesta_dict["error"])
    else:
        print(respuesta_dict["res"])

