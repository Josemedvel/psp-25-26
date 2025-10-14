import time
from multiprocessing import Process, Lock

lock_1 = Lock() # ping
lock_2 = Lock() # pong

lock_2.acquire() # bloquear pong

def ping(lock_1, lock_2):
    while True:
        lock_1.acquire()
        print("ping")
        time.sleep(0.2)
        lock_2.release()

def pong(lock_1, lock_2):
    while True:
        lock_2.acquire()
        print("\t\tpong")
        time.sleep(0.2)
        lock_1.release()
    


Process(target=ping, args=(lock_1, lock_2)).start()
Process(target=pong, args=(lock_1, lock_2)).start()