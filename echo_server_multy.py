import socket
import os

def es(conn):
    if os.fork() != 0:
        return

    while True:
            data = conn.recv(1024)
            if not data:
                    break
            sd = data.decode("utf-8") 
            if sd == 'close':
                    break;
            conn.send(data)
    conn.close()
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2224))
s.listen(10)
while True:
    conn, addr = s.accept()
    es(conn)
