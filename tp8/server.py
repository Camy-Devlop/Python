import threading
import socket

HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADRR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADRR)

def handle_client(conn, addr):
    print(f"[Nouvelle Connection] {addr} connecté")

    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                connected=False
            print(f"[{addr}] {msg}")
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] server is listningon {SERVER}")
    while True:
        conn, addr =server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACtive connection] {threading.activeCount()-1}")

print("[STARTING] server is starting...")
start()