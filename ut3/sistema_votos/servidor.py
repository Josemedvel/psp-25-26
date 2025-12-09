import socket
import json
import threading
from pprint import pprint

dir_server = ("127.0.0.1", 5000)
lista_candidatos = ["A", "B", "C", "D"]
dicc_votos = {}
lock = threading.Lock()

def enviar_mensaje(sock, mensaje):
    try:
        sock.send(mensaje.encode())
    except Exception as e:
        print("Error al enviar el mensaje:",e)

def recibir_mensaje(sock):
    try:
        mensaje = sock.recv(1024)
        mensaje_json = json.loads(mensaje)
        return mensaje_json
    except Exception as e:
        print("Error al recibir el mensaje:",e)


def manejar_cliente(sock, direccion_cliente):
    global dicc_votos
    fin = False
    while not fin:
        mensaje = recibir_mensaje(sock)
        if mensaje is None: # error de conexion
            break
        try:
            comando = mensaje.get("comando")
            match comando:
                case "FIN":
                    fin = True
                    continue
                case "CANDIDATOS":
                    json_envio = {
                        "res" : "OK",
                        "datos" : lista_candidatos
                    }
                case "VOTAR":
                    with lock:
                        if direccion_cliente in dicc_votos: # ya se ha votado
                            json_envio = {
                                "res": "error",
                                "error": "Ya se ha votado anteriormente"
                            }
                        else:
                            opcion = mensaje.get("candidato")
                            if opcion not in lista_candidatos:
                                json_envio = {
                                    "res": "error",
                                    "error": "Candidato inexistente, comprueba la lista"
                                }
                            else:
                                dicc_votos[direccion_cliente] = opcion
                                pprint(dicc_votos)
                                json_envio = {
                                    "res" : "OK"
                                }
            enviar_mensaje(sock, json.dumps(json_envio))
        except Exception as e:
            print("Error al desempaquetar el json:", e)

    sock.close()



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(dir_server)
sock.listen()

while True:
    cliente, dir_cliente = sock.accept()
    threading.Thread(target=manejar_cliente, args=(cliente, dir_cliente)).start()
