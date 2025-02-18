import socket

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(('localhost', 5000))
print("Connected to server")
name = input("Enter your name: ")
# Send messages and receive responses
while True:
    msg = input("Enter message: ")
    outgoing = f"{name}: {msg}"
    if not msg:
        break
    client.send(outgoing.encode())
    response = client.recv(1024).decode()
    print(f"Server says: {response}")

client.close()