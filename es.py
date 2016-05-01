import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
exitApp = True
while exitApp:
    conn, addr = s.accept()
    while exitApp:
        data = conn.recv(1024)
        if not data:
            break
        sd = data.decode("utf-8") 
        #print(data, sd)
        if sd == 'close':
            break;
        conn.send(data)
    conn.close()

            

