import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8888))
s.send('Hello'.encode())

data = s.recv(1024)
print(data.decode())

msg = input("Calcul à envoyer: ")

s.send(msg.encode())

s_data = s.recv(1024)
print(s_data.decode())

s.close()
