import socket
import json
import subprocess
from datetime import datetime
from threading import Thread
import time

valid_comms = ["listar", "crear_f"]

dir_server = ("127.0.0.1", 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(dir_server)

sock.listen(5)

def listar():
    p = subprocess.run(["bash", "-c", "ls"], capture_output=True, text=True)
    print(type(p.stderr), p.stderr)
    resultado = {"res": p.stdout, "status": "OK"}
    return resultado


def petition_handler(cliente, direccion):
    respuesta_json = {"res": "", "status": ""}
    mensaje_comando = cliente.recv(1024)
    if mensaje_comando:
        comando_json = json.loads(mensaje_comando)
        if comando_json["comm"] not in valid_comms:
            respuesta_json["status"] = f"ERROR: No existe el comando [{comando_json['comm']}]"
            respuesta_texto = json.dumps(respuesta_json)
            cliente.send(respuesta_texto.encode())
        else:
            res = ""
            match comando_json["comm"]:
                case "listar":
                    res = listar()
                case _:
                    print("error")
            cliente.send(json.dumps(res).encode())
    cliente.close()

while True:
    cliente, direccion = sock.accept()
    Thread(target=petition_handler, args=(cliente, direccion)).start()



