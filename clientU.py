import socket

HEADER_SIZE = 64
PORT = 3000
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "E"
# Update the server IP address as required
SERVER_IP_ADDRESS = "192.168.8.103"
REMOTE_ADDRESS = (SERVER_IP_ADDRESS, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(REMOTE_ADDRESS)

def send(msg):

    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER_SIZE - len(send_length))
    client.send(send_length)
    client.send(message)

# Continuous message sending
while True:
    message = input("Enter message to send (or type '!DISCONNECT' to exit): ")
    send(message)
    if message == DISCONNECT_MESSAGE:
        break

client.close()
