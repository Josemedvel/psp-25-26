import json
import socket
import requests
from threading import Thread

def bromita(cliente, dir_cliente):
    datos = requests.get("https://icanhazdadjoke.com/", json=True)
    json_datos = ""#json.loads(datos.text) # mirar como imprimir el json entero
    if "joke" in json_datos:
        broma = json_datos["joke"]
        print(broma)
    else:
        print("Ha habido un error en la petición")

    datos_envio = {
        "direccion_cliente" : dir_cliente
    }
    json_envio = json.dumps(datos_envio)
    cliente.send(json_envio.encode())
    cliente.close()

direccion = ("127.0.0.1", 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(direccion)

sock.listen()
print(f"SERVER BROMITAS ESCUCHANDO EN {direccion}")

while True:
    cliente, dir_cliente = sock.accept()
    Thread(target=bromita, args=(cliente, dir_cliente)).start()

