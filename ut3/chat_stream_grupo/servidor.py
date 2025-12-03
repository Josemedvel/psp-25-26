import socket
import threading

dir_server = ("127.0.0.1", 5000)
clientes_conectados = []
lock = threading.Lock()

def broadcast(mensaje, emisor):
    with lock:
        for sock in clientes_conectados:
            if sock != emisor: # mientras que no sea yo
                try:
                    sock.send(mensaje.encode())
                except Exception as e:
                    print("Cliente desconectado")
                    clientes_conectados.remove(sock)


def manejar_comunicacion(cliente, direccion_cliente):
    broadcast(f"[{direccion_cliente}] nueva conexión", cliente)
    with lock:
        num_clientes_conectados = len(clientes_conectados)
    broadcast(f"Hay un total de {num_clientes_conectados} clientes conectados al chat", None)

    while True:
        try:
            mensaje = cliente.recv(1024)
            if mensaje:
                broadcast(mensaje.decode(), cliente)
            else:
                cliente.close()
                broadcast(f"[{direccion_cliente}] se ha desconectado", None)
        except Exception as e:
            print(f"Ha habido un error: {e}")
            break

    # contamos con que se ha desconectado el cliente
    with lock:
        if cliente in clientes_conectados:
            clientes_conectados.remove(cliente)
        num_clientes_conectados = len(clientes_conectados)
    broadcast(f"[{direccion_cliente}] se ha desconectado del chat, quedan {num_clientes_conectados} conectados", None)
        


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(dir_server)

sock.listen()

while True:
    conn, dir_cliente = sock.accept()
    clientes_conectados.append(conn)
    hilo_cliente = threading.Thread(target=manejar_comunicacion, args=(conn, dir_cliente))
    hilo_cliente.start()




