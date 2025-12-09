import socket
import json

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

def gestionar_mensaje_recibido(mensaje):
    try:
        resultado = mensaje.get("res")
        if resultado == "error":
            error = mensaje.get("error")
            print("El error que reporta el servidor es: ", error)
        if resultado == "OK":
            if "datos" in mensaje: # opciones de voto
                for i,c in enumerate(mensaje["datos"]):#for i in range(len(mensaje["datos"])):
                    print(f"{i + 1}.{c}")
            else:
                print("Voto realizado exitosamente")
    except Exception as e:
        print("Ha habido un error al intentar leer el json:", e)


dir_server = ("127.0.0.1", 5000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(dir_server)

print("Conectados con el server!")

comando = ""

while comando != "FIN":
    comando = input("Ingresa un comando:\t").strip().upper()
    match comando:
        case "CANDIDATOS":
            json_envio = {
                "comando": comando
            }
        case "VOTAR":
            candidato = ""
            while not candidato:
                candidato = input("Elige un candidato:\t").strip().upper()
            json_envio = {
                "comando": comando,
                "candidato": candidato
            }
        case "FIN":
            json_envio = {"comando": comando}
        case _:
            print("Por favor, usa un comando válido ('CANDIDATOS', 'VOTAR', 'FIN')")
            continue

    enviar_mensaje(sock, json.dumps(json_envio))
    if comando != "FIN":
        mensaje = recibir_mensaje(sock)
        gestionar_mensaje_recibido(mensaje)