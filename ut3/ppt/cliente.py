import socket


def pedir_jugada():
    jugada = ""
    while not jugada:
        jug_intento = input("Por favor, ingresa tu jugada:\t")
        if jug_intento.strip().lower() in ["piedra", "papel", "tijera"]:
            jugada = jug_intento.strip().lower()
    return jugada

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dir_server = ("127.0.0.1", 5000)

sock.connect(dir_server)

jugando = True

while jugando:
    # esperar solicitud de jugada
    try:
        mensaje = sock.recv(1024)

        if not mensaje:
            raise Exception("Desconexion")
            
        mensaje_dec = mensaje.decode()

        print(mensaje_dec)
        if "la partida" in mensaje_dec: # fin
            jugando = False
            continue
        else: # mandar jugada
            jugada = pedir_jugada()
            sock.send(jugada.encode())

    except Exception as e:
        print(f"Ha habido un problema:{e}")