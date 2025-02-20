import socket
import threading

# Function to handle each client connection
def handle_client(client_socket, addr):
    print(f"New connection from {addr}")
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break  # Client disconnected
            print(f"Received from {addr}: {msg}")
            client_socket.send(msg.encode())  # Echo back the message
        except ConnectionResetError:
            break  # Handle client disconnection
    print(f"Connection closed for {addr}")
    client_socket.close()

hostname = socket.gethostname()
host = socket.gethostbyname(hostname)

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = host  # Listen on all network interfaces
port = int(input("Input port: "))

# Bind and listen
server.bind((host, port))
server.listen(5)  # Allows up to 5 pending connections
print(f"Server listening on {host}:{port}")

# Accept multiple clients
while True:
    client, addr = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client, addr))
    client_thread.start()

# Close server (This will never reach due to infinite loop)
server.close()
