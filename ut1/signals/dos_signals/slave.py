import signal
import os

def ping(signum, frame):
    print("ping")

def pong(signum, frame):
    print("pong")

signal.signal(signal.SIGUSR1, ping)
signal.signal(signal.SIGUSR2, pong)

print(os.getpid())

while True:
    signal.pause()