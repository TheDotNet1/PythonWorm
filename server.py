import socket

ada = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "0.0.0.0"
port = 8080

ada.bind((host, port))

ada.listen(1)

clientsocket, addr = ada.accept()

mr = clientsocket.recv(1024)
print(mr.decode())
clientsocket.send(b"[*] Connection Enstabilished")
clientsocket.close()
