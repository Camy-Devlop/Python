import socket
import threading
import socket

HEADER=64
PORT=5050
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"
SERVER="127.0.0.1"
ADRR=(SERVER,PORT)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADRR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b' '* (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


msg_fin="fin"
m=""
while msg_fin!=m:
    m=input("entre un message ")
    send(m)

send(DISCONNECT_MESSAGE)