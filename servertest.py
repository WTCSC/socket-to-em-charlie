import socket
import threading

clients = []  # List to store all connected clients

# Function to handle each client connection
def handle_client(client_socket, addr):
    print(f"New connection from {addr}")
    clients.append(client_socket)  # Add client to list

    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break  # Client disconnected

            print(f"Received from {addr}: {msg}")

            # Send the received message to ALL connected clients (including the sender)
            broadcast(msg)

        except ConnectionResetError:
            break  # Handle client disconnection

    print(f"Connection closed for {addr}")
    clients.remove(client_socket)  # Remove client from list when disconnected
    client_socket.close()

# Function to broadcast message to all connected clients
def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode())
        except:
            clients.remove(client)  # Remove any dead connections

hostname = socket.gethostname()
host = socket.gethostbyname(hostname)

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = int(input("Input port: "))  # User inputs port number

server.bind((host, port))
server.listen(5)  # Allows up to 5 pending connections
print(f"Server listening on {host}:{port}")

# Accept multiple clients
while True:
    client, addr = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client, addr))
    client_thread.start()
