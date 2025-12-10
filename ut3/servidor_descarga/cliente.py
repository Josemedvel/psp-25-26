import json
import socket
import os
from pprint import pprint

comandos_validos = ["listar", "descargar", "fin"]

def conseguir_directorio_cliente():
    directorio = ""
    fin = False
    while not fin:
        directorio = input("Ingresa el directorio de descarga del archivo (raíz por defecto):\t")
        directorio = "." if not directorio else directorio
        if os.path.exists(directorio):
            fin = True
    return directorio


def conseguir_comando():
    comando = None
    while not comando:
        comando = input("Ingresa el comando:\t").strip().lower()
        if comando not in comandos_validos:
            print(f"COMANDO NO VÁLIDO: solo se admiten los comandos[{comandos_validos}]")
    return comando     

def listar(sock):
    directorio = input("Ingrese directorio a listar (desde la raíz del servidor) ('directorio raíz por defecto'):\t")
    directorio = "." if not directorio else directorio
    json_envio = {
        "comm" : "listar",
        "data" : directorio
    }
    #pprint(json_envio)
    sock.send(json.dumps(json_envio).encode()) # envío de comando
    try:
        respuesta = sock.recv(2048)
        respuesta_json = json.loads(respuesta)
        respuesta_estado = respuesta_json.get("res")
        respuesta_datos = respuesta_json.get("data")
        if respuesta_estado == "ERROR":
            print(f"La carpeta {directorio} no existe o no es un directorio o está vacío")
        else:
            print(f"Los resultados de listar el directorio {directorio} son:")
            for i,item in enumerate(respuesta_datos):
                print(f"{i+1}. {item}")
    except Exception as e:
        print(f"Ha habido un error al listar: {e}")


def descargar(sock):
    archivo = input("Ingrese un archivo a descargar:\t")
    directorio = conseguir_directorio_cliente()
    json_envio = {
        "comm" : "descargar",
        "data" : archivo
    }
    try:
        sock.send(json.dumps(json_envio).encode()) # petición descarga
        
        # respuesta estado
        mensaje = sock.recv(1024)
        mensaje_json = json.loads(mensaje)
        estado_mensaje = mensaje_json.get("res")
        datos_mensaje = mensaje_json.get("data")
        if estado_mensaje == "ERROR":
            print(f"Ha habido un error con el archivo: {datos_mensaje}")
        else: 
            # empieza el bucle de descarga
            with open(f"{os.path.join(directorio,os.path.basename(archivo))}", "wb") as file:
                num_bytes = 0
                while num_bytes < datos_mensaje:
                    chunk_pkg = sock.recv(1024)
                    num_bytes += file.write(chunk_pkg)
            print("Archivo guardado!")

    except Exception as e:
        print(f"Ha habido un error en la descarga: {e}")

def envio_fin(sock):
    json_envio = {
        "comm" : "fin",
        "data" : ""
    }
    sock.send(json.dumps(json_envio).encode())

dir_server = ("127.0.0.1", 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(dir_server)
print("Conectado!")


fin = False

while not fin:
    comando = conseguir_comando()
    match comando:
        case "listar":
            listar(sock)
        case "descargar":
            descargar(sock)
        case "fin":
            envio_fin(sock)
            fin = True
