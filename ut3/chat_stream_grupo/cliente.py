import socket
import threading
import sys

dir_server = ("127.0.0.1", 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(dir_server)

parar = False

def leer():
    global parar
    while not parar:
        try:
            mensaje = sock.recv(1024).decode()
            print(mensaje)
        except Exception as e:
            print(f"Ha habido un problema leyendo: {e}")
            parar = True

def escribir():
    global parar
    while not parar:
        try:
            mensaje = input("")
            if mensaje.strip().lower() in ["stop", "quit"]:
                sock.close()
                sys.exit(0)
                parar = True
            else:
                sock.send(mensaje.encode())
        except Exception as e:
            print(f"Ha habido un problema escribiendo: {e}")
            parar = True

hilo_leer = threading.Thread(target=leer)
hilo_escribir = threading.Thread(target=escribir)

hilo_leer.start()
hilo_escribir.start()




