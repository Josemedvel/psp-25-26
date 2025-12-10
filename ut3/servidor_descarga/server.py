'''
with open("texto.txt", "rb") as file:
    while True:
        chunk = file.read(128)
        if not chunk:
            break
'''
import json
import socket
import threading
import os
from pprint import pprint


def gestionar_cliente(cliente, dir_cliente):
    fin = False
    while not fin:
        try:
            mensaje = cliente.recv(1024)
            mensaje_json = json.loads(mensaje)
            comando = mensaje_json.get("comm")
            datos = mensaje_json.get("data")
            pprint(mensaje_json)
            match comando:
                case "listar":
                    lista = listar(datos)
                    print(lista)
                    json_envio = {
                        "res": "OK" if len(lista) > 0 else "ERROR",
                        "data": lista
                    }

                    cliente.send(json.dumps(json_envio).encode())

                case "descargar":
                    descargar(cliente, datos)
                case "fin":
                    fin = True
        except Exception as e:
            print(f"Ha habido un error al leer el comando del cliente, {e}")
    
    cliente.close()


def listar(ruta):
    print(ruta)
    resultado = []
    if os.path.exists(ruta) and os.path.isdir(ruta):
        resultado = os.listdir(ruta)
    return resultado


def descargar(cliente, ruta):
    if os.path.exists(ruta) and not os.path.isdir(ruta):
        json_respuesta = {
            "res" : "OK",
            "data" : os.path.getsize(ruta)
            }
        cliente.send(json.dumps(json_respuesta).encode())

        with open(ruta, "rb") as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                cliente.send(chunk)
    else:
        json_respuesta = {
            "res" : "ERROR",
            "data" : "Archivo no encontrado"
        }
        cliente.send(json.dumps(json_respuesta).encode())


    

dir_server = ("127.0.0.1", 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(dir_server)
sock.listen()

while True:
    try:
        cliente, dir_cliente = sock.accept()
        threading.Thread(target=gestionar_cliente, args=(cliente, dir_cliente)).start()
    except Exception as e:
        print("Servidor de descarga cerrado")
        os._exit(0)