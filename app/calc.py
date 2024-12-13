import socket

def evaluate_expression(expression):
    try:
       
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Erreur : {str(e)}"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen(1)

print("Serveur en attente de connexion...")

client_socket, client_address = server_socket.accept()
print(f"Connexion de {client_address}")

msg = client_socket.recv(1024).decode()
print(f"Message de salutation reçu : {msg}")
client_socket.send("Serveur prêt à recevoir des calculs".encode())

while True:
    msg = client_socket.recv(1024).decode()
    print(f"Message reçu du client : {msg}")
    
    if msg.lower() == 'exit':
        break

    print(f"Calcul demandé : {msg}")
    
    result = evaluate_expression(msg)
    print(f"Résultat calculé : {result}")
    
    client_socket.send(result.encode())
    
client_socket.close()
server_socket.close()
