import socket
import threading

dir_server = ("127.0.0.1", 5000)
clientes_conectados = []

def broadcast(mensaje, emisor):
    for sock in clientes_conectados:
        if sock != emisor: # mientras que no sea yo
            sock.send(mensaje.encode())


def manejar_comunicacion(cliente, direccion_cliente):
    broadcast(f"[{direccion_cliente}] nueva conexión", cliente)
    broadcast(f"Hay un total de {len(clientes_conectados)} clientes conectados al chat", None)

    while True:
        try:
            mensaje = cliente.recv(1024)
            if mensaje:
                broadcast(mensaje.decode(), cliente)
            else:
                cliente.close()
                broadcast(f"[{direccion_cliente}] nueva conexión", None)
        except Exception as e:
            print(f"Ha habido un error: {e}")
            break

    # contamos con que se ha desconectado el cliente
    if cliente in clientes_conectados:
        clientes_conectados.remove(cliente)
    broadcast(f"[{direccion_cliente}] se ha desconectado del chat, quedan {len(clientes_conectados)} conectados", None)
        


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(dir_server)

sock.listen()

while True:
    conn, dir_cliente = sock.accept()
    clientes_conectados.append(conn)
    hilo_cliente = threading.Thread(target=manejar_comunicacion, args=(conn, dir_cliente))
    hilo_cliente.start()




